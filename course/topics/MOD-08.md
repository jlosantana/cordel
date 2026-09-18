---
id: MOD-08
title: "Transferência e evolução"
status: draft
duration: 3 horas
bloco: "III — Prova e transferência"
ferramenta: "Cordel e o contexto real de cada participante"
related_objectives:
  - OA-02
  - OA-04
  - OA-12
updated: 2026-08-31
---

# MOD-08 — Transferência e evolução

## MOD-08-INT — Intenção do módulo

Fechar o curso respondendo à pergunta que decide se ele valeu: o que cada pessoa leva para o
próprio time, que provavelmente não usa a ferramenta ensinada aqui?

A turma faz duas coisas. Primeiro, olha para dentro do método: transforma a experiência do
laboratório em proposta de evolução, distinguindo problema local de lacuna portátil. Depois
olha para fora: cada participante traduz os controles do curso para as ferramentas e o
processo que já usa no trabalho.

A segunda parte é o teste de transferência, e é ele que revela se o curso ensinou princípio
ou procedimento.

## MOD-08-TESE — Tese

> O que se aprende aqui precisa sobreviver à troca de ferramenta, de time e de empresa. O
> método evolui quando uma mudança resolve problema recorrente ou risco relevante e pode ser
> avaliada; particularidades continuam perto do projeto que as exige.

## MOD-08-OBJ — Resultados de aprendizagem

Ao final, a pessoa participante deverá conseguir:

1. distinguir núcleo, adaptador e contexto local;
2. definir autoridade de fontes em um time ou sistema distribuído;
3. identificar atrito útil, desperdício e lacuna de controle;
4. formular hipótese de evolução com evidência de uso;
5. desenhar eval para skill ou workflow;
6. traduzir cada controle do curso para as ferramentas que o próprio time já usa;
7. identificar qual controle é inegociável, qual é adaptável e qual não se aplica ao seu
   contexto;
8. planejar piloto incremental de 30 dias com condições de sucesso e de abandono.

## MOD-08-CON — Conceitos

### MOD-08-CON-01 — Núcleo portátil

**Princípio.** Conjunto de invariantes que resolve o mesmo problema em contextos diferentes:
origem, AS-IS, autorização, unidade verificável, evidência e reconciliação.

**Prática.** Teste de portabilidade: o controle continua fazendo sentido em um time que usa
outra linguagem, outro processo e outra ferramenta de IA? Se depender de um nome de arquivo
ou de um comando, é adaptador.

### MOD-08-CON-02 — Adaptador do projeto

**Princípio.** Declara caminhos, comandos, arquitetura, prefixos, políticas, fontes e
dependências locais. Permite aplicar o núcleo sem embutir tecnologia ou domínio no método.

### MOD-08-CON-03 — Conhecimento federado

**Princípio.** Contexto local ao serviço fica perto do código; requisitos e decisões
transversais podem viver em sistemas especializados. Cada fonte registra responsável e escopo.
Integração não substitui autoridade.

### MOD-08-CON-04 — Sinais para evolução

**Princípio.** Uma mudança no método se justifica quando há:

- decisão errada recorrente;
- informação redescoberta em vários trabalhos;
- risco relevante não coberto;
- campo ou gate que nunca altera decisão;
- regra local repetida em contextos independentes;
- execução inconsistente da mesma skill.

**Prática.** Um caso isolado não é sinal. Preferência pessoal não é sinal. A ausência de sinal
é motivo suficiente para não mudar nada.

### MOD-08-CON-05 — Hipótese e avaliação

**Princípio.** Uma proposta descreve problema, evidência, alcance, alternativa, efeito
esperado e forma de refutação. Evals medem comportamento do agente ou do workflow em casos
representativos.

**Prática.** Sem forma de refutação, a proposta é opinião. A pergunta que fecha qualquer
proposta: que observação me faria concluir que isto não funcionou?

### MOD-08-CON-06 — Versionamento e migração

**Princípio.** Skills e adaptadores possuem versões. Mudança de estrutura precisa de roteiro
de migração, compatibilidade e validação. Conhecimento histórico não é reescrito para parecer
atual.

### MOD-08-CON-07 — Adoção incremental

**Princípio.** Comece tornando o projeto legível, escolha uma demanda pequena, percorra a
cadeia mínima, registre o atrito e só então amplie alcance ou automação.

**Prática.** O erro típico de adoção é começar pelo projeto mais crítico, para "provar valor".
Um piloto pequeno separa problemas do método de problemas do produto; um piloto grande mistura
os dois e o método leva a culpa.

### MOD-08-CON-08 — Tradução para o contexto real

**Princípio.** Um controle não depende do artefato que o carrega. "Registrar quem autorizou o
escopo" pode viver em uma story do Cordel, em um campo do Jira, em um comentário de pull
request ou em uma ata — o que não pode é não existir.

**Prática.** A maior parte dos times não adotará um método inteiro. Adotará dois ou três
controles, nas ferramentas que já usa. Saber quais dois ou três importam mais no seu contexto
é o resultado prático do curso. Correspondências comuns:

| Controle | Onde pode viver sem o Cordel |
|---|---|
| origem preservada | campo de origem no item de backlog; link para o incidente |
| AS-IS confirmado | seção da descrição do pull request com endereços verificáveis |
| autorização explícita | quem aprovou e com que limites, registrado no item |
| escopo e fora do escopo | descrição do item, revisada antes de começar |
| estratégia de prova | critérios de aceite com forma de verificação, antes do código |
| revisão contra escopo | política de revisão que compara arquivos alterados ao pedido |
| reconciliação | atualização de documentação como parte do critério de pronto |

### MOD-08-CON-09 — O que não se transfere

**Princípio.** Alguns controles dependem de condições que nem todo time tem: autoridade para
bloquear, tempo de investigação antes de implementar, fonte canônica com responsável. Fingir
que se aplicam produz cerimônia sem efeito.

**Prática.** Reconhecer o que não se aplica hoje, e sob que condição passaria a se aplicar, é
uma resposta melhor que uma adoção completa e falsa.

## MOD-08-DEMO — Demonstração: três destinos para uma melhoria

Use a proposta "toda story deve incluir o campo schema Oracle afetado". Classifique:

- no projeto Oracle: possível regra do adaptador;
- em projetos sem banco Oracle: sem aplicabilidade;
- no núcleo: inadequada, por ser tecnologia específica.

Extraia o problema portátil subjacente: impactos em dados precisam ser avaliados quando
aplicáveis. Essa formulação pode pertencer ao núcleo; o campo e o vocabulário permanecem no
adaptador.

Depois mostre como testar se um novo checklist realmente evita omissões ou apenas aumenta
preenchimento — a diferença entre controle e cerimônia.

## MOD-08-LAB — Laboratório: retrospectiva, proposta e transferência

### Etapa 1 — Inventário de evidências, 15 minutos

Reunir os registros dos sete encontros: bloqueios, redescobertas, erros evitados, campos sem
efeito, correções do agente, decisões alteradas e a divergência medida no encontro 1.

Incluir a medida do Bloco I: quantos controles do protocolo mínimo o grupo identificou sozinho
antes de conhecer o Cordel.

### Etapa 2 — Classificar problemas, 15 minutos

Para cada item, decidir se é:

- falha do cenário ou da infraestrutura do curso;
- regra local do projeto;
- problema recorrente candidato ao núcleo;
- necessidade de skill, script, modelo ou documentação;
- preferência sem evidência suficiente.

### Etapa 3 — Formular proposta, 20 minutos

Preencher:

| Campo | Conteúdo |
|---|---|
| problema observado | |
| evidência | |
| frequência ou risco | |
| alcance proposto | núcleo / adaptador / local |
| mudança | |
| resultado esperado | |
| custo e risco | |
| avaliação | |
| critério de adoção | |

Propostas vindas de controles do protocolo mínimo sem correspondência no método, identificados
no encontro 5, são candidatas naturais.

### Etapa 4 — Desenhar eval, 15 minutos

Criar ao menos três casos: comum, limite e adversarial. Definir comportamento esperado e
critério mensurável, evitando avaliar somente estilo textual.

### Etapa 5 — Teste de transferência, 25 minutos

Trabalho **individual**, não em grupo — o contexto de cada pessoa é diferente. Cada
participante descreve o próprio time e preenche:

| Controle do curso | Onde viveria no meu time | Ferramenta | Classificação |
|---|---|---|---|
| | | | inegociável / adaptável / não se aplica hoje |

Para cada item marcado como "não se aplica hoje", registrar a condição que precisaria mudar.

Ao final, cada pessoa escolhe **os três controles** que introduziria primeiro no próprio time
e escreve, em duas frases, o problema concreto que espera resolver com cada um. Três é
deliberado: uma lista de doze não é adotada.

### Etapa 6 — Plano de 30 dias, 10 minutos

Definir projeto-piloto, demanda inicial, responsáveis, fontes, comandos, checkpoints, métricas
e a decisão de continuidade — incluindo o que faria o piloto ser abandonado.

## MOD-08-ENT — Entrega

1. retrospectiva baseada no rastro dos oito encontros;
2. classificação entre núcleo, adaptador e local;
3. proposta de evolução com hipótese, evidência e forma de refutação;
4. conjunto inicial de evals;
5. riscos e custo da própria mudança;
6. **teste de transferência individual**, com os três controles prioritários e o problema que
   cada um resolve;
7. plano de adoção de 30 dias com critérios para continuar, ajustar ou abandonar;
8. apresentação final ligando problema, controle, resultado e aprendizado — enunciada sem o
   vocabulário do Cordel, conforme o critério de conclusão do curso.

## MOD-08-ROTEIRO — Cronograma de 3 horas

| Tempo | Atividade |
|---:|---|
| 0–20 min | núcleo, adaptador e conhecimento federado |
| 20–35 min | sinais de evolução, hipótese e refutação |
| 35–50 min | evals, versionamento e adoção incremental |
| 50–70 min | tradução para o contexto real e o que não se transfere |
| 70–85 min | demonstração dos três destinos |
| 85–95 min | intervalo |
| 95–125 min | inventário, classificação e proposta |
| 125–140 min | eval |
| 140–165 min | teste de transferência individual |
| 165–180 min | plano de 30 dias, apresentações e fechamento |

## MOD-08-AVAL — Critérios de avaliação

| Critério | Evidência esperada |
|---|---|
| usa dados do curso | problema ligado a registros reais dos encontros |
| escolhe alcance correto | regra local não promovida sem recorrência |
| formula hipótese | efeito esperado e possibilidade de refutação |
| avalia comportamento | casos e critérios além de estilo |
| traduz sem a ferramenta | controle enunciado e alocado em ferramenta que o time já usa |
| prioriza | três controles escolhidos, com problema concreto por trás |
| reconhece o limite | itens que não se aplicam hoje, com a condição que mudaria isso |
| planeja adoção pequena | demanda, responsáveis, métricas e critério de abandono |
| reconhece custo | melhoria não apresentada como benefício gratuito |

Relaciona-se a `OA-04` e `OA-12`.

## MOD-08-EQUIVOCOS — Equívocos a observar

- "Todo atrito deve ser removido." Alguns pontos existem para preservar decisão ou segurança.
- "Se funcionou no laboratório, entra no núcleo." Um caso não demonstra portabilidade.
- "Mais campos tornam o método completo." Campos sem decisão associada criam ruído.
- "Eval é perguntar se a resposta parece boa." Precisa de tarefa e critério observável.
- "MCP transforma fonte externa em fonte do método." Oferece acesso; a autoridade permanece.
- "Adoção começa pelo maior projeto." Um piloto pequeno separa problemas do método e do
  produto.
- "Transferir é convencer o time a adotar o Cordel." É levar os controles, na ferramenta que
  o time já usa. A ferramenta é uma decisão posterior, e pode ser outra.
- "Se meu time não me deixa bloquear, nada disso se aplica." Parte se aplica; identificar o
  que não se aplica hoje é resposta válida e mais honesta que adoção de fachada.

## MOD-08-MAT — Materiais e preparação

- retrospectivas e artefatos de todos os encontros, por grupo;
- protocolos mínimos anotados no `MOD-05`, com os controles sem correspondência;
- métricas de tempo, bloqueio e retrabalho coletadas ao longo do curso;
- exemplos de regra local e de regra portátil;
- modelo de proposta de evolução;
- modelo de caso de eval;
- modelo do teste de transferência;
- tabela de correspondências entre controles e ferramentas comuns — item de backlog, pull
  request, CI, documentação — como ponto de partida, não como resposta;
- roteiro de adoção de 30 dias;
- rubrica da apresentação final.

## MOD-08-FONTES — Fontes no método

- [`../../method/adoption.md`](../../method/adoption.md)
- [`../../method/team-knowledge.md`](../../method/team-knowledge.md)
- [`../../method/catalog.md`](../../method/catalog.md)
- [`../../source/inventario-experiencias.md`](../../source/inventario-experiencias.md)
- [`CURSO-04.md`](CURSO-04.md)
- [`CURSO-05.md`](CURSO-05.md)

## MOD-08-PEND — Pendências

- o teste de transferência é novo nesta revisão e ainda não foi aplicado em turma;
- escrever o modelo do teste de transferência e a tabela de correspondências;
- decidir se o teste de transferência é entregue ao instrutor ou fica com a pessoa — ele
  contém informação sobre o time de origem, o que levanta questão de confidencialidade;
- criar modelo de proposta de evolução;
- definir formato de eval compatível com o agente escolhido;
- preparar dados fictícios caso a turma não registre atrito suficiente;
- criar rubrica da apresentação final, que precisa avaliar a enunciação sem o vocabulário do
  método;
- definir responsáveis e marcos do plano de 30 dias;
- testar a distinção entre checklist útil e burocracia;
- planejar como os resultados de turmas futuras serão agregados, incluindo a medida de quantos
  controles cada turma identifica sozinha no Bloco I.
