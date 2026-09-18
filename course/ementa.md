# Engenharia de software com agentes de IA: contexto, decisão e evidência

*Aplicando o método Cordel.*

## Identificação do curso

- **Carga horária sugerida:** 24 horas, em 8 encontros de 3 horas.
- **Formato:** treinamento prático, presencial ou remoto, com exposição curta, demonstração,
  laboratório orientado e retrospectiva.
- **Público-alvo:** pessoas desenvolvedoras, tech leads, arquitetas, analistas de qualidade,
  produto e demais profissionais que participam da definição, implementação ou validação de
  mudanças de software.
- **Pré-requisitos:** experiência básica com desenvolvimento de software, Git, leitura de
  código e execução de testes. Não é necessário conhecer ferramentas de IA em profundidade.
- **Projeto-laboratório:** aplicação pequena, versionada e executável, com requisitos,
  código, testes e demandas deliberadamente ambíguas ou incompletas.
- **Ferramenta de referência:** o Cordel é usado a partir do quinto encontro como
  implementação concreta dos controles estudados antes. Os quatro primeiros encontros são
  conduzidos com qualquer agente disponível, sem método instalado.

## Ementa

Fundamentos de inteligência artificial aplicada à engenharia de software. Como um agente
transforma uma solicitação em ação: modelo, janela de contexto, ferramentas, ciclo de
observação e ação, não determinismo, custo e latência. Condução deliberada de agentes:
decomposição, especificação de tarefa, restrições, checkpoints, calibragem de autonomia e
critérios para não usar IA. Verificação do que a IA produz: plausibilidade e evidência,
revisão de diferenças, padrões típicos de erro do agente, teste adversarial. Ambiente de
controle: skills, scripts, MCP, harness, permissões, guardrails, observabilidade, evals,
segurança e confidencialidade em fluxos assistidos por IA.

Riscos introduzidos ou ampliados por agentes: respostas plausíveis sem sustentação,
aceleração na direção errada, perda de contexto, autoridade implícita, baixa
rastreabilidade, automação de erros, instrução hostil em conteúdo lido, exposição de dados
sensíveis e divergência entre documentação, código e testes.

Aplicação do Cordel como uma implementação possível desses controles, orientada por
contexto, especificações e evidências. Fontes da verdade, fatos, alegações, inferências,
evidências, artefatos e projeções. Cadeia origem, classificação, AS-IS, decisão,
story/spec, gate, implementação, prova e reconciliação. Transferência dos controles para o
contexto de trabalho de cada participante, com ou sem a ferramenta usada no curso, e
evolução do método com evidência de uso.

## Problema orientador

> Conteúdo detalhado: [Markdown](topics/CURSO-03.md) · [HTML](topics/CURSO-03.html).

Agentes de IA reduzem o custo de pesquisar, explicar, planejar, escrever, testar e revisar
software. Esse ganho também reduz o intervalo entre uma premissa errada e uma alteração
concreta. O desafio deixa de ser apenas produzir código e passa a incluir controlar:

- qual necessidade deu origem à mudança;
- o que é fato, relato, inferência ou decisão;
- o que o sistema realmente faz hoje;
- quem autorizou uma mudança de escopo;
- como o resultado esperado será observado;
- qual prova sustenta a afirmação de que o trabalho terminou;
- como documentação, código, testes e conhecimento do produto voltarão a concordar.

Essas sete perguntas são o currículo real do curso. O Cordel será estudado como uma resposta
de engenharia a elas — não como a única resposta possível, não como mecanismo para eliminar
julgamento humano e não como garantia de que um modelo esteja correto. Uma pessoa que
conclua o curso deve conseguir responder às sete perguntas em um time que não use o Cordel.

## Objetivo geral

Capacitar a turma a conduzir uma mudança de software com auxílio de agentes de IA de forma
rastreável, verificável e proporcional ao risco, e a transferir esses controles para o
próprio contexto de trabalho, tendo o Cordel como implementação de referência aplicada em um
projeto-laboratório.

## Objetivos de aprendizagem

> Conteúdo detalhado: [Markdown](topics/CURSO-04.md) · [HTML](topics/CURSO-04.html).

Cada objetivo é enunciado como competência independente de ferramenta. Quando o Cordel
oferece uma implementação direta daquela competência, ela aparece entre parênteses. Ao final
do curso, cada participante deverá ser capaz de:

1. explicar como um agente transforma uma solicitação em ação — modelo, janela de contexto,
   ferramentas, ciclo de observação e ação — e por que o resultado não é determinístico;
2. reconhecer em quais etapas da engenharia de software a IA gera ganho real, em quais o
   custo de verificação supera o ganho e quando a decisão correta é não usar IA;
3. conduzir um agente deliberadamente: decompor a tarefa, declarar objetivo, restrições e
   critério de pronto, e escolher entre refinar a sessão ou reiniciá-la;
4. calibrar autonomia, ferramentas e permissões conforme risco e reversibilidade da ação
   (no Cordel: harness declarado e política mínima de permissões);
5. separar fato, relato, inferência, decisão e evidência em qualquer afirmação técnica,
   produzida por pessoa ou por agente;
6. verificar produção de IA: revisar diferenças contra o escopo, reconhecer padrões típicos
   de erro do agente e projetar um teste capaz de falhar (no Cordel: estratégia de prova);
7. confirmar o comportamento atual do sistema em fonte inspecionável antes de propor uma
   mudança (no Cordel: AS-IS confirmado);
8. localizar a origem de uma demanda e distinguir necessidade de autorização (no Cordel:
   origem e triagem em filtros);
9. transformar um pedido em unidade de trabalho verificável, com objetivo observável,
   escopo, fora do escopo e critérios que tenham forma de prova (no Cordel: necessidade,
   story e, quando justificada, spec);
10. decidir e registrar, de modo contestável por outra pessoa, se há informação suficiente
    para autorizar a mudança (no Cordel: gate com três resultados);
11. reconhecer riscos de segurança e confidencialidade próprios de agentes: instrução hostil
    em conteúdo lido, exposição de dados de cliente, credenciais em registros e fronteiras
    de confiança de integrações;
12. fechar uma mudança reconciliando fontes, implementação e testes, e transferir os
    controles aprendidos para o próprio time, com ou sem a ferramenta usada no curso (no
    Cordel: reconciliação, núcleo portátil e adaptador do projeto).

## Hipótese pedagógica

> Conteúdo detalhado: [Markdown](topics/CURSO-05.md) · [HTML](topics/CURSO-05.html).

O curso usa uma única demanda como fio condutor. Em vez de exercícios isolados de prompt,
a turma recebe um pedido incompleto, investiga o projeto, toma decisões nos papéis
apropriados, prepara a mudança, usa o agente para implementá-la e precisa provar o
resultado. Novas informações são liberadas durante os encontros para simular drift,
ambiguidade, mudança de escopo e evidência insuficiente.

A ordem é deliberada: **princípio antes da ferramenta**. Nos três primeiros encontros a
turma trabalha sem método instalado e sente na prática cada falha que o Cordel endereça. Ao
final do terceiro encontro, cada grupo escreve seu próprio **protocolo mínimo** de trabalho
com IA — uma página em Markdown, com os controles que o grupo julga indispensáveis. No
quinto encontro o Cordel é apresentado ao lado desse protocolo, em comparação explícita:
quais controles o grupo já havia identificado, quais faltaram, quais o Cordel implementa de
forma diferente e por quê.

Essa inversão existe para evitar o efeito mais comum em treinamentos de ferramenta: a pessoa
aprende o procedimento sem reconhecer o problema que ele resolve e, ao trocar de ferramenta
ou de empresa, não leva nada consigo.

A distribuição sugerida de cada encontro é:

- 45 minutos de conceitos e discussão;
- 30 minutos de demonstração pelo instrutor;
- 90 minutos de laboratório em duplas ou trios;
- 15 minutos de registro de evidências e retrospectiva.

## Estrutura em três blocos

| Bloco | Encontros | Pergunta que o bloco responde | Ferramenta |
|---|---|---|---|
| I — Fundamentos | 1 a 3 | Como se trabalha com um agente sem se enganar? | qualquer agente, sem método instalado |
| II — Controle e método | 4 a 6 | Como transformar esses controles em prática repetível de time? | harness explícito e Cordel |
| III — Prova e transferência | 7 e 8 | Como provar o resultado e levar isso para o meu time? | Cordel e o contexto real de cada participante |

## Matriz de problemas, riscos e mitigação

> Conteúdo detalhado: [Markdown](topics/CURSO-06.md) · [HTML](topics/CURSO-06.html).

A coluna de mitigação enuncia primeiro o controle, que é independente de ferramenta, e
depois a forma como o Cordel o implementa.

| O que a IA ajuda a resolver | Problema novo ou ampliado | Controle ensinado e implementação no Cordel | Limite ou risco residual |
|---|---|---|---|
| Pesquisa rápida em código e documentação | resposta plausível baseada em fonte errada ou desatualizada | declarar quais fontes têm autoridade e exigir evidência endereçável para cada afirmação; no Cordel, fontes da verdade, índice curto e contexto carregado sob demanda | a fonte canônica também pode estar errada; revisão humana continua necessária |
| Compreensão de sistemas legados | modelo completa lacunas com suposições | investigar do geral ao específico e confirmar o comportamento atual em fonte inspecionável antes de propor mudança; no Cordel, AS-IS confirmado e separação entre relato e observação | buscas negativas não provam ausência absoluta |
| Geração acelerada de código | implementação veloz do problema errado | exigir decisão humana explícita e unidade verificável antes do código; no Cordel, origem, classificação e gate de entrada | um gate mal revisado pode apenas formalizar uma premissa ruim |
| Detalhamento de requisitos e soluções | documento de solução tratado como origem, autorização ou prova | distinguir necessidade, requisito, unidade de trabalho e detalhamento técnico; no Cordel, necessidade, story e spec com papéis distintos | ambiguidades de negócio não são eliminadas pelo método |
| Geração de testes | testes que confirmam a interpretação equivocada do próprio agente | definir critérios observáveis e projetar o teste antes da implementação, garantindo que ele possa falhar; no Cordel, estratégia de prova declarada no gate | cobertura e qualidade dos oráculos ainda exigem julgamento técnico |
| Revisão e leitura de diferenças | volume de código gerado excede a capacidade de revisão atenta | revisar a diferença contra o escopo declarado e reconhecer padrões típicos de erro do agente; no Cordel, escopo e fora do escopo explícitos na story | revisão cansa; lotes grandes reduzem a detecção independentemente do método |
| Atualização de documentação | propagação rápida de informação falsa e documentos divergentes | manter fontes canônicas e regenerar projeções em vez de editá-las; no Cordel, reconciliação obrigatória no fechamento | sem responsáveis e revisão, o conhecimento volta a envelhecer |
| Operação de ferramentas e integrações | alteração externa sem autoridade, vazamento ou ação destrutiva | separar leitura, escrita e publicação, conceder permissão mínima por etapa e tratar cada integração como fronteira de confiança; no Cordel, política de permissões versionada com o projeto | controles dependem da configuração correta do harness e dos serviços externos |
| Leitura autônoma de conteúdo externo | instrução hostil embutida em issue, página, log ou dependência lida pelo agente | tratar conteúdo lido como dado, nunca como instrução, e confirmar ações sensíveis fora do canal que as sugeriu | nenhuma defesa é completa; reduzir o alcance da ação limita o dano |
| Uso de dados reais em contexto | exposição de dados de cliente, credenciais e segredos em prompts, registros e artefatos | definir o que pode entrar no contexto, usar dados fictícios em exemplos e revisar registros antes de compartilhar | um dado exposto não volta atrás; a prevenção é o único controle eficaz |
| Repetição de procedimentos especializados | skill obsoleta ou excessivamente específica passa a orientar todos os casos | separar julgamento de execução determinística e versionar procedimentos; no Cordel, distinção entre skill, script, modelo e adaptador | skills precisam de versionamento, avaliação e manutenção |
| Autonomia em tarefas longas | deriva de objetivo, automação de erro e dificuldade de auditoria | dividir em passos observáveis, calibrar autonomia por risco e interromper ao surgir escopo novo; no Cordel, gates, checkpoints e registro de execução | agentes continuam não determinísticos |
| Síntese de status e rastreabilidade | "lavagem de evidência": documento, issue ou relatório tratado como prova | exigir que a promoção de estado dependa de evidência acessível e pertinente, não de alegação; no Cordel, vereditos com evidência obrigatória | evidência pode envelhecer ou cobrir apenas parte da afirmação |

## Cronograma detalhado

### Bloco I — Fundamentos do trabalho com agentes

### Encontro 1 — Como um agente funciona e por que erra

> Conteúdo detalhado: [Markdown](topics/MOD-01.md) · [HTML](topics/MOD-01.html).

**Conceitos:** panorama do uso de IA na engenharia de software; o que o modelo enxerga do
seu problema; janela de contexto e o que acontece quando ela se esgota; corte de
conhecimento; não determinismo entre execuções; custo e latência como variáveis de projeto;
produtividade local versus entrega correta; o duplo efeito da aceleração.

**Prática:** pedir ao agente que responda a uma demanda ambígua do projeto-laboratório, sem
método e sem preparo. Executar a mesma solicitação três vezes e comparar as respostas. A
turma identifica suposições, decisões implícitas, fontes ausentes, afirmações sem prova e a
variação entre execuções.

**Entrega:** diagnóstico inicial com benefícios percebidos, riscos observados, divergência
medida entre execuções e perguntas que deveriam ter sido respondidas antes de alterar
código.

### Encontro 2 — Condução: da intenção à tarefa executável

> Conteúdo detalhado: [Markdown](topics/MOD-02.md) · [HTML](topics/MOD-02.html).

**Conceitos:** decomposição de uma demanda em tarefas executáveis; especificação de tarefa —
objetivo, restrições, fora do escopo e critério de pronto; uso de exemplos e contraexemplos;
seleção deliberada do que entra no contexto; refinamento iterativo versus reinício de
sessão; calibragem de autonomia por risco e reversibilidade; critérios para não usar IA.

**Prática:** refazer a demanda do primeiro encontro com condução deliberada. Cada dupla
declara objetivo, restrições e critério de pronto antes de acionar o agente, e registra
onde precisou intervir. Comparação direta com o resultado do encontro anterior.

**Entrega:** especificação da tarefa, registro das intervenções necessárias e análise
comparativa entre a condução ingênua e a deliberada.

### Encontro 3 — Verificação: o que a IA produziu merece crédito?

> Conteúdo detalhado: [Markdown](topics/MOD-03.md) · [HTML](topics/MOD-03.html).

**Conceitos:** plausibilidade não é evidência; fato, relato, inferência, decisão e
evidência; confirmar o comportamento atual antes de propor o novo; leitura de diferenças
contra escopo declarado; padrões típicos de erro do agente — teste que confirma a própria
interpretação, abstração prematura, tratamento de erro decorativo, alteração fora do pedido;
teste adversarial e a pergunta "este teste consegue falhar?".

**Prática:** auditar a produção do encontro anterior. Cada grupo revisa o trabalho de outro
grupo, classifica cada afirmação do agente, localiza o que foi alterado sem pedido e tenta
quebrar os testes gerados.

**Entrega:** relatório de auditoria e, ao final do encontro, o **protocolo mínimo** do grupo:
uma página com os controles que o grupo considera indispensáveis para trabalhar com IA.
Esse documento será confrontado com o Cordel no quinto encontro.

### Bloco II — Ambiente de controle e método

### Encontro 4 — Harness, permissões e segurança

> Conteúdo detalhado: [Markdown](topics/MOD-04.md) · [HTML](topics/MOD-04.html).

**Conceitos:** modelo, agente, ferramenta, skill, script, modelo de documento, MCP, harness;
engenharia de contexto; permissões e guardrails; observabilidade e evals; segurança
específica de agentes — instrução hostil em conteúdo lido, exfiltração, credenciais em
registros, dados de cliente no contexto e cada integração como fronteira de confiança.

**Prática:** desenhar o harness do laboratório — instruções, fontes, ferramentas de leitura
e escrita, ações que exigem confirmação e verificações obrigatórias. Em seguida, cenário
adversarial: o instrutor planta uma instrução hostil em um arquivo do projeto e a turma
observa o comportamento do agente.

**Entrega:** mapa do ambiente do agente, política mínima de permissões e lista de dados que
não podem entrar no contexto.

### Encontro 5 — Cordel como implementação do protocolo

> Conteúdo detalhado: [Markdown](topics/MOD-05.md) · [HTML](topics/MOD-05.html).

**Conceitos:** confronto entre o protocolo mínimo escrito no encontro 3 e o Cordel — o que
a turma já havia identificado, o que faltou e o que o método resolve de forma diferente;
manifesto; fonte da verdade; produto versus projeto; artefato versus projeção; conhecimento
ativo, canônico, histórico, gerado e local; núcleo portátil versus adaptador do projeto.

**Prática:** inicializar o Cordel, preencher `.cordel/project.json`, organizar o índice e
executar a verificação até obter `GO`. Classificar documentos e registros fornecidos. Cada
grupo marca, no próprio protocolo, quais controles passaram a ser cobertos pela ferramenta e
quais continuam sendo responsabilidade humana.

**Entrega:** adaptador do projeto versionável, inventário das fontes com responsável e
escopo, e protocolo mínimo anotado com a comparação.

### Encontro 6 — Da demanda à unidade autorizada

> Conteúdo detalhado: [Markdown](topics/MOD-06.md) · [HTML](topics/MOD-06.html).

**Conceitos:** cadeia mínima; origem da demanda; classificação em defeito, lacuna
documental, detalhamento de compromisso existente ou escopo novo; busca negativa; drift de
ambiente; necessidade versus unidade autorizada; objetivo observável; escopo e fora do
escopo; critérios de aceite com forma de prova; quando criar uma spec; impactos, riscos,
dependências e ADRs; gate com três resultados.

**Prática:** localizar a origem da demanda, pesquisar fontes integrais, inspecionar código e
testes, registrar evidências e confirmar o AS-IS. Em seguida, simulação de decisão pelo
responsável de produto e criação da story e, quando justificada, da spec. Cada critério
precisa de uma forma de prova.

**Entrega:** análise de triagem, AS-IS confirmado, unidade de trabalho rastreável e veredito
de gate. Grupos bloqueados devem explicar o que falta em vez de fabricar uma decisão.

### Bloco III — Prova e transferência

### Encontro 7 — Implementação assistida e prova

> Conteúdo detalhado: [Markdown](topics/MOD-07.md) · [HTML](topics/MOD-07.html).

**Conceitos:** contexto mínimo pertinente; execução incremental e checkpoints; detecção de
escopo emergente; diferença entre código produzido e resultado provado; relações declaradas
e inferidas; estados de rastreabilidade; evidência suficiente; vereditos `verificado`,
`parcial`, `divergente`, `nao-iniciado` e `nao-rastreavel`; integração do rastro com branch,
pull request, revisão humana e CI.

**Prática:** usar o agente para planejar e implementar a story aprovada, revisando as
diferenças em checkpoints. Uma mudança de escopo é introduzida durante o laboratório; a
resposta esperada é separá-la e devolvê-la à triagem. Em seguida, relacionar cada aceite a
uma prova, executar build e testes, revisar as evidências de outro grupo, atualizar o AS-IS
e regenerar as projeções.

**Entrega:** alteração funcional com testes proporcionais ao risco, registro das ações,
dossiê de evidências, contexto canônico reconciliado e decisão justificada entre
`implementado` e `verificado`.

### Encontro 8 — Transferência e evolução

> Conteúdo detalhado: [Markdown](topics/MOD-08.md) · [HTML](topics/MOD-08.html).

**Conceitos:** núcleo portátil versus adaptador local; conhecimento federado; responsáveis
por fontes; versionamento de skills; evals de workflows; sinais de atrito; critérios para
generalização; adoção incremental; tradução dos controles para ferramentas que o time já
usa.

**Prática:** retrospectiva baseada nos artefatos do curso. Cada grupo propõe uma melhoria ao
método, classifica-a como regra local ou candidata ao núcleo e desenha uma avaliação que
possa refutar ou sustentar a proposta. Em seguida, o **teste de transferência**: cada
participante descreve, individualmente, como aplicaria os controles do curso no próprio
time, que provavelmente não usa o Cordel, indicando qual controle é inegociável, qual seria
adaptado e qual não se aplica.

**Entrega:** plano de adoção de 30 dias, proposta de evolução com problema observado,
evidência, alcance, risco, hipótese e forma de avaliação, e o teste de transferência
individual.

## Origem do conteúdo por módulo

Tabela de rastreamento desta revisão. A numeração dos módulos é posicional: ao aplicar a
reestruturação, o conteúdo indicado na coluna de origem migra para o novo identificador.

| Novo | Título | Origem |
|---|---|---|
| MOD-01 | Como um agente funciona e por que erra | MOD-01 anterior, ampliado com mecânica do modelo |
| MOD-02 | Condução: da intenção à tarefa executável | novo |
| MOD-03 | Verificação: o que a IA produziu merece crédito? | novo, absorve partes de MOD-01, MOD-04 e MOD-07 anteriores |
| MOD-04 | Harness, permissões e segurança | MOD-02 anterior, ampliado com segurança e confidencialidade |
| MOD-05 | Cordel como implementação do protocolo | MOD-03 anterior, com o confronto contra o protocolo mínimo |
| MOD-06 | Da demanda à unidade autorizada | MOD-04 e MOD-05 anteriores, fundidos |
| MOD-07 | Implementação assistida e prova | MOD-06 e MOD-07 anteriores, fundidos, mais integração com git e CI |
| MOD-08 | Transferência e evolução | MOD-08 anterior, mais o teste de transferência |

## Padrão editorial dos módulos

Cada conceito apresentado em um módulo deve ser escrito em três níveis, nesta ordem:

1. **Princípio** — a afirmação válida independentemente de ferramenta.
2. **Prática** — como aplicá-la com qualquer agente disponível.
3. **No Cordel** — como o método formaliza, automatiza ou impõe aquele controle.

O terceiro nível é opcional; o primeiro não é. Um conceito que só exista no terceiro nível é
sinal de que o curso está ensinando a ferramenta no lugar do fundamento.

## Projeto-laboratório

O projeto deve ser pequeno o bastante para ser compreendido no curso e completo o bastante
para conter decisões reais. Recomenda-se que tenha:

- aplicação executável com dois ou três componentes;
- pelo menos uma integração ou persistência simples;
- suíte de testes parcialmente útil, mas não perfeita;
- documentação AS-IS com uma lacuna intencional;
- requisito válido e uma decisão histórica;
- uma demanda que possa parecer defeito, mas revele escopo novo após investigação;
- código existente que contradiga uma alegação fornecida no início;
- identificadores controlados, para que a turma não possa inventá-los;
- uma projeção gerada que diverge da fonte;
- um evento de drift ou mudança de escopo liberado durante a implementação;
- um arquivo com instrução hostil plantada, para o cenário adversarial do encontro 4;
- dados fictícios em todos os exemplos, sem credenciais reais em nenhum ponto do repositório.

Papéis de produto, engenharia, qualidade e responsável por decisão podem ser distribuídos
entre participantes. O instrutor controla a liberação das fontes e registra quais decisões
foram realmente autorizadas.

## Artefatos produzidos pela turma

1. diagnóstico do uso ingênuo de IA, com divergência medida entre execuções;
2. especificação de tarefa e análise comparativa de condução;
3. relatório de auditoria da produção do agente;
4. protocolo mínimo do grupo;
5. mapa do harness, política de permissões e lista de dados vedados ao contexto;
6. `.cordel/project.json`, índice de contexto e protocolo mínimo anotado;
7. análise de triagem, evidências do AS-IS, story, spec quando aplicável e gate;
8. implementação, testes e diferenças revisadas;
9. relação aceite-prova, evidências finais e contexto canônico reconciliado;
10. retrospectiva, plano de adoção, proposta de evolução e teste de transferência.

## Avaliação

A avaliação é contínua e baseada no rastro produzido, não no volume de código. As dimensões
são independentes de ferramenta; os artefatos do Cordel entram como evidência, não como
critério.

| Dimensão | Peso | Evidência esperada |
|---|---:|---|
| Condução do agente | 20% | tarefa decomposta, objetivo e restrições declarados, contexto selecionado com motivo, autonomia proporcional ao risco |
| Verificação do que a IA produziu | 20% | diferenças revisadas contra o escopo, afirmações classificadas, testes capazes de falhar, ceticismo calibrado |
| Rastreabilidade da decisão | 15% | origem localizada, AS-IS confirmado, autorização explícita e bloqueios honestos |
| Implementação e qualidade técnica | 15% | mudança coerente, testes proporcionais e ausência de escopo não autorizado |
| Segurança e limites de operação | 15% | permissões mínimas, dados sensíveis fora do contexto e reação correta ao cenário adversarial |
| Transferência para o próprio contexto | 15% | controles enunciados sem depender do vocabulário do Cordel e adaptação justificada ao time real |

Uma entrega tecnicamente funcional não recebe pontuação máxima se não for rastreável ou se
estiver fora da autorização. Uma equipe pode demonstrar competência ao manter o gate
`BLOQUEADO` quando faltarem condições reais para avançar. Reproduzir corretamente o
procedimento do Cordel sem saber explicar qual risco ele mitiga não caracteriza domínio da
competência.

## Critérios de conclusão

Para concluir o curso, a pessoa participante deve:

- participar das decisões e revisões do projeto-laboratório;
- entregar a cadeia da demanda até o fechamento, ainda que o veredito final seja
  justificadamente `parcial` ou `BLOQUEADO`;
- demonstrar, na revisão final, onde o agente ajudou, onde introduziu risco e qual controle
  alterou uma decisão ou evitou um erro;
- responder às sete perguntas do problema orientador sem usar o vocabulário do Cordel,
  demonstrando que o fundamento foi aprendido e não apenas o procedimento;
- apresentar uma proposta de adoção ou evolução que preserve a separação entre núcleo e
  adaptador do projeto.

## Evolução do próprio curso

Cada turma deve gerar dados para melhorar o treinamento. Registre tempo por etapa,
bloqueios, erros evitados, informações redescobertas, campos que não alteraram decisões,
falhas de compreensão e diferenças entre grupos. Registre também quantos controles do
protocolo mínimo cada grupo identificou por conta própria antes do encontro 5: essa medida
indica se o Bloco I está cumprindo sua função.

Uma mudança entra no material-base quando resolve uma dificuldade recorrente ou um risco
relevante. Particularidades da linguagem, arquitetura, organização ou ferramenta do
laboratório permanecem no guia daquela edição. Essa regra permite ensinar a evolução do
Cordel aplicando ao próprio curso o princípio de evoluir com evidência de uso.

## Leituras de apoio no repositório

1. [`../method/manifesto.md`](../method/manifesto.md)
2. [`../method/concepts.md`](../method/concepts.md)
3. [`../method/ai-driven-development.md`](../method/ai-driven-development.md)
4. [`../method/catalog.md`](../method/catalog.md)
5. [`../method/traceability.md`](../method/traceability.md)
6. [`../method/adoption.md`](../method/adoption.md)
7. [`../method/team-knowledge.md`](../method/team-knowledge.md)
8. [`../skill/cordel/references/`](../skill/cordel/references/)

## Estado desta revisão

Esta ementa, os oito módulos em `topics/MOD-01.md` a `topics/MOD-08.md` e as quatro unidades
transversais em `topics/CURSO-03.md` a `topics/CURSO-06.md` já refletem a reestruturação em
três blocos, com o padrão editorial de três níveis aplicado às seções de conceitos e as
projeções HTML regeneradas.

A projeção navegável `ementa.html` e os nove decks em `apresentacao/` também já
refletem esta revisão: um deck de abertura, que apresenta o curso, e oito decks de aula,
um por encontro, com os conceitos, as demonstrações e as etapas de laboratório. São
gerados por `scripts/build_deck.py` e não devem ser editados à mão.

O arquivo `apresentacao/cordel-na-pratica.pptx` corresponde à estrutura anterior e foi
substituído.

Nenhum conteúdo desta revisão foi aplicado em turma. As pendências de cada módulo registram,
uma a uma, o que precisa ser produzido, cronometrado ou validado antes da primeira edição —
com atenção especial aos módulos `MOD-02`, `MOD-03`, `MOD-06` e `MOD-07`.
