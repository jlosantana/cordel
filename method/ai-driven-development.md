# Conceitos de desenvolvimento orientado por IA

## Visão do conjunto

Neste método, desenvolvimento orientado por IA não significa delegar decisões ao modelo.
Significa preparar um ambiente no qual um agente consegue investigar, planejar, executar e
provar mudanças dentro de limites explícitos.

```text
                        harness
  instruções + contexto + permissões + observabilidade + avaliações
                              |
                         agente + modelo
                         /             \
                    skills          ferramentas
                                        |
                                       MCP
                              |
                  spec + código + testes + evidências
```

Os elementos são complementares; nenhum deles substitui requisitos, código, testes ou
julgamento humano.

## Conceitos fundamentais

### Spec-driven development (SDD)

Prática de definir e refinar o comportamento esperado antes da implementação, usando a
spec como contrato compartilhado entre pessoas e agentes. Um fluxo comum é
`spec -> plano -> tarefas -> implementação`.

No Cordel, SDD é uma parte do método, não o processo
inteiro. A spec descreve o TO-BE, mas só deve ser criada depois de localizar a origem,
classificar a demanda e confirmar o AS-IS. Mudanças simples podem não exigir uma spec;
critérios de aceite e estratégia de prova continuam obrigatórios.

### Agente

Sistema que usa um modelo para perseguir um objetivo, interpretar instruções, escolher
ferramentas, observar resultados e iterar. O modelo raciocina e gera respostas; o agente
acrescenta estado, ferramentas e um ciclo de execução. Um agente não recebe autoridade
implícita: escopo, permissões e decisões humanas continuam limitando suas ações.

### Skill

Pacote reutilizável de instruções, referências, scripts e modelos para um trabalho que
exige conhecimento ou procedimento especializado. Uma skill ensina **como conduzir** uma
tarefa e quando aplicar determinado workflow. Ela não é uma ferramenta externa nem uma
garantia de execução correta; seus resultados ainda precisam de validação.

### MCP (Model Context Protocol)

Protocolo aberto de integração entre aplicações de IA e servidores que expõem
**ferramentas**, **recursos** e **prompts**. MCP padroniza a conexão; não define o método de
desenvolvimento, a autorização do usuário ou a qualidade da fonte. Cada servidor deve ser
tratado como uma fronteira de confiança, com acesso mínimo e operações mutáveis sujeitas a
controle explícito.

### Harness

Nome dado aqui à infraestrutura que envolve o modelo e torna o trabalho do agente
repetível e controlável. Inclui instruções do repositório, carregamento de contexto,
skills, ferramentas e MCPs, permissões, sandbox, limites de execução, registro de ações,
gates e verificações. O termo não possui uma definição única no setor; este é o significado
adotado pelo Cordel.

Um bom harness torna o caminho correto fácil de seguir e ações perigosas difíceis de
executar por acidente. `AGENTS.md`, a configuração `.cordel/project.json`, esta
skill e os comandos de validação são partes do harness de referência.

## Conceitos complementares necessários

### Engenharia de contexto

Seleção deliberada das instruções, fontes e evidências fornecidas ao agente em cada etapa.
Mais contexto não é necessariamente melhor: ele deve ser atual, pertinente, rastreável e
carregado sob demanda. Fontes canônicas prevalecem sobre conversas e resumos antigos.

### Ferramentas, permissões e guardrails

Ferramentas permitem ao agente observar ou alterar sistemas. Permissões definem o que ele
pode fazer; guardrails verificam ou bloqueiam entradas, chamadas e saídas. Operações de
leitura, escrita e publicação devem ser distinguidas, e autorização para analisar não
equivale a autorização para modificar.

### Avaliações (evals) e observabilidade

Testes verificam o produto; evals medem o comportamento do agente ou workflow em um
conjunto de tarefas e critérios. Traces e logs tornam decisões e chamadas inspecionáveis.
Esse nível complementa a evidência da entrega: é possível o código passar nos testes e o
agente ainda seguir um processo inseguro ou inconsistente.

## Relação com o método

| Elemento | Papel no Cordel | Não deve ser confundido com |
|---|---|---|
| Spec | contrato do TO-BE quando a complexidade exige | origem, autorização ou prova |
| Skill | procedimento reutilizável | agente ou ferramenta |
| MCP | protocolo de integração | servidor, ferramenta ou política de acesso |
| Agente | executor orientado a objetivos | modelo isolado ou decisor de negócio |
| Harness | ambiente de controle e execução | método de desenvolvimento |
| Evidência | sustentação confirmável de uma afirmação | relato, status ou artefato apenas citado |

## Referências externas

- [GitHub Spec Kit: Spec-Driven Development](https://github.github.com/spec-kit/)
- [Especificação do Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18/server/index)
- [OpenAI Agents SDK: ferramentas](https://openai.github.io/openai-agents-python/tools/)
- [OpenAI Agents SDK: guardrails](https://openai.github.io/openai-agents-python/guardrails/)
