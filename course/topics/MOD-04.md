---
id: MOD-04
title: "Harness, permissões e segurança"
status: draft
duration: 3 horas
bloco: "II — Controle e método"
ferramenta: "harness explícito, ainda sem Cordel"
related_objectives:
  - OA-01
  - OA-04
  - OA-11
updated: 2026-08-31
---

# MOD-04 — Harness, permissões e segurança

## MOD-04-INT — Intenção do módulo

Abrir o Bloco II deslocando o foco do resultado para o ambiente que o produz. Os três
primeiros encontros trataram do que uma pessoa faz diante de um agente. Este trata do que o
ambiente permite que aconteça, mesmo quando ninguém está prestando atenção.

A turma fixa o vocabulário — modelo, agente, ferramenta, skill, script, MCP, harness — e
desenha o ambiente do projeto-laboratório com permissões explícitas. Depois submete esse
desenho a um cenário adversarial: uma instrução hostil plantada em um arquivo que o agente
vai ler.

Este é o encontro que o público da consultoria — órgãos públicos e instituições financeiras
— costuma considerar o mais crítico do curso.

## MOD-04-TESE — Tese

> Capacidade não é autorização. Um bom ambiente torna a ação correta fácil de executar e a
> ação perigosa difícil por acidente.

## MOD-04-OBJ — Resultados de aprendizagem

Ao final, a pessoa participante deverá conseguir:

1. distinguir modelo, agente, ferramenta, skill, script, modelo de documento, MCP e harness;
2. mapear o fluxo entre pedido, contexto, ferramenta, ação e prova;
3. classificar operações em leitura, escrita e publicação;
4. aplicar permissão mínima por etapa em vez de permissão global;
5. reconhecer instrução hostil embutida em conteúdo lido pelo agente;
6. definir o que não pode entrar no contexto por confidencialidade;
7. identificar risco residual sem apresentar controle como garantia absoluta.

## MOD-04-CON — Conceitos

### MOD-04-CON-01 — Modelo

**Princípio.** Componente que interpreta entradas e produz saídas. Pode raciocinar sobre o
contexto recebido, mas não possui sozinho acesso ao repositório, memória operacional ou
autoridade para agir.

**Prática.** Quando alguém diz "o modelo apagou o arquivo", o que houve foi: o modelo emitiu
uma ação, o ambiente a permitiu e a ferramenta a executou. Três elos, três pontos de
controle.

### MOD-04-CON-02 — Agente

**Princípio.** Sistema que usa o modelo para perseguir um objetivo, escolher ações, observar
resultados e iterar. O agente acrescenta ciclo de execução, estado e acesso a ferramentas.

**Prática.** A autonomia do agente é a extensão desse ciclo antes de uma pessoa olhar. É a
variável calibrada no encontro 2 e formalizada aqui.

### MOD-04-CON-03 — Ferramenta

**Princípio.** Capacidade concreta exposta ao agente: ler arquivo, executar teste, consultar
fonte, editar código, publicar artefato. Ferramentas definem o que é tecnicamente possível,
não o que é autorizado em cada situação.

**Prática.** A pergunta de desenho não é "de que o agente precisa?" e sim "o que ele
consegue fazer se interpretar errado?". Uma ferramenta disponível será usada.

### MOD-04-CON-04 — Skill, script e modelo de documento

**Princípio.**

- skill orienta trabalho que exige julgamento;
- script executa transformação ou validação determinística;
- modelo de documento fornece estrutura inicial a ser preenchida com análise.

Uma skill pode invocar scripts e usar modelos, mas não garante que a execução ou a decisão
estejam corretas.

**Prática.** O que puder ser script deve ser script: é reproduzível, testável e barato.
Colocar em skill o que era determinístico introduz variação onde ela não agrega nada.

### MOD-04-CON-05 — MCP

**Princípio.** Protocolo de integração que permite expor ferramentas, recursos e prompts.
Padroniza a conexão; não define qualidade da fonte, permissão de negócio ou método de
desenvolvimento.

**Prática.** Cada servidor é uma fronteira de confiança. O que ele retorna entra no contexto
do agente com o mesmo peso do resto — e foi escrito por alguém que você talvez não conheça.
Conectar um servidor é uma decisão de segurança, não de conveniência.

### MOD-04-CON-06 — Harness

**Princípio.** Infraestrutura que envolve modelo e agente: instruções do repositório,
contexto, skills, ferramentas, integrações, permissões, sandbox, limites, registros, gates e
verificações.

**Prática.** O harness é o único controle que funciona quando ninguém está olhando. Tudo o
que depende de a pessoa lembrar de fazer falha em algum momento; o que está no ambiente,
não.

**No Cordel.** O adaptador do projeto declara fontes, comandos e políticas. É a parte do
harness que fica versionada junto do código.

### MOD-04-CON-07 — Engenharia de contexto

**Princípio.** Seleção deliberada das fontes e instruções relevantes à etapa. Contexto útil é
atual, pertinente, rastreável e carregado sob demanda. Volume não substitui autoridade.

**Prática.** Retomada do encontro 2, agora como propriedade do ambiente e não do operador:
o que o agente carrega por padrão importa mais do que o que uma pessoa lembra de incluir.

### MOD-04-CON-08 — Permissões e guardrails

**Princípio.** Permissão define o que a execução pode fazer. Guardrail verifica ou bloqueia
entradas, ações ou saídas. Nenhum dos dois corrige uma decisão de negócio errada; ambos
reduzem determinados caminhos de falha.

**Prática.** Permissão mínima é por etapa, não por projeto. Investigar exige leitura;
implementar exige escrita no diretório afetado; publicar exige confirmação própria. Conceder
tudo no início porque "vai precisar depois" anula o controle.

### MOD-04-CON-09 — Observabilidade e evals

**Princípio.** Registros permitem inspecionar chamadas, resultados e decisões. Evals medem o
comportamento do agente ou do workflow em tarefas definidas. Testes do produto e evals do
workflow respondem a perguntas diferentes.

**Prática.** Sem registro, um erro de agente é irreproduzível e, portanto, incorrigível. O
mínimo útil: o que foi pedido, que arquivos foram lidos e alterados, que comandos rodaram e
com que resultado.

### MOD-04-CON-10 — Instrução hostil em conteúdo lido

**Princípio.** O agente não distingue, por si, dado de instrução. Um texto que ele lê para
analisar — issue, comentário, log, página, README de dependência, resposta de um servidor —
pode conter uma ordem endereçada a ele. Se esse texto entra no contexto com o mesmo estatuto
das suas instruções, ele pode ser obedecido.

**Prática.** Três controles, em ordem de eficácia:

1. reduzir o alcance da ação — o dano possível é o que as permissões permitem;
2. tratar conteúdo lido explicitamente como dado, nunca como instrução;
3. confirmar ação sensível fora do canal que a sugeriu — se um arquivo pede para enviar algo,
   a confirmação não vem do arquivo.

O padrão mais perigoso combina leitura de conteúdo externo com capacidade de escrita ou
publicação na mesma sessão. Separar as duas coisas custa pouco e remove a maior parte do
risco.

### MOD-04-CON-11 — Dados que não podem entrar no contexto

**Princípio.** O que entra no contexto sai do seu perímetro. Prompts, registros e artefatos
gerados podem ser armazenados, inspecionados e compartilhados de formas que quem colou o
dado não previu. Um dado exposto não volta atrás.

**Prática.** Defina a lista antes, não durante:

| Categoria | Exemplo | Alternativa |
|---|---|---|
| credenciais | token, senha, chave de API, string de conexão | referência ao cofre; nunca o valor |
| dados pessoais | CPF, nome, endereço, dados de cliente | dados fictícios, como `cliente-exemplo.com.br` |
| topologia sensível | IP interno, nome de host, diagrama de rede | faixas de documentação, como `192.0.2.0/24` |
| conteúdo contratual | proposta, valor, cláusula de terceiro | descrição genérica do requisito |

Quando uma credencial aparecer em log ou arquivo enviado, o procedimento é sinalizar,
substituir por marcador e rotacionar a credencial — a substituição no texto não desfaz a
exposição.

**No Cordel.** A política de dados fica declarada no adaptador do projeto, versionada e
revisável, em vez de depender da memória de cada pessoa.

### MOD-04-CON-12 — Risco residual

**Princípio.** Todo controle deixa resto. Um controle apresentado como garantia é pior que
nenhum, porque desliga a atenção.

**Prática.** Para cada controle do mapa, escreva o que ele não cobre e quem decide quando
ele falhar.

## MOD-04-DEMO — Demonstração: a mesma tarefa, três ambientes

Use uma tarefa simples: localizar onde uma regra é aplicada e sugerir uma correção.

### Ambiente A — conversa isolada

O modelo recebe apenas a pergunta. Discuta quais fontes faltam e por que a resposta tende a
ser genérica.

### Ambiente B — agente com leitura

O agente pesquisa repositório e documentação, executa buscas e cita arquivos. Discuta como o
contexto muda a qualidade e quais afirmações ainda são inferências.

### Ambiente C — agente com escrita e execução

O agente pode editar e testar. Antes de permitir, identifique objetivo, escopo,
reversibilidade, prova e ações que ainda exigem confirmação.

O foco não é demonstrar uma ferramenta específica, mas mostrar que a mesma solicitação
produz riscos diferentes conforme o ambiente.

## MOD-04-LAB — Laboratório: desenhar o harness e testá-lo

### Etapa 1 — Inventário, 15 minutos

Listar componentes do ambiente do projeto-laboratório:

| Elemento | Exemplo no projeto | Responsável | Limite conhecido |
|---|---|---|---|
| modelo | | | |
| agente | | | |
| instruções | | | |
| fontes | | | |
| skills | | | |
| ferramentas | | | |
| integrações | | | |
| permissões | | | |
| verificações | | | |

### Etapa 2 — Fluxo de execução, 15 minutos

Desenhar o caminho entre pedido, carregamento de contexto, escolha de ferramenta, observação,
decisão, alteração e prova. Marcar onde existe checkpoint humano.

### Etapa 3 — Política de operações, 20 minutos

Classificar cada operação:

| Operação | Leitura / escrita / publicação | Impacto | Reversível? | Confirmação? |
|---|---|---|---|---|
| | | | | |

### Etapa 4 — Política de dados, 15 minutos

Preencher a lista do que não pode entrar no contexto neste projeto, com a alternativa
correspondente. Revisar os registros produzidos nos encontros 1 a 3 e verificar se algo que
não deveria ter entrado entrou.

### Etapa 5 — Cenário adversarial, 20 minutos

O instrutor planta uma instrução hostil em um arquivo do projeto — um comentário de código,
um item de backlog ou um README de dependência — pedindo ao agente algo fora do escopo, como
ler um arquivo de configuração e incluí-lo na resposta.

O grupo pede ao agente uma análise que exija ler aquele arquivo e observa o que acontece.
Depois responde:

- o agente seguiu a instrução, mencionou ou ignorou?
- se tivesse permissão de escrita ou de rede, qual seria o dano?
- qual controle do mapa teria contido, e qual não teria?
- o que muda na política de permissões depois deste teste?

### Etapa 6 — Revisão cruzada, 5 minutos

Outro grupo tenta identificar capacidade sem autoridade, controle sem evidência ou checkpoint
ausente.

## MOD-04-ENT — Entrega

Mapa do harness contendo:

1. modelo, agente, skills, scripts, ferramentas e MCPs;
2. fontes e fronteiras de confiança;
3. fluxo de contexto e execução, com checkpoints marcados;
4. operações de leitura, escrita e publicação classificadas;
5. permissões mínimas por etapa;
6. lista de dados vedados ao contexto, com alternativas;
7. resultado do cenário adversarial e o que ele mudou na política;
8. registros, testes e evals disponíveis;
9. risco residual por controle e responsável pela decisão.

## MOD-04-ROTEIRO — Cronograma de 3 horas

| Tempo | Atividade |
|---:|---|
| 0–10 min | retomada: do operador para o ambiente |
| 10–40 min | modelo, agente, ferramentas, skill, script e MCP |
| 40–55 min | harness, contexto, permissões e guardrails |
| 55–70 min | instrução hostil em conteúdo lido |
| 70–85 min | dados que não podem entrar no contexto |
| 85–95 min | observabilidade, evals e risco residual |
| 95–105 min | intervalo |
| 105–115 min | demonstração dos três ambientes |
| 115–145 min | inventário, fluxo e política de operações |
| 145–160 min | política de dados |
| 160–175 min | cenário adversarial |
| 175–180 min | revisão cruzada e entrega |

## MOD-04-AVAL — Critérios de avaliação

| Critério | Evidência esperada |
|---|---|
| usa vocabulário sem confundir elementos | mapa com papéis corretos |
| separa capacidade e autoridade | ferramenta não implica autorização |
| aplica menor privilégio | permissões ligadas a etapas concretas |
| trata conteúdo lido como dado | reação correta ao cenário adversarial e mudança na política |
| protege dados | lista específica do projeto, não genérica |
| prevê observação | registros ou checkpoints localizados no fluxo |
| reconhece residual | controle não apresentado como garantia absoluta |

Relaciona-se a `OA-01`, `OA-04` e `OA-11`.

## MOD-04-EQUIVOCOS — Equívocos a observar

- "O modelo acessa o projeto." O acesso é oferecido pelo ambiente e pelas ferramentas.
- "MCP é a ferramenta." MCP é o protocolo; servidor e ferramenta são elementos distintos.
- "Skill executa a tarefa." Skill orienta; execução depende do agente e das ferramentas.
- "Sandbox resolve qualquer risco." Limita certos efeitos, não premissas ou decisões.
- "Analisar autoriza editar." Leitura, escrita e publicação exigem distinção explícita.
- "Mais contexto sempre melhora." Contexto irrelevante ou antigo compete com fontes úteis.
- "Injeção só acontece com conteúdo da internet." Um comentário no próprio repositório, um
  item de backlog ou o README de uma dependência bastam.
- "Se o agente ignorou a instrução hostil, estamos protegidos." O comportamento não é
  determinístico; a proteção é o alcance limitado da ação, não a recusa observada uma vez.
- "Anonimizar depois resolve." Trocar o valor no texto não desfaz a exposição; a credencial
  precisa ser rotacionada.

## MOD-04-MAT — Materiais e preparação

- diagrama incompleto do ambiente;
- lista de ferramentas e permissões reais ou simuladas;
- exemplos de skill, script e modelo de documento;
- cenário com servidor MCP e fronteira de confiança;
- registros de uma execução curta;
- arquivo com instrução hostil plantada, em versão contida e sem efeito real;
- ambiente isolado para o cenário adversarial, sem acesso de rede ou escrita fora do
  laboratório;
- modelo da lista de dados vedados ao contexto;
- modelo do mapa do harness.

## MOD-04-FONTES — Fontes no método

- [`../../method/ai-driven-development.md`](../../method/ai-driven-development.md)
- [`../../method/concepts.md`](../../method/concepts.md)
- [`../../method/team-knowledge.md`](../../method/team-knowledge.md)
- [`CURSO-06.md`](CURSO-06.md)

## MOD-04-PEND — Pendências

- escolher o agente usado no laboratório;
- mapear ferramentas reais disponíveis à turma;
- produzir registros da demonstração;
- escrever a instrução hostil do cenário adversarial de forma didática e contida, e validar
  que o ambiente impede qualquer efeito real;
- definir o procedimento caso um grupo exponha dado sensível durante o curso;
- definir política de permissões do ambiente de treinamento;
- decidir se haverá um servidor MCP real ou somente simulado;
- preparar alternativa quando integrações externas estiverem indisponíveis;
- avaliar se a segurança merece encontro próprio em turmas de setor regulado, o que levaria
  o curso a nove encontros.
