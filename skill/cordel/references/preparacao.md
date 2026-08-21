# Preparação e gate de entrada

## Preparar a unidade de trabalho

Depois de localizar a origem e obter as decisões necessárias, registre:

- objetivo observável;
- escopo e fora do escopo;
- critérios de aceite testáveis;
- AS-IS com evidências;
- impactos em componentes, dados, estados, permissões e integrações;
- estratégia de prova por critério;
- dependências, riscos e decisões abertas.

Crie spec quando a solução alterar contratos, dados existentes, estados, integrações,
segurança, concorrência, vários componentes ou uma decisão técnica relevante.

## Gate

- [ ] origem identificada e acessível;
- [ ] classificação e cobertura sustentadas por fonte válida;
- [ ] escopo novo autorizado pelo responsável competente;
- [ ] AS-IS confirmado no código/dados com evidência;
- [ ] ambiente reconciliado ou ressalva de drift explicitada;
- [ ] story completa, com escopo e fora do escopo;
- [ ] critérios de aceite observáveis e estratégia de prova;
- [ ] impactos e dependências avaliados;
- [ ] decisões bloqueantes resolvidas;
- [ ] spec revisada quando necessária;
- [ ] relações formais não apontam para identificadores órfãos.

Classifique como `BLOQUEADO`, `PRONTO PARA ESPECIFICAR` ou `PRONTO PARA IMPLEMENTAR`.
Não altere código funcional se o pedido autoriza somente planejamento ou se o gate exige
uma decisão ainda ausente.
