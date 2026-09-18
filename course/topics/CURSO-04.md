---
id: CURSO-04
title: "Objetivos de aprendizagem"
status: draft
duration: 45 minutos de apresentação e uso transversal
related_modules:
  - MOD-01
  - MOD-02
  - MOD-03
  - MOD-04
  - MOD-05
  - MOD-06
  - MOD-07
  - MOD-08
updated: 2026-08-31
---

# CURSO-04 — Objetivos de aprendizagem

## CURSO-04-INT — Intenção da unidade

Esta unidade define o contrato de aprendizagem do curso. Ela explica o que uma pessoa deve
ser capaz de fazer ao final do treinamento e quais evidências permitem reconhecer essa
capacidade.

Os objetivos não servem apenas para abrir a apresentação. Eles orientam a escolha dos
conteúdos, as atividades do projeto-laboratório, o feedback e a avaliação final. Um tópico
que não contribui para nenhum objetivo deve ter sua presença questionada. Um objetivo sem
prática ou evidência correspondente ainda não está coberto pelo curso.

## CURSO-04-TESE — Tese central

> O objeto de aprendizagem é o trabalho com agentes de IA, não uma ferramenta. Cada objetivo
> é enunciado como competência independente de ferramenta; o Cordel aparece como a
> implementação de referência, entre parênteses.

Uma pessoa pode conhecer as definições de agente, skill, evidência e gate e ainda não
conseguir usá-las diante de uma demanda ambígua. Pior: pode executar o procedimento do
Cordel corretamente sem saber qual risco cada etapa mitiga — e, ao mudar de time ou de
ferramenta, não levar nada consigo. Por isso os objetivos são formulados com verbos
observáveis e testados, no encerramento, sem o vocabulário do método.

## CURSO-04-OBJ-GERAL — Objetivo geral

Ao final do curso, a pessoa participante deverá ser capaz de conduzir, com auxílio de agentes
de IA, uma mudança de software rastreável, verificável e proporcional ao risco, e de
transferir esses controles para o próprio contexto de trabalho, tendo o Cordel como
implementação de referência aplicada em um projeto-laboratório.

O objetivo geral combina cinco dimensões:

- **condução:** transformar intenção em tarefa que o agente executa sem inventar decisões;
- **verificação:** decidir, diante de um resultado pronto, o que merece crédito;
- **controle:** contexto, ferramentas e permissões proporcionais ao risco, com segurança;
- **rastro:** origem, decisão, preparação, implementação, prova e reconciliação;
- **transferência:** aplicar os controles em ferramentas que o próprio time já usa.

## CURSO-04-PERFIL — Perfis de entrada e saída

### CURSO-04-PERFIL-ENT — Perfil de entrada

A pessoa participante sabe ler código, usar controle de versão e executar testes, mas pode:

- tratar respostas plausíveis do agente como fatos;
- entregar ao agente a intenção em vez da tarefa, e atribuir o resultado ruim ao modelo;
- decidir com base em uma execução que não conseguiria reproduzir;
- aceitar "os testes passaram" como conclusão suficiente;
- começar uma mudança pela solução técnica;
- confundir necessidade registrada com autorização;
- carregar contexto demais ou contexto sem autoridade clara;
- desconhecer que conteúdo lido pelo agente pode conter instrução endereçada a ele;
- encerrar o trabalho sem atualizar o conhecimento do produto.

Esses comportamentos são hipóteses pedagógicas, não pré-julgamentos sobre a turma. A
atividade diagnóstica do `MOD-01` deve confirmar quais realmente aparecem.

### CURSO-04-PERFIL-SAI — Perfil de saída

A pessoa formada pelo curso consegue:

- explicar por que um agente erra, em termos de mecanismo e não de opinião;
- delimitar a tarefa antes de delegá-la, e reconhecer quando não delegar;
- verificar produção de IA em vez de confiar nela;
- investigar antes de afirmar e tornar inferências e incertezas visíveis;
- preservar decisões humanas e limites de autorização;
- preparar unidades de trabalho observáveis, com prova planejada antes do código;
- operar dentro de permissões proporcionais ao risco e proteger dados sensíveis;
- relacionar critérios a provas pertinentes e reconciliar a entrega com as fontes;
- levar os controles para o próprio time, com ou sem o Cordel;
- melhorar o método sem generalizar uma exceção local.

## CURSO-04-PROGRESSAO — Progressão de competências

Os objetivos formam uma progressão alinhada aos três blocos do curso. Ela não é
completamente linear, mas organiza o percurso.

```text
entender o mecanismo
  -> conduzir
  -> verificar
  -> controlar o ambiente
  -> formalizar em método
  -> provar e reconciliar
  -> transferir e evoluir
```

| Etapa | Bloco | Objetivos predominantes | Pergunta de domínio |
|---|---|---|---|
| Entender o mecanismo | I | OA-01, OA-02 | A pessoa explica por que o agente erra, e não apenas que erra? |
| Conduzir | I | OA-03, OA-09 | Consegue transformar intenção em tarefa executável sem invenção? |
| Verificar | I | OA-05, OA-06, OA-07 | Consegue decidir o que merece crédito diante de um resultado pronto? |
| Controlar o ambiente | II | OA-04, OA-11 | Consegue limitar o que pode acontecer quando ninguém está olhando? |
| Formalizar em método | II | OA-08, OA-10 | Consegue ligar cada peça do método ao problema que ela resolve? |
| Provar e reconciliar | III | OA-06, OA-10, OA-12 | Consegue sustentar o resultado e atualizar o conhecimento durável? |
| Transferir e evoluir | III | OA-02, OA-12 | Consegue aplicar os controles onde o Cordel não existe? |

## CURSO-04-COMPETENCIAS — Competências detalhadas

### OA-01 — Explicar como um agente transforma uma solicitação em ação

**Competência esperada:** descrever modelo, janela de contexto, ferramentas e ciclo de
observação e ação, e explicar por que o resultado não é determinístico.

**Comportamento observável:** diante de um erro do agente, a pessoa atribui a causa a um
mecanismo — contexto ausente, janela esgotada, corte de conhecimento, geração provável — em
vez de a uma qualidade genérica do modelo.

**Evidência de domínio:** tabela de divergência entre execuções preenchida com aspectos
concretos, e mapa comentado do ambiente relacionando cada componente à sua responsabilidade.

**Erro que não demonstra domínio:** dizer que "o modelo acessou o repositório", chamar uma
skill de ferramenta ou assumir que MCP define permissões e política de negócio.

**Desenvolvido principalmente em:** `MOD-01` e `MOD-04`.

### OA-02 — Reconhecer onde a IA gera ganho e quando não usá-la

**Competência esperada:** identificar as etapas em que o agente acelera o trabalho de fato,
aquelas em que o custo de verificação supera o ganho, e os casos em que fazer à mão é a
decisão correta.

**Comportamento observável:** a pessoa evita tanto delegação irrestrita quanto rejeição
genérica; justifica a escolha por custo de revisão, criticidade, confidencialidade ou
necessidade de julgamento com dono.

**Evidência de domínio:** caso concreto, identificado pela própria pessoa, em que não usar IA
é melhor — e, no teste de transferência, a escolha dos três controles prioritários para o
próprio time.

**Erro que não demonstra domínio:** afirmar que a ferramenta "garante qualidade" ou que não
pode ser usada em nenhuma atividade crítica.

**Desenvolvido principalmente em:** `MOD-01`, `MOD-02` e `MOD-08`.

### OA-03 — Conduzir um agente deliberadamente

**Competência esperada:** decompor uma demanda em tarefas com resultado observável e
especificar cada uma com objetivo, restrições, fora do escopo e critério de pronto; escolher
entre refinar a sessão e reiniciá-la.

**Comportamento observável:** a pessoa declara a fronteira antes de acionar o agente,
justifica cada item incluído no contexto e reconhece o momento em que corrigir por cima sai
mais caro que recomeçar.

**Evidência de domínio:** especificação de tarefa completa, registro das intervenções com
causa, e análise que separa lacuna de condução de lacuna de fonte ou decisão.

**Erro que não demonstra domínio:** tratar condução como redação de prompt; deixar o campo
fora do escopo genérico ou vazio.

**Desenvolvido principalmente em:** `MOD-02` e exercitado em `MOD-07`.

### OA-04 — Calibrar autonomia, ferramentas e permissões conforme o risco

**Competência esperada:** escolher o nível de autonomia por tarefa, com base em custo do erro
e reversibilidade, e aplicar permissão mínima por etapa em vez de permissão global.

**Comportamento observável:** a pessoa distingue leitura, escrita e publicação; separa
capacidade de autorização; exige confirmação própria para ação irreversível ou externa.

**Evidência de domínio:** política de operações classificada e política mínima de permissões
ligada a etapas concretas do trabalho.

**Erro que não demonstra domínio:** conceder acesso amplo por conveniência, ou tratar a
autorização para analisar como autorização para modificar.

**No Cordel:** harness declarado e política de permissões versionada no adaptador.

**Desenvolvido principalmente em:** `MOD-04`, introduzido em `MOD-02` e aplicado em `MOD-08`.

### OA-05 — Separar fato, relato, inferência, decisão e evidência

**Competência esperada:** classificar afirmações pelo seu papel e impedir que um relato ou
uma inferência seja promovido silenciosamente a fato confirmado.

**Comportamento observável:** a pessoa marca o que foi relatado, o que concluiu, qual fonte
sustenta a conclusão e o que ainda depende de responsável competente.

**Evidência de domínio:** tabela de classificação com afirmação, natureza, endereço da
evidência e veredito sobre se ela sustenta o que alega.

**Erro que não demonstra domínio:** usar uma story, um resumo do agente ou um link não
verificado como prova técnica.

**No Cordel:** alegação, inferência, evidência declarada e evidência confirmada; alegação não
promove estado.

**Desenvolvido principalmente em:** `MOD-03`, introduzido em `MOD-01`, retomado em `MOD-05`.

### OA-06 — Verificar o que a IA produziu

**Competência esperada:** revisar a diferença contra o escopo declarado, reconhecer padrões
típicos de erro do agente e projetar um teste capaz de falhar.

**Comportamento observável:** a pessoa começa pela lista de arquivos alterados antes do
conteúdo; identifica alteração sem motivo no pedido; introduz um defeito real para confirmar
que o teste acusa.

**Evidência de domínio:** revisão da diferença com arquivos fora do escopo identificados, e
tabela de testes quebrados com veredito de cobertura ou prova.

**Erro que não demonstra domínio:** aceitar cobertura como prova; listar comandos de teste sem
explicar qual critério cada resultado demonstra.

**No Cordel:** estratégia de prova definida no gate, antes da implementação.

**Desenvolvido principalmente em:** `MOD-03` e demonstrado em `MOD-07`.

### OA-07 — Confirmar o comportamento atual antes de propor a mudança

**Competência esperada:** descrever o que o sistema faz hoje com evidências pertinentes em
código, dados, configuração, execução ou testes, delimitando o alcance das buscas.

**Comportamento observável:** a pessoa distingue ausência comprovada de busca incompleta,
registra termos e caminhos consultados e sinaliza drift ou incerteza.

**Evidência de domínio:** afirmações técnicas acompanhadas de endereços que outra pessoa
consegue localizar e revisar, e buscas negativas com alcance declarado.

**Erro que não demonstra domínio:** usar apenas um documento de requisito para afirmar o que a
implementação faz hoje; concluir "não existe" a partir de uma busca cujo alcance não foi
relatado.

**No Cordel:** AS-IS confirmado, exigido antes da decisão.

**Desenvolvido principalmente em:** `MOD-03` e demonstrado em `MOD-06`.

### OA-08 — Localizar a origem e distinguir necessidade de autorização

**Competência esperada:** encontrar o insumo que deu origem à demanda e classificá-la como
defeito, lacuna documental, detalhamento de compromisso existente ou escopo novo, sem
converter pedido em aprovação.

**Comportamento observável:** a pessoa registra o resultado de cada filtro com sustentação e
encaminha a decisão a quem tem competência para tomá-la.

**Evidência de domínio:** análise de triagem com origem acessível, cobertura investigada,
classificação sustentada e decisão necessária identificada.

**Erro que não demonstra domínio:** criar uma story pronta para implementação apenas porque a
necessidade parece útil, ou fabricar a decisão para não travar o trabalho.

**No Cordel:** origem preservada e triagem em filtros ordenados.

**Desenvolvido principalmente em:** `MOD-06`, introduzido em `MOD-01`.

### OA-09 — Transformar um pedido em unidade de trabalho verificável

**Competência esperada:** produzir objetivo observável, escopo, fora do escopo e critérios de
aceite com forma de prova, decidindo quando a complexidade exige desenho adicional.

**Comportamento observável:** a pessoa escreve o objetivo como resultado percebido, não como
atividade técnica; nomeia no fora do escopo aquilo que um leitor razoável inferiria que faz
parte; associa uma verificação a cada critério antes do código.

**Evidência de domínio:** unidade completa, com spec proporcional à complexidade e sem
decisões bloqueantes escondidas.

**Erro que não demonstra domínio:** escrever critérios depois da implementação; confundir
critério com tarefa; criar spec extensa para toda alteração simples.

**No Cordel:** necessidade, story e, quando justificada, spec.

**Desenvolvido principalmente em:** `MOD-06`, introduzido em `MOD-02`.

### OA-10 — Decidir e registrar se há informação suficiente para autorizar

**Competência esperada:** avaliar se as condições para agir estão presentes e registrar essa
avaliação de modo que outra pessoa possa contestá-la.

**Comportamento observável:** a pessoa identifica a decisão, evidência, autorização ou desenho
que falta, e sustenta o bloqueio quando ele é a resposta correta.

**Evidência de domínio:** veredito acompanhado de origem, classificação, comportamento atual,
unidade de trabalho, estratégia de prova, impactos e pendências.

**Erro que não demonstra domínio:** declarar prontidão porque a equipe pretende começar ou
porque o agente já produziu um plano; tratar o resultado como etiqueta de andamento.

**No Cordel:** gate com três resultados — `BLOQUEADO`, `PRONTO PARA ESPECIFICAR`,
`PRONTO PARA IMPLEMENTAR`.

**Desenvolvido principalmente em:** `MOD-06` e revalidado em `MOD-07`.

### OA-11 — Reconhecer riscos de segurança e confidencialidade próprios de agentes

**Competência esperada:** identificar instrução hostil embutida em conteúdo lido, exposição de
dados de cliente e credenciais, e fronteiras de confiança de integrações.

**Comportamento observável:** a pessoa trata conteúdo lido como dado e não como instrução;
define previamente o que não pode entrar no contexto; confirma ação sensível fora do canal
que a sugeriu; reduz o alcance da ação em vez de confiar na recusa do modelo.

**Evidência de domínio:** lista específica de dados vedados ao contexto, com alternativas, e
reação correta ao cenário adversarial, com a mudança que ele provocou na política.

**Erro que não demonstra domínio:** concluir que o ambiente está protegido porque o agente
ignorou a instrução hostil uma vez; acreditar que substituir o valor no texto desfaz a
exposição de uma credencial.

**Desenvolvido principalmente em:** `MOD-04`.

> Este é o único objetivo concentrado em um único módulo. Ver
> [`CURSO-04-COBERTURA`](#curso-04-cobertura) e a pendência correspondente.

### OA-12 — Fechar reconciliando e transferir os controles

**Competência esperada:** atualizar o conhecimento durável após a entrega e traduzir os
controles do curso para as ferramentas e o processo do próprio time.

**Comportamento observável:** a pessoa atualiza o contexto atual, preserva decisões
históricas, regenera projeções e separa entrega de dívida preexistente; depois aloca cada
controle em uma ferramenta que o time já usa e reconhece o que não se aplica hoje.

**Evidência de domínio:** dossiê de fechamento com critérios, provas, fontes atualizadas e
resultado da reconciliação; e teste de transferência com três controles prioritários, cada um
ligado a um problema concreto.

**Erro que não demonstra domínio:** editar uma projeção gerada à mão; encerrar o trabalho
porque o build passou; propor ao próprio time a adoção do método inteiro sem distinguir o que
é inegociável do que é adaptável.

**No Cordel:** reconciliação, e a separação entre núcleo portátil e adaptador do projeto.

**Desenvolvido principalmente em:** `MOD-08`, introduzido em `MOD-05` e praticado em `MOD-07`.

## CURSO-04-MATRIZ — Cobertura por módulo

`I` significa introdução, `P` prática orientada e `D` demonstração de domínio. Uma célula pode
conter mais de uma marca quando o módulo introduz e exercita a mesma competência.

| Objetivo | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 |
|---|---|---|---|---|---|---|---|---|
| OA-01 mecânica do agente | I P | | | D | | | | |
| OA-02 onde a IA ganha, e quando não usar | I | P | | | | | | D |
| OA-03 condução deliberada | | I P D | | | | | P | |
| OA-04 autonomia e permissões | | I | | P D | | | | P |
| OA-05 naturezas da afirmação | I | | P D | | P | | | |
| OA-06 verificar a produção de IA | | | I P | | | | D | |
| OA-07 confirmar o comportamento atual | | | I P | | | D | | |
| OA-08 origem e autorização | I | | | | | P D | | |
| OA-09 unidade verificável | | I | | | | P D | | |
| OA-10 decisão de autorizar | | | | | | I P D | P | |
| OA-11 segurança e confidencialidade | | | | I P D | | | | |
| OA-12 fechamento e transferência | | | | | I | | P | D |

O campo `related_objectives` no cabeçalho de cada módulo lista os objetivos em que aquele
módulo carrega `P` ou `D`. As marcas `I` isoladas não aparecem lá, para não diluir o foco do
módulo.

### CURSO-04-COBERTURA — Leitura da matriz

Uma linha sem `P` ou `D` indica objetivo mencionado, não aprendido. Uma coluna sem relação com
objetivos indica módulo desconectado do propósito do curso. Nesta revisão, duas observações
merecem atenção:

- **`OA-11` aparece em um único módulo.** Segurança e confidencialidade são introduzidas,
  praticadas e demonstradas apenas no `MOD-04`. Para turmas de setor regulado — órgãos
  públicos e instituições financeiras — essa concentração é frágil, e a pendência registrada
  no `MOD-04` prevê avaliar um encontro próprio, o que levaria o curso a nove.
- **O Bloco I concentra as marcas `I`.** É esperado: os três primeiros encontros existem para
  criar o repertório que os demais formalizam. O risco correspondente é o inverso do problema
  que motivou esta revisão — introduzir muito e demonstrar pouco. As demonstrações de `OA-01`,
  `OA-02` e `OA-06` foram deliberadamente empurradas para os blocos II e III por isso.

A matriz deve ser revista sempre que o cronograma mudar.

## CURSO-04-AVALIACAO — Alinhamento com a avaliação

As seis dimensões da avaliação são independentes de ferramenta. Os artefatos do Cordel entram
como evidência, não como critério.

| Dimensão | Peso | Objetivos avaliados |
|---|---:|---|
| Condução do agente | 20% | OA-03, OA-09 |
| Verificação do que a IA produziu | 20% | OA-05, OA-06 |
| Rastreabilidade da decisão | 15% | OA-07, OA-08, OA-10 |
| Implementação e qualidade técnica | 15% | OA-09, OA-10 |
| Segurança e limites de operação | 15% | OA-04, OA-11 |
| Transferência para o próprio contexto | 15% | OA-02, OA-12 |

### CURSO-04-AVALIACAO-DIA — Diagnóstica

No `MOD-01`, uma demanda ambígua é apresentada sem método e sem preparo. A resposta revela o
repertório inicial da turma em `OA-01`, `OA-02`, `OA-05` e `OA-07`. O diagnóstico não compõe
nota; orienta ênfase e ritmo.

### CURSO-04-AVALIACAO-FOR — Formativa

Durante o laboratório, cada artefato recebe feedback enquanto ainda pode melhorar o trabalho
seguinte:

- diagnóstico e tabela de divergência: `OA-01`, `OA-02`;
- especificação de tarefa e registro de intervenções: `OA-03`, `OA-09`;
- auditoria cruzada e protocolo mínimo: `OA-05`, `OA-06`, `OA-07`;
- mapa do harness e política de dados: `OA-01`, `OA-04`, `OA-11`;
- comparação protocolo × método: `OA-05`, `OA-12`;
- triagem, story e gate: `OA-07`, `OA-08`, `OA-09`, `OA-10`;
- implementação e dossiê de prova: `OA-03`, `OA-06`, `OA-10`, `OA-12`.

### CURSO-04-AVALIACAO-SOM — Somativa

O dossiê final e a apresentação demonstram o percurso completo. A proposta de evolução e o
teste de transferência avaliam `OA-02`, `OA-04` e `OA-12`.

A apresentação final tem uma exigência específica: as sete perguntas do problema orientador
devem ser respondidas **sem o vocabulário do Cordel**. Reproduzir corretamente o procedimento
do método sem saber explicar qual risco ele mitiga não caracteriza domínio da competência.

## CURSO-04-NIVEIS — Estados de aprendizagem

Para acompanhar o desenvolvimento sem confundir presença com domínio, cada objetivo pode
receber um dos estados abaixo:

| Estado | Significado |
|---|---|
| `nao-observado` | ainda não houve atividade que permita avaliar |
| `introduzido` | a pessoa reconhece o conceito com apoio |
| `praticado` | executa em atividade orientada e recebe feedback |
| `demonstrado` | executa em situação nova com justificativa e evidência |
| `a-revisar` | a evidência apresenta erro conceitual ou operacional relevante |

Esses estados pertencem ao acompanhamento do curso. Não devem ser confundidos com os estados
de rastreabilidade de uma mudança de software.

## CURSO-04-ATV — Atividade de alinhamento

### Objetivo

Fazer a turma entender o resultado esperado do curso e reconhecer que produzir artefatos não
basta para demonstrar competência.

### Parte 1 — O que seria evidência?, 10 minutos

Distribua três afirmações:

1. "A pessoa entende o que é evidência."
2. "A pessoa preencheu uma tabela de evidências."
3. "A pessoa relacionou um critério de aceite a uma prova acessível e explicou por que ela
   demonstra o comportamento."

Os grupos discutem qual afirmação descreve competência observável e por quê.

### Parte 2 — Mapeamento, 15 minutos

Cada grupo recebe um artefato do projeto-laboratório e responde:

- quais objetivos ele pode ajudar a demonstrar;
- o que precisa estar presente para servir como evidência;
- qual erro tornaria essa evidência insuficiente;
- em qual módulo a competência será praticada.

### Parte 3 — Compromisso individual, 5 minutos

Cada pessoa escolhe dois objetivos que considera mais desafiadores e registra qual evidência
pretende produzir durante o curso. A escolha é retomada no teste de transferência do `MOD-08`.

## CURSO-04-USO — Como usar os objetivos durante o curso

### Para a pessoa participante

- consulte o objetivo antes da atividade;
- saiba qual comportamento será observado;
- peça feedback sobre a competência, não apenas sobre o formato do artefato;
- preserve evidências que demonstrem mudança de entendimento ou decisão;
- use a matriz para reconhecer lacunas antes do encerramento.

### Para o instrutor

- apresente somente os objetivos relevantes no início de cada módulo;
- observe decisões e justificativas, não apenas entregáveis preenchidos;
- devolva feedback usando o identificador do objetivo;
- registre objetivos não observados em vez de presumir domínio;
- ajuste atividades quando uma competência aparece apenas em exposição;
- resista à tentação de antecipar o Cordel nos três primeiros encontros: a ordem é o
  mecanismo pedagógico, não uma limitação de agenda.

### Para quem revisa o curso

- elimine conteúdo que não contribui para objetivo algum;
- acrescente prática quando houver introdução sem demonstração;
- revise o objetivo se nenhuma evidência objetiva puder sustentá-lo;
- não crie novos objetivos apenas para acomodar conteúdo interessante;
- verifique se cada objetivo continua enunciável sem o vocabulário do método;
- mantenha o vocabulário consistente entre ementa, atividades e avaliação.

## CURSO-04-CRITERIOS — Critérios de qualidade dos objetivos

Um objetivo está bem definido quando:

1. descreve uma ação da pessoa participante;
2. pode ser observado em uma situação de trabalho;
3. possui evidência compatível com sua importância;
4. aparece em atividade e avaliação;
5. não depende apenas de memorização de termos;
6. preserva os limites do método e da autoridade humana;
7. é específico o suficiente para orientar feedback;
8. continua aplicável em diferentes tecnologias, domínios **e ferramentas de IA**;
9. permanece enunciável sem citar um artefato do Cordel.

Os dois últimos critérios são novos nesta revisão. São eles que impedem o curso de voltar a
ser um treinamento de ferramenta.

## CURSO-04-EQUIVOCOS — Equívocos a observar

### "Completar todos os modelos demonstra domínio do Cordel."

Os modelos dão estrutura ao trabalho. O domínio aparece nas escolhas, fontes, decisões e
evidências usadas para preenchê-los.

### "Saber operar o método é o objetivo do curso."

O objetivo é o trabalho com agentes. O método é a implementação de referência. Quem sai
sabendo apenas operar a ferramenta não atinge `OA-12`.

### "Objetivos são apenas uma formalidade da ementa."

Sem objetivos observáveis, conteúdo, atividade e avaliação podem medir coisas diferentes.

### "Toda pessoa precisa chegar ao mesmo resultado técnico."

Soluções diferentes podem demonstrar as mesmas competências quando respeitam origem,
autorização, critérios e evidências.

### "Bloqueio significa que a pessoa não conseguiu concluir."

Declarar um bloqueio real, identificar sua causa e evitar implementação indevida pode
demonstrar mais domínio que produzir código baseado em suposição.

### "Um objetivo foi aprendido porque foi explicado."

Exposição introduz vocabulário. Domínio exige aplicação em uma situação na qual a pessoa
precisa escolher, justificar e provar.

## CURSO-04-ROTEIRO — Roteiro sugerido

| Tempo | Etapa | Condução |
|---:|---|---|
| 0–5 min | Contrato | Objetivo geral e a diferença entre conhecer e fazer |
| 5–12 min | Progressão | Percorra as sete etapas e os três blocos |
| 12–22 min | Objetivos | Apresente os 12 objetivos em grupos, não como lista isolada |
| 22–32 min | Atividade | Relacione artefatos, evidências e objetivos |
| 32–38 min | Avaliação | Estados de aprendizagem, pesos e uso do rastro |
| 38–43 min | Compromisso | Cada pessoa escolhe dois objetivos prioritários |
| 43–45 min | Fechamento | Como os identificadores serão usados no feedback |

A matriz volta a aparecer no início e no fim de cada módulo. Os 45 minutos representam a
apresentação inicial; o uso dos objetivos é transversal às 24 horas.

## CURSO-04-MAT — Materiais necessários

- matriz impressa ou digital de objetivos por módulo;
- exemplos de artefato preenchido com e sem evidência suficiente;
- quadro de estados de aprendizagem;
- ficha individual de acompanhamento por objetivo;
- rubrica final do projeto-laboratório;
- rubrica específica para a apresentação final sem o vocabulário do método.

## CURSO-04-FONTES — Fontes no método

- [`../../method/manifesto.md`](../../method/manifesto.md)
- [`../../method/concepts.md`](../../method/concepts.md)
- [`../../method/ai-driven-development.md`](../../method/ai-driven-development.md)
- [`../../method/traceability.md`](../../method/traceability.md)
- [`../../method/adoption.md`](../../method/adoption.md)
- [`../../skill/cordel/references/preparacao.md`](../../skill/cordel/references/preparacao.md)
- [`../../skill/cordel/references/fechamento.md`](../../skill/cordel/references/fechamento.md)

## CURSO-04-PEND — Pontos para a próxima revisão

- os objetivos `OA-01`, `OA-03`, `OA-06` e `OA-11` são novos ou substancialmente reescritos
  nesta revisão e ainda não foram avaliados em turma;
- decidir se `OA-11` merece módulo próprio em turmas de setor regulado;
- criar a ficha de acompanhamento individual por objetivo;
- escrever exemplos de evidência suficiente e insuficiente para cada objetivo;
- definir critérios mínimos para os estados `praticado` e `demonstrado`;
- escrever a rubrica da apresentação final sem o vocabulário do método — é o instrumento que
  mede se o curso deixou de ser sobre a ferramenta;
- testar a atividade com uma turma-piloto e revisar a duração;
- avaliar se `OA-04` precisa de rubricas separadas para autonomia e para permissões.
