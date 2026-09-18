---
id: CURSO-06
title: "Riscos e controles"
status: draft
duration: 90 minutos de introdução e uso transversal
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

# CURSO-06 — Riscos e controles

## CURSO-06-INT — Intenção da unidade

Esta unidade ensina a analisar o uso de agentes sem cair em dois extremos: tratar a IA como
fonte automática de produtividade ou proibir seu uso por riscos descritos de forma genérica.
A turma aprende a relacionar uma capacidade concreta a um mecanismo de falha, um impacto,
controles observáveis e risco residual.

O objetivo não é afirmar que o Cordel elimina riscos. Cada risco do catálogo enuncia primeiro
o **controle**, que é independente de ferramenta, e depois a forma como o método o implementa.
Quem sai do curso deve conseguir aplicar o controle em um time que não use o Cordel.

## CURSO-06-TESE — Tese central

> Toda capacidade que permite ao agente acelerar uma entrega também permite acelerar uma
> falha. O controle adequado preserva o benefício, reduz a exposição e torna o risco restante
> explícito.

Um risco não deve ser descrito apenas como "a IA pode errar". Essa frase não informa onde o
erro nasce, o que pode atingir, como detectá-lo ou quem deve aceitar o risco remanescente.

## CURSO-06-VOCAB — Vocabulário de risco

### CURSO-06-VOCAB-01 — Capacidade

Aquilo que o agente consegue fazer no cenário: pesquisar, interpretar, escrever, executar,
publicar ou operar uma integração.

### CURSO-06-VOCAB-02 — Mecanismo de falha

Caminho pelo qual a capacidade produz um resultado indesejado. Exemplo: selecionar uma fonte
antiga, completar uma lacuna por inferência e propagar a conclusão como fato.

### CURSO-06-VOCAB-03 — Impacto

Consequência observável da falha sobre produto, pessoas, dados, segurança, operação,
conformidade, custo ou conhecimento.

### CURSO-06-VOCAB-04 — Controle

Medida preventiva, detectiva ou corretiva que reduz probabilidade, alcance ou impacto.
Controle declarado sem aplicação verificável ainda é intenção.

### CURSO-06-VOCAB-05 — Evidência do controle

Registro ou resultado que permite confirmar que o controle foi aplicado no caso analisado.
Exemplo: gate revisado, permissão efetiva, registro de chamada de ferramenta ou relação
critério-prova.

### CURSO-06-VOCAB-06 — Risco residual

Exposição que continua existindo depois dos controles. Deve ser aceita, reduzida por controle
adicional, transferida ao responsável adequado ou usada para bloquear a ação.

### CURSO-06-VOCAB-07 — Responsável

Pessoa ou papel com autoridade para decidir sobre o risco dentro daquele escopo. O agente pode
identificar e explicar; não assume automaticamente a aceitação.

## CURSO-06-MODELO — Modelo de análise

Para uma ação concreta, responda na ordem:

1. **Contexto:** qual tarefa, ambiente e resultado esperado?
2. **Capacidade:** o que o agente poderá observar ou alterar?
3. **Falha:** por qual mecanismo a ação pode produzir resultado incorreto?
4. **Impacto:** quem ou o que será afetado?
5. **Controle:** o que previne, detecta ou corrige a falha?
6. **Evidência:** como confirmar que o controle foi aplicado?
7. **Residual:** o que continua incerto ou exposto?
8. **Decisão:** quem pode autorizar a ação nessas condições?

```text
capacidade -> mecanismo de falha -> impacto
                   |
              controles aplicados
                   |
          evidência -> risco residual -> decisão
```

## CURSO-06-DIMENSOES — Dimensões para calibrar o controle

| Dimensão | Pergunta | Sinal de maior exposição |
|---|---|---|
| Impacto | Qual dano pode ocorrer? | dados, segurança, clientes ou operação crítica |
| Alcance | Quantos componentes, registros ou pessoas podem ser afetados? | mudança ampla ou propagação automática |
| Reversibilidade | É possível desfazer com segurança? | publicação, exclusão ou efeito externo irreversível |
| Sensibilidade | Que dados ou credenciais ficam disponíveis? | segredos, dados pessoais ou informação regulada |
| Detectabilidade | A falha aparece antes de produzir efeito? | ausência de testes, registros, revisão ou ambiente isolado |
| Reprodutibilidade | O resultado que sustenta a decisão pode ser obtido de novo? | conclusão baseada em uma única execução não repetida |
| Incerteza | Quanto do comportamento atual, requisito e ambiente está confirmado? | fontes conflitantes ou busca incompleta |
| Autonomia | Quantas decisões e ações ocorrem sem checkpoint? | tarefa longa com ferramentas mutáveis |
| Maturidade | O workflow já foi avaliado em casos semelhantes? | skill nova, sem avaliação ou sem responsáveis claros |

Quanto maior a exposição, mais explícitos precisam ser escopo, permissão, checkpoint,
estratégia de prova e responsável pelo residual.

A dimensão **reprodutibilidade** é nova nesta revisão e decorre do não determinismo tratado no
`MOD-01`: uma conclusão obtida em uma execução que ninguém repetiu não deveria sustentar uma
decisão relevante.

## CURSO-06-CONTROLES — Camadas de controle

Cada camada é enunciada como controle independente de ferramenta. A implementação no Cordel
aparece depois, entre parênteses.

### CURSO-06-CONTROLES-01 — Condução da tarefa

Delimitar objetivo, restrições, fora do escopo e critério de pronto antes de acionar o agente.
Reduz o risco de o agente preencher por conta própria as decisões que ninguém tomou. Ensinado
no `MOD-02`. (No Cordel: os campos da story.)

### CURSO-06-CONTROLES-02 — Verificação da produção

Revisar a diferença contra o escopo declarado, reconhecer padrões típicos de erro do agente e
exigir que o teste possa falhar. Reduz o risco de aceitar como correto o que é apenas
plausível. Ensinado no `MOD-03`. (No Cordel: estratégia de prova definida antes do código.)

### CURSO-06-CONTROLES-03 — Origem e classificação

Localizar de onde veio o pedido e classificá-lo antes de tratá-lo. Reduz o risco de resolver
uma formulação sem contexto ou tratar escopo novo como defeito. (No Cordel: origem preservada
e triagem em filtros.)

### CURSO-06-CONTROLES-04 — Comportamento atual e fontes com autoridade

Confirmar o que o sistema faz hoje em fonte inspecionável e declarar quem tem autoridade sobre
cada fato. Reduz o risco de planejar sobre alegações, documentos antigos ou entendimento
incompleto. (No Cordel: AS-IS confirmado e fontes da verdade declaradas.)

### CURSO-06-CONTROLES-05 — Decisão humana e limites de autorização

Exigir que escopo novo seja autorizado por quem tem competência, com limites explícitos.
Reduz o risco de o agente assumir compromissos de produto, prioridade, custo ou aceitação de
risco. (No Cordel: decisão registrada antes da story.)

### CURSO-06-CONTROLES-06 — Unidade verificável e critério para agir

Definir resultado observável e avaliar se há informação suficiente antes de começar. Reduz o
risco de iniciar implementação sem impacto avaliado ou com decisão bloqueante em aberto. (No
Cordel: story, spec quando necessária, e gate com três resultados.)

### CURSO-06-CONTROLES-07 — Ambiente, ferramentas e permissões

Limitar o que o agente consegue fazer, por etapa, distinguindo leitura, escrita e publicação.
Reduz o alcance operacional de qualquer erro, inclusive dos que ninguém previu. Ensinado no
`MOD-04`. (No Cordel: política de permissões versionada no adaptador.)

### CURSO-06-CONTROLES-08 — Fronteiras de confiança e proteção de dados

Tratar conteúdo lido como dado e nunca como instrução; definir previamente o que não pode
entrar no contexto. Reduz o risco de instrução hostil e de exposição de informação sensível.
Ensinado no `MOD-04`.

### CURSO-06-CONTROLES-09 — Testes, evidências e revisão independente

Exigir que a promoção de estado dependa de evidência acessível e pertinente, verificada por
quem não conduziu o trabalho. Impede que status, narrativa ou código produzido sejam aceitos
como prova. (No Cordel: vereditos com evidência obrigatória.)

### CURSO-06-CONTROLES-10 — Reconciliação e conhecimento durável

Atualizar as fontes ao final para que documentação, código e testes voltem a concordar. Reduz
a propagação de documentação divergente e a necessidade de redescobrir decisões. (No Cordel:
reconciliação no fechamento e regeneração de projeções.)

### CURSO-06-CONTROLES-11 — Avaliação e observabilidade

Registrar o que foi feito e medir o comportamento do workflow em casos definidos. Permitem
avaliar agente e procedimento mesmo quando o produto final passa nos testes. (No Cordel: evals
de skills e workflows.)

## CURSO-06-RISCOS — Catálogo detalhado

Os identificadores `RC-01` a `RC-10` são estáveis desde a primeira versão do curso. `RC-11` a
`RC-13` foram acrescentados nesta revisão.

### RC-01 — Pesquisa rápida em código e documentação

**Capacidade:** pesquisar muitas fontes e sintetizar uma resposta em pouco tempo.

**Mecanismo de falha:** o agente encontra uma fonte antiga, secundária ou fora do escopo,
combina trechos e apresenta uma conclusão coerente sem indicar a autoridade de cada fonte.

**Impacto:** decisão e implementação partem de um contexto incorreto; a conclusão pode ser
replicada em documentos e artefatos posteriores.

**Controle ensinado:** declarar quais fontes têm autoridade sobre cada fato e exigir evidência
endereçável para cada afirmação relevante. No Cordel: fontes da verdade com responsável e
escopo, índice curto, leitura sob demanda e confirmação semântica.

**Evidência do controle:** lista das fontes consultadas, revisão ou data aplicável e endereço
usado para sustentar cada afirmação.

**Risco residual:** a fonte canônica pode estar desatualizada ou errada. Autoridade não
garante correção do conteúdo.

**Decisão prática:** se fontes canônicas divergem, interromper a conclusão e levar a
divergência ao responsável pela fonte.

**Onde é ensinado:** `MOD-03` e `MOD-06`.

### RC-02 — Compreensão de sistemas legados

**Capacidade:** explicar fluxos, dependências e regras a partir de código fragmentado.

**Mecanismo de falha:** o agente preenche partes não observadas com padrões comuns ou
suposições plausíveis, especialmente após buscas negativas.

**Impacto:** a solução altera o ponto errado, ignora efeito lateral ou duplica comportamento
existente.

**Controle ensinado:** investigar do geral ao específico e confirmar o comportamento atual em
fonte inspecionável antes de propor mudança, delimitando o alcance de cada busca. No Cordel:
AS-IS confirmado, com separação entre relato e observação.

**Evidência do controle:** mapa do fluxo com endereços verificados e marcação explícita das
partes inferidas ou ainda não observadas.

**Risco residual:** caminhos dinâmicos, dados raros e integrações indisponíveis podem não ser
observados durante a análise.

**Decisão prática:** ampliar a investigação ou reduzir o escopo da afirmação; não promover
"não encontrei" a "não existe".

**Onde é ensinado:** `MOD-03` e `MOD-06`.

### RC-03 — Geração acelerada de código

**Capacidade:** transformar rapidamente uma descrição em alterações funcionais.

**Mecanismo de falha:** uma interpretação não confirmada se torna código, testes e
documentação antes que origem, cobertura e autorização sejam verificadas.

**Impacto:** retrabalho, regressão, escopo indevido ou criação de compromisso não aceito.

**Controle ensinado:** exigir decisão humana explícita e unidade verificável antes do código.
No Cordel: origem, triagem, AS-IS, story, estratégia de prova e gate.

**Evidência do controle:** veredito de prontidão com pendências resolvidas e vínculo entre
trabalho implementado e escopo autorizado.

**Risco residual:** um gate pode formalizar uma premissa ruim se a revisão for superficial.

**Decisão prática:** calibrar revisão e autonomia pelo impacto; mudanças de baixo risco não
precisam do mesmo volume documental de mudanças críticas.

**Onde é ensinado:** `MOD-06` e `MOD-07`.

### RC-04 — Detalhamento de requisitos e soluções

**Capacidade:** decompor uma necessidade em critérios, casos e desenho técnico.

**Mecanismo de falha:** o agente cria detalhes não presentes na origem e eles passam a ser
tratados como requisito, autorização ou decisão de negócio.

**Impacto:** a solução fica precisa em torno de uma escolha que ninguém competente fez.

**Controle ensinado:** distinguir necessidade, requisito, unidade de trabalho e detalhamento
técnico, e marcar inferências como tais. No Cordel: necessidade, story, spec e ADR com papéis
distintos.

**Evidência do controle:** cada decisão relevante possui fonte ou responsável; alternativas
não escolhidas permanecem identificadas.

**Risco residual:** responsáveis humanos também podem decidir com informação insuficiente ou
manter ambiguidade.

**Decisão prática:** registrar a incerteza e seu impacto; não usar o documento de solução para
esconder uma decisão ainda aberta.

**Onde é ensinado:** `MOD-06`.

### RC-05 — Criação de testes

**Capacidade:** gerar casos e automatizar verificações junto da implementação.

**Mecanismo de falha:** os testes codificam a mesma interpretação equivocada usada para gerar
a solução e passam por consistência interna.

**Impacto:** falsa confiança, regressão não detectada ou aceite de comportamento diferente do
esperado.

**Controle ensinado:** definir critérios observáveis e projetar a verificação antes da
implementação, e confirmar que cada teste consegue falhar diante de um defeito real. No
Cordel: estratégia de prova declarada no gate.

**Evidência do controle:** relação explícita entre critério, verificação executada, resultado
e evidência preservada; registro dos defeitos introduzidos e do que cada teste acusou.

**Risco residual:** oráculos podem estar errados; ambientes e dados de teste podem não
representar condições relevantes.

**Decisão prática:** usar revisão independente, testes em outros níveis ou observação real
quando o risco não é coberto por teste gerado junto da solução.

**Onde é ensinado:** `MOD-03` e `MOD-06`.

### RC-06 — Atualização de documentação

**Capacidade:** atualizar rapidamente várias descrições, índices e registros.

**Mecanismo de falha:** uma conclusão falsa ou provisória é propagada e ganha aparência de
consenso por repetição.

**Impacto:** trabalhos futuros usam contexto incorreto; fontes e projeções passam a divergir.

**Controle ensinado:** manter uma fonte com autoridade por fato e regenerar as projeções em vez
de editá-las. No Cordel: separação entre artefato e projeção, promoção revisada ao contexto
canônico e reconciliação no fechamento.

**Evidência do controle:** alteração na fonte correta, revisão proporcional e projeções
regeneradas sem edição manual.

**Risco residual:** conhecimento envelhece quando não existe responsável ativo ou gatilho de
revisão.

**Decisão prática:** registrar responsável, escopo e condição de atualização; remover
duplicações que não possuem função própria.

**Onde é ensinado:** `MOD-07`.

### RC-07 — Operação de ferramentas e integrações

**Capacidade:** ler, escrever, publicar e operar sistemas externos.

**Mecanismo de falha:** análise é interpretada como autorização para alterar; credenciais
amplas permitem ação destrutiva, vazamento ou publicação prematura.

**Impacto:** perda de dados, indisponibilidade, exposição de informação ou comunicação externa
indevida.

**Controle ensinado:** separar leitura, escrita e publicação; conceder permissão mínima por
etapa; exigir confirmação para operação mutável e alvo exato. No Cordel: política de permissões
versionada com o projeto.

**Evidência do controle:** permissões efetivas, registro de chamadas, confirmação exigida
quando aplicável e verificação posterior do estado.

**Risco residual:** falha de configuração, serviço externo comprometido ou operação autorizada
sobre premissa errada.

**Decisão prática:** reduzir alcance, preferir ações reversíveis e exigir responsável humano
quando impacto ou irreversibilidade forem altos.

**Onde é ensinado:** `MOD-04`.

### RC-08 — Repetição de procedimentos especializados

**Capacidade:** skills e scripts tornam workflows especializados reutilizáveis.

**Mecanismo de falha:** instrução obsoleta, regra local generalizada ou script correto para uma
versão passa a orientar todos os casos.

**Impacto:** erro sistemático e repetível, difícil de perceber porque o procedimento parece
padronizado.

**Controle ensinado:** separar julgamento de execução determinística, versionar procedimentos e
avaliá-los em casos representativos. No Cordel: distinção entre skill, script, modelo e
adaptador.

**Evidência do controle:** versão esperada, casos de avaliação, resultados comparáveis e
registro da fonte que justifica a regra.

**Risco residual:** mudanças externas e casos novos podem ultrapassar os exemplos avaliados.

**Decisão prática:** limitar o escopo declarado da skill e revisar quando ambiente, fonte ou
workflow mudar.

**Onde é ensinado:** `MOD-04` e `MOD-08`.

### RC-09 — Autonomia em tarefas longas

**Capacidade:** perseguir um objetivo, escolher ferramentas, observar resultados e iterar.

**Mecanismo de falha:** pequenas interpretações se acumulam, o objetivo deriva, o agente amplia
o escopo ou repete uma ação errada sem checkpoint. A janela de contexto se esgota e restrições
combinadas no início deixam de ser respeitadas.

**Impacto:** alteração ampla, consumo desnecessário, dificuldade de auditoria e mistura de
trabalho autorizado com trabalho emergente.

**Controle ensinado:** dividir em passos observáveis, calibrar autonomia por risco e
reversibilidade, e interromper ao surgir escopo novo. No Cordel: gates, checkpoints e registro
de execução.

**Evidência do controle:** registro de ações e decisões, checkpoints concluídos e separação
formal de novas necessidades.

**Risco residual:** agentes são não determinísticos e podem falhar entre checkpoints.

**Decisão prática:** reduzir o tamanho da unidade autônoma à medida que impacto, incerteza ou
irreversibilidade aumentam.

**Onde é ensinado:** `MOD-02` e `MOD-07`.

### RC-10 — Síntese de status e rastreabilidade

**Capacidade:** resumir grande volume de trabalho e construir visões de cobertura.

**Mecanismo de falha:** unidade concluída, item fechado, matriz preenchida ou relatório do
agente é tratado como prova de implementação.

**Impacto:** estados são promovidos sem sustentação, lacunas desaparecem do painel e decisões
passam a depender de falsa cobertura.

**Controle ensinado:** exigir que a promoção de estado dependa de evidência acessível e
semanticamente pertinente, não de alegação. No Cordel: alegação não promove estado; vereditos
`parcial` e `divergente` disponíveis e legítimos.

**Evidência do controle:** cada estado `verificado` pode ser percorrido até uma prova acessível
que demonstra as condições relevantes.

**Risco residual:** evidência envelhece, cobre apenas parte da afirmação ou deixa de ser
reproduzível.

**Decisão prática:** registrar revisão ou data quando a prova puder envelhecer e rebaixar o
estado quando a sustentação deixar de existir.

**Onde é ensinado:** `MOD-07`.

### RC-11 — Revisão e leitura de diferenças em volume

**Capacidade:** produzir, em minutos, mais alteração do que uma pessoa revisa com atenção em
uma hora.

**Mecanismo de falha:** a diferença cresce além do que cabe em uma leitura atenta; a revisão
passa a confirmar aparência. Alterações não pedidas — renomeação, reformatação, abstração
prematura, correção de código vizinho — atravessam despercebidas porque estão misturadas ao
que foi pedido.

**Impacto:** escopo excedido sem autorização, regressão introduzida em código não relacionado,
e perda da revisão humana como controle real.

**Controle ensinado:** revisar a diferença contra uma lista declarada do que foi pedido,
começando pelos arquivos alterados antes do conteúdo; manter o passo pequeno o bastante para
caber em uma leitura. No Cordel: escopo e fora do escopo explícitos na story, e implementação
em checkpoints.

**Evidência do controle:** lista de arquivos alterados com o motivo de cada um no escopo
declarado, e o registro dos checkpoints em que a diferença foi observada.

**Risco residual:** revisão cansa. Lotes grandes reduzem a detecção independentemente do
método, e nenhum controle compensa uma sessão de revisão longa demais.

**Decisão prática:** quando a diferença não couber em uma leitura atenta, o problema é o
tamanho do passo, não a disciplina de quem revisa; dividir antes de revisar.

**Onde é ensinado:** `MOD-03` e `MOD-07`.

### RC-12 — Leitura autônoma de conteúdo externo

**Capacidade:** ler issues, páginas, registros, comentários de código e arquivos de
dependências para compor o contexto de trabalho.

**Mecanismo de falha:** o agente não distingue, por si, dado de instrução. Um texto lido para
análise pode conter uma ordem endereçada a ele e, se entrar no contexto com o mesmo estatuto
das instruções legítimas, pode ser obedecido. O padrão mais perigoso combina leitura de
conteúdo externo com capacidade de escrita ou publicação na mesma sessão.

**Impacto:** ação fora do escopo, exfiltração de informação disponível no contexto, alteração
não autorizada ou comunicação externa disparada por um texto que ninguém revisou.

**Controle ensinado:** reduzir o alcance da ação — o dano possível é o que as permissões
permitem; tratar conteúdo lido explicitamente como dado; confirmar ação sensível fora do canal
que a sugeriu; separar a sessão que lê conteúdo externo da que escreve ou publica.

**Evidência do controle:** resultado do cenário adversarial, com o comportamento observado do
agente e a mudança que ele provocou na política de permissões.

**Risco residual:** nenhuma defesa é completa, e a recusa observada uma vez não é garantia — o
comportamento não é determinístico. Reduzir o alcance da ação limita o dano; não o elimina.

**Decisão prática:** desenhar assumindo que a instrução hostil será obedecida em algum momento,
e perguntar o que aconteceria se fosse.

**Onde é ensinado:** `MOD-04`.

### RC-13 — Uso de dados reais em contexto

**Capacidade:** trabalhar sobre dados, logs, configurações e documentos do próprio negócio.

**Mecanismo de falha:** credenciais, dados pessoais, topologia interna ou conteúdo contratual
entram no contexto por conveniência e passam a existir em prompts, registros, artefatos
gerados e históricos de sessão que quem colou o dado não controla.

**Impacto:** exposição de informação de cliente, violação de dever de confidencialidade,
comprometimento de credencial e, em setor regulado, consequência regulatória.

**Controle ensinado:** definir antes, não durante, o que não pode entrar no contexto, com a
alternativa correspondente — referência ao cofre em vez do valor, dados fictícios em exemplos,
faixas de documentação em vez de endereços internos.

**Evidência do controle:** lista específica do projeto, com alternativas, e revisão dos
registros produzidos para confirmar que nada vedado entrou.

**Risco residual:** um dado exposto não volta atrás. A prevenção é o único controle
efetivamente eficaz; a detecção posterior apenas limita a propagação.

**Decisão prática:** quando uma credencial aparecer em log ou arquivo, sinalizar, substituir por
marcador e **rotacionar a credencial** — trocar o valor no texto não desfaz a exposição.

**Onde é ensinado:** `MOD-04`.

## CURSO-06-MATRIZ — Matriz operacional

| ID | Capacidade | Falha predominante | Controle principal | Residual que exige atenção |
|---|---|---|---|---|
| RC-01 | pesquisar | fonte inadequada | autoridade e evidência | fonte canônica incorreta |
| RC-02 | compreender | suposição preenche lacuna | confirmação do comportamento atual | caminho não observado |
| RC-03 | gerar código | implementar interpretação errada | decisão e unidade verificável | premissa ruim formalizada |
| RC-04 | detalhar | inventar decisão | papéis e autorização | decisão humana insuficiente |
| RC-05 | testar | confirmar a própria solução | prova planejada antes do código | oráculo incorreto |
| RC-06 | documentar | propagar conclusão falsa | fonte única e reconciliação | envelhecimento |
| RC-07 | operar | agir sem autoridade adequada | permissão mínima e confirmação | configuração falha |
| RC-08 | reutilizar | repetir regra obsoleta | versionamento e avaliação | caso novo não avaliado |
| RC-09 | agir autonomamente | derivar objetivo | checkpoint e observabilidade | falha entre checkpoints |
| RC-10 | sintetizar | promover alegação a estado | evidência confirmada | prova parcial ou antiga |
| RC-11 | produzir em volume | revisão vira aparência | diferença contra escopo declarado | fadiga de revisão |
| RC-12 | ler conteúdo externo | instrução tratada como ordem | alcance reduzido da ação | recusa não é garantia |
| RC-13 | usar dados reais | exposição por conveniência | lista prévia de dados vedados | exposição é irreversível |

## CURSO-06-ATV — Clínica de risco

### Objetivo

Analisar uma tarefa real do projeto-laboratório e propor controles que preservem o benefício do
agente sem esconder o risco residual.

### Preparação

Cada grupo recebe um cenário diferente:

- investigar uma regra em código legado;
- gerar uma migração de dados;
- atualizar uma documentação canônica;
- executar testes e sintetizar cobertura;
- operar uma integração de publicação;
- conduzir uma implementação autônoma de 40 minutos;
- revisar uma alteração de 600 linhas produzida em dez minutos;
- analisar um item de backlog escrito por alguém de fora da equipe.

Os dois últimos cenários são novos e correspondem a `RC-11` e `RC-12`.

### Rodada 1 — Construção, 20 minutos

O grupo preenche:

| Campo | Resposta do grupo |
|---|---|
| resultado esperado | |
| capacidade concedida | |
| mecanismo de falha | |
| impacto e alcance | |
| controles preventivos | |
| controles detectivos | |
| evidência dos controles | |
| risco residual | |
| responsável pela decisão | |

### Rodada 2 — Teste adversarial, 15 minutos

Outro grupo tenta encontrar:

- controle apenas declarado, sem evidência;
- permissão maior que a tarefa;
- risco residual apresentado como eliminado;
- decisão atribuída ao agente;
- falha que o teste proposto não conseguiria detectar;
- controle que depende de alguém lembrar de fazer, em vez de estar no ambiente.

### Rodada 3 — Decisão, 10 minutos

O grupo revisa a análise e escolhe uma saída:

- autorizar nas condições propostas;
- reduzir escopo ou permissão;
- acrescentar controle;
- exigir decisão humana;
- bloquear até obter evidência.

### Produto

Registro de risco com decisão justificada e pelo menos uma evidência verificável de controle.

## CURSO-06-ROTEIRO — Roteiro sugerido

| Tempo | Etapa | Condução |
|---:|---|---|
| 0–10 min | Caso inicial | Compare a mesma tarefa com leitura e com publicação |
| 10–20 min | Vocabulário | Diferencie falha, impacto, controle, evidência e residual |
| 20–30 min | Modelo | Aplique as oito perguntas a um exemplo |
| 30–45 min | Catálogo | Distribua os treze riscos entre grupos para explicação curta |
| 45–65 min | Clínica, rodada 1 | Grupos constroem a análise |
| 65–80 min | Clínica, rodada 2 | Revisão adversarial entre grupos |
| 80–87 min | Decisão | Revisão e autorização, redução ou bloqueio |
| 87–90 min | Fechamento | Registre o residual mais frequentemente esquecido |

Os 90 minutos introduzem o modelo. A matriz volta a ser usada nos laboratórios seguintes,
especialmente antes de conceder ferramentas ou ampliar autonomia.

Esta unidade não é um encontro próprio: seu conteúdo é distribuído entre os módulos, com maior
concentração no `MOD-04`. Em turmas de setor regulado, `RC-07`, `RC-12` e `RC-13` justificam
tempo adicional, conforme a pendência registrada naquele módulo.

## CURSO-06-AVAL — Verificação da aprendizagem

Uma análise demonstra domínio quando:

1. descreve uma tarefa concreta, não "uso de IA" em geral;
2. explica o mecanismo de falha, não apenas afirma que o agente pode errar;
3. relaciona impacto a alcance e reversibilidade;
4. escolhe controles aplicáveis ao cenário;
5. apresenta evidência de que o controle foi aplicado;
6. reconhece risco residual;
7. atribui a decisão a um responsável com autoridade;
8. preserva o benefício que justificou usar o agente;
9. enuncia o controle de forma aplicável em um time que não use o Cordel.

## CURSO-06-EQUIVOCOS — Equívocos a observar

### "Se existe revisão humana, o risco está controlado."

Revisão é um controle somente quando responsável, escopo, informação disponível e critério de
decisão estão claros. Revisão rápida de grande volume pode apenas validar aparência — é
exatamente o mecanismo de `RC-11`.

### "Sandbox resolve segurança."

Sandbox reduz determinado alcance operacional. Não corrige requisito errado, fonte antiga,
decisão indevida ou vazamento por ferramenta autorizada.

### "Mais controles sempre significam mais segurança."

Controles sem relação com o mecanismo de falha criam custo e falsa confiança. O objetivo é
controle proporcional e verificável.

### "Risco residual é falha do método."

Todo controle possui limite. Tornar o residual explícito permite decisão consciente e evita
promessas de segurança absoluta.

### "Operação reversível não precisa de autorização."

Reversibilidade reduz impacto, mas não concede autoridade nem elimina efeitos externos, custos
ou exposição de dados.

### "O modelo é treinado para não obedecer instruções maliciosas."

O comportamento não é determinístico e não constitui controle. A proteção é o alcance limitado
da ação.

### "Esses riscos são do Cordel."

São do trabalho com agentes. O Cordel implementa alguns controles; outros dependem do ambiente,
da organização e de decisões humanas que nenhum método toma no lugar de ninguém.

## CURSO-06-MAT — Materiais necessários

- matriz das oito perguntas de risco;
- cartões com os oito cenários da clínica;
- exemplos de permissões de leitura, escrita e publicação;
- registro de chamadas de ferramenta do projeto-laboratório;
- exemplos de controle declarado e controle evidenciado;
- exemplo de alteração grande demais para uma leitura atenta, para o cenário de `RC-11`;
- item de backlog com instrução hostil embutida, para o cenário de `RC-12`;
- ficha de revisão adversarial;
- matriz `RC-01` a `RC-13`.

## CURSO-06-FONTES — Fontes no método

- [`../../method/manifesto.md`](../../method/manifesto.md)
- [`../../method/concepts.md`](../../method/concepts.md)
- [`../../method/ai-driven-development.md`](../../method/ai-driven-development.md)
- [`../../method/catalog.md`](../../method/catalog.md)
- [`../../method/traceability.md`](../../method/traceability.md)
- [`../../method/team-knowledge.md`](../../method/team-knowledge.md)
- [`../../skill/cordel/references/investigacao.md`](../../skill/cordel/references/investigacao.md)
- [`../../skill/cordel/references/preparacao.md`](../../skill/cordel/references/preparacao.md)
- [`../../skill/cordel/references/fechamento.md`](../../skill/cordel/references/fechamento.md)

## CURSO-06-PEND — Pontos para a próxima revisão

- `RC-11`, `RC-12` e `RC-13` são novos nesta revisão e ainda não foram usados em turma;
- escrever os dois cartões novos da clínica e validar que cabem no mesmo tempo dos demais;
- definir uma escala simples de impacto e exposição para uso no laboratório;
- criar exemplos de evidência de permissão e observabilidade;
- validar o catálogo com incidentes e quase-erros das experiências de origem, em especial se há
  caso real de `RC-12` para citar;
- revisar riscos após escolher a tecnologia do laboratório;
- testar se a atividade diferencia controle declarado de controle aplicado;
- avaliar, com a área de segurança do cliente, se `RC-12` e `RC-13` devem ser aprofundados em
  turmas de setor regulado;
- definir responsáveis pela manutenção futura do catálogo.
