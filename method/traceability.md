# Modelo portátil de rastreabilidade

## Relações

```text
origem -> necessidade/requisito -> story -> spec -> código/teste -> evidência
```

Cada relação deve indicar se é declarada ou inferida. Citação em texto não equivale a um
vínculo formal, e vínculo formal com uma story não equivale a prova técnica.

## Estados sugeridos

| Estado | Significado |
|---|---|
| `nao-analisado` | Nenhuma verificação técnica suficiente foi registrada |
| `asis-confirmado` | O comportamento atual foi descrito com evidência |
| `lacuna-confirmada` | A ausência foi investigada e revisada |
| `planejado` | Existe unidade de trabalho autorizada ainda não iniciada |
| `em-implementacao` | Existe trabalho ativo |
| `implementado` | Trabalho foi concluído, mas a prova final é insuficiente |
| `verificado` | Evidência atual e confirmável sustenta o comportamento |
| `nao-aplicavel` | Decisão humana registrou que verificação técnica não se aplica |
| `substituido` | Outro artefato ou decisão tomou seu lugar |

Os projetos podem mapear nomes diferentes, mas devem preservar a distinção entre
planejamento, implementação declarada e comportamento verificado.

## Evidência suficiente

Uma evidência é adequada quando:

1. pode ser localizada no estado atual do projeto;
2. está no lugar canônico da afirmação;
3. demonstra especificamente o fato alegado;
4. registra data ou revisão quando puder envelhecer;
5. distingue ausência comprovada de busca incompleta.

O formato padrão para código é `caminho/arquivo.ext:linha`. Projetos podem declarar outro
formato desde que continue sendo confirmável.
