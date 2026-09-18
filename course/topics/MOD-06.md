---
id: MOD-06
title: "Da demanda à unidade autorizada"
status: draft
duration: 3 horas
bloco: "II — Controle e método"
ferramenta: "Cordel"
related_objectives:
  - OA-07
  - OA-08
  - OA-09
  - OA-10
updated: 2026-08-31
---

# MOD-06 — Da demanda à unidade autorizada

## MOD-06-INT — Intenção do módulo

Percorrer a cadeia do pedido ambíguo até o trabalho autorizado: localizar a origem,
classificar a demanda, confirmar o comportamento atual, registrar a decisão humana e produzir
uma unidade que possa ser implementada sem invenção.

Este módulo funde o que eram dois encontros na versão anterior do curso. A fusão é possível
porque as competências de fundo — confirmar o AS-IS, avaliar evidência, delimitar busca
negativa, declarar fronteiras — já foram trabalhadas nos encontros 2 e 3. O que resta aqui é
a mecânica do método, e ela é mais rápida de ensinar sobre terreno preparado.

A fusão aperta o cronograma. A investigação profunda do encontro anterior vira, em parte,
material entregue pronto: o instrutor fornece parte das fontes já localizadas para que o
tempo seja gasto na classificação e na decisão, não na busca. Se a turma for júnior ou o
domínio for complexo, este módulo deve virar dois encontros — o curso passa a nove.

## MOD-06-TESE — Tese

> Antes de desenhar o que o sistema deve fazer, confirme por que a demanda existe e o que o
> sistema faz hoje. Uma unidade está pronta quando o agente pode implementá-la sem inventar
> uma decisão e a equipe sabe, antes do código, como observará o resultado.

## MOD-06-OBJ — Resultados de aprendizagem

Ao final, a pessoa participante deverá conseguir:

1. preservar origem, relato, ambiente e anexos;
2. classificar a demanda em defeito, lacuna documental, detalhamento de compromisso existente
   ou escopo novo;
3. confirmar o AS-IS registrando evidências e buscas negativas com alcance;
4. distinguir necessidade de story autorizada;
5. registrar objetivo observável, escopo e fora do escopo;
6. formular critérios de aceite com estratégia de prova por critério;
7. avaliar impactos, dependências e decidir quando criar spec e ADR;
8. declarar o gate com pendências e próxima ação.

## MOD-06-CON — Conceitos

### MOD-06-CON-01 — Origem

**Princípio.** Pedido, documento, incidente, reunião ou decisão que explica por que a análise
existe. A origem precisa preservar autoria, data, ambiente e material suficiente para revisão.

**Prática.** Sem origem, não há como distinguir "alguém importante pediu" de "isto foi
decidido". A pergunta prática: se este trabalho for questionado daqui a três meses, o que
mostro?

**No Cordel.** Primeiro elo da cadeia mínima; nada avança sem ele.

### MOD-06-CON-02 — Triagem em filtros

**Princípio.** Classifique na ordem: defeito, lacuna documental, detalhamento de compromisso
existente, escopo novo. A ordem evita criar funcionalidade fictícia para algo que já existe
e evita tratar divergência de implementação como melhoria.

**Prática.** A mesma frase pode cair em qualquer um dos quatro. O que determina a
classificação não é o texto do pedido, é a relação entre origem, compromisso existente e
comportamento atual — as três coisas que a investigação precisa estabelecer.

### MOD-06-CON-03 — Investigação do geral ao específico

**Princípio.** Comece por drift de ambiente e contexto AS-IS, delimite o sintoma, depois abra
código, configuração, migrações, dados e testes nos pontos afetados.

**Prática.** O erro típico, humano e do agente, é saltar para o primeiro arquivo cujo nome
parece relacionado. É rápido e frequentemente leva ao lugar errado, porque o nome reflete a
intenção de quem criou, não o comportamento atual.

**No Cordel.** A investigação registra escopo, fontes consultadas e revisão, para que outra
pessoa possa refazer o caminho.

### MOD-06-CON-04 — Evidência e busca negativa

**Princípio.** Retomada do encontro 3, agora como registro obrigatório. `caminho:linha` é
endereço, não garantia; a evidência precisa demonstrar a afirmação. "Não encontrei no alcance
X" é mais preciso, e mais útil, que "não existe".

**Prática.** No laboratório, toda busca negativa que sustente uma classificação precisa
declarar termos, caminhos e revisão. Uma classificação de "escopo novo" apoiada em busca sem
alcance declarado é rejeitada na revisão cruzada.

### MOD-06-CON-05 — Descoberta e promoção

**Princípio.** Uma regra durável descoberta na análise deve ser promovida ao contexto atual do
produto. A análise histórica preserva o caminho; não se torna automaticamente fonte canônica.

**Prática.** É assim que a investigação deixa de ser desperdício: o que foi descoberto uma vez
não precisa ser redescoberto.

### MOD-06-CON-06 — Decisão antes da unidade

**Princípio.** Escopo novo precisa de responsável competente. A decisão delimita o que foi
autorizado e o que permanece fora. A story preserva essa decisão; não a cria.

**Prática.** Quando não há quem decida disponível, o estado correto é bloqueado. Fabricar a
decisão para não travar o trabalho é a falha mais cara do método inteiro, porque produz um
rastro que parece íntegro.

### MOD-06-CON-07 — Objetivo observável

**Princípio.** Descreve resultado percebido, não atividade técnica. "Enviar um aviso único ao
solicitante quando a aprovação for concluída" é observável; "alterar o serviço X" é meio de
solução.

**Prática.** Objetivo escrito como atividade técnica fecha a solução antes da análise e
impede que o agente encontre um caminho melhor dentro do mesmo resultado.

### MOD-06-CON-08 — Escopo e fora do escopo

**Princípio.** Escopo enumera resultados incluídos. Fora do escopo protege fronteiras que
poderiam ser inferidas. Ambos devem ser compatíveis com a decisão registrada.

**Prática.** É o mesmo campo praticado no encontro 2, agora com autorização anexada. Um fora
do escopo genérico — "não fazer mais nada" — não protege; ele precisa nomear o que um leitor
razoável inferiria que faz parte.

### MOD-06-CON-09 — Critérios de aceite

**Princípio.** Condições específicas e testáveis, cobrindo caminho principal, condições
relevantes e restrições, sem antecipar detalhes técnicos não decididos.

**Prática.** Critério não é tarefa. "Implementar o envio" é tarefa; "o solicitante recebe
exatamente um aviso por aprovação concluída" é critério.

### MOD-06-CON-10 — Estratégia de prova

**Princípio.** Para cada critério, define teste ou verificação, ambiente, dados e evidência
esperada. É planejada antes da implementação para não se ajustar ao que o código produziu.

**Prática.** É a resposta direta ao problema demonstrado no encontro 3: um teste escrito
depois, a partir do código, tende a confirmar a implementação em vez do critério. Definir a
prova antes remove esse grau de liberdade.

### MOD-06-CON-11 — Impactos e dependências

**Princípio.** Avalie componentes, dados, estados, permissões, integrações, compatibilidade,
implantação, reversão, observabilidade e fontes que precisarão ser atualizadas.

### MOD-06-CON-12 — Quando criar spec

**Princípio.** Spec é recomendada quando há alteração de contrato, dados existentes, estados,
integração, segurança, concorrência, vários componentes ou decisão técnica relevante. Mudança
simples ainda exige critérios e prova, mas não documentação excessiva.

**Prática.** O custo da cerimônia desnecessária é real e foi discutido no encontro 5: um
método que exige spec para tudo é abandonado.

### MOD-06-CON-13 — Gate com três resultados

**Princípio.**

- `BLOQUEADO`: falta origem, evidência, autorização ou decisão;
- `PRONTO PARA ESPECIFICAR`: trabalho válido, desenho incompleto;
- `PRONTO PARA IMPLEMENTAR`: unidade verificável sem decisão bloqueante.

**Prática.** O gate é a formalização de uma pergunta que qualquer pessoa deveria fazer antes
de começar: sei o suficiente para agir, e outra pessoa concordaria com essa avaliação? O
valor está em ser revisável, não em ser um carimbo.

## MOD-06-DEMO — Demonstração: classificar e refinar sem inventar

### Parte 1 — Quatro classificações, 15 minutos

Use quatro variações da mesma frase "o sistema deve avisar quando aprovado":

1. requisito exige aviso, reprodução mostra ausência: possível defeito;
2. código e teste demonstram aviso, documentação AS-IS omite: lacuna documental;
3. requisito de comunicação cobre o comportamento, mas o canal está ambíguo: detalhamento;
4. nenhuma cobertura válida após busca delimitada: possível escopo novo.

A frase não determina a classificação. A relação entre origem, compromisso e AS-IS determina
o próximo passo.

### Parte 2 — Refinar sem inventar, 15 minutos

Apresente uma decisão simulada: aviso interno ao solicitante, uma vez por aprovação
concluída; e-mail e reenvio histórico ficam fora. Construa em voz alta objetivo observável,
escopo e fora do escopo, três critérios, estratégia de prova de cada um, impactos,
justificativa para criar ou não spec, e o gate final.

Ao surgir uma dúvida sobre comportamento de negócio, pare e marque decisão pendente em vez de
completar a story por plausibilidade. Esse é o momento mais didático da demonstração.

## MOD-06-LAB — Laboratório: da triagem ao gate

### Cenário

Cada grupo recebe a demanda, a origem preservada e um dossiê parcial de fontes já localizadas
pelo instrutor. A busca completa não cabe no tempo; o objetivo é a classificação e a decisão.

### Etapa 1 — Preservar e reconciliar, 10 minutos

Registrar origem, data, autor, ambiente, relato e anexos, separando o que foi recebido da
interpretação do grupo. Executar o comando de reconciliação de ambiente configurado no
encontro 5, ou registrar por que não está disponível.

### Etapa 2 — Confirmar o AS-IS, 25 minutos

Consultar o dossiê, o requisito integral e o contexto AS-IS. Inspecionar código, configuração
e testes nos pontos afetados. Construir a tabela de afirmação e evidência, marcando buscas
negativas com alcance:

| Afirmação | Evidência ou busca negativa | Alcance declarado | Sustenta? |
|---|---|---|---|

### Etapa 3 — Aplicar filtros, 15 minutos

Responder, em ordem, se é defeito, lacuna documental, compromisso existente ou escopo novo.
Uma resposta positiva precisa de sustentação na tabela anterior.

### Etapa 4 — Decisão simulada, 10 minutos

O responsável de produto recebe os fatos da triagem e escolhe entre rejeitar, adiar, autorizar
com limites ou pedir especificação adicional. A decisão fica registrada com autor e limites.

### Etapa 5 — Necessidade, story e prova, 25 minutos

Atualizar a necessidade e criar a story somente para o escopo autorizado. Preencher:

| Critério | Teste ou verificação | Dados / ambiente | Evidência esperada |
|---|---|---|---|

### Etapa 6 — Impactos, spec e gate, 15 minutos

Percorrer o checklist de impactos. Se alguma condição justificar desenho adicional, criar spec
com âncoras verificadas, contratos antes e depois, migração e invariantes. Revisar origem,
cobertura, autorização, AS-IS, ambiente, story, aceites, impactos, decisões, spec e relações,
e declarar uma das três saídas do gate.

### Etapa 7 — Revisão cruzada, 10 minutos

Outro grupo escolhe uma evidência e tenta localizá-la, questiona o alcance de uma busca
negativa e verifica se a story não amplia a decisão registrada.

## MOD-06-ENT — Entrega

1. origem e relato preservados;
2. escopo da investigação e fontes consultadas;
3. tabela de afirmações, evidências e buscas negativas com alcance;
4. resultado de cada filtro e classificação final com grau de confiança;
5. regra durável a promover ao AS-IS, quando houver;
6. decisão humana registrada, com autor e limites;
7. necessidade atualizada;
8. story com objetivo observável, escopo e fora do escopo;
9. critérios de aceite com estratégia de prova por critério;
10. avaliação de impactos, spec e ADR quando necessários;
11. gate completo com pendências e próxima ação autorizada.

Grupos bloqueados entregam o mesmo rastro, deixando clara a condição ausente. Um gate
`BLOQUEADO` bem justificado vale mais que um `PRONTO PARA IMPLEMENTAR` fabricado.

## MOD-06-ROTEIRO — Cronograma de 3 horas

| Tempo | Atividade |
|---:|---|
| 0–10 min | retomada: da configuração para a cadeia |
| 10–30 min | origem, filtros de triagem e investigação |
| 30–45 min | evidência, busca negativa e promoção de descoberta |
| 45–60 min | decisão, objetivo observável, escopo e critérios |
| 60–75 min | estratégia de prova, impactos, spec e gate |
| 75–95 min | demonstração: quatro classificações e refinamento |
| 95–105 min | intervalo |
| 105–115 min | laboratório: preservar e reconciliar |
| 115–140 min | confirmar o AS-IS |
| 140–150 min | filtros e decisão simulada |
| 150–170 min | story, aceites, prova e gate |
| 170–180 min | revisão cruzada e entrega |

## MOD-06-AVAL — Critérios de avaliação

| Critério | Evidência esperada |
|---|---|
| preserva relato | texto recebido separado da interpretação |
| confirma AS-IS | afirmações sustentadas por fonte pertinente e localizável |
| delimita ausência | busca negativa com alcance explícito |
| classifica em ordem | resultado de todos os filtros, com sustentação |
| preserva autorização | story não amplia a decisão registrada |
| protege fronteiras | fora do escopo com itens plausíveis e específicos |
| antecipa prova | cada aceite com verificação planejada antes do código |
| calibra documentação | spec justificada pela complexidade, não pelo hábito |
| usa gate corretamente | pendências compatíveis com o estado declarado |

Relaciona-se a `OA-07`, `OA-08`, `OA-09` e `OA-10`.

## MOD-06-EQUIVOCOS — Equívocos a observar

- "Se há relato de erro, é defeito." É preciso comportamento esperado e divergência.
- "Se não há story, não há implementação." Story declara trabalho, não prova código.
- "Se existe código, está coberto." Código pode divergir do requisito ou estar inativo.
- "Busca sem resultado prova ausência." Prova apenas o alcance executado.
- "Escopo novo deve ser rejeitado." Deve ser registrado e levado à decisão competente.
- "Análise histórica é o novo AS-IS." A descoberta precisa ser promovida à fonte correta.
- "Necessidade aprovada é story pronta." Ainda exige unidade verificável.
- "Critério é uma tarefa." Critério descreve comportamento ou restrição observável.
- "Fora do escopo limita criatividade." Preserva autorização e reduz deriva.
- "Spec é obrigatória para tudo." É proporcional a complexidade e risco.
- "Plano de testes depois basta." A estratégia anterior protege contra prova conveniente.
- "Pronto significa que alguém vai começar." Significa ausência de decisão bloqueante.

## MOD-06-MAT — Materiais e preparação

- chamado ou demanda com origem preservada;
- dossiê parcial de fontes já localizadas, para caber no tempo;
- requisito e decisão relacionados;
- código com evidência contraditória e teste parcial;
- possibilidade de drift preparada;
- uma busca negativa com alcance enganoso, para a revisão cruzada;
- cartões de decisão de produto com limites definidos;
- modelos de necessidade, story, spec e ADR;
- checklist de gate;
- exemplo de critério observável e de critério que não é;
- exemplo de impacto que justifica spec;
- gabaritos de classificação e de limites autorizados.

## MOD-06-FONTES — Fontes no método

- [`../../skill/cordel/references/triagem.md`](../../skill/cordel/references/triagem.md)
- [`../../skill/cordel/references/investigacao.md`](../../skill/cordel/references/investigacao.md)
- [`../../skill/cordel/references/preparacao.md`](../../skill/cordel/references/preparacao.md)
- [`../../skill/cordel/assets/templates/necessidade.md`](../../skill/cordel/assets/templates/necessidade.md)
- [`../../skill/cordel/assets/templates/story.md`](../../skill/cordel/assets/templates/story.md)
- [`../../skill/cordel/assets/templates/spec.md`](../../skill/cordel/assets/templates/spec.md)
- [`../../skill/cordel/assets/templates/adr.md`](../../skill/cordel/assets/templates/adr.md)
- [`../../method/catalog.md`](../../method/catalog.md)
- [`../../method/traceability.md`](../../method/traceability.md)

## MOD-06-PEND — Pendências

- este módulo funde dois encontros da versão anterior e ainda não foi cronometrado em turma;
- montar o dossiê parcial de fontes, calibrando quanto é entregue pronto — entregar demais
  esvazia a etapa 2, entregar de menos estoura o tempo;
- construir as quatro variantes do caso;
- preparar as evidências em código e testes;
- definir o comando de reconciliação do laboratório;
- criar a busca negativa com alcance enganoso;
- escrever os cartões de decisão e limites;
- definir os critérios de aceite do caso condutor;
- criar exemplos de gate bloqueado e pronto;
- preparar rubrica para critérios observáveis;
- decidir o ponto de corte para desdobrar este módulo em dois encontros, e documentar o
  critério para o instrutor decidir antes da turma começar.
