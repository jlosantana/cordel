# Fechamento e reconciliação

## Fechar o ciclo

1. Execute testes, builds e verificações proporcionais ao risco.
2. Relacione evidências finais a cada critério de aceite.
3. Atualize o contexto AS-IS para refletir o comportamento entregue.
4. Atualize story, spec, decisões e registros de QA aplicáveis.
5. Atualize o grafo/configuração quando dependências declaradas mudarem.
6. Regenere projeções e valide links e identificadores.
7. Execute o comando de reconciliação configurado.
8. Separe entrega atual, dívida preexistente e decisão ainda pendente.

O trabalho pode estar implementado sem estar verificado. Não feche como verificado se a
prova estiver ausente, quebrada, desatualizada ou não demonstrar semanticamente o critério.

Decisão aceita não deve ser silenciosamente reescrita: registre uma nova decisão que
supersede a anterior quando o projeto adotar ADRs imutáveis.
