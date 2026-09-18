---
id: MOD-07
title: "Implementação assistida e prova"
status: draft
duration: 3 horas
bloco: "III — Prova e transferência"
ferramenta: "Cordel"
related_objectives:
  - OA-03
  - OA-06
  - OA-10
  - OA-12
updated: 2026-08-31
---

# MOD-07 — Implementação assistida e prova

## MOD-07-INT — Intenção do módulo

Executar a unidade aprovada e provar o resultado. A turma implementa com o agente dentro do
gate, revisando em checkpoints, reage a uma mudança de escopo introduzida no meio do
trabalho, relaciona cada critério a uma prova, audita o dossiê de outro grupo e reconcilia o
projeto.

Este módulo funde os dois últimos encontros da versão anterior. A fusão se sustenta porque a
condução do agente foi ensinada no encontro 2 e a verificação no encontro 3 — aqui as duas
aparecem como execução dentro de um gate, não como conteúdo novo. Ainda assim é o encontro
mais apertado do curso; a implementação precisa ser pequena por projeto, e o cronograma
abaixo assume que a story cabe em cerca de quarenta minutos de execução assistida.

## MOD-07-TESE — Tese

> O gate não encerra o julgamento: ele cria condições para agir. E uma entrega só pode ser
> chamada de verificada quando outra pessoa consegue percorrer a afirmação até uma evidência
> atual que demonstra especificamente o comportamento.

## MOD-07-OBJ — Resultados de aprendizagem

Ao final, a pessoa participante deverá conseguir:

1. montar contexto mínimo pertinente e transformar aceites em plano incremental;
2. conceder ferramentas e permissões compatíveis com a etapa;
3. revisar diferenças em checkpoints, contra escopo e fora do escopo;
4. distinguir descoberta técnica de escopo funcional novo e devolver o segundo à triagem;
5. executar a estratégia de prova e avaliar se a evidência sustenta o critério;
6. aplicar os vereditos de rastreabilidade e diferenciar `implementado` de `verificado`;
7. promover descobertas duráveis ao contexto AS-IS e regenerar projeções;
8. articular o rastro do método com branch, pull request, revisão humana e CI.

## MOD-07-CON — Conceitos

### MOD-07-CON-01 — Contexto de execução

**Princípio.** Inclui story, spec, AS-IS, decisões, arquivos afetados, convenções e comandos.
Materiais não pertinentes ficam fora. O contexto pode crescer quando a execução revela uma
dependência, mas cada inclusão precisa de motivo.

**No Cordel.** O índice torna essa seleção barata: aponta-se a rota, o agente carrega o que
precisa.

### MOD-07-CON-02 — Plano incremental

**Princípio.** Divide a mudança em passos verificáveis, preservando compatibilidade e
feedback. Cada passo deve permitir observar progresso sem depender de uma longa cadeia não
revisada.

**Prática.** O tamanho do passo é uma decisão de revisão, não de produtividade: um passo é
grande demais quando a diferença não cabe em uma leitura atenta.

### MOD-07-CON-03 — Ferramentas por etapa

**Princípio.** Pesquisa e leitura podem ocorrer antes da escrita. Build e testes validam
hipóteses. Publicação ou operação externa permanece separada da implementação local e exige
autorização própria.

**Prática.** Aplicação direta da escala de autonomia do encontro 2 e da política de permissões
do encontro 4.

### MOD-07-CON-04 — Testes como feedback

**Princípio.** Testes ajudam a detectar regressão e orientar a execução. A prova final ainda
precisa ser relacionada aos critérios; teste verde isolado não promove a entrega a
`verificado`.

### MOD-07-CON-05 — Escopo emergente

**Princípio.** Se a implementação revela necessidade não coberta, essa parte é interrompida e
volta à triagem. Correção estritamente necessária para cumprir o aceite pode permanecer na
unidade quando sustentada pelo escopo e revisada.

**Prática.** A distinção prática: a descoberta impede cumprir o critério autorizado, ou
acrescenta um resultado novo? A primeira fica; a segunda volta.

### MOD-07-CON-06 — Observabilidade da execução

**Princípio.** Registre plano, arquivos alterados, comandos, resultados, decisões e desvios. O
objetivo não é narrar cada tecla, mas permitir reconstruir escolhas relevantes.

### MOD-07-CON-07 — Relações e prova

**Princípio.** Origem, requisito, story, spec, código e teste podem estar formalmente ligados.
O vínculo ajuda a navegação, mas não demonstra sozinho que a condição foi implementada
corretamente.

### MOD-07-CON-08 — Evidência suficiente

**Princípio.** Uma evidência é adequada quando pode ser localizada, está no lugar autorizado,
demonstra a afirmação, registra revisão quando envelhece e distingue ausência de busca
incompleta.

**Prática.** Os mesmos critérios do encontro 3, agora aplicados ao fechamento e sujeitos a
revisão por outro grupo.

### MOD-07-CON-09 — Vereditos

**Princípio.**

- `verificado`: condições relevantes presentes e provadas;
- `parcial`: parte presente ou provada;
- `divergente`: implementação difere da fonte esperada;
- `nao-iniciado`: busca delimitada não encontrou implementação;
- `nao-rastreavel`: o texto não permite verificação objetiva.

**Prática.** O veredito honesto mais comum, em trabalho real, é `parcial`. Um curso em que
todos os grupos declaram `verificado` provavelmente afrouxou o critério de evidência.

### MOD-07-CON-10 — Estados do trabalho

**Princípio.** `implementado` indica conclusão técnica com prova insuficiente. `verificado`
exige evidência confirmável. O estado pode regredir quando a evidência quebra, envelhece ou
perde pertinência.

### MOD-07-CON-11 — Reconciliação

**Princípio.** Atualiza story, spec, contexto AS-IS, decisões, dependências e projeções para
refletir a entrega. Fonte aceita não é reescrita silenciosamente; uma nova decisão substitui
a anterior.

**Prática.** É a etapa mais pulada em times reais, e a razão de o conhecimento envelhecer. O
sinal de que foi feita: a próxima pessoa que investigar aquele comportamento encontra a
resposta certa sem perguntar a ninguém.

### MOD-07-CON-12 — Revisão independente

**Princípio.** Uma pessoa que não conduziu a implementação tenta confirmar as afirmações.
Dependência de memória ou de explicação oral revela uma lacuna no rastro.

### MOD-07-CON-13 — O rastro e o fluxo de trabalho existente

**Princípio.** O rastro do método precisa conviver com branch, pull request, revisão humana e
CI — não substituí-los nem duplicá-los. Cada informação vive em um lugar só: a decisão e a
evidência no artefato, a discussão da alteração no pull request, a execução das verificações
na CI.

**Prática.** Padrão que costuma funcionar: a story referenciada na descrição do pull request;
os comandos da estratégia de prova executados pela CI, com o resultado endereçável; a revisão
humana focada na diferença contra o escopo, já que a verificação mecânica ficou na esteira.
Duplicar o conteúdo do artefato dentro do pull request cria duas versões que divergem na
primeira alteração.

## MOD-07-DEMO — Demonstração: checkpoints e evidência parcial

### Parte 1 — Implementação em três checkpoints, 12 minutos

1. localizar o ponto de mudança e confirmar a âncora;
2. implementar o comportamento mínimo e o teste do caminho principal;
3. cobrir a condição de repetição e executar as verificações proporcionais.

Após cada passo, compare diferença, teste e critério. No segundo passo, introduza uma sugestão
de "aproveitar e enviar e-mail" e demonstre como registrar a nova necessidade sem incorporá-la
ao escopo atual.

### Parte 2 — Teste verde, evidência parcial, 8 minutos

Retome o exemplo do encontro 3, agora com o critério formalizado na story: o teste confirma a
chamada ao serviço, o critério exige aviso único ao solicitante correto. Mostre o veredito
`parcial` sendo declarado sem constrangimento, e o que seria necessário para chegar a
`verificado`.

## MOD-07-LAB — Laboratório: executar, provar e reconciliar

### Etapa 1 — Revalidar o gate e preparar, 10 minutos

Confirmar que fontes, branch, dependências e decisões continuam atuais. Drift relevante vira
ressalva ou bloqueio. Selecionar contexto, definir os passos e associar cada passo a um
feedback.

### Etapa 2 — Implementar em checkpoints, 40 minutos

O agente pode editar e executar comandos dentro do escopo. O grupo revisa as diferenças e os
resultados entre passos, evitando acumular grande alteração sem observação.

### Etapa 3 — Evento de escopo, 10 minutos

O instrutor libera uma solicitação adicional plausível. O grupo decide se pertence ao critério
atual. Se não pertencer, registra necessidade separada e continua apenas o autorizado.

### Etapa 4 — Executar a estratégia de prova, 20 minutos

Para cada critério, executar o teste ou a verificação planejada e registrar resultado,
ambiente, dados e endereço da evidência. Separar falhas preexistentes das introduzidas pela
mudança.

### Etapa 5 — Revisão entre grupos, 20 minutos

O revisor escolhe pelo menos dois critérios, abre as evidências e atribui veredito, registrando
condição existente, ausente ou divergente. Verifica também se todo arquivo alterado tem motivo
no escopo.

### Etapa 6 — Correção e reconciliação, 15 minutos

Corrigir prova, texto ou implementação quando autorizado; se a revisão revelar escopo novo,
registrar necessidade separada. Atualizar AS-IS, story, spec, decisões e dependências;
regenerar projeções; executar o comando de reconciliação.

## MOD-07-ENT — Entrega

1. plano incremental executado e registro de contexto e ferramentas utilizadas;
2. código e testes da story;
3. diferença revisada contra escopo e fora do escopo;
4. nova necessidade para o escopo emergente, quando aplicável;
5. tabela critério-prova executada, com evidências acessíveis e pertinentes;
6. separação entre falhas preexistentes e introduzidas;
7. parecer da revisão independente e vereditos por condição;
8. contexto AS-IS atualizado, story e spec reconciliadas, projeções regeneradas;
9. resultado do comando de reconciliação;
10. separação entre entrega, dívida e pendência;
11. estado final justificado entre `implementado` e `verificado`.

## MOD-07-ROTEIRO — Cronograma de 3 horas

| Tempo | Atividade |
|---:|---|
| 0–10 min | retomada do gate e do plano |
| 10–25 min | contexto de execução, plano incremental e ferramentas por etapa |
| 25–40 min | escopo emergente e observabilidade da execução |
| 40–55 min | evidência suficiente, vereditos e estados |
| 55–70 min | reconciliação e articulação com branch, pull request e CI |
| 70–90 min | demonstração: checkpoints e evidência parcial |
| 90–100 min | intervalo |
| 100–110 min | laboratório: revalidar o gate e preparar |
| 110–150 min | implementar em checkpoints |
| 150–160 min | evento de escopo |
| 160–172 min | estratégia de prova e revisão entre grupos |
| 172–180 min | reconciliação, veredito e entrega |

O cronograma não comporta a revisão entre grupos com folga. Se a implementação atrasar, a
etapa 5 vira leitura cruzada de dossiês, sem execução — mas não deve ser cortada: é onde a
diferença entre `implementado` e `verificado` aparece.

## MOD-07-AVAL — Critérios de avaliação

| Critério | Evidência esperada |
|---|---|
| revalida condições | gate e ambiente ainda aplicáveis |
| usa contexto pertinente | fontes selecionadas com motivo |
| executa incrementalmente | checkpoints com feedback registrado |
| preserva autorização | escopo emergente separado e devolvido |
| revisa contra escopo | todo arquivo alterado com motivo |
| verifica semanticamente | prova demonstra o critério específico |
| aceita veredito parcial | lacuna não escondida por status |
| permite revisão independente | rastro percorrível sem explicação oral |
| atualiza fonte correta | AS-IS promovido e projeção regenerada |
| separa responsabilidades | dívida e pendência fora da entrega atual |

Relaciona-se a `OA-03`, `OA-06`, `OA-10` e `OA-12`.

## MOD-07-EQUIVOCOS — Equívocos a observar

- "Gate pronto impede novas descobertas." Ele representa o conhecimento no ponto de entrada.
- "O agente pode aproveitar para limpar o código." Só se a limpeza estiver no escopo.
- "Contexto mínimo significa informação insuficiente." Significa pertinência, não privação.
- "Checkpoint é aprovação humana de cada linha." É observação proporcional ao risco.
- "Todo desvio exige abandonar a story." Corrija dentro do escopo; trie o que o amplia.
- "Story concluída prova implementação." Ela registra trabalho, não comportamento.
- "Qualquer teste que passa é evidência." Precisa demonstrar a condição alegada.
- "Verificado é estado permanente." Evidências envelhecem e podem perder validade.
- "Matriz decide cobertura." Ela orienta navegação; a prova sustenta o estado.
- "Reconciliação é atualizar status." Inclui fontes, conhecimento e projeções.
- "Dívida preexistente invalida tudo." Deve ser separada e avaliada pelo impacto real.
- "O pull request substitui o rastro." São camadas diferentes; duplicar conteúdo cria
  divergência.

## MOD-07-MAT — Materiais e preparação

- story e gate produzidos no `MOD-06`;
- branch individual ou por grupo;
- comandos de build e teste estáveis e cronometrados;
- política de permissões do `MOD-04`;
- cartão de escopo emergente;
- falha preexistente conhecida, distinguível da introduzida;
- exemplo de teste verde com evidência parcial, já usado no `MOD-03`;
- projeção divergente preparada;
- fonte AS-IS a atualizar;
- comando de reconciliação funcionando;
- rubrica da revisão independente;
- modelo de dossiê final;
- mecanismo de restauração do laboratório entre turmas.

## MOD-07-FONTES — Fontes no método

- [`../../skill/cordel/references/preparacao.md`](../../skill/cordel/references/preparacao.md)
- [`../../skill/cordel/references/rastreabilidade.md`](../../skill/cordel/references/rastreabilidade.md)
- [`../../skill/cordel/references/fechamento.md`](../../skill/cordel/references/fechamento.md)
- [`../../method/traceability.md`](../../method/traceability.md)
- [`../../method/ai-driven-development.md`](../../method/ai-driven-development.md)
- [`../../method/team-knowledge.md`](../../method/team-knowledge.md)

## MOD-07-PEND — Pendências

- este módulo funde dois encontros da versão anterior e é o mais apertado do curso; cronometrar
  em turma antes de fixar;
- dimensionar a story do caso condutor para caber em cerca de quarenta minutos de execução
  assistida;
- implementar o estado inicial e a solução de referência;
- definir os checkpoints do caso;
- criar o cartão de escopo emergente;
- preparar a falha preexistente distinguível;
- medir o tempo real de build e testes;
- definir as permissões reais de escrita e execução;
- preparar a projeção divergente e a fonte AS-IS a atualizar;
- escrever a rubrica da revisão entre grupos;
- definir se a CI do laboratório será real ou simulada, e como o resultado vira evidência
  endereçável;
- definir política de retenção dos dossiês;
- garantir restauração rápida entre turmas e testar o fechamento em ambiente limpo.
