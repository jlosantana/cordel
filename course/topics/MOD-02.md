---
id: MOD-02
title: "Condução: da intenção à tarefa executável"
status: draft
duration: 3 horas
bloco: "I — Fundamentos"
ferramenta: "qualquer agente, sem método instalado"
related_objectives:
  - OA-02
  - OA-03
  - OA-04
updated: 2026-08-31
---

# MOD-02 — Condução: da intenção à tarefa executável

## MOD-02-INT — Intenção do módulo

O encontro anterior mostrou o que acontece quando se entrega uma intenção vaga a um agente.
Este encontro ensina o outro lado: como transformar essa intenção em uma tarefa que o agente
consegue executar sem preencher lacunas por conta própria.

Não se trata de técnicas de redação de prompt. Trata-se de uma competência de engenharia —
decompor trabalho, declarar fronteiras, escolher o que entra no contexto e decidir quanta
autonomia a tarefa merece. É a mesma competência exigida para delegar trabalho a uma pessoa
que acabou de entrar no time, com uma diferença importante: essa pessoa pergunta quando não
entende, e o agente não.

Nenhum método está instalado neste ponto do curso. Tudo aqui se aplica a qualquer agente.

## MOD-02-TESE — Tese

> A maior parte do que se atribui à qualidade do modelo é, na verdade, qualidade da tarefa
> que foi entregue a ele. Uma tarefa mal delimitada não é salva por um modelo melhor.

## MOD-02-OBJ — Resultados de aprendizagem

Ao final, a pessoa participante deverá conseguir:

1. decompor uma demanda em tarefas com resultado observável;
2. escrever uma especificação de tarefa com objetivo, restrições, fora do escopo e critério
   de pronto;
3. escolher deliberadamente o que entra no contexto e justificar cada inclusão;
4. usar exemplos e contraexemplos para fixar formato e convenção;
5. decidir entre refinar a sessão atual e reiniciá-la;
6. calibrar autonomia conforme risco e reversibilidade da ação;
7. reconhecer quando a decisão correta é não usar IA.

## MOD-02-CON — Conceitos

### MOD-02-CON-01 — Decomposição

**Princípio.** Uma demanda não é uma tarefa. "Fazer o sistema avisar quando aprovar" contém
pelo menos quatro tarefas — descobrir onde a aprovação acontece, decidir o canal, implementar
o envio, provar que o aviso chega. Entregar tudo de uma vez força o agente a resolver as
quatro ao mesmo tempo, e ele resolverá as três primeiras por suposição para poder chegar à
quarta.

**Prática.** Quebre até que cada parte tenha um resultado que você consegue observar ao
final. Se você não sabe dizer como saberá que a parte terminou, ela ainda não é uma tarefa.
Tarefas de investigação e tarefas de alteração não se misturam: a primeira produz
informação, a segunda produz mudança.

**No Cordel.** A unidade de trabalho verificável, estudada no encontro 6, é a forma
documentada dessa decomposição.

### MOD-02-CON-02 — Especificação de tarefa

**Princípio.** Quatro elementos tornam uma tarefa executável sem invenção:

- **objetivo** — o resultado percebido, não a atividade técnica;
- **restrições** — o que precisa ser respeitado: convenção, biblioteca, compatibilidade,
  arquivos que não podem ser tocados;
- **fora do escopo** — o que um leitor razoável poderia inferir que faz parte e não faz;
- **critério de pronto** — como se observa que terminou.

**Prática.** O campo mais negligenciado é o fora do escopo, e é o que mais economiza revisão.
O agente tende a "aproveitar e melhorar": renomear, extrair função, ajustar formatação,
corrigir um erro vizinho. Cada uma dessas iniciativas é plausível e nenhuma foi pedida.
Declarar a fronteira custa uma linha e evita metade das diferenças indesejadas.

**No Cordel.** Objetivo observável, escopo, fora do escopo e critérios de aceite são campos
da story. A story é essa especificação com autorização e rastro anexados.

### MOD-02-CON-03 — Seleção do contexto

**Princípio.** Contexto útil é pertinente e atual, não volumoso. Material irrelevante compete
por espaço com o que importa e, pior, sugere caminhos falsos: um arquivo antigo incluído
"por garantia" será tratado como se descrevesse o presente.

**Prática.** Para cada item que você inclui, saiba dizer por que ele está ali. Prefira
apontar o caminho e deixar o agente ler a fonte a colar um trecho que pode estar
desatualizado. Quando a execução revelar uma dependência nova, inclua-a — com motivo.

**No Cordel.** É a engenharia de contexto: um índice curto que aponta para fontes, com
carregamento sob demanda.

### MOD-02-CON-04 — Exemplos e contraexemplos

**Princípio.** Descrever um formato em palavras é caro e ambíguo. Mostrar um caso pronto é
barato e preciso. Um contraexemplo — "assim não" — delimita o que a descrição sozinha deixa
em aberto.

**Prática.** Aponte um arquivo existente que já segue o padrão desejado, em vez de descrever
o padrão. Para convenções que o projeto abandonou, mostre o caso antigo e diga explicitamente
que ele não deve ser seguido; sem isso, o agente encontrará o arquivo antigo sozinho e o
tratará como referência.

### MOD-02-CON-05 — Refinar ou reiniciar

**Princípio.** Quando uma sessão entra em caminho errado, corrigir por cima costuma sair pior
que recomeçar. Toda a trajetória equivocada continua no contexto, e as correções sucessivas
competem com ela. O sintoma clássico: o agente conserta o que você apontou e reintroduz o
problema anterior.

**Prática.** Refine quando o desvio é pontual e o rumo geral está certo. Reinicie quando o
entendimento do problema está errado, quando a mesma correção já foi pedida duas vezes, ou
quando a sessão está longa e as restrições iniciais começaram a ser esquecidas. Ao
reiniciar, leve o que aprendeu — escrito, não de memória.

**No Cordel.** É a razão de a decisão e o critério viverem em arquivo: reiniciar a sessão não
pode custar o conhecimento acumulado.

### MOD-02-CON-06 — Autonomia proporcional ao risco

**Princípio.** Autonomia não é uma configuração global; é uma escolha por tarefa. As
variáveis são o custo do erro e a facilidade de desfazê-lo. Ler código é irreversível apenas
no tempo gasto. Alterar um arquivo versionado é reversível. Escrever em um banco, publicar
ou disparar uma comunicação, não.

**Prática.** Use uma escala explícita:

| Nível | Quando usar | O que o agente faz |
|---|---|---|
| consulta | dúvida, exploração, leitura | responde; nada é alterado |
| proposta | alteração de baixo risco | propõe a diferença; a pessoa aplica |
| execução com checkpoint | trabalho reversível e de escopo definido | executa em passos, com revisão entre eles |
| execução contínua | tarefa mecânica, verificável por comando | executa e reporta ao final |

Ação irreversível ou externa não entra em nenhum nível sem confirmação própria.

**No Cordel.** Vira a política de permissões e os checkpoints, tratados no encontro 4.

### MOD-02-CON-07 — Quando não usar IA

**Princípio.** A delegação compensa quando o custo de executar supera o custo de revisar.
Quando se inverte, o agente vira despesa disfarçada de produtividade.

**Prática.** Casos em que fazer à mão é a decisão correta:

- a alteração é menor que o esforço de descrevê-la;
- você não saberia reconhecer um resultado errado — falta conhecimento do domínio para
  revisar, e aceitar sem revisar não é opção;
- o código é crítico e a revisão exigiria a mesma atenção de escrevê-lo;
- os dados necessários não podem entrar no contexto por confidencialidade;
- a tarefa depende de julgamento que só a pessoa responsável pode exercer.

O último caso não é sobre capacidade técnica. Uma decisão de negócio delegada a um agente
continua sem dono.

## MOD-02-DEMO — Demonstração: a mesma demanda, duas conduções

Retome a demanda do `MOD-01` e conduza-a duas vezes, em voz alta.

### Condução A — repetição do encontro 1, 5 minutos

Solicitação direta, sem preparo. Recupere a resposta preservada no encontro anterior em vez
de executar de novo, para economizar tempo.

### Condução B — deliberada, 15 minutos

Construa diante da turma, nesta ordem:

1. decomposição em tarefas com resultado observável;
2. escolha da primeira tarefa: investigação, não alteração;
3. especificação com objetivo, restrições, fora do escopo e critério de pronto;
4. seleção do contexto, justificando cada item incluído;
5. nível de autonomia escolhido e por quê;
6. execução e leitura do resultado.

### Comparação, 10 minutos

Coloque as duas lado a lado e pergunte à turma: quanto do ganho veio do modelo e quanto veio
da tarefa? Aponte pelo menos uma suposição que a condução B eliminou e pelo menos uma que
ela não eliminou — parte das lacunas depende de fonte ou decisão, não de condução.

## MOD-02-LAB — Laboratório: refazer com condução deliberada

### Cenário

O mesmo do encontro anterior, com a mesma demanda. O agente pode ler e propor; a alteração de
arquivos é permitida somente na etapa 4 e apenas na tarefa escolhida.

### Etapa 1 — Decompor, 15 minutos

Quebrar a demanda em tarefas com resultado observável e classificar cada uma como
investigação ou alteração. Escolher a primeira tarefa a executar e justificar a ordem.

### Etapa 2 — Especificar, 20 minutos

Preencher, para a tarefa escolhida:

| Campo | Conteúdo |
|---|---|
| objetivo observável | |
| restrições | |
| fora do escopo | |
| critério de pronto | |
| contexto incluído e por quê | |
| nível de autonomia e por quê | |

### Etapa 3 — Executar, 25 minutos

Acionar o agente com a especificação. Registrar cada intervenção necessária e sua causa:

| Intervenção | Causa | Era evitável na especificação? |
|---|---|---|
| | lacuna de contexto / fronteira ausente / decisão de negócio / limite do modelo | |

A última coluna é o coração do exercício: separa o que a condução resolve do que exige fonte,
decisão ou verificação — assunto do encontro 3.

### Etapa 4 — Refinar ou reiniciar, 15 minutos

Ao surgir o primeiro desvio relevante, o grupo decide entre corrigir na sessão e recomeçar
com o que aprendeu. A decisão é registrada com a justificativa, e o resultado das duas
abordagens é comparado quando houver tempo.

### Etapa 5 — Comparar, 15 minutos

Confrontar com o resultado do encontro anterior:

- o que a condução deliberada eliminou;
- o que ela não eliminou;
- quanto tempo custou a mais, e se compensou;
- em que ponto desta tarefa fazer à mão teria sido melhor.

## MOD-02-ENT — Entrega

1. decomposição da demanda em tarefas com resultado observável;
2. especificação completa da tarefa executada;
3. registro das intervenções com causa e evitabilidade;
4. decisão de refinar ou reiniciar, com justificativa;
5. análise comparativa entre a condução ingênua e a deliberada;
6. lista do que a condução não resolve — insumo direto para o encontro 3;
7. um caso identificado pelo grupo em que não usar IA seria a decisão correta.

## MOD-02-ROTEIRO — Cronograma de 3 horas

| Tempo | Atividade |
|---:|---|
| 0–10 min | retomada do diagnóstico do MOD-01 |
| 10–35 min | decomposição e especificação de tarefa |
| 35–55 min | seleção de contexto, exemplos e contraexemplos |
| 55–70 min | refinar ou reiniciar; autonomia proporcional ao risco |
| 70–85 min | quando não usar IA |
| 85–100 min | demonstração das duas conduções |
| 100–110 min | intervalo |
| 110–125 min | laboratório: decompor |
| 125–145 min | especificar |
| 145–165 min | executar e decidir sobre reinício |
| 165–180 min | comparar, entregar e retrospectiva |

## MOD-02-AVAL — Critérios de avaliação

| Critério | Evidência esperada |
|---|---|
| decompõe até o observável | cada tarefa com resultado verificável ao final |
| declara fronteiras | fora do escopo preenchido com itens plausíveis, não genéricos |
| justifica o contexto | cada inclusão com motivo; nada incluído "por garantia" |
| calibra autonomia | nível escolhido compatível com reversibilidade |
| distingue causas de intervenção | separa lacuna de condução de lacuna de fonte ou decisão |
| reconhece o limite | identifica caso concreto em que não usar IA é melhor |

Relaciona-se a `OA-02`, `OA-03` e `OA-04`.

## MOD-02-EQUIVOCOS — Equívocos a observar

- "Condução é escrever prompts melhores." É delimitar trabalho. O texto é consequência.
- "Especificar demais engessa o agente." Restrição reduz invenção, não capacidade.
- "Fora do escopo é óbvio." O que é óbvio para quem conhece o projeto é invisível para quem
  vê apenas o texto recebido.
- "Reiniciar é desperdiçar o que já foi feito." Desperdício maior é arrastar um entendimento
  errado por mais dez interações.
- "Mais contexto sempre ajuda." Contexto irrelevante ou antigo compete com o pertinente e
  sugere caminhos falsos.
- "Autonomia é configuração da ferramenta." É decisão por tarefa, baseada em risco e
  reversibilidade.
- "Se a condução foi boa, o resultado está certo." Condução reduz invenção; não substitui
  verificação. É o encontro seguinte.

## MOD-02-MAT — Materiais e preparação

- respostas preservadas do `MOD-01`, por grupo;
- modelo da especificação de tarefa;
- modelo do registro de intervenções;
- escala de autonomia impressa ou projetada;
- exemplo pronto de bom fora do escopo e de fora do escopo vazio;
- arquivo do projeto que segue a convenção atual, para uso como exemplo;
- arquivo que segue convenção abandonada, para uso como contraexemplo;
- ambiente que permita abrir sessões limpas com rapidez;
- lista preparada de casos em que não usar IA é a escolha correta, para a discussão final.

## MOD-02-FONTES — Fontes no método

- [`../../method/ai-driven-development.md`](../../method/ai-driven-development.md)
- [`../../method/concepts.md`](../../method/concepts.md)
- [`CURSO-05.md`](CURSO-05.md)
- [`CURSO-06.md`](CURSO-06.md)

## MOD-02-PEND — Pendências

- este módulo é novo nesta revisão do curso e ainda não foi aplicado em turma;
- escrever a especificação-modelo da tarefa condutora;
- preparar o par exemplo/contraexemplo de convenção no projeto-laboratório;
- definir a escala de autonomia conforme o agente escolhido para o curso;
- testar se as cinco etapas cabem em 70 minutos, ou fundir as etapas 4 e 5;
- criar a rubrica para avaliar a coluna de evitabilidade das intervenções;
- decidir se a etapa 4 executa as duas abordagens ou apenas registra a escolha;
- preparar caso de dados confidenciais para a discussão de "quando não usar IA", articulado
  com o encontro 4.
