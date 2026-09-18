#!/usr/bin/env python3
"""Tema, componentes e renderizador comuns aos decks do curso.

Não é executado diretamente: `build_deck.py` importa daqui.

Um deck é uma lista de slides. Cada slide tem um identificador estável, um
título para o índice, um corpo em HTML, notas do apresentador e classes de
apresentação. Os componentes abaixo produzem o HTML de cada tipo de slide.
"""

from __future__ import annotations

import html

# ---------------------------------------------------------------- blocos

BLOCOS = {
    "I": ("Bloco I — Fundamentos", "cyan", "qualquer agente, sem método instalado"),
    "II": ("Bloco II — Controle e método", "yellow", "harness explícito e Cordel"),
    "III": ("Bloco III — Prova e transferência", "red",
            "Cordel e o contexto real de cada pessoa"),
}


def e(texto: str) -> str:
    return html.escape(texto, quote=False)


class Deck:
    """Coleção ordenada de slides."""

    def __init__(self, titulo: str, subtitulo: str = "") -> None:
        self.titulo = titulo
        self.subtitulo = subtitulo
        self.slides: list[tuple[str, str, str, str, str]] = []

    def add(self, sid: str, titulo_indice: str, corpo: str, nota: str = "",
            classe: str = "") -> None:
        self.slides.append((sid, titulo_indice, corpo, nota, classe))


# ---------------------------------------------------------------- peças

def head(eyebrow: str, titulo: str, cor: str = "cyan") -> str:
    return (f'<header class="s-head accent-{cor}">'
            f'<p class="eyebrow">{e(eyebrow)}</p>'
            f'<h2>{e(titulo)}</h2></header>')


def foot(texto: str) -> str:
    return f'<p class="s-foot">{e(texto)}</p>'


def callout(texto: str, tom: str = "cyan") -> str:
    return f'<p class="callout tone-{tom}">{e(texto)}</p>'


def card(rotulo: str, linhas: list[str], cor: str = "cyan") -> str:
    itens = "".join(f"<p>{e(l)}</p>" for l in linhas)
    return f'<article class="card accent-{cor}"><h3>{e(rotulo)}</h3>{itens}</article>'


def tabela(cabecalho: list[str], linhas: list[tuple], classe: str = "") -> str:
    th = "".join(f"<th>{e(c)}</th>" for c in cabecalho)
    corpo = ""
    for linha in linhas:
        tds = ""
        for pos, valor in enumerate(linha):
            cls = ' class="key"' if pos == 0 else ""
            tds += f"<td{cls}>{e(str(valor))}</td>"
        corpo += f"<tr>{tds}</tr>"
    return (f'<div class="table-wrap"><table class="{classe}">'
            f"<thead><tr>{th}</tr></thead><tbody>{corpo}</tbody></table></div>")


def tabela_vazia(cabecalho: list[str], linhas: int = 3, classe: str = "") -> str:
    """Tabela em branco, para a turma preencher durante o laboratório."""
    th = "".join(f"<th>{e(c)}</th>" for c in cabecalho)
    corpo = ("<tr>" + "<td>&nbsp;</td>" * len(cabecalho) + "</tr>") * linhas
    return (f'<div class="table-wrap"><table class="vazia {classe}">'
            f"<thead><tr>{th}</tr></thead><tbody>{corpo}</tbody></table></div>")


# ---- slides de aula ------------------------------------------------

def capa_encontro(numero: str, bloco: str, titulo: str, tese: str) -> str:
    rotulo, cor, ferramenta = BLOCOS[bloco]
    return f"""
      <div class="cover-body">
        <p class="eyebrow">Encontro {e(numero)} · {e(rotulo)}</p>
        <h1>{e(titulo)}</h1>
        <p class="tese-capa">{e(tese)}</p>
        <p class="divider-foot tone-{cor}">{e(ferramenta)}</p>
      </div>"""


def conceito(cid: str, posicao: str, titulo: str, principio: str,
             pratica: str = "", exemplo: str = "", cor: str = "cyan") -> str:
    corpo = head(f"{cid} · {posicao}", titulo, cor)
    corpo += f'<p class="principio">{e(principio)}</p>'
    if pratica:
        corpo += (f'<div class="pratica accent-{cor}"><b>Na prática</b>'
                  f'<p>{e(pratica)}</p></div>')
    if exemplo:
        corpo += f'<p class="exemplo">{e(exemplo)}</p>'
    return corpo


def frase_grande(texto: str, tamanho: int = 32) -> str:
    """Frase destacada em slide claro, sem cabeçalho."""
    return f'<p class="principio" style="font-size:{tamanho}px">{e(texto)}</p>'


def statement(texto: str, autor: str = "") -> str:
    rodape = f'<p class="statement-foot">{e(autor)}</p>' if autor else ""
    return f'<div class="statement"><p>{e(texto)}</p>{rodape}</div>'


def lista_simples(itens: list[str], cor: str = "cyan", numerada: bool = True) -> str:
    tag = "ol" if numerada else "ul"
    lis = "".join(f"<li>{e(i)}</li>" for i in itens)
    return f'<{tag} class="simples tone-{cor}">{lis}</{tag}>'


def par_rotulado(itens: list[tuple[str, str]], cor: str = "cyan",
                 colunas: int = 2) -> str:
    lis = "".join(f'<li class="tone-{cor}"><b>{e(r)}</b>{e(t)}</li>'
                  for r, t in itens)
    uma = " one" if colunas == 1 else ""
    return f'<ul class="dgrid{uma}">{lis}</ul>'


def etapa(numero: int, titulo: str, tempo: str, instrucoes: list[str],
          extra: str = "", cor: str = "blue") -> str:
    passos = "".join(f"<li>{e(i)}</li>" for i in instrucoes)
    return f"""
      <header class="s-head accent-{cor} etapa-head">
        <span class="etapa-num tone-{cor}">{numero}</span>
        <div><p class="eyebrow">Laboratório · {e(tempo)}</p><h2>{e(titulo)}</h2></div>
      </header>
      <ul class="passos">{passos}</ul>{extra}"""


def demo(titulo: str, partes: list[tuple[str, str, str]], observar: list[str],
         cor: str = "cyan") -> str:
    corpo = head("Demonstração do instrutor", titulo, cor)
    linhas = "".join(
        f'<li><span class="demo-t">{e(tempo)}</span>'
        f'<span class="demo-b"><b>{e(nome)}</b>{e(txt)}</span></li>'
        for nome, tempo, txt in partes)
    corpo += f'<ol class="demo">{linhas}</ol>'
    if observar:
        itens = "".join(f"<li>{e(o)}</li>" for o in observar)
        corpo += ('<div class="observar"><b>O que a turma deve observar</b>'
                  f"<ul>{itens}</ul></div>")
    return corpo


def equivocos(pares: list[tuple[str, str]], cor: str = "red") -> str:
    lis = "".join(
        f'<li><p class="mito">“{e(m)}”</p><p class="fato">{e(f)}</p></li>'
        for m, f in pares)
    return f'<ul class="equivocos tone-{cor}">{lis}</ul>'


def checklist(itens: list[str], cor: str = "cyan") -> str:
    lis = "".join(f'<li>{e(i)}</li>' for i in itens)
    return f'<ul class="checklist tone-{cor}">{lis}</ul>'


def roteiro(linhas: list[tuple[str, str]], destaque: list[int] | None = None) -> str:
    destaque = destaque or []
    trs = ""
    for pos, (tempo, atividade) in enumerate(linhas):
        cls = ' class="mark"' if pos in destaque else ""
        trs += (f"<tr{cls}><td class=\"key\">{e(tempo)}</td>"
                f"<td>{e(atividade)}</td></tr>")
    return ('<div class="table-wrap"><table class="roteiro">'
            "<thead><tr><th>Tempo</th><th>Atividade</th></tr></thead>"
            f"<tbody>{trs}</tbody></table></div>")


# ---------------------------------------------------------------- CSS

CSS = """
:root{
  --ink:#13243a; --ink-soft:#43566e; --paper:#f6f8fb; --surface:#fff;
  --line:#d8e0e9; --blue:#164b73; --blue-deep:#092c48; --cyan:#1c8ea0;
  --cyan-pale:#dff5f4; --yellow:#f2bd43; --yellow-pale:#fff5d8;
  --yellow-ink:#96700f; --red:#bb4d4a; --red-pale:#fbeeee; --mist:#c7d8e6;
}
*{box-sizing:border-box}
html,body{margin:0;height:100%;overflow:hidden;background:#0b1a2a}
body{font-family:"Segoe UI Variable Text","Segoe UI","Helvetica Neue",Arial,sans-serif;
  color:var(--ink);-webkit-font-smoothing:antialiased}

#stage{position:absolute;top:50%;left:50%;width:1280px;height:720px;
  transform-origin:center center;background:var(--paper);
  box-shadow:0 30px 90px rgba(0,0,0,.45)}

.slide{position:absolute;inset:0;padding:46px 60px 54px;background:var(--paper);
  display:none;flex-direction:column;justify-content:center;overflow:hidden}
.slide.on{display:flex}
.slide.dark{background:var(--blue-deep);color:#fff;padding-left:94px}
.slide.dark::before{content:"";position:absolute;left:0;top:0;bottom:0;width:14px;
  background:var(--cyan)}
.slide.divider-yellow::before{background:var(--yellow)}
.slide.divider-red::before{background:var(--red)}

.s-head{border-left:6px solid var(--cyan);padding-left:20px;margin:0 0 20px}
.s-head.accent-blue{border-color:var(--blue)}
.s-head.accent-yellow{border-color:var(--yellow)}
.s-head.accent-red{border-color:var(--red)}
.eyebrow{margin:0 0 6px;font-size:12px;letter-spacing:.09em;text-transform:uppercase;
  font-weight:700;color:var(--cyan)}
.accent-blue .eyebrow{color:var(--blue)}
.accent-yellow .eyebrow{color:var(--yellow-ink)}
.accent-red .eyebrow{color:var(--red)}
.s-head h2{margin:0;font-size:33px;font-weight:600;line-height:1.12;
  letter-spacing:-.01em}
.intro{margin:0 0 16px;font-size:15px;color:var(--ink-soft);line-height:1.45}
.s-foot{position:absolute;left:60px;right:60px;bottom:24px;margin:0;
  font-size:11px;color:#8a9bad}

/* capas e divisores */
.cover-body{max-width:960px}
.cover-body .eyebrow{color:var(--cyan);font-size:13px;margin-bottom:18px}
.divider-yellow .cover-body .eyebrow{color:var(--yellow)}
.divider-red .cover-body .eyebrow{color:var(--red)}
.cover-body h1{margin:0 0 20px;font-size:52px;line-height:1.06;font-weight:600;
  letter-spacing:-.02em}
.cover-body .lead{margin:0;font-size:20px;line-height:1.45;color:var(--mist)}
.tese-capa{margin:0;font-size:20px;line-height:1.45;color:var(--mist);
  padding-left:18px;border-left:3px solid rgba(255,255,255,.22);max-width:860px}
.divider-foot{margin:32px 0 0;font-size:14px}
.tone-cyan{color:var(--cyan)}.tone-yellow{color:var(--yellow)}.tone-red{color:var(--red)}
.chips{display:flex;gap:34px;list-style:none;margin:42px 0 0;padding:0}
.chips li{font-size:13px;color:var(--mist);padding-left:12px;
  border-left:4px solid var(--cyan)}
.chips li.tone-yellow{border-color:var(--yellow)}
.chips li.tone-red{border-color:var(--red)}

/* frase de impacto */
.statement{max-width:1020px}
.statement p{margin:0;font-size:36px;line-height:1.3;font-weight:600;
  letter-spacing:-.01em;color:#fff}
.statement-foot{margin:26px 0 0!important;font-size:14px!important;
  font-weight:400!important;color:var(--mist)!important}

/* conceito */
.principio{margin:0 0 22px;font-size:25px;line-height:1.35;font-weight:600;
  color:var(--ink);max-width:1080px}
.pratica{border-left:5px solid var(--cyan);padding:2px 0 2px 20px;max-width:1080px}
.pratica.accent-blue{border-color:var(--blue)}
.pratica.accent-yellow{border-color:var(--yellow)}
.pratica.accent-red{border-color:var(--red)}
.pratica b{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.08em;
  color:var(--cyan);margin-bottom:5px}
.pratica.accent-blue b{color:var(--blue)}
.pratica.accent-yellow b{color:var(--yellow-ink)}
.pratica.accent-red b{color:var(--red)}
.pratica p{margin:0;font-size:17px;line-height:1.5;color:var(--ink-soft)}
.exemplo{margin:20px 0 0;padding:13px 18px;background:var(--surface);
  border:1px solid var(--line);font-size:15px;line-height:1.45;color:var(--ink-soft);
  max-width:1080px}

/* listas */
.simples{margin:0;padding-left:26px;font-size:19px;line-height:1.65;color:var(--ink)}
.simples li{margin-bottom:9px;padding-left:6px}
.simples li::marker{color:var(--cyan);font-weight:700}
.simples.tone-blue li::marker{color:var(--blue)}
.simples.tone-yellow li::marker{color:var(--yellow-ink)}
.simples.tone-red li::marker{color:var(--red)}

.dgrid{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;
  gap:11px 40px}
.dgrid.one{grid-template-columns:1fr;gap:13px}
.dgrid li{border-left:4px solid var(--cyan);padding-left:14px;font-size:15px}
.dgrid li.tone-blue{border-color:var(--blue)}
.dgrid li.tone-yellow{border-color:var(--yellow)}
.dgrid li.tone-red{border-color:var(--red)}
.dgrid li b{display:block;font-size:11px;font-weight:700;text-transform:uppercase;
  letter-spacing:.05em;color:var(--cyan);margin-bottom:1px}
.dgrid li.tone-blue b{color:var(--blue)}
.dgrid li.tone-yellow b{color:var(--yellow-ink)}
.dgrid li.tone-red b{color:var(--red)}

.qgrid{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;
  gap:13px 40px}
.qgrid li{border-left:4px solid var(--cyan);padding-left:14px}
.qgrid .tag{display:block;font-size:11px;font-weight:700;color:var(--cyan);
  letter-spacing:.05em;text-transform:uppercase;margin-bottom:2px}
.qgrid .txt{font-size:16px}

/* laboratório */
.etapa-head{display:flex;gap:20px;align-items:flex-start;border-left:0;padding-left:0}
.etapa-num{flex:0 0 66px;height:66px;line-height:66px;text-align:center;
  font-size:30px;font-weight:700;color:#fff;background:var(--blue)}
.etapa-num.tone-cyan{background:var(--cyan)}
.etapa-num.tone-red{background:var(--red)}
.etapa-head h2{font-size:31px}
.passos{margin:0 0 18px;padding-left:24px;font-size:18px;line-height:1.55;
  color:var(--ink)}
.passos li{margin-bottom:8px}
.passos li::marker{color:var(--blue)}

/* demonstração */
.demo{list-style:none;margin:0 0 20px;padding:0}
.demo li{display:flex;gap:18px;align-items:baseline;margin-bottom:12px}
.demo-t{flex:0 0 78px;font-size:13px;font-weight:700;color:var(--cyan);
  text-align:right;font-variant-numeric:tabular-nums}
.demo-b{font-size:17px;line-height:1.45;color:var(--ink-soft)}
.demo-b b{display:block;color:var(--ink);font-size:18px;margin-bottom:1px}
.observar{background:var(--cyan-pale);padding:15px 20px}
.observar b{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.08em;
  color:var(--blue);margin-bottom:6px}
.observar ul{margin:0;padding-left:20px;font-size:15px;line-height:1.55;
  color:var(--blue)}

/* equívocos */
.equivocos{list-style:none;margin:0;padding:0;display:grid;
  grid-template-columns:1fr 1fr;gap:16px 34px}
.equivocos li{border-left:4px solid var(--red);padding-left:16px}
.equivocos .mito{margin:0 0 4px;font-size:16px;font-weight:600;color:var(--red)}
.equivocos .fato{margin:0;font-size:15px;line-height:1.45;color:var(--ink-soft)}

/* checklist */
.checklist{list-style:none;margin:0;padding:0;display:grid;
  grid-template-columns:1fr 1fr;gap:10px 40px}
.checklist li{position:relative;padding-left:30px;font-size:16px;line-height:1.4}
.checklist li::before{content:"";position:absolute;left:0;top:2px;width:16px;
  height:16px;border:2px solid var(--cyan)}
.checklist.tone-blue li::before{border-color:var(--blue)}

/* cartões e blocos */
.card{background:var(--surface);border:1px solid var(--line);
  border-top:5px solid var(--cyan);padding:16px 20px 14px}
.card.accent-blue{border-top-color:var(--blue)}
.card.accent-yellow{border-top-color:var(--yellow)}
.card.accent-red{border-top-color:var(--red)}
.card h3{margin:0 0 9px;font-size:12px;font-weight:700;text-transform:uppercase;
  letter-spacing:.07em;color:var(--cyan)}
.card.accent-blue h3{color:var(--blue)}
.card.accent-yellow h3{color:var(--yellow-ink)}
.card.accent-red h3{color:var(--red)}
.card p{margin:0 0 6px;font-size:15px;line-height:1.45;color:var(--ink-soft)}
.card p:last-child{margin-bottom:0}
.card p.mid{margin-top:10px;font-size:10px;color:#a3b4c4;font-weight:700;
  letter-spacing:.05em}
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:18px}
.grid-3{display:grid;grid-template-columns:1fr 1fr;gap:14px 20px}
.grid-4{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:16px}

.blocks{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.block{background:var(--surface);border:1px solid var(--line);
  border-top:5px solid var(--cyan);padding:18px 20px;display:flex;flex-direction:column}
.block.accent-yellow{border-top-color:var(--yellow)}
.block.accent-red{border-top-color:var(--red)}
.block-name{margin:0;font-size:12px;font-weight:700;text-transform:uppercase;
  letter-spacing:.05em;color:var(--cyan);min-height:2.6em;line-height:1.3}
.block.accent-yellow .block-name{color:var(--yellow-ink)}
.block.accent-red .block-name{color:var(--red)}
.block-when{margin:0 0 14px;font-size:12px;color:var(--ink-soft)}
.block h3{margin:0 0 14px;font-size:19px;line-height:1.25;font-weight:600}
.block ul{margin:0;padding-left:16px;font-size:14px;color:var(--ink-soft);
  line-height:1.6}
.block-tool{margin:auto 0 0;padding-top:14px;font-size:12px;font-style:italic;
  color:var(--cyan)}
.block.accent-yellow .block-tool{color:var(--yellow-ink)}
.block.accent-red .block-tool{color:var(--red)}

.olist{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}
.olist li{display:flex;gap:18px;align-items:flex-start}
.oid{flex:0 0 74px;text-align:center;padding:8px 0;font-size:13px;font-weight:700;
  color:#fff;background:var(--cyan)}
.oid.tone-blue{background:var(--blue)}
.obody{padding-top:1px;font-size:16px;line-height:1.35}
.obody b{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.06em;
  color:var(--cyan);margin-bottom:2px;font-weight:700}
.olist.accent-blue .obody b{color:var(--blue)}

.chain{list-style:none;display:grid;grid-template-columns:repeat(9,1fr);gap:8px;
  margin:0 0 20px;padding:0}
.chain li{background:var(--surface);border:1px solid var(--line);
  border-top:4px solid var(--cyan);padding:11px 6px;font-size:11px;text-align:center;
  line-height:1.25;color:var(--ink)}
.chain li.tone-yellow{border-top-color:var(--yellow)}
.chain li.tone-red{border-top-color:var(--red)}

/* tabelas */
table{width:100%;border-collapse:collapse;font-size:13px}
thead th{background:var(--blue);color:#fff;text-align:left;padding:9px 12px;
  font-size:12px;font-weight:700}
tbody td{padding:8px 12px;border-bottom:1px solid var(--line);color:var(--ink-soft);
  line-height:1.35;vertical-align:top}
tbody tr:nth-child(even){background:#fbfcfe}
td.key{font-weight:700;color:var(--ink);white-space:nowrap}
table.vazia tbody td{height:36px;border:1px solid var(--line);background:var(--surface)}
table.vazia tbody tr:nth-child(even){background:none}
table.vazia thead th{background:var(--cyan)}
table.roteiro{font-size:15px}
table.roteiro td{padding:7px 14px}
table.roteiro tr.mark td{background:var(--cyan-pale);color:var(--blue);font-weight:600}
table.riscos td:nth-child(2){width:15%}
table.riscos td:nth-child(3){width:22%}
table.riscos td:nth-child(4){width:29%}
table.aval td.key{width:64px}
table.aval td:nth-child(2){width:30%;font-weight:600;color:var(--ink)}

/* callout */
.callout{margin:18px 0 0;padding:15px 20px;background:var(--cyan-pale);
  font-size:15px;font-weight:600;color:var(--blue);line-height:1.4}
.callout.tone-yellow{background:var(--yellow-pale);color:var(--ink)}
.callout.tone-red{background:var(--red-pale);color:var(--ink)}
.callout.big{font-weight:400;color:var(--ink-soft);font-size:14px}
.callout.big b{display:block;font-size:17px;color:var(--ink);margin-bottom:4px}

/* cromo */
#chrome{position:fixed;inset:auto 0 0 0;height:4px;background:rgba(255,255,255,.12);
  z-index:20}
#bar{height:100%;background:var(--cyan);transition:width .2s}
#counter{position:fixed;right:16px;bottom:14px;z-index:21;font-size:12px;margin:0;
  color:rgba(255,255,255,.55);font-variant-numeric:tabular-nums}
#help{position:fixed;left:16px;bottom:14px;z-index:21;font-size:12px;margin:0;
  color:rgba(255,255,255,.38)}
#deckname{position:fixed;left:16px;top:12px;z-index:21;font-size:12px;margin:0;
  color:rgba(255,255,255,.32)}

#notes{position:fixed;left:0;right:0;bottom:0;height:26vh;overflow:auto;
  background:#071523;color:#c9d8e6;border-top:2px solid var(--cyan);padding:16px 22px;
  font-size:14px;line-height:1.55;z-index:30;display:none}
#notes.on{display:block}
#notes b{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.08em;
  color:var(--cyan);margin-bottom:6px}

#index{position:fixed;inset:0;background:rgba(7,21,35,.97);z-index:40;display:none;
  padding:36px 56px;overflow:auto}
#index.on{display:block}
#index h2{color:#fff;font-size:19px;margin:0 0 18px;font-weight:600}
#index ol{list-style:none;margin:0;padding:0;columns:2;column-gap:56px}
#index li{margin-bottom:6px;break-inside:avoid}
#index button{background:none;border:0;color:#c9d8e6;font:inherit;font-size:14px;
  cursor:pointer;text-align:left;padding:3px 0;width:100%}
#index button:hover,#index button.cur{color:var(--cyan)}
#index .n{display:inline-block;width:34px;color:#5d7a93;
  font-variant-numeric:tabular-nums}

@media print{
  @page{size:1280px 720px;margin:0}
  html,body{overflow:visible;background:#fff;height:auto}
  #stage{position:static;transform:none!important;height:auto;box-shadow:none}
  .slide{display:flex!important;position:relative;width:1280px;height:720px;
    break-after:page}
  #chrome,#counter,#help,#notes,#index,#deckname{display:none!important}
}
"""

JS = """
const slides=[...document.querySelectorAll('.slide')];
const notesData=slides.map(s=>s.dataset.notes||'');
const ids=slides.map(s=>s.dataset.sid);
const bar=document.getElementById('bar');
const counter=document.getElementById('counter');
const notes=document.getElementById('notes');
const index=document.getElementById('index');
let i=0;

function fit(){
  const st=document.getElementById('stage');
  const aberto=notes.classList.contains('on');
  const disponivel=aberto?innerHeight*0.74:innerHeight;
  const k=Math.min(innerWidth/1280,disponivel/720)*(aberto?0.94:0.90);
  st.style.transform='translate(-50%,-50%) scale('+k+')';
  st.style.top=aberto?'37%':'50%';
}
function show(n,push){
  i=Math.max(0,Math.min(slides.length-1,n));
  slides.forEach((s,k)=>s.classList.toggle('on',k===i));
  bar.style.width=((i+1)/slides.length*100)+'%';
  counter.textContent=(i+1)+' / '+slides.length;
  notes.innerHTML='<b>Notas do apresentador</b>'+(notesData[i]||'<i>sem notas</i>');
  [...index.querySelectorAll('button')].forEach((b,k)=>b.classList.toggle('cur',k===i));
  if(push!==false) history.replaceState(null,'','#'+ids[i]);
}
addEventListener('keydown',function(ev){
  const k=ev.key;
  if(index.classList.contains('on')&&k!=='o'&&k!=='O'&&k!=='Escape') return;
  if(k==='ArrowRight'||k==='ArrowDown'||k===' '||k==='PageDown'){ev.preventDefault();show(i+1);}
  else if(k==='ArrowLeft'||k==='ArrowUp'||k==='PageUp'){ev.preventDefault();show(i-1);}
  else if(k==='Home'){show(0);}
  else if(k==='End'){show(slides.length-1);}
  else if(k==='n'||k==='N'){notes.classList.toggle('on');fit();}
  else if(k==='o'||k==='O'){index.classList.toggle('on');}
  else if(k==='Escape'){index.classList.remove('on');}
  else if(k==='f'||k==='F'){document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen();}
  else if(k==='p'||k==='P'){print();}
});
addEventListener('click',function(ev){
  if(ev.target.closest('#index')||ev.target.closest('#notes'))return;
  show(i+(ev.clientX<innerWidth*0.25?-1:1));
});
addEventListener('resize',fit);
document.querySelectorAll('#index button').forEach(function(b){
  b.addEventListener('click',function(){show(+b.dataset.go);index.classList.remove('on');});
});
const inicial=ids.indexOf(location.hash.slice(1));
fit();
show(inicial>=0?inicial:0,false);
"""


def render(deck: Deck) -> str:
    corpo = ""
    for sid, _titulo, html_corpo, nota, classe in deck.slides:
        nota_attr = html.escape(nota, quote=True) if nota else ""
        corpo += (f'<section class="slide {classe}" data-sid="{sid}" '
                  f'data-notes="{nota_attr}">{html_corpo}</section>\n')

    itens = ""
    for pos, slide in enumerate(deck.slides):
        itens += (f'<li><button data-go="{pos}"><span class="n">{pos + 1:02d}</span>'
                  f'{e(slide[1])}</button></li>')

    titulo_pagina = deck.titulo
    if deck.subtitulo:
        titulo_pagina += f" — {deck.subtitulo}"

    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{html.escape(titulo_pagina, quote=True)}">
<title>{e(titulo_pagina)}</title>
<!-- Projeção gerada por course/scripts/build_deck.py. Não editar à mão. -->
<style>{CSS}</style>
</head>
<body>
<div id="stage">
{corpo}</div>

<div id="chrome"><div id="bar"></div></div>
<p id="deckname">{e(deck.titulo)}</p>
<p id="counter"></p>
<p id="help">← → navegar · N notas · O índice · F tela cheia · P imprimir</p>
<div id="notes"></div>
<div id="index"><h2>{e(titulo_pagina)}</h2><ol>{itens}</ol></div>

<script>{JS}</script>
</body>
</html>
"""
