# Roteiro de adoção em um projeto-piloto

## 1. Configurar sem mudar o processo ainda

Execute o inicializador, preencha nome, repositórios, fontes e comandos. Rode `check` até
obter `GO`. Nesta fase, apenas torne o projeto legível pelo método.

O inicializador cria `.cordel/`, mas não copia o núcleo do Cordel para o projeto. Versione
o adaptador, o índice e o conhecimento compartilhado; mantenha `local/` e `generated/`
fora do Git.

Instale a skill separadamente com
`python skill/cordel/scripts/cordel.py install`. Esse comando cria o diretório de skills
do Codex e copia o pacote; `python skill/cordel/scripts/cordel.py init <projeto>`, por sua
vez, cria a estrutura `.cordel/` no projeto consumidor e integra as orientações em
`AGENTS.md` e `CLAUDE.md`.
O conteúdo preexistente desses arquivos é preservado; somente o bloco delimitado pelos
marcadores `cordel:start` e `cordel:end` pertence ao inicializador.

Por padrão, os dois arquivos são integrados. Use `--codex`, `--claude`, `--all` ou
`--no-agent-files` para controlar o comportamento. A integração é idempotente e uma
execução posterior atualiza o bloco quando as orientações empacotadas evoluírem.

### Projeto único, monorepo ou workspace agregador

Escolha como raiz do Cordel o menor diretório que contenha todo o escopo das demandas:

- em um projeto único, use a raiz do próprio repositório;
- em um monorepo, use a raiz do monorepo;
- quando vários repositórios irmãos participam das mesmas demandas, use a pasta comum
  que os contém e mantenha nela uma única `.cordel/`.

Preencha `project.repositories` com caminhos relativos à raiz escolhida, por exemplo
`["backend", "frontend", "shared/contracts"]`. O `check` confirma que cada caminho
existe, permanece dentro da raiz e pode ser usado para localizar código e evidências.

Artefatos transversais ficam na `.cordel/` agregadora e devem declarar os repositórios
afetados no campo `scope`. Contexto e decisões exclusivos de um repositório podem ficar
perto do código, desde que sejam registrados como fontes `path` no `project.json`. Não
mantenha configurações Cordel concorrentes para a mesma demanda sem declarar qual delas
é a autoridade.

## 2. Escolher uma demanda real e pequena

Prefira uma mudança com origem conhecida, comportamento atual observável e baixo risco.
Evite usar uma grande iniciativa como primeiro teste, pois problemas de adoção ficam
misturados aos problemas do produto.

## 3. Produzir a cadeia mínima

Registre origem, classificação, evidência AS-IS, story, critério de aceite, estratégia de
prova e evidência final. Crie spec somente se a complexidade justificar.

## 4. Avaliar o método

Ao fechar, registre:

- decisões erradas evitadas;
- informações que ainda precisaram ser redescobertas;
- campos ou gates que não mudaram nenhuma decisão;
- regras locais que pertencem ao adaptador;
- lacunas que apareceram também em outro contexto e podem entrar no núcleo.

## 5. Evoluir com evidência de uso

Não generalize cada exceção do piloto. Ajuste o núcleo somente quando o problema for
recorrente ou representar risco relevante; particularidades permanecem na configuração ou
nas instruções do projeto.

Arquive unidades encerradas, promova descobertas duráveis ao contexto canônico e mantenha
o índice curto. Em equipes ou sistemas distribuídos, siga
[`team-knowledge.md`](team-knowledge.md) para definir a autoridade de cada fonte.
