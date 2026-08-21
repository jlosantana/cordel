# Conceitos portáteis

Este documento define os artefatos e estados do método. Para os componentes específicos
do trabalho com IA — spec-driven development, agentes, skills, MCPs e harness — consulte
[`ai-driven-development.md`](ai-driven-development.md).

## Fonte da verdade

Local autorizado para manter um fato. Um projeto deve declarar onde vivem contrato,
contexto AS-IS, decisões, unidades de trabalho e evidências. Visões geradas não substituem
essas fontes.

## Artefato e projeção

- **Artefato:** preserva conteúdo, contexto ou decisão e requer revisão proporcional ao
  impacto, como requisito, necessidade, story, análise ou ADR.
- **Projeção:** visão recalculável das fontes, como matriz, índice ou dashboard. Corrige-se
  a fonte ou o gerador, não a projeção manualmente.

## Skill, script e modelo

- **Skill:** orienta trabalho que exige julgamento.
- **Script:** executa transformação ou validação determinística.
- **Modelo:** dá estrutura inicial a um artefato preenchido com julgamento.

## Requisito, contexto AS-IS, necessidade e story

- **Requisito:** comportamento ou restrição assumida como compromisso externo.
- **Contexto AS-IS:** comportamento atual confirmado por evidência.
- **Necessidade:** pedido ou descoberta ainda sem destino ou autorização definidos.
- **Story:** unidade de trabalho explicitamente autorizada.

Nenhum desses artefatos substitui os demais. Story concluída não prova comportamento;
necessidade registrada não autoriza implementação.

## Alegação, inferência e evidência

- **Alegação:** afirmação ainda não verificada.
- **Inferência:** conclusão derivada de fontes, identificada como tal.
- **Evidência declarada:** endereço ou artefato citado como prova.
- **Evidência confirmada:** endereço acessível e semanticamente pertinente à afirmação.

## Produto e projeto

- Conhecimento durável sobre o sistema pertence ao acervo de produto.
- Investigações, stories, atas, gates e releases pertencem ao rastro do projeto.

Uma descoberta feita numa análise histórica deve ser promovida ao contexto canônico se
ela passar a descrever o sistema atual.
