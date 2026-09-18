# Conteúdo do curso

## Decks

O curso tem nove decks HTML em [`apresentacao/`](apresentacao/), todos autocontidos,
sem dependência externa — abrem em qualquer navegador, inclusive offline.

| Arquivo | O que é |
|---|---|
| `00-abertura.html` | apresenta o curso: estrutura, objetivos, avaliação. Usado nos primeiros minutos do encontro 1 e como material de apresentação do treinamento. **Não é material de aula.** |
| `encontro-01.html` a `encontro-08.html` | conteúdo de aula de cada encontro: conceitos, demonstração, etapas de laboratório, entrega e fechamento |

Atalhos durante a aula:

| Tecla | Ação |
|---|---|
| `←` `→` `espaço` | navegar entre slides |
| `N` | notas do apresentador |
| `O` | índice, para saltar a qualquer slide |
| `F` | tela cheia |
| `P` | imprimir, ou exportar em PDF |

Cada slide tem uma âncora estável no endereço (`#MOD-03-CON-02`, `#LAB-4`), então dá para
linkar um slide específico. O rodapé de cada slide aponta o arquivo-fonte do conteúdo.

**As notas do apresentador não são opcionais.** Elas carregam a condução: o que observar em
cada etapa, o que não antecipar, o que cortar quando o tempo apertar. Nos decks dos
encontros 1 a 3, carregam também o nível *"No Cordel"* de cada conceito, marcado como
`NÃO PROJETAR` — o Bloco I acontece sem o método na tela, e antecipá-lo destrói o mecanismo
pedagógico do bloco.

Os decks são **projeções**: não edite o HTML gerado. Quando a ementa ou os módulos mudarem,
ajuste o módulo de conteúdo e regenere:

```bash
python course/scripts/build_deck.py               # gera todos
python course/scripts/build_deck.py encontro-03   # gera um só
```

Organização dos scripts:

```text
scripts/deck_theme.py         tema, componentes e renderizador comuns
scripts/deck_abertura.py      apresentação do curso
scripts/deck_encontro_01.py   conteúdo de aula do encontro 1
...                           um módulo por encontro
scripts/build_deck.py         orquestrador
```

> O arquivo `apresentacao/cordel-na-pratica.pptx` corresponde à estrutura antiga do curso e
> foi substituído. Pode ser removido quando não houver mais turmas na versão anterior.

[`ementa.md`](ementa.md) é a fonte textual da ementa e
[`ementa.html`](ementa.html) é sua apresentação navegável.

Cada unidade detalhada possui uma fonte Markdown em `topics/` e uma projeção HTML com o
mesmo nome. Edite sempre o Markdown. Para regenerar a versão HTML:

```bash
python course/scripts/render_topic.py course/topics/CURSO-03.md
```

O renderizador usa os identificadores presentes nos títulos para criar âncoras, índice e
botões de cópia. Preserve o padrão:

```text
## CURSO-03-TESE — Tese central
### PROB-01 — Qual necessidade deu origem à mudança?
```

Não edite manualmente o HTML gerado. Quando o conteúdo mudar, regenere a projeção e valide
os links antes de fechar o trabalho.
