# Catálogo de técnicas e padrões

## Técnicas

| Técnica | Problema tratado | Aplicação portátil |
|---|---|---|
| Investigação do AS-IS | solução desenhada sobre premissa falsa | ler fontes e código, registrar evidências antes do TO-BE |
| Triagem em filtros | defeito e escopo novo confundidos | testar defeito, lacuna documental, cobertura existente e só então escopo novo |
| Evidência endereçável | afirmações técnicas não auditáveis | citar endereço confirmável e pertinente à afirmação |
| Estratégia de prova por aceite | aceite subjetivo ou tardio | definir como cada resultado será observado antes de implementar |
| Reconciliação antes/depois | evidência colhida ou entrega feita em ambiente divergente | verificar dependências e projeções nas duas fronteiras do ciclo |
| Atualização do contexto canônico | conhecimento morre em chats e análises | promover descobertas duráveis à fonte AS-IS |
| Diff semântico de requisitos | mudança de redação passa despercebida | comparar identidade, significado e condições, não apenas arquivos |

## Padrões

### Fonte versus projeção

Mantenha fatos em artefatos canônicos e derive matrizes, índices e dashboards. Projeção
editada manualmente mascara erro e inevitavelmente diverge.

### Gate com três resultados

- `BLOQUEADO`: falta origem, evidência, autorização ou decisão.
- `PRONTO PARA ESPECIFICAR`: trabalho válido, desenho incompleto.
- `PRONTO PARA IMPLEMENTAR`: unidade verificável sem decisão bloqueante.

### Alegação não promove estado

Relato, menção ou story concluída pode orientar a busca, mas não promove comportamento a
`verificado`. A promoção depende de evidência confirmada.

### Decisão humana explícita

O agente ou automação coleta fatos, classifica e apresenta alternativas. O responsável
competente decide escopo, prioridade, ambiguidade de negócio e aceitação de risco.

### Documento histórico acumulativo

Análises, atas e decisões preservam o que se sabia no momento. Uma correção relevante é
registrada em nova seção datada ou em artefato sucessor; não se reescreve silenciosamente
o passado.

### Adaptador por projeto

O método define invariantes. O adaptador declara caminhos, prefixos, arquitetura, comandos,
fontes, políticas e dependências locais. Uma particularidade observada num projeto só entra
no núcleo quando resolve o mesmo problema em contextos diferentes.

## Antipadrões

- começar a implementação por busca de arquivo sem localizar a origem;
- inferir ausência de implementação pela ausência de story;
- criar identificador interno no namespace pertencente ao cliente;
- converter necessidade em story sem decisão;
- declarar prontidão sem critério observável e estratégia de prova;
- atualizar dashboard ou matriz no lugar da fonte;
- usar análise histórica como descrição atual do produto;
- fechar trabalho com testes executados, mas sem relacioná-los aos critérios de aceite.
