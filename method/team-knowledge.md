# Conhecimento crescente e colaboração em equipe

## Cordel, adaptador e conhecimento

O Cordel é instalado como skill ou pacote. Cada repositório mantém apenas o
adaptador e o conhecimento que acompanha seu código em `.cordel/`:

```text
.cordel/
├── project.json
├── index.md
├── product/       # contexto e decisões canônicas
├── work/          # necessidades, stories, specs e análises ativas
├── evidence/      # provas endereçáveis
├── archive/       # artefatos encerrados ou substituídos
├── generated/     # projeções regeneráveis; ignoradas pelo Git
└── local/         # contexto pessoal; ignorado pelo Git
```

Não copie a implementação completa do Cordel para cada serviço. `cordel_version` registra
a versão esperada e permite evoluir o pacote separadamente dos projetos consumidores.

## Ciclo de vida documental

- **Ativo:** unidade de trabalho em andamento, mantida em `work/`.
- **Canônico:** conhecimento atual e durável sobre o produto, mantido em `product/`.
- **Histórico:** registro encerrado ou substituído, movido para `archive/` sem reescrever o passado.
- **Gerado:** índice, matriz ou dashboard recalculável, mantido em `generated/`.
- **Local:** notas pessoais e contexto temporário que não podem sustentar decisões do time.

Prefira um arquivo pequeno por identificador, como `SPEC-042.md` ou `ADR-008.md`. Use
frontmatter com `id`, `status`, `owners`, `scope`, `updated` e `supersedes` quando
aplicável. `.cordel/index.md` deve apontar para as fontes relevantes, não duplicá-las.
O agente lê primeiro o índice e carrega documentos sob demanda.

## Modelo federado de fontes

Mantenha perto do código o contexto AS-IS, decisões locais, contratos, specs e evidências
do serviço. Requisitos de negócio, decisões entre serviços e andamento podem continuar em
sistemas especializados. Registre cada fonte em `project.json` com:

```json
{
  "kind": "url",
  "location": "https://tracker.example.com/project",
  "owner": "product-team",
  "scope": "pedidos"
}
```

Uma fonte `path` é validada dentro do workspace; uma fonte `url` permanece sob autoridade
do sistema e responsável declarados. MCP pode oferecer acesso à fonte externa, mas é um
mecanismo de integração, não uma nova fonte da verdade.

## Política para times

- Revise por pull request todo conhecimento que precisa evoluir com o código.
- Não promova conversa, resumo de agente ou nota em `local/` diretamente a fato canônico.
- Registre responsável e escopo para evitar documentos sem manutenção.
- Substitua decisões com novo artefato e vínculo `supersedes`; não apague o histórico.
- Não carregue todo o acervo no contexto do agente: selecione por demanda e escopo.
- Nunca registre segredos, tokens ou dados pessoais no adaptador versionado.
