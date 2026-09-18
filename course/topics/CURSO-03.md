---
id: CURSO-03
title: "Problema orientador"
status: draft
duration: 75 minutos
related_modules:
  - MOD-01
  - MOD-05
  - MOD-06
  - MOD-07
updated: 2026-08-31
---

# CURSO-03 — Problema orientador

## CURSO-03-INT — Intenção da unidade

Esta unidade estabelece o problema que justifica o restante do curso. A turma deve sair
dela entendendo que a IA não elimina os problemas clássicos da engenharia de software. Ela
reduz o custo de agir sobre eles e, por isso, aumenta tanto a capacidade de entrega quanto
a capacidade de produzir mudanças erradas em pouco tempo.

As sete perguntas formuladas aqui são o currículo real do curso. O Cordel é apresentado
como **uma** resposta de engenharia a elas — não a única, não uma garantia de acerto, não um
substituto do processo decisório e não uma coleção de documentos obrigatórios.

A distinção importa para o desenho do curso: no `MOD-01` esta unidade é usada sem que o
método seja nomeado como solução. A turma constrói o próprio protocolo no `MOD-03` e só
encontra o Cordel no `MOD-05`, já sabendo que problema ele resolve.

## CURSO-03-TESE — Tese central

> Agentes de IA reduzem o custo de pesquisar, explicar, planejar, escrever, testar e
> revisar software. O mesmo ganho reduz o intervalo entre uma premissa errada e uma
> alteração concreta.

Antes da IA, uma ideia mal compreendida podia demorar dias para se transformar em código.
Nesse intervalo, conversas, refinamentos, revisões e dificuldades técnicas criavam ocasiões
para que o erro fosse percebido. Esse processo era lento e não era necessariamente bom,
mas continha pontos naturais de fricção.

Com agentes, parte dessa fricção desaparece. Uma pessoa pode apresentar uma frase curta,
receber uma interpretação, um plano, uma implementação e testes na mesma sessão. Quando a
interpretação está correta, isso é uma vantagem importante. Quando está errada, toda a
cadeia pode apenas tornar o engano mais convincente.

O problema orientador do curso, portanto, não é “como gerar mais código com IA?”. É:

> Como aproveitar a velocidade dos agentes sem perder a ligação entre a necessidade
> original, as decisões humanas, o comportamento real do sistema e a prova do resultado?

## CURSO-03-OBJ — Objetivos específicos

Ao final desta unidade, a pessoa participante deverá ser capaz de:

1. explicar por que produtividade local não equivale a resultado correto;
2. distinguir problemas preexistentes da engenharia de software de riscos ampliados pela
   IA;
3. reconhecer quando uma resposta tecnicamente plausível depende de premissas ainda não
   verificadas;
4. explicar por que necessidade, autorização, implementação e prova são coisas diferentes;
5. usar as sete perguntas do problema orientador para avaliar uma mudança;
6. descrever o papel de um método sem atribuir a ele garantias que não oferece;
7. responder às sete perguntas sem depender do vocabulário de uma ferramenta específica.

## CURSO-03-CONTEXTO — O problema já existia antes da IA

Projetos de software sempre conviveram com requisitos ambíguos, conhecimento espalhado,
documentação desatualizada, decisões não registradas, ambientes divergentes e testes que
não demonstram o que o negócio realmente precisa. Também sempre foi possível implementar
uma solução tecnicamente boa para o problema errado.

A IA não é a origem desses problemas. Ela altera três propriedades do trabalho:

### CURSO-03-CONTEXTO-01 — Velocidade

O tempo entre pedido e alteração diminui. Há menos oportunidades naturais para questionar
a interpretação antes que ela apareça como código funcional.

### CURSO-03-CONTEXTO-02 — Escala

Uma única pessoa consegue explorar e modificar áreas maiores do sistema. O ganho de alcance
também amplia o impacto de uma premissa incorreta.

### CURSO-03-CONTEXTO-03 — Plausibilidade

O agente apresenta explicações, planos, código e testes de forma coerente mesmo quando a
base factual está incompleta. Coerência textual e correção técnica não são equivalentes.

### CURSO-03-CONTEXTO-04 — Autonomia operacional

Quando recebe ferramentas, o agente deixa de apenas sugerir e passa a observar ou alterar
sistemas. A diferença entre analisar, escrever e publicar se torna uma questão de
autoridade e segurança, não apenas de qualidade da resposta.

## CURSO-03-DUPLO-EFEITO — O duplo efeito da IA

| Capacidade | Benefício possível | Falha correspondente |
|---|---|---|
| Pesquisar rapidamente | localizar código e documentos relevantes | selecionar uma fonte antiga e tratá-la como verdade atual |
| Explicar sistemas | reduzir o tempo para formar entendimento inicial | preencher lacunas com uma narrativa plausível |
| Planejar mudanças | antecipar impactos e decompor trabalho | planejar sobre um AS-IS não confirmado |
| Gerar código | reduzir trabalho mecânico e acelerar experimentos | implementar escopo não autorizado com grande velocidade |
| Criar testes | ampliar feedback e cobertura | testar a interpretação do agente, não o comportamento esperado |
| Atualizar documentação | registrar descobertas durante o trabalho | propagar uma conclusão falsa por várias fontes |
| Operar ferramentas | executar ciclos completos de engenharia | realizar ações externas sem autoridade suficiente |

A leitura correta da tabela não é evitar essas capacidades. É associar cada uma delas a
fontes, limites, decisões e verificações proporcionais ao risco.

## CURSO-03-PERGUNTAS — As sete perguntas de controle

As perguntas abaixo formam o problema operacional que o Cordel procura tornar visível.
Elas não são uma sequência de formulário. Cada uma protege uma distinção importante.

### PROB-01 — Qual necessidade deu origem à mudança?

Sem origem, o agente pode resolver uma formulação que já perdeu parte do contexto. A origem
permite voltar ao pedido, documento, incidente ou decisão e entender por que o trabalho
existe.

- **Falha típica:** começar pela busca de arquivos depois de receber uma frase isolada.
- **Controle do Cordel:** localizar a origem antes de tratar a demanda como trabalho.
- **Sinal observável:** existe uma fonte acessível, com autoria, data ou contexto suficiente
  para orientar a análise.

### PROB-02 — O que é fato, relato, inferência ou decisão?

Uma pessoa pode relatar que “o sistema não envia notificações”. Isso é um insumo valioso,
mas ainda não prova o comportamento do sistema. O agente pode inferir uma causa, mas a
inferência precisa continuar identificada como tal.

- **Falha típica:** transformar uma afirmação repetida em fato confirmado.
- **Controle do Cordel:** separar alegação, inferência, evidência e decisão.
- **Sinal observável:** cada afirmação técnica relevante indica seu estado e sua sustentação.

### PROB-03 — O que o sistema realmente faz hoje?

Documentos de requisito descrevem compromissos ou expectativas. Código, dados, configuração
e testes ajudam a confirmar o comportamento atual. Projetar o TO-BE sem investigar o AS-IS
faz a solução depender de uma premissa invisível.

- **Falha típica:** concluir que algo não existe porque nenhuma story foi encontrada.
- **Controle do Cordel:** investigar o AS-IS e registrar evidência localizável.
- **Sinal observável:** outra pessoa consegue abrir a evidência e confirmar a afirmação.

### PROB-04 — Quem autorizou a mudança de escopo?

Descobrir uma necessidade não concede autoridade para implementá-la. Um agente pode apontar
alternativas e impactos, mas não assume sozinho compromissos de produto, risco ou prazo.

- **Falha típica:** converter automaticamente uma melhoria razoável em story pronta.
- **Controle do Cordel:** decisão humana explícita para escopo novo.
- **Sinal observável:** a decisão, o responsável e os limites da autorização estão
  registrados.

### PROB-05 — Como o resultado esperado será observado?

Expressões como “melhorar”, “corrigir” ou “funcionar corretamente” não definem uma condição
de conclusão. O resultado precisa ser observável antes que a implementação comece.

- **Falha típica:** escrever critérios depois do código para descrever o que foi feito.
- **Controle do Cordel:** critérios de aceite objetivos e estratégia de prova antecipada.
- **Sinal observável:** cada critério descreve comportamento e possui uma forma prevista de
  verificação.

### PROB-06 — Qual prova sustenta a afirmação de que terminou?

Código alterado, story concluída e teste executado são informações sobre o trabalho. Só se
tornam evidência do resultado quando demonstram especificamente o critério alegado.

- **Falha típica:** tratar o status “concluído” como prova de comportamento.
- **Controle do Cordel:** evidência acessível, atual e semanticamente pertinente.
- **Sinal observável:** é possível percorrer o caminho do critério até a prova correspondente.

### PROB-07 — Como fontes, código e testes voltarão a concordar?

Uma entrega pode corrigir o código e deixar a documentação antiga. Também pode atualizar
uma matriz sem corrigir a fonte que a alimenta. O ciclo termina quando o conhecimento
durável, a implementação e as evidências descrevem o mesmo estado.

- **Falha típica:** encerrar após os testes sem atualizar o contexto canônico.
- **Controle do Cordel:** reconciliação e regeneração de projeções no fechamento.
- **Sinal observável:** fontes canônicas, implementação, testes e visões derivadas não
  apresentam divergências conhecidas sobre o comportamento entregue.

## CURSO-03-CADEIA — Uma resposta possível: a cadeia do Cordel

> Esta seção não é usada no `MOD-01`. Ela entra no `MOD-05`, depois que a turma escreveu o
> próprio protocolo mínimo, e serve de base para o confronto entre os dois.

O Cordel organiza as perguntas em uma cadeia rastreável:

```text
demanda
  -> origem
  -> classificação
  -> AS-IS confirmado
  -> decisão humana, quando necessária
  -> story e spec, quando aplicável
  -> gate
  -> implementação e testes
  -> evidência final
  -> reconciliação
```

Cada elo evita uma substituição indevida:

| Elemento | Não substitui |
|---|---|
| Necessidade | autorização |
| Requisito | confirmação do AS-IS |
| Story | prova de implementação |
| Spec | origem ou decisão de negócio |
| Teste executado | evidência de todo critério de aceite |
| Matriz ou dashboard | fonte da verdade |
| Agente | responsável por decisão de produto |

O método permite que etapas simples tenham poucos artefatos. O que não pode desaparecer é a
distinção que cada elo protege — e essa distinção é portátil: pode ser preservada em um item
de backlog, em um pull request ou em uma ata, desde que exista. É esse o objeto do teste de
transferência no `MOD-08`.

## CURSO-03-CASO — Caso condutor

Use a seguinte demanda para apresentar o problema:

> “O sistema deve avisar quando uma solicitação for aprovada.”

À primeira vista, o pedido parece suficiente para implementar uma notificação. Antes de
agir, porém, a turma deve lidar com perguntas como:

- “avisar” significa e-mail, mensagem interna, evento ou outra ação?
- quem deve ser avisado?
- qual estado representa aprovação?
- o sistema já produz algum aviso em parte do fluxo?
- existe requisito assumindo esse comportamento?
- trata-se de defeito, lacuna de documentação ou escopo novo?
- quem pode autorizar o novo custo operacional e o tratamento de dados?
- como a turma provará que a pessoa correta recebeu o aviso uma única vez?

### CURSO-03-CASO-A — Resposta rápida, mas frágil

O agente procura o ponto em que o status muda para “aprovado”, adiciona o envio de e-mail e
cria um teste unitário que verifica a chamada ao serviço de mensagens. A solução compila e o
teste passa.

Ainda não sabemos se e-mail era o canal esperado, se o destinatário está correto, se o
comportamento já existia em outro componente, se a mudança foi autorizada ou se o teste
demonstra o resultado para o usuário.

### CURSO-03-CASO-B — Resposta controlada

O agente localiza a origem, separa relato de evidência, investiga o fluxo atual e classifica
a demanda. Se houver escopo novo, apresenta as decisões necessárias. Depois da autorização,
prepara critérios observáveis e a estratégia de prova, declara o gate e só então implementa.
No fechamento, relaciona cada aceite à evidência e atualiza o contexto AS-IS.

A segunda resposta pode produzir o mesmo código da primeira. A diferença está na confiança
justificada de que esse código corresponde à necessidade autorizada.

## CURSO-03-ATV — Atividade prática

### Objetivo

Fazer a turma experimentar como uma resposta coerente pode esconder decisões e premissas.

### Organização

- grupos de duas ou três pessoas;
- uma demanda curta e ambígua por grupo;
- acesso parcial ao projeto-laboratório;
- quadro com quatro colunas: `afirmação`, `tipo`, `evidência disponível`, `decisão necessária`.

### Rodada 1 — Resposta imediata, 10 minutos

Cada grupo pede ao agente um plano de implementação sem fornecer o Cordel ou as sete
perguntas. O grupo marca no plano:

- fatos que possuem fonte;
- inferências apresentadas como fatos;
- escolhas técnicas razoáveis, mas ainda não autorizadas;
- critérios de conclusão criados pelo próprio agente.

### Rodada 2 — Controle, 15 minutos

O grupo reapresenta a demanda usando as sete perguntas. Não é necessário responder a todas.
É aceitável concluir que faltam origem, acesso, evidência ou decisão.

### Comparação, 10 minutos

Os grupos comparam as duas respostas e registram:

1. quais suposições ficaram visíveis;
2. qual ação teria sido executada cedo demais;
3. qual evidência precisa ser buscada;
4. qual decisão pertence a uma pessoa responsável;
5. se o resultado atual é `BLOQUEADO`, `PRONTO PARA ESPECIFICAR` ou
   `PRONTO PARA IMPLEMENTAR`.

### Produto da atividade

Um diagnóstico curto que demonstre pelo menos uma diferença entre plausibilidade e
evidência, e uma diferença entre necessidade e autorização.

## CURSO-03-ROTEIRO — Roteiro sugerido para o instrutor

| Tempo | Etapa | Condução |
|---:|---|---|
| 0–5 min | Abertura | Apresente a demanda do caso e peça soluções imediatas |
| 5–15 min | Tensão | Mostre como várias soluções plausíveis dependem de decisões diferentes |
| 15–25 min | Tese | Explique velocidade, escala, plausibilidade e autonomia |
| 25–40 min | Estrutura | Percorra as sete perguntas de controle |
| 40–50 min | Cordel | Relacione perguntas, cadeia mínima e gates |
| 50–60 min | Atividade, rodada 1 | Resposta imediata e marcação de premissas |
| 60–70 min | Atividade, rodada 2 | Nova análise com as sete perguntas |
| 70–75 min | Fechamento | Registre a principal mudança de percepção da turma |

## CURSO-03-MENSAGENS — Mensagens essenciais

- Velocidade de produção não é velocidade de aprendizado sobre o problema.
- Uma resposta plausível pode estar tecnicamente correta e ainda resolver o problema errado.
- Mais documentação não resolve falta de autoridade ou de evidência.
- A necessidade explica por que investigar; não autoriza automaticamente uma mudança.
- O gate não é burocracia de status. Ele declara se ainda existe uma decisão bloqueante.
- Estar implementado não significa estar verificado.
- O Cordel reduz riscos e torna incertezas visíveis; não remove a necessidade de julgamento.

## CURSO-03-EQUIVOCOS — Equívocos a observar

### “Se os testes passam, a mudança está correta.”

Os testes demonstram as condições que foram codificadas. Eles podem confirmar uma
interpretação incorreta ou cobrir apenas parte do resultado esperado.

### “O agente deveria descobrir tudo sozinho.”

O agente pode investigar fontes e apresentar alternativas. Ele não deve inventar uma
decisão de negócio nem assumir acesso ou autoridade que não recebeu.

### "Existe um método que resolve isso."

Um método formaliza controles e os torna revisáveis. Ele não elimina ambiguidade de negócio,
não substitui conhecimento de domínio e não garante que a fonte canônica esteja correta. O que
faz é tornar essas falhas visíveis e atribuíveis.

### "O Cordel serve para impedir o agente de programar."


O método procura permitir implementação autônoma quando o trabalho está realmente pronto.
Bloqueios honestos tornam mais segura a autonomia posterior.

### “Toda mudança precisa de uma spec extensa.”

Mudanças simples podem ser conduzidas com origem, AS-IS, story, critérios e prova. A spec é
usada quando a complexidade ou o risco exigem desenho adicional.

### “Evidência é qualquer link incluído na análise.”

Um endereço é evidência declarada. Ele só sustenta a afirmação quando está acessível, atual
e demonstra semanticamente o fato alegado.

## CURSO-03-AVAL — Verificação da aprendizagem

Apresente uma nova demanda curta e peça uma resposta individual de cinco minutos. A pessoa
deve:

1. identificar duas alegações que ainda precisam de evidência;
2. indicar uma possível decisão humana;
3. formular um resultado observável;
4. decidir se há informação suficiente para autorizar a mudança, e justificar;
5. explicar qual risco surgiria ao pedir implementação imediata.

### Critério de domínio

A resposta demonstra domínio quando não inventa fatos ou autorização, indica evidência
pertinente a buscar e trata as decisões ainda abertas como bloqueio, não como detalhe. Em
turmas que já percorreram o Bloco II, exige-se ainda que a justificativa seja compreensível
para alguém que não conhece o Cordel.

## CURSO-03-MAT — Materiais necessários

- demanda inicial do caso condutor;
- duas respostas contrastantes do agente;
- quadro das sete perguntas;
- acesso ao projeto-laboratório ou a um recorte de código;
- modelo de análise, quando a unidade for usada a partir do `MOD-05`;
- espaço compartilhado para registrar afirmações e evidências.

## CURSO-03-FONTES — Fontes no método

- [`../../method/manifesto.md`](../../method/manifesto.md)
- [`../../method/concepts.md`](../../method/concepts.md)
- [`../../method/ai-driven-development.md`](../../method/ai-driven-development.md)
- [`../../method/catalog.md`](../../method/catalog.md)
- [`../../skill/cordel/references/triagem.md`](../../skill/cordel/references/triagem.md)
- [`../../skill/cordel/references/preparacao.md`](../../skill/cordel/references/preparacao.md)
- [`../../skill/cordel/references/fechamento.md`](../../skill/cordel/references/fechamento.md)

## CURSO-03-PEND — Pontos para a próxima revisão

- escolher a tecnologia e o domínio do projeto-laboratório;
- escrever a demanda alternativa usada na avaliação individual;
- produzir as duas respostas contrastantes do agente;
- criar o quadro visual das sete perguntas;
- testar a atividade com uma turma-piloto e ajustar a duração com dados reais.

