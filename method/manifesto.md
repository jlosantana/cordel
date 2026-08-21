# Manifesto do Cordel

Cordel é uma abordagem de engenharia de software orientada por contexto, especificações e
evidências. O método procura manter intenção, decisão, implementação e prova em
concordância.

## Princípios

1. **Começar pela origem, não pelo código.** Toda mudança tem uma razão rastreável.
2. **Separar fatos de alegações.** Documento, código, relato e decisão têm pesos distintos.
3. **Confirmar o AS-IS antes de desenhar o TO-BE.** Código e dados provam o comportamento
   atual; documentos de requisito dizem o comportamento esperado.
4. **Não transformar necessidade em autorização.** Escopo novo depende de decisão humana.
5. **Planejar uma unidade verificável.** Critérios de aceite descrevem resultados
   observáveis e indicam como serão provados.
6. **Usar gates com significado operacional.** Um item pronto pode ser implementado sem
   decisão bloqueante; não significa apenas intenção de começar.
7. **Tratar documentação e código como um sistema reconciliável.** O ciclo termina quando
   fontes, implementação, testes e projeções voltam a concordar.
8. **Automatizar mecânica, preservar julgamento.** Scripts geram e validam; pessoas decidem
   escopo, prioridade, risco e ambiguidades de negócio.

## Cadeia mínima

```text
demanda
  -> origem documental
  -> classificação
  -> AS-IS confirmado
  -> decisão humana, quando necessária
  -> story e spec
  -> gate de entrada
  -> implementação e testes
  -> evidência final
  -> reconciliação
```

O método pode ser adotado parcialmente, mas não se deve usar o rótulo “verificado” quando
a evidência correspondente não existe ou não pôde ser confirmada.
