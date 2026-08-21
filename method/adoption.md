# Roteiro de adoção em um projeto-piloto

## 1. Configurar sem mudar o processo ainda

Execute o inicializador, preencha nome, repositórios, fontes e comandos. Rode `check` até
obter `GO`. Nesta fase, apenas torne o projeto legível pelo método.

O inicializador cria `.cordel/`, mas não copia o núcleo do Cordel para o projeto. Versione
o adaptador, o índice e o conhecimento compartilhado; mantenha `local/` e `generated/`
fora do Git.

## 2. Escolher uma demanda real e pequena

Prefira uma mudança com origem conhecida, comportamento atual observável e baixo risco.
Evite usar uma grande iniciativa como primeiro teste, pois problemas de adoção ficam
misturados aos problemas do produto.

## 3. Produzir a cadeia mínima

Registre origem, classificação, evidência AS-IS, story, critério de aceite, estratégia de
prova e evidência final. Crie spec somente se a complexidade justificar.

## 4. Avaliar o método

Ao fechar, registre:

- decisões erradas evitadas;
- informações que ainda precisaram ser redescobertas;
- campos ou gates que não mudaram nenhuma decisão;
- regras locais que pertencem ao adaptador;
- lacunas que apareceram também em outro contexto e podem entrar no núcleo.

## 5. Evoluir com evidência de uso

Não generalize cada exceção do piloto. Ajuste o núcleo somente quando o problema for
recorrente ou representar risco relevante; particularidades permanecem na configuração ou
nas instruções do projeto.

Arquive unidades encerradas, promova descobertas duráveis ao contexto canônico e mantenha
o índice curto. Em equipes ou sistemas distribuídos, siga
[`team-knowledge.md`](team-knowledge.md) para definir a autoridade de cada fonte.
