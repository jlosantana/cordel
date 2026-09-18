---
id: MOD-05
title: "Cordel como implementação do protocolo"
status: draft
duration: 3 horas
bloco: "II — Controle e método"
ferramenta: "Cordel, a partir deste encontro"
related_objectives:
  - OA-05
  - OA-12
updated: 2026-08-31
---

# MOD-05 — Cordel como implementação do protocolo

## MOD-05-INT — Intenção do módulo

Este é o encontro em que a ferramenta entra — e a ordem importa. A turma passou três
encontros descobrindo controles por conta própria e um encontro desenhando o ambiente que os
sustenta. Agora recebe de volta o protocolo mínimo que escreveu no encontro 3 e o compara,
item a item, com um método pronto.

A comparação é o conteúdo. Um curso que apresentasse o Cordel primeiro ensinaria um
procedimento; apresentando-o depois, ensina um critério — a turma consegue dizer qual problema
cada peça do método resolve, porque sentiu o problema antes.

Ao final, o projeto-laboratório está configurado, sem que seu comportamento funcional tenha
mudado.

## MOD-05-TESE — Tese

> O Cordel é uma resposta possível a um conjunto de problemas reais, não a única. Quem
> entende os problemas consegue avaliar a resposta — e substituí-la quando o contexto exigir.

## MOD-05-OBJ — Resultados de aprendizagem

Ao final, a pessoa participante deverá conseguir:

1. mapear os controles do próprio protocolo contra as peças do Cordel;
2. identificar controles que o método não cobre e que continuam sendo trabalho humano;
3. explicar os princípios do manifesto em linguagem operacional;
4. distinguir fonte da verdade, artefato e projeção;
5. separar requisito, AS-IS, necessidade, story e evidência;
6. distinguir conhecimento de produto, rastro do projeto e contexto local;
7. configurar `.cordel/project.json` sem inventar convenções externas;
8. organizar um índice curto para carregamento de contexto sob demanda;
9. executar `init` e `check` até obter `GO`, sabendo o que esse resultado não significa.

## MOD-05-CON — Conceitos

### MOD-05-CON-01 — Do protocolo ao método

**Princípio.** Times que trabalham com IA convergem para um conjunto pequeno e recorrente de
controles: saber de onde veio o pedido, confirmar o que o sistema faz hoje, separar quem
decide de quem executa, declarar como o resultado será observado, e reconciliar o que ficou
divergente ao final. Um método é a formalização desses controles — com nomes, artefatos e
momentos definidos.

**Prática.** A formalização traz três ganhos e um custo. Ganhos: o controle deixa de depender
de quem está na sala, vira revisável por outra pessoa e pode ser automatizado em parte.
Custo: cerimônia. Um método que exige mais registro do que o risco justifica é abandonado na
primeira semana difícil, e nesse caso o time fica pior do que estava com o protocolo
informal.

**No Cordel.** A cadeia `origem → classificação → AS-IS → decisão → story/spec → gate →
implementação → prova → reconciliação` é a formalização. Os encontros 6 e 7 percorrem-na.

### MOD-05-CON-02 — Manifesto em operação

**Princípio.** Os princípios orientam ações concretas: começar pela origem, separar fatos de
alegações, confirmar o AS-IS, preservar decisão humana, planejar unidade verificável, usar
gates com significado, reconciliar fontes e automatizar mecânica sem delegar julgamento.

**Prática.** Cada um desses princípios já apareceu no curso como problema antes de aparecer
como regra. Ao ler o manifesto, a turma deve conseguir apontar em que momento dos encontros
1 a 4 sentiu a falta de cada um.

### MOD-05-CON-03 — Fonte da verdade

**Princípio.** Local autorizado para manter determinado fato. Autoridade depende de
responsável e escopo. Uma fonte de requisitos não substitui o código como evidência do
comportamento atual.

**Prática.** A pergunta que resolve a maioria das disputas: se este fato mudar, qual arquivo
ou sistema precisa ser alterado para que a mudança valha? Esse é a fonte. Os demais lugares
onde o fato aparece são cópias, e cópias envelhecem.

### MOD-05-CON-04 — Artefato e projeção

**Princípio.** Artefato preserva contexto ou decisão e requer revisão. Projeção é
recalculável: índice, matriz, painel. Quando a projeção diverge, corrige-se a fonte ou o
gerador.

**Prática.** Corrigir a projeção à mão é a tentação mais comum e a mais cara: resolve a
aparência, preserva a divergência e destrói o sinal que a divergência dava.

### MOD-05-CON-05 — Tipos de trabalho

**Princípio.**

- requisito: compromisso externo;
- contexto AS-IS: comportamento atual confirmado;
- necessidade: pedido sem destino ou autorização definidos;
- story: unidade de trabalho autorizada;
- spec: desenho do TO-BE quando necessário;
- evidência: sustentação confirmável de uma afirmação.

**Prática.** A distinção que mais evita erro é entre necessidade e story: a primeira registra
que alguém pediu, a segunda registra que alguém autorizou. Confundi-las é como o escopo cresce
sem que ninguém tenha decidido nada.

### MOD-05-CON-06 — Ciclo de vida documental

**Princípio.** `work/` mantém trabalho ativo; `product/` conhecimento atual e durável;
`archive/` histórico encerrado ou substituído; `generated/` projeções; `local/` notas pessoais
sem autoridade compartilhada.

**Prática.** A separação existe para o agente saber o que pode citar como verdade atual. Um
documento arquivado que continua no meio dos ativos volta como fonte em alguma investigação
futura.

### MOD-05-CON-07 — Núcleo e adaptador

**Princípio.** O núcleo define invariantes portáteis. `.cordel/` declara fontes, comandos,
identificadores, políticas e particularidades do projeto. Convenções de uma arquitetura não
entram silenciosamente no método.

**Prática.** Este é o mecanismo que permite responder à pergunta do encontro 8: o que levo
comigo quando mudo de time? O núcleo. O adaptador fica.

### MOD-05-CON-08 — Engenharia de contexto

**Princípio.** O índice aponta para fontes, não as duplica. O agente começa pelo índice e
carrega somente o necessário para a demanda. Fonte canônica atual prevalece sobre conversa ou
resumo antigo.

**Prática.** É a resposta estrutural ao problema da janela de contexto, apresentado no
encontro 1: em vez de tentar caber tudo, tornar tudo encontrável.

### MOD-05-CON-09 — O que o método não resolve

**Princípio.** Nenhum método elimina ambiguidade de negócio, substitui conhecimento do
domínio, garante que a fonte canônica esteja correta ou impede que um gate mal revisado
formalize uma premissa ruim. O que ele faz é tornar essas falhas visíveis e atribuíveis.

**Prática.** Cada grupo deve terminar o encontro sabendo apontar pelo menos dois controles do
próprio protocolo que continuam sendo trabalho humano depois de instalar a ferramenta.

## MOD-05-DEMO — Demonstração: do protocolo ao método, e do repositório opaco ao legível

### Parte 1 — O confronto, 15 minutos

Projete lado a lado um protocolo mínimo real produzido no encontro 3 e a cadeia do Cordel.
Percorra três categorias, sem defender o método:

- **controles que a turma identificou e o Cordel implementa** — costumam ser a maioria:
  confirmar o comportamento atual, declarar o que fica fora, definir como provar;
- **controles que a turma não identificou** — em geral origem, autorização explícita e
  reconciliação final, que só aparecem quando o trabalho é acompanhado até o fechamento;
- **controles que a turma identificou e o Cordel resolve de forma diferente** — discuta a
  diferença como escolha de projeto, não como correção.

Se um controle do protocolo não existir no método e for bom, isso é matéria do encontro 8.

### Parte 2 — Antes, 5 minutos

Mostre o agente pesquisando um repositório sem configuração: ele precisa descobrir caminhos,
comandos, fontes e autoridade misturando busca e inferência.

### Parte 3 — Inicialização, 5 minutos

Execute:

```bash
python skill/cordel/scripts/cordel.py init /caminho/do/projeto
```

Explique o que foi criado, o que permanece vazio e por que o comando não deve sobrescrever
arquivos existentes.

### Parte 4 — Configuração e verificação, 10 minutos

Preencha um exemplo de fonte, comando e política. Mostre que `kind: url` registra autoridade
externa, mas não prova acesso ou conteúdo. Execute `check`, leia cada erro, corrija a fonte
correspondente e repita até `GO`. Diferencie validação estrutural de confirmação do conteúdo.

## MOD-05-LAB — Laboratório: comparar e configurar

### Etapa 1 — Comparação, 20 minutos

Cada grupo recebe de volta o próprio protocolo mínimo e preenche:

| Controle do protocolo | Problema que o motivou | Peça do Cordel que o cobre | Cobertura |
|---|---|---|---|
| | | | total / parcial / nenhuma / resolvido de outro modo |

Ao final, listar separadamente:

- controles do protocolo sem correspondência no método;
- peças do método sem correspondência no protocolo, com a hipótese de por que a turma não
  chegou nelas.

### Etapa 2 — Inventário de fontes, 15 minutos

Classificar os materiais fornecidos por tipo, autoridade, responsável e escopo. Itens sem
responsável permanecem registrados como lacuna.

### Etapa 3 — Inicialização, 10 minutos

Executar `init` duas vezes e confirmar idempotência. Revisar os arquivos criados antes de
editá-los.

### Etapa 4 — Adaptador, 25 minutos

Preencher nome, repositórios, fontes, armazenamento, identificadores, comandos e políticas.
Não criar identificadores pertencentes a uma fonte externa. Incorporar a política de dados
definida no encontro 4.

### Etapa 5 — Índice e classificação, 20 minutos

Criar `.cordel/index.md` com rotas para contexto, decisões e trabalho, sem copiar o conteúdo
integral das fontes. Distribuir os documentos entre `product`, `work`, `archive`, `generated`
e `local`, justificando autoridade e ciclo de vida.

### Etapa 6 — Check, 10 minutos

Executar até `GO`, preservando uma lista separada de aspectos semanticamente não verificados.
A pergunta de fechamento: o que este `GO` não garante?

## MOD-05-ENT — Entrega

1. tabela de comparação entre protocolo mínimo e Cordel;
2. lista de controles do protocolo sem correspondência no método;
3. lista de controles que continuam sendo trabalho humano após a configuração;
4. `.cordel/project.json` válido;
5. `.cordel/index.md` curto e navegável;
6. estrutura de diretórios coerente;
7. inventário de fontes com responsável e escopo;
8. resultado `GO` do verificador;
9. lista de lacunas que o verificador estrutural não consegue detectar;
10. justificativa de pelo menos uma informação mantida no adaptador e não no núcleo.

## MOD-05-ROTEIRO — Cronograma de 3 horas

| Tempo | Atividade |
|---:|---|
| 0–10 min | devolução dos protocolos mínimos |
| 10–30 min | demonstração: o confronto |
| 30–50 min | do protocolo ao método: ganhos e custo da formalização |
| 50–70 min | fontes, artefatos, projeções e tipos de trabalho |
| 70–85 min | ciclo de vida, núcleo e adaptador, engenharia de contexto |
| 85–95 min | o que o método não resolve |
| 95–105 min | intervalo |
| 105–115 min | demonstração de init, configuração e check |
| 115–135 min | laboratório: comparação |
| 135–150 min | inventário e inicialização |
| 150–172 min | adaptador, índice e classificação |
| 172–180 min | check, entrega e retrospectiva |

## MOD-05-AVAL — Critérios de avaliação

| Critério | Evidência esperada |
|---|---|
| liga peça a problema | cada correspondência justificada pelo problema que a motivou |
| reconhece o não coberto | controles que seguem humanos identificados explicitamente |
| declara autoridade por fonte | responsável e escopo explícitos |
| separa ciclos de vida | ativo, canônico, histórico, gerado e local coerentes |
| evita duplicação | índice aponta, não reescreve fontes |
| preserva portabilidade | regra local permanece no adaptador |
| entende limite do check | `GO` não tratado como verdade semântica |

Relaciona-se a `OA-05` e `OA-12`.

## MOD-05-EQUIVOCOS — Equívocos a observar

- "O protocolo do grupo era o rascunho; o Cordel é a versão certa." São respostas ao mesmo
  problema, com maturidades diferentes. Um controle do protocolo ausente no método pode ser
  uma boa proposta de evolução.
- "Instalar o método resolve os problemas dos encontros 1 a 4." Ele endereça parte deles e
  torna o restante visível.
- "Fonte da verdade é sempre um arquivo local." Pode ser sistema externo com responsável.
- "URL vira verdade porque está no JSON." A configuração declara autoridade, não conteúdo.
- "Projeção pode ser corrigida rapidamente à mão." Isso mascara a fonte divergente.
- "Tudo deve entrar no contexto do agente." Contexto demais reduz pertinência e controle.
- "`GO` significa que o projeto está correto." Significa que invariantes estruturais passaram.
- "Notas locais podem sustentar decisão da equipe." Não possuem autoridade compartilhada.

## MOD-05-MAT — Materiais e preparação

- protocolos mínimos de todos os grupos, do `MOD-03`;
- um protocolo real de turma anterior, ou fictício verossímil, para a demonstração;
- quadro comparativo protocolo × cadeia do Cordel, preparado para projeção;
- projeto sem `.cordel/`;
- conjunto misto de fontes e projeções;
- exemplo de `project.json` válido;
- Python 3.8 ou superior e script `cordel.py` acessível;
- política de dados produzida no `MOD-04`;
- gabarito de autoridade e ciclo de vida;
- uma fonte sem responsável, para discussão;
- falhas estruturais preparadas para o exercício de `check`.

## MOD-05-FONTES — Fontes no método

- [`../../method/manifesto.md`](../../method/manifesto.md)
- [`../../method/concepts.md`](../../method/concepts.md)
- [`../../method/team-knowledge.md`](../../method/team-knowledge.md)
- [`../../method/adoption.md`](../../method/adoption.md)
- [`../../method/project.schema.json`](../../method/project.schema.json)

## MOD-05-PEND — Pendências

- produzir o protocolo mínimo de referência para a demonstração, caso a turma seja a
  primeira;
- montar o quadro comparativo protocolo × Cordel em formato projetável;
- preparar estado inicial do projeto sem `.cordel/`;
- criar conjunto de documentos para classificação;
- definir fontes externas simuladas;
- testar comandos em Windows, Linux e macOS quando aplicável;
- criar gabarito de `project.json` sem expor segredos;
- preparar falhas estruturais para o exercício de `check`;
- validar se a comparação e a configuração cabem no mesmo encontro; se não couberem, a
  configuração pode virar pré-trabalho do encontro 6.
