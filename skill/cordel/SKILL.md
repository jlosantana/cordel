---
name: cordel
description: Aplica engenharia de software orientada por contexto, especificações e evidências. Use ao classificar demandas, confirmar o comportamento atual, preparar mudanças rastreáveis, avaliar prontidão para implementar ou reconciliar documentação, código e provas.
---

# Cordel

Conduza engenharia de software orientada por contexto, especificações e evidências.

Conduza mudanças pela cadeia **origem -> classificação -> AS-IS -> decisão -> unidade de
trabalho -> implementação -> prova -> reconciliação**. Preserve as escolhas do usuário e
as fronteiras de autorização; uma análise não autoriza publicação ou alteração externa.

## Descobrir o projeto

Localize `.cordel/project.json` a partir da raiz do workspace. Leia a configuração
antes de assumir caminhos, prefixos, comandos, arquitetura ou fontes da verdade. Se ela
não existir e o usuário pediu adoção do Cordel, use `scripts/cordel.py init <projeto>`.

Se a configuração não existir numa análise comum, use as convenções documentadas pelo
próprio projeto e informe quais partes não puderam ser verificadas pelo método.

Comece por `.cordel/index.md` e carregue somente as fontes pertinentes à demanda. Não use
conteúdo de `.cordel/local/` como conhecimento compartilhado ou fonte canônica.

## Selecionar o workflow

- Pedido novo, dúvida de cobertura ou possível escopo novo: leia
  [references/triagem.md](references/triagem.md).
- Incidente, reclamação ou comportamento inesperado: leia
  [references/investigacao.md](references/investigacao.md).
- Pedido para planejar, começar ou implementar uma mudança: leia
  [references/preparacao.md](references/preparacao.md).
- Pergunta sobre implementação ou rastreabilidade: leia
  [references/rastreabilidade.md](references/rastreabilidade.md).
- Mudança concluída ou pedido de fechamento: leia
  [references/fechamento.md](references/fechamento.md).

Leia apenas os workflows necessários à tarefa atual.

## Invariantes

- Não invente identificadores que pertencem a uma fonte externa ou ao cliente.
- Não trate alegação, matriz, issue ou story concluída como prova de implementação.
- Confirme afirmações técnicas com evidência localizável e semanticamente pertinente.
- Não transforme necessidade, incidente ou reunião em autorização automática.
- Marque inferências, incertezas e decisões humanas pendentes.
- Não altere código funcional antes do gate quando o projeto exige esse gate.
- Não edite projeções geradas; corrija a fonte ou o gerador.
- Se surgir escopo novo durante a implementação, interrompa essa parte e volte à triagem.

## Saída de prontidão

Antes de codificar, apresente:

```text
Situação: BLOQUEADO | PRONTO PARA ESPECIFICAR | PRONTO PARA IMPLEMENTAR
Origem:
Classificação:
AS-IS e evidências:
Unidade de trabalho e spec:
Critérios de aceite e estratégia de prova:
Impactos e dependências:
Decisões humanas pendentes:
Próxima ação autorizada:
```

Use `PRONTO PARA IMPLEMENTAR` somente quando não houver decisão bloqueante e os critérios
do workflow de preparação estiverem satisfeitos.
