# Triagem de demanda

Use este workflow quando não estiver claro se o pedido é trabalho devido, descoberta do
AS-IS, detalhamento de algo já assumido ou escopo novo.

## Classificar nesta ordem

1. **Defeito:** existe comportamento esperado documentado ou demonstrável e o sistema
   diverge dele. Encaminhe para investigação/correção, preservando o relato e a reprodução.
2. **Lacuna de documentação:** o comportamento já existe, mas a fonte AS-IS não o registra.
   Atualize o contexto canônico; não crie trabalho funcional fictício.
3. **Detalhamento de compromisso existente:** a demanda cabe num requisito ou decisão já
   assumida, ainda que a redação seja mais ampla. Registre o vínculo e leve ambiguidades
   ao responsável pelo produto.
4. **Escopo novo:** não há cobertura demonstrável. Registre uma necessidade com origem e
   aguarde decisão explícita antes de criar trabalho pronto para implementação.

Pesquise o texto integral das fontes, não apenas identificadores ou títulos. Procure no
código antes de afirmar ausência. Uma busca negativa é evidência da busca executada, não
prova absoluta sem revisão do alcance.

## Produto da triagem

Registre origem, evidências, resultado de cada filtro, conclusão e decisão necessária. A
conclusão é um destino documental; não é autorização automática para desenvolver.
