# Inventário das experiências de origem

Este arquivo registra de onde vieram as ideias do Cordel. Elas foram extraídas de experiências
do autor no desenvolvimento e na manutenção de projetos de software com agentes de IA. O
inventário não define as regras portáteis do método.

## Práticas generalizadas

| Prática observada nos projetos | Conceito extraído |
|---|---|
| Desenvolvimento guiado por requisitos | origem -> AS-IS -> autorização -> unidade verificável |
| Separação entre produto e execução | conhecimento durável versus rastro do trabalho |
| Triagem de necessidades | separar defeito, lacuna documental, escopo existente e escopo novo |
| Matrizes e dossiês | projeções derivadas de fontes canônicas |
| Evidência `caminho:linha` | afirmação técnica deve ser confirmável |
| Gate de prontidão | distinguir bloqueio, especificação e implementação |
| Verificação do ambiente | reconciliar dependências antes e depois da mudança |
| ADRs imutáveis | decisão aceita é substituída por outra, não reescrita |

## Particularidades deixadas fora do núcleo

- nomes de organizações, produtos, sistemas e módulos;
- linguagens, frameworks, servidores e bancos de dados de cada projeto;
- prefixos internos de requisitos e unidades de trabalho;
- caminhos, formatos de frontmatter e comandos existentes;
- regras contratuais e vocabulário de cada domínio;
- topologias específicas de módulos, artefatos, migrations e schemas.

Esses itens pertencem ao adaptador do projeto quando forem necessários.

## Tipos de fonte consultados

- documentação do fluxo de desenvolvimento;
- padrões de documentação e rastreabilidade;
- modelos de necessidade, story, spec e ADR;
- skills usadas para triagem, investigação e preparação;
- scripts de validação e reconciliação;
- código, testes e registros produzidos durante mudanças reais.

O núcleo preserva os padrões que se mostraram úteis em mais de um contexto. Detalhes que
só fazem sentido em um projeto permanecem fora do Cordel.
