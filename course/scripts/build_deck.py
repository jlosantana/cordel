#!/usr/bin/env python3
"""Gera os decks HTML do curso.

Os decks são projeções: não edite o HTML gerado. Quando a ementa ou os módulos
mudarem, ajuste o módulo de conteúdo correspondente e regenere.

    python course/scripts/build_deck.py            # gera todos
    python course/scripts/build_deck.py 00-abertura
    python course/scripts/build_deck.py encontro-01

Organização:
    deck_theme.py         tema, componentes e renderizador comuns
    deck_abertura.py      apresentação do curso (não é material de aula)
    deck_encontro_01.py   conteúdo de aula do encontro 1
    ...                   um módulo por encontro

Navegação no deck: setas ou espaço para avançar, N para notas do apresentador,
O para o índice, F para tela cheia, P para imprimir em PDF.
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from deck_theme import render  # noqa: E402

# nome do arquivo -> módulo que constrói o deck
DECKS: dict[str, str] = {
    "00-abertura": "deck_abertura",
    "encontro-01": "deck_encontro_01",
    "encontro-02": "deck_encontro_02",
    "encontro-03": "deck_encontro_03",
    "encontro-04": "deck_encontro_04",
    "encontro-05": "deck_encontro_05",
    "encontro-06": "deck_encontro_06",
    "encontro-07": "deck_encontro_07",
    "encontro-08": "deck_encontro_08",
}

PENDENTES: list[str] = []


def gerar(nome: str, destino_dir: Path) -> Path:
    modulo = importlib.import_module(DECKS[nome])
    deck = modulo.build()
    destino = destino_dir / f"{nome}.html"
    destino.write_text(render(deck), encoding="utf-8")
    print(f"  {destino.name:<20} {len(deck.slides):>3} slides")
    return destino


def main() -> None:
    raiz = Path(__file__).resolve().parent.parent
    destino_dir = raiz / "apresentacao"
    destino_dir.mkdir(parents=True, exist_ok=True)

    alvos = sys.argv[1:] or list(DECKS)
    desconhecidos = [a for a in alvos if a not in DECKS]
    if desconhecidos:
        raise SystemExit(f"deck desconhecido: {', '.join(desconhecidos)}\n"
                         f"disponíveis: {', '.join(DECKS)}")

    print("Gerando decks em course/apresentacao/")
    for nome in alvos:
        gerar(nome, destino_dir)

    if not sys.argv[1:] and PENDENTES:
        print(f"\nPendentes ({len(PENDENTES)}): {', '.join(PENDENTES)}")


if __name__ == "__main__":
    main()
