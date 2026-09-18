---
id: MOD-01
title: "Como um agente funciona e por que erra"
status: draft
duration: 3 horas
bloco: "I — Fundamentos"
ferramenta: "qualquer agente, sem método instalado"
related_objectives:
  - OA-01
  - OA-02
updated: 2026-08-31
---

# MOD-01 — Como um agente funciona e por que erra

## MOD-01-INT — Intenção do módulo

Abrir o curso com duas experiências concretas. A primeira: uma demanda curta produz
rapidamente plano, código e testes plausíveis, embora decisões importantes ainda não tenham
sido tomadas. A segunda: a mesma solicitação, executada três vezes, produz três respostas
diferentes.

A turma deve sair do encontro entendendo por que isso acontece — não como defeito de uma
ferramenta específica, mas como consequência de como um agente transforma uma solicitação
em ação. Velocidade de produção e confiança justificada são medidas diferentes.

Este módulo aplica o conteúdo de [`CURSO-03`](CURSO-03.md) e produz o diagnóstico que será
revisitado nos demais encontros. Nenhum método está instalado neste ponto do curso.

## MOD-01-TESE — Tese

> A IA encurta o caminho até uma alteração concreta. O trabalho de engenharia precisa
> garantir que esse caminho continue ligado à necessidade, à decisão e à prova.

## MOD-01-OBJ — Resultados de aprendizagem

Ao final, a pessoa participante deverá conseguir:

1. descrever o ciclo de observação e ação de um agente e o que ele enxerga do problema;
2. explicar o efeito prático da janela de contexto sobre trabalhos longos;
3. reconhecer que o resultado não é determinístico e medir essa variação;
4. identificar tarefas em que o agente reduz esforço ou tempo de forma real;
5. reconhecer premissas não confirmadas em uma resposta tecnicamente plausível;
6. explicar por que código e testes não provam, sozinhos, que o problema correto foi
   resolvido;
7. produzir um diagnóstico inicial sem transformar análise em autorização.

## MOD-01-CON — Conceitos

Cada conceito é apresentado em três níveis: o princípio, válido independentemente de
ferramenta; a prática, aplicável com qualquer agente; e, quando existir, a forma como o
Cordel o implementa. Neste módulo o terceiro nível aparece apenas como antecipação — a
ferramenta só entra no encontro 5.

### MOD-01-CON-01 — O que o modelo enxerga do seu problema

**Princípio.** O modelo não tem acesso ao seu projeto. Ele recebe um texto — a solicitação,
mais o que o ambiente decidiu incluir — e produz uma continuação provável desse texto. Tudo
o que não estiver nesse texto, ou não puder ser buscado por uma ferramenta, simplesmente não
existe para ele. Um comportamento óbvio para a equipe e não escrito em lugar nenhum é
invisível.

**Prática.** Antes de julgar uma resposta, pergunte o que o agente tinha em mãos quando a
produziu. Boa parte do que parece erro de raciocínio é ausência de informação. Verifique se
o que faltava estava disponível em algum lugar do repositório ou se ninguém nunca escreveu.

### MOD-01-CON-02 — Janela de contexto

**Princípio.** Existe um limite para quanto texto entra em uma única interação. Conversa,
arquivos lidos, saídas de comando e respostas anteriores competem pelo mesmo espaço. Quando
o limite se aproxima, informação antiga é resumida ou descartada — e o agente continua
respondendo com a mesma segurança, agora sobre uma versão comprimida do que foi combinado.

**Prática.** Trabalhos longos degradam de forma silenciosa. Sintomas típicos: uma restrição
combinada no início deixa de ser respeitada, um arquivo já corrigido volta ao estado
anterior, uma decisão é reaberta. O controle é manter o que importa em arquivo, não na
conversa, e recomeçar a sessão apontando para esse arquivo.

**No Cordel.** É a razão de existir um índice curto que aponta para fontes em vez de
duplicá-las, e de o contexto ser carregado sob demanda.

### MOD-01-CON-03 — Corte de conhecimento

**Princípio.** O modelo foi treinado até certa data. Bibliotecas, APIs, versões e práticas
posteriores a esse ponto são desconhecidas ou conhecidas de forma incompleta — e o modelo
não sinaliza a diferença. Ele responde sobre a versão que conhece com a mesma naturalidade
com que responderia sobre a versão atual.

**Prática.** Para qualquer afirmação sobre biblioteca, versão, sintaxe ou comportamento de
ferramenta, exija a fonte. O que o projeto usa está no arquivo de dependências, não na
memória do modelo.

### MOD-01-CON-04 — Não determinismo

**Princípio.** A mesma solicitação pode produzir resultados diferentes em execuções
diferentes. Não é falha: é como o modelo gera texto. Duas execuções podem escolher arquivos
distintos, estruturas distintas e até conclusões distintas sobre o mesmo código.

**Prática.** Um resultado que você não consegue reproduzir não pode ser a base de uma
decisão. O que precisa ser estável — a decisão, o critério, o comando — vai para um arquivo
versionado. O que pode variar — a redação, a ordem da explicação — não precisa de controle.

**No Cordel.** É por isso que o método registra a decisão e a evidência em artefatos, e não
trata a conversa com o agente como fonte.

### MOD-01-CON-05 — Custo e latência

**Princípio.** Cada execução consome tempo e dinheiro. Uma tarefa que exige três tentativas
e uma revisão longa pode custar mais — em relógio e em atenção humana — do que fazer à mão.

**Prática.** Estime antes de delegar: quanto tempo levaria fazer, quanto tempo levará
revisar. Quando a revisão for mais cara que a execução, a delegação não compensa. Esse
cálculo é retomado no encontro 2, quando a decisão de não usar IA vira critério explícito.

### MOD-01-CON-06 — Produtividade local e resultado do sistema

**Princípio.** Produtividade local mede quanto uma etapa ficou mais rápida: pesquisar um
arquivo, escrever uma função, gerar um teste. Resultado do sistema considera se a mudança
atende à necessidade, respeita decisões, não cria impacto indevido e pode ser provada. Uma
tarefa localmente eficiente pode aumentar retrabalho ou risco no fluxo completo.

**Prática.** Ao relatar ganho, informe a etapa medida. "Escrevi o teste em dois minutos" e
"a mudança está pronta" são afirmações de naturezas diferentes.

### MOD-01-CON-07 — Plausibilidade não é evidência

**Princípio.** Modelos produzem continuações coerentes a partir do contexto recebido. Uma
explicação pode parecer completa porque preenche lacunas de modo provável. Coerência interna
não é sinal de correção.

**Prática.** Toda afirmação técnica importante precisa ser ligada a uma fonte ou permanecer
marcada como inferência. As duas coisas são aceitáveis; o que não é aceitável é a mistura
silenciosa das duas.

**No Cordel.** Corresponde à separação entre alegação, inferência, evidência declarada e
evidência confirmada. Este é o tema central do encontro 3.

### MOD-01-CON-08 — O duplo efeito da aceleração

**Princípio.** Pesquisa, explicação, planejamento, código, testes e documentação ficam mais
rápidos. Os mecanismos de falha correspondentes também: escolher fonte errada, consolidar
suposição, implementar escopo indevido, testar a própria interpretação e propagar contexto
falso. O intervalo entre uma premissa errada e uma alteração concreta encurta na mesma
proporção.

**Prática.** Onde a aceleração é maior, o controle precisa ser mais próximo. Não é o
contrário.

### MOD-01-CON-09 — Necessidade, autorização e prova

**Princípio.** Uma necessidade justifica investigação. Uma decisão autoriza determinado
escopo. Uma implementação materializa uma solução. Uma evidência sustenta uma afirmação
sobre o resultado. Nenhum desses elementos substitui os outros.

**Prática.** A confusão mais comum e mais cara é tratar necessidade como autorização: alguém
pediu, logo está aprovado. O agente reproduz essa confusão porque não tem como perceber a
diferença.

**No Cordel.** É a cadeia mínima do método, estudada a partir do encontro 6.

### MOD-01-CON-10 — As sete perguntas

Formam o currículo real do curso e voltam em todos os encontros:

- qual necessidade deu origem à mudança?
- o que é fato, relato, inferência ou decisão?
- o que o sistema realmente faz hoje?
- quem autorizou a mudança de escopo?
- como o resultado será observado?
- qual prova sustentará a conclusão?
- como fontes, código e testes voltarão a concordar?

## MOD-01-DEMO — Demonstração do instrutor

Use a demanda: "o sistema deve avisar quando uma solicitação for aprovada".

### Primeira passagem, 8 minutos

Peça ao agente um plano de implementação. Não forneça requisito integral, canal,
destinatário, estado exato, código ou política de autorização. Preserve a resposta original.

### Três execuções, 7 minutos

Repita a mesma solicitação, do zero, mais duas vezes. Coloque as três respostas lado a lado
e destaque o que variou: arquivos escolhidos, canal presumido, estrutura proposta,
profundidade da análise. A turma costuma esperar variação de redação e encontrar variação de
conclusão.

### Leitura crítica, 15 minutos

Marque uma das respostas com quatro categorias:

| Marca | Significado | Exemplo possível |
|---|---|---|
| F | fato sustentado | arquivo efetivamente localizado |
| A | alegação recebida | "o sistema não avisa" |
| I | inferência | "o canal deve ser e-mail" |
| D | decisão necessária | destinatário e momento do envio |

### Fechamento, 5 minutos

Mostre que o plano pode ser tecnicamente razoável e ainda depender de várias decisões. Não
ridicularize a primeira resposta: seu valor é revelar como uma solicitação insuficiente
produz uma solução convincente.

## MOD-01-LAB — Laboratório: diagnóstico sem método

### Cenário

Cada grupo recebe uma demanda ambígua do projeto-laboratório e acesso parcial ao
repositório. O agente pode ler, pesquisar e propor; não deve alterar arquivos.

### Etapa 1 — Resposta imediata, 15 minutos

O grupo pede análise e plano como faria normalmente. Deve guardar solicitação, fontes usadas
e resposta, sem corrigi-los durante a primeira execução.

### Etapa 2 — Medição de divergência, 15 minutos

Executar a mesma solicitação mais duas vezes, em sessões novas. Preencher:

| Aspecto | Execução 1 | Execução 2 | Execução 3 | Divergiu? |
|---|---|---|---|---|
| arquivos consultados | | | | |
| causa apontada | | | | |
| solução proposta | | | | |
| decisões assumidas | | | | |

A pergunta de fechamento: qual dessas três respostas você teria implementado se tivesse
executado apenas uma vez?

### Etapa 3 — Auditoria de premissas, 25 minutos

Para cada afirmação relevante de uma das respostas, registrar:

| Afirmação | Tipo | Fonte disponível | O que falta |
|---|---|---|---|
| | fato / relato / inferência / decisão | | |

### Etapa 4 — Aplicação das sete perguntas, 20 minutos

O grupo responde apenas com o que consegue confirmar. Respostas desconhecidas viram busca ou
decisão pendente, não suposição.

### Etapa 5 — Comparação e preparação da entrega, 15 minutos

Identificar:

- ganho real oferecido pelo agente;
- primeira ação que teria sido executada cedo demais;
- fonte que deveria ter sido consultada;
- decisão que pertence a uma pessoa;
- prova que ainda não poderia ser definida.

Escolher um exemplo claro para apresentar à turma, preservando as respostas originais como
evidência do diagnóstico.

## MOD-01-ENT — Entrega

Diagnóstico inicial contendo:

1. demanda recebida e contexto disponível;
2. as três respostas originais do agente;
3. tabela de divergência entre execuções;
4. mapa de fatos, relatos, inferências e decisões;
5. benefícios observados, ligados a tarefas concretas;
6. riscos e perguntas ausentes;
7. ação que o grupo considera autorizada neste momento;
8. justificativa, sem antecipar conteúdos ainda não ensinados.

O diagnóstico será revisitado em `MOD-03`, `MOD-06` e `MOD-08`.

## MOD-01-ROTEIRO — Cronograma de 3 horas

| Tempo | Atividade |
|---:|---|
| 0–15 min | apresentação do curso, dos três blocos e da demanda condutora |
| 15–30 min | respostas espontâneas e discussão inicial |
| 30–55 min | como o modelo enxerga o problema: contexto, janela, corte de conhecimento |
| 55–70 min | não determinismo, custo e latência |
| 70–85 min | produtividade local, plausibilidade e duplo efeito |
| 85–100 min | demonstração: primeira passagem e três execuções |
| 100–110 min | intervalo |
| 110–125 min | laboratório: resposta imediata |
| 125–140 min | medição de divergência |
| 140–165 min | auditoria de premissas e sete perguntas |
| 165–180 min | comparação, entrega e retrospectiva |

## MOD-01-AVAL — Critérios de avaliação

| Critério | Evidência esperada |
|---|---|
| explica o mecanismo | falha atribuída a contexto ausente ou geração provável, não a "burrice do modelo" |
| mede a variação | tabela de divergência preenchida com aspectos concretos |
| reconhece benefício sem promessa absoluta | benefício ligado a tarefa concreta |
| separa natureza das afirmações | quadro sem promover inferência a fato |
| identifica autoridade | decisão não atribuída automaticamente ao agente |
| evita implementação prematura | próxima ação limitada a análise autorizada |

Relaciona-se a `OA-01` e `OA-02`.

## MOD-01-EQUIVOCOS — Equívocos a observar

- "O objetivo é provar que o agente é ruim." O objetivo é calibrar confiança e controle.
- "Toda inferência é proibida." Inferências são úteis quando permanecem identificadas e
  podem ser verificadas.
- "Mais prompt resolveria tudo." Parte das lacunas depende de fonte, acesso ou decisão. O
  encontro 2 mostra até onde a condução resolve — e onde ela para.
- "Se compila, está correto." Compilação não prova necessidade, autorização ou aceite.
- "A variação some com temperatura zero." Reduz, não elimina; e o problema de fundo é
  decidir com base em um resultado não reproduzido.
- "O modelo sabe qual versão da biblioteca usamos." Ele sabe o que estava no treino, ou o
  que uma ferramenta buscou agora.

## MOD-01-MAT — Materiais e preparação

- demanda ambígua por grupo;
- projeto-laboratório em estado inicial reproduzível;
- acesso de leitura ao agente, com possibilidade de abrir sessões novas;
- modelo da tabela de divergência;
- quadro de classificação das afirmações;
- gabarito das decisões ainda ausentes;
- exemplo preparado de afirmação desatualizada sobre biblioteca, para o corte de
  conhecimento;
- mecanismo para preservar solicitações e respostas.

## MOD-01-FONTES — Fontes no método

- [`../../method/manifesto.md`](../../method/manifesto.md)
- [`../../method/concepts.md`](../../method/concepts.md)
- [`../../method/ai-driven-development.md`](../../method/ai-driven-development.md)
- [`../../method/catalog.md`](../../method/catalog.md)
- [`CURSO-03.md`](CURSO-03.md)
- [`CURSO-06.md`](CURSO-06.md)

## MOD-01-PEND — Pendências

- escolher as demandas ambíguas do laboratório;
- produzir as três respostas-modelo para a demonstração, já capturadas, como plano B;
- verificar se o agente escolhido permite abrir sessões limpas com rapidez suficiente;
- preparar o exemplo de afirmação desatualizada sobre dependência;
- criar o quadro visual das sete perguntas;
- definir como solicitações e respostas serão preservadas;
- testar se o laboratório cabe em 70 minutos;
- preparar alternativa para indisponibilidade do agente.
