---
id: SOCIAL-05
series: serie-01-problema-solucao
status: draft
title: "Implementado não é verificado"
image: ../../images/serie-01/social-05.png
sources:
  - ../../../method/traceability.md
  - ../../../course/topics/MOD-07.md
published_at:
published_url:
---

# Implementado não é verificado

O código foi alterado. O build passou. A story foi fechada.

Ainda falta uma pergunta: qual evidência demonstra que cada critério de aceite foi atendido?

Durante o desenvolvimento do Cordel, percebi como é fácil usar sinais de atividade como
prova de resultado. Um teste pode passar e demonstrar apenas que um método foi chamado,
enquanto o aceite exige que a pessoa correta receba um aviso uma única vez.

Por isso o método separa dois estados. Implementado significa que o trabalho técnico foi
concluído. Verificado exige uma evidência atual, acessível e pertinente à afirmação.

Essa diferença incomoda no começo, porque impede o fechamento automático. Depois ela ajuda
a equipe a discutir exatamente o que ainda não foi provado.

No seu projeto, o que precisa acontecer para uma entrega sair de “feito” e chegar a
“verificado”?

#QualidadeDeSoftware #Testes #EngenhariaDeSoftware #Cordel
