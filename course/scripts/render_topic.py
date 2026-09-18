#!/usr/bin/env python3
"""Render a detailed Cordel course topic from Markdown to standalone HTML."""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$")
TOPIC_HEADING_RE = re.compile(r"^([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+)\s+[—-]\s+(.+)$")
LINK_RE = re.compile(r"\[([^]]+)]\(([^)]+)\)")
CODE_RE = re.compile(r"`([^`]+)`")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")


def inline_markup(value: str) -> str:
    """Escape text and apply the small inline Markdown subset used by course topics."""
    escaped = html.escape(value, quote=True)
    escaped = LINK_RE.sub(r'<a href="\2">\1</a>', escaped)
    escaped = CODE_RE.sub(r"<code>\1</code>", escaped)
    return BOLD_RE.sub(r"<strong>\1</strong>", escaped)


def split_frontmatter(lines: list[str]) -> tuple[dict[str, str], list[str]]:
    """Read scalar frontmatter fields and return the Markdown body."""
    if not lines or lines[0].strip() != "---":
        return {}, lines
    metadata: dict[str, str] = {}
    end = next((index for index in range(1, len(lines)) if lines[index].strip() == "---"), 0)
    if not end:
        return {}, lines
    for line in lines[1:end]:
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"')
    return metadata, lines[end + 1 :]


def heading_parts(value: str) -> tuple[str | None, str]:
    match = TOPIC_HEADING_RE.match(value)
    if not match:
        return None, value
    return match.group(1), match.group(2)


def collect_headings(lines: list[str]) -> list[tuple[int, str, str]]:
    headings: list[tuple[int, str, str]] = []
    for line in lines:
        match = HEADING_RE.match(line)
        if not match:
            continue
        level = len(match.group(1))
        topic_id, title = heading_parts(match.group(2))
        if topic_id and level <= 3:
            headings.append((level, topic_id, title))
    return headings


def render_table(lines: list[str]) -> str:
    rows = [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in lines]
    header = rows[0]
    body = rows[2:]
    output = ['<div class="table-wrap"><table><thead><tr>']
    output.extend(f"<th>{inline_markup(cell)}</th>" for cell in header)
    output.append("</tr></thead><tbody>")
    for row in body:
        output.append("<tr>")
        output.extend(f"<td>{inline_markup(cell)}</td>" for cell in row)
        output.append("</tr>")
    output.append("</tbody></table></div>")
    return "".join(output)


def render_markdown(lines: list[str]) -> tuple[str, str, str]:
    """Render the constrained Markdown used by the course material."""
    output: list[str] = []
    paragraph: list[str] = []
    first_id = "TOPIC"
    first_title = "Conteúdo do curso"
    list_type: str | None = None
    in_code = False
    code_lines: list[str] = []
    index = 0

    def flush_paragraph() -> None:
        if paragraph:
            output.append(f"<p>{inline_markup(' '.join(paragraph))}</p>")
            paragraph.clear()

    def close_list() -> None:
        nonlocal list_type
        if list_type:
            output.append(f"</{list_type}>")
            list_type = None

    while index < len(lines):
        line = lines[index].rstrip()

        if line.startswith("```"):
            flush_paragraph()
            close_list()
            if in_code:
                output.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
                code_lines.clear()
                in_code = False
            else:
                in_code = True
            index += 1
            continue
        if in_code:
            code_lines.append(line)
            index += 1
            continue

        heading = HEADING_RE.match(line)
        if heading:
            flush_paragraph()
            close_list()
            level = len(heading.group(1))
            topic_id, title = heading_parts(heading.group(2))
            if level == 1:
                first_id = topic_id or first_id
                first_title = title
            else:
                anchor = topic_id or re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
                badge = (
                    f'<button class="topic-id" data-copy="{anchor}" title="Copiar identificador">{anchor}</button>'
                    if topic_id
                    else ""
                )
                output.append(
                    f'<section class="topic-section level-{level}" id="{anchor}">'
                    f'<div class="section-head"><h{level}>{inline_markup(title)}</h{level}>{badge}</div>'
                )
                next_index = index + 1
                while next_index < len(lines):
                    next_heading = HEADING_RE.match(lines[next_index])
                    if next_heading and len(next_heading.group(1)) <= level:
                        break
                    next_index += 1
                inner, _, _ = render_markdown(lines[index + 1 : next_index])
                output.append(inner)
                output.append("</section>")
                index = next_index
                continue
            index += 1
            continue

        if line.startswith("> "):
            flush_paragraph()
            close_list()
            quote_lines = []
            while index < len(lines) and lines[index].startswith(">"):
                quote_lines.append(lines[index].lstrip("> ").strip())
                index += 1
            output.append(f"<blockquote>{inline_markup(' '.join(quote_lines))}</blockquote>")
            continue

        if "|" in line and index + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-+", lines[index + 1]):
            flush_paragraph()
            close_list()
            table_lines = [line, lines[index + 1]]
            index += 2
            while index < len(lines) and "|" in lines[index] and lines[index].strip():
                table_lines.append(lines[index])
                index += 1
            output.append(render_table(table_lines))
            continue

        unordered = re.match(r"^[-*]\s+(.+)$", line)
        ordered = re.match(r"^\d+\.\s+(.+)$", line)
        if unordered or ordered:
            flush_paragraph()
            desired = "ul" if unordered else "ol"
            if list_type != desired:
                close_list()
                output.append(f"<{desired}>")
                list_type = desired
            item = (unordered or ordered).group(1)
            output.append(f"<li>{inline_markup(item)}</li>")
            index += 1
            continue

        if not line.strip():
            flush_paragraph()
            close_list()
        else:
            paragraph.append(line.strip())
        index += 1

    flush_paragraph()
    close_list()
    return "".join(output), first_id, first_title


STYLE = """
:root{--ink:#13243a;--muted:#53677d;--paper:#f5f8fb;--surface:#fff;--line:#d6e0e9;--blue:#0b3554;--cyan:#168da0;--cyan-pale:#e2f5f5;--yellow:#f2bd43;--red:#b54d49;--shadow:0 14px 40px rgba(14,47,73,.09);--content:76rem}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;overflow-x:hidden;color:var(--ink);background:linear-gradient(rgba(22,141,160,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(22,141,160,.035) 1px,transparent 1px),var(--paper);background-size:24px 24px;font-family:"Segoe UI Variable Text","Segoe UI",Arial,sans-serif;line-height:1.65}
a{color:#12658a}code,.topic-id,.eyebrow,.meta,.back-link{font-family:"Cascadia Code",Consolas,monospace}code{padding:.12rem .32rem;border-radius:.25rem;background:#e8eff4;font-size:.88em}.skip{position:fixed;top:.5rem;left:.5rem;z-index:20;transform:translateY(-180%);padding:.7rem 1rem;background:#fff;border:2px solid var(--cyan)}.skip:focus{transform:none}
header{color:#fff;background:var(--blue);border-bottom:.42rem solid var(--yellow)}.hero{position:relative;max-width:var(--content);margin:auto;padding:4.5rem 2rem 3.5rem}.hero:before{content:"";position:absolute;right:1rem;top:0;width:10rem;height:100%;opacity:.16;background:repeating-linear-gradient(90deg,transparent 0 12px,var(--cyan) 12px 14px,transparent 14px 27px,var(--yellow) 27px 29px);transform:skewX(-9deg)}.eyebrow{position:relative;margin:0 0 1rem;color:#82dedc;font-size:.76rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase}h1,h2,h3{font-family:Bahnschrift,"DIN Alternate","Arial Narrow",sans-serif;font-stretch:condensed;text-transform:uppercase;line-height:1.07}h1{position:relative;max-width:15ch;margin:0;font-size:clamp(3rem,7vw,6rem);font-weight:600;letter-spacing:-.035em}.hero p{position:relative;max-width:52rem;color:#c8d8e5;font-size:1.1rem}.meta-row{position:relative;display:flex;flex-wrap:wrap;gap:.55rem;margin-top:1.5rem}.meta{padding:.4rem .65rem;border:1px solid rgba(255,255,255,.3);border-radius:999px;font-size:.7rem}.back-link{display:inline-block;margin-bottom:1.2rem;color:#8de1df;font-size:.72rem;text-decoration:none}
.layout{display:grid;grid-template-columns:16rem minmax(0,1fr);gap:3rem;max-width:calc(var(--content) + 19rem);margin:auto;padding:2.5rem 1.5rem 6rem}.toc{position:sticky;top:1.5rem;align-self:start;max-height:calc(100vh - 3rem);overflow:auto;padding:1rem;background:rgba(255,255,255,.9);border:1px solid var(--line);border-radius:.65rem;box-shadow:var(--shadow)}.toc strong{display:block;margin-bottom:.7rem;font-family:"Cascadia Code",Consolas,monospace;color:var(--muted);font-size:.68rem;letter-spacing:.1em;text-transform:uppercase}.toc a{display:grid;grid-template-columns:6.7rem 1fr;gap:.35rem;padding:.42rem;color:var(--muted);border-left:2px solid transparent;text-decoration:none;font-size:.76rem;line-height:1.25}.toc a span:first-child{color:var(--cyan);font-family:"Cascadia Code",Consolas,monospace;font-size:.65rem}.toc a:hover,.toc a:focus-visible{border-color:var(--yellow);background:#fff6dc;outline:none}
main{min-width:0}.topic-section{scroll-margin-top:1.5rem;margin-bottom:1.2rem;padding:clamp(1.3rem,3vw,2rem);background:var(--surface);border:1px solid var(--line);border-radius:.7rem;box-shadow:0 7px 24px rgba(14,47,73,.045)}.topic-section .topic-section{margin-top:1rem;margin-bottom:0;box-shadow:none;background:#f8fafc}.section-head{display:flex;align-items:flex-start;justify-content:space-between;gap:1rem;margin-bottom:1rem;padding-bottom:.8rem;border-bottom:1px solid var(--line)}h2,h3{margin:0;color:var(--blue);font-weight:600;letter-spacing:-.01em}h2{font-size:clamp(1.7rem,4vw,2.5rem)}h3{font-size:1.35rem}.topic-id{flex:none;padding:.35rem .58rem;color:#075f78;background:var(--cyan-pale);border:1px solid #b9dfe3;border-radius:999px;font-size:.66rem;font-weight:700;cursor:pointer}.topic-id:focus-visible{outline:3px solid var(--yellow);outline-offset:2px}blockquote{margin:1.3rem 0;padding:1.2rem 1.35rem;border-left:.42rem solid var(--yellow);background:#fff6dc;font-size:1.13rem;font-weight:600}pre{overflow:auto;padding:1.2rem;color:#d8edf2;background:#092b43;border-left:.35rem solid var(--cyan);border-radius:.35rem}pre code{padding:0;background:none}.table-wrap{overflow-x:auto}table{width:100%;border-collapse:collapse;font-size:.9rem}th,td{padding:.75rem;border:1px solid var(--line);vertical-align:top}th{color:#fff;background:#155273;text-align:left}tbody tr:nth-child(even){background:#f4f8fa}li+li{margin-top:.35rem}.notice{position:fixed;right:1rem;bottom:1rem;padding:.65rem .9rem;color:#fff;background:var(--blue);border-radius:.35rem;opacity:0;transform:translateY(.5rem);transition:.2s}.notice.show{opacity:1;transform:none}
@media(max-width:850px){.layout{display:block;padding:1rem}.toc{position:relative;top:auto;max-height:none;margin-bottom:1rem}.toc nav{display:grid;grid-template-columns:repeat(2,minmax(0,1fr))}.hero{padding:3.5rem 1.25rem 2.5rem}}@media(max-width:560px){.toc nav{grid-template-columns:1fr}.section-head{display:block}.section-head .topic-id{margin-top:.6rem}.topic-section{padding:1.15rem}h1{font-size:3rem}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important}}@media print{body{background:#fff;font-size:10pt}header{color:var(--ink);background:#fff;border-bottom:2px solid var(--ink)}.hero{padding:1cm 0}.hero:before,.toc,.notice{display:none}.hero p,.eyebrow,.back-link{color:var(--ink)}.layout{display:block;padding:0}.topic-section{break-inside:avoid;box-shadow:none}}
"""


def render_document(source: Path) -> str:
    raw_lines = source.read_text(encoding="utf-8").splitlines()
    metadata, body_lines = split_frontmatter(raw_lines)
    body, topic_id, title = render_markdown(body_lines)
    headings = collect_headings(body_lines)
    toc = "".join(
        f'<a href="#{anchor}" class="level-{level}"><span>{anchor}</span><span>{html.escape(label)}</span></a>'
        for level, anchor, label in headings
        if level > 1
    )
    status = metadata.get("status", "draft")
    duration = metadata.get("duration", "")
    updated = metadata.get("updated", "")
    return f"""<!doctype html>
<!-- Gerado por course/scripts/render_topic.py. Edite o arquivo Markdown de origem. -->
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Conteúdo detalhado {html.escape(topic_id)} — {html.escape(title)}"><title>{html.escape(topic_id)} — {html.escape(title)}</title>
<style>{STYLE}</style></head><body><a class="skip" href="#conteudo">Ir para o conteúdo</a>
<header><div class="hero"><a class="back-link" href="../ementa.html">← Voltar ao mapa do curso</a><p class="eyebrow">{html.escape(topic_id)} · conteúdo detalhado</p><h1>{html.escape(title)}</h1>
<p>Unidade didática do curso Cordel na prática.</p><div class="meta-row"><span class="meta">status: {html.escape(status)}</span><span class="meta">duração: {html.escape(duration)}</span><span class="meta">atualizado: {html.escape(updated)}</span></div></div></header>
<div class="layout"><aside class="toc"><strong>Nesta unidade</strong><nav>{toc}</nav></aside><main id="conteudo">{body}</main></div>
<div class="notice" role="status" aria-live="polite">Identificador copiado</div><script>
const notice=document.querySelector('.notice');let timer;document.addEventListener('click',async e=>{{const b=e.target.closest('[data-copy]');if(!b)return;const value=b.dataset.copy;try{{await navigator.clipboard.writeText(value);notice.textContent=`${{value}} copiado`}}catch(_){{notice.textContent=`Identificador: ${{value}}`}}notice.classList.add('show');clearTimeout(timer);timer=setTimeout(()=>notice.classList.remove('show'),1500)}});
</script></body></html>"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Markdown topic file")
    parser.add_argument("--output", type=Path, help="HTML output path")
    args = parser.parse_args()
    source = args.source.resolve()
    output = args.output.resolve() if args.output else source.with_suffix(".html")
    output.write_text(render_document(source), encoding="utf-8", newline="\n")
    print(f"Rendered {source} -> {output}")


if __name__ == "__main__":
    main()
