---
id: MOD-03
title: "Verificação: o que a IA produziu merece crédito?"
status: draft
duration: 3 horas
bloco: "I — Fundamentos"
ferramenta: "qualquer agente, sem método instalado"
related_objectives:
  - OA-05
  - OA-06
  - OA-07
updated: 2026-08-31
---

# MOD-03 — Verificação: o que a IA produziu merece crédito?

## MOD-03-INT — Intenção do módulo

O encontro 1 mostrou que uma resposta plausível pode estar errada. O encontro 2 mostrou até
onde a condução reduz o problema — e onde ela para. Este encontro trata do que sobra: como
decidir, diante de um resultado pronto, o que merece crédito.

É a competência que mais escala com o uso de IA. Quanto mais código um time gera, mais a
capacidade de revisão vira o gargalo real, e menos ela pode depender de leitura distraída.

O encontro fecha o Bloco I com a entrega mais importante do curso: cada grupo escreve seu
próprio protocolo mínimo de trabalho com IA. Esse documento será confrontado com o Cordel no
encontro 5.

## MOD-03-TESE — Tese

> Não existe resultado confiável, existe resultado verificado. A pergunta não é se o agente
> acertou, é como você sabe.

## MOD-03-OBJ — Resultados de aprendizagem

Ao final, a pessoa participante deverá conseguir:

1. classificar afirmações em fato, relato, inferência, decisão e evidência;
2. confirmar o comportamento atual do sistema em fonte inspecionável antes de propor
   mudança;
3. avaliar se uma evidência é localizável, autorizada e pertinente à afirmação;
4. delimitar o alcance de uma busca negativa;
5. revisar uma diferença contra o escopo declarado, identificando o que não foi pedido;
6. reconhecer padrões típicos de erro do agente;
7. projetar um teste capaz de falhar e distinguir cobertura de prova;
8. redigir um protocolo mínimo de trabalho com IA, justificando cada controle.

## MOD-03-CON — Conceitos

### MOD-03-CON-01 — Cinco naturezas de afirmação

**Princípio.** Uma afirmação técnica pode ser:

- **fato** — sustentado por fonte que qualquer pessoa consegue abrir;
- **relato** — alguém disse; verdadeiro ou não, é testemunho, não observação;
- **inferência** — conclusão provável a partir do que se sabe;
- **decisão** — escolha que alguém com autoridade fez, ou precisa fazer;
- **evidência** — o material concreto que sustenta um fato.

Nenhuma se transforma na outra por repetição. Um relato repetido três vezes continua relato.

**Prática.** O agente produz as cinco misturadas, no mesmo tom, sem sinalizar a transição.
Ao revisar, marque cada afirmação relevante. As inferências não são o problema — são úteis e
inevitáveis. O problema é a inferência que atravessa o texto vestida de fato e chega ao
código como premissa.

**No Cordel.** Corresponde à separação entre alegação, inferência, evidência declarada e
evidência confirmada, e ao princípio de que alegação não promove estado.

### MOD-03-CON-02 — Confirmar o comportamento atual

**Princípio.** Antes de decidir o que o sistema deve passar a fazer, é preciso saber o que
ele faz hoje — em fonte inspecionável, não em memória de equipe nem em documentação
desatualizada. É a pergunta mais barata de fazer e a mais cara de pular.

**Prática.** O agente é bom nisso e é exatamente aqui que ele mais engana: pedido a
descrever um comportamento, ele produz uma descrição coerente misturando o que leu com o que
é plausível. Exija o endereço. "O envio acontece em `notificador.py:88`" é verificável;
"o sistema já envia notificações" não é.

**No Cordel.** É o AS-IS confirmado, e a razão de a cadeia exigi-lo antes da decisão. Volta
como prática documentada no encontro 6.

### MOD-03-CON-03 — Evidência localizável e pertinente

**Princípio.** Uma evidência serve quando pode ser localizada por outra pessoa, está no lugar
que tem autoridade sobre aquele fato, e demonstra especificamente a afirmação que sustenta.
As três condições são independentes, e a terceira é a que mais falha.

**Prática.** `caminho:linha` é endereço, não garantia. Um teste que chama um método prova que
o método é chamado — não que o usuário recebe o aviso. Ao aceitar uma evidência, faça a
pergunta inversa: se a afirmação fosse falsa, esta evidência seria diferente?

### MOD-03-CON-04 — Busca negativa

**Princípio.** Não encontrar não é o mesmo que não existir. Uma busca só sustenta uma
conclusão quando seu alcance está declarado.

**Prática.** Registre termos, caminhos e revisão consultados. "Não encontrei
`notific|aviso|alerta` em `src/` na revisão atual" é uma afirmação verificável e refutável.
"O sistema não notifica" não é. O agente enuncia a segunda com frequência, a partir de uma
busca cujo alcance ele não relatou.

### MOD-03-CON-05 — Leitura da diferença contra o escopo

**Princípio.** Revisar código gerado não é ler linha a linha procurando erro de lógica. É
responder duas perguntas: todo arquivo alterado tinha motivo no que foi pedido? Tudo que
foi pedido aparece em algum arquivo alterado?

**Prática.** Comece pela lista de arquivos, antes do conteúdo. Um arquivo que você não
esperava é o sinal mais barato e mais confiável de escopo excedido. Só depois leia as
alterações, na ordem em que o comportamento acontece, não na ordem em que a ferramenta
apresenta. Lotes grandes derrotam qualquer revisor: quando a diferença não cabe em uma
leitura atenta, o problema é o tamanho do passo, não a disciplina de quem revisa.

**No Cordel.** Escopo e fora do escopo declarados na story tornam essa revisão objetiva —
existe uma lista contra a qual comparar.

### MOD-03-CON-06 — Padrões típicos de erro do agente

**Princípio.** Erros de agente não são aleatórios. Concentram-se em um conjunto pequeno e
reconhecível, e conhecê-lo transforma revisão em busca dirigida.

**Prática.** Os mais frequentes:

| Padrão | Como se manifesta | Onde procurar |
|---|---|---|
| teste que confirma a interpretação | o teste passa porque foi escrito a partir do código, não do critério | teste que espelha a implementação linha a linha |
| tratamento de erro decorativo | captura a exceção, registra e segue como se nada tivesse acontecido | blocos de exceção que não alteram o fluxo |
| abstração prematura | cria camada, interface ou utilitário para um caso único | arquivos novos não previstos |
| alteração fora do pedido | renomeia, reformata, "melhora" código vizinho | arquivos alterados sem relação com o objetivo |
| confiança em API inexistente | usa método plausível de biblioteca que não o tem | chamadas não cobertas por teste executado |
| caso limite silencioso | lista vazia, nulo, concorrência e repetição não tratados | ausência de teste, não presença de erro |
| corrigir o sintoma | ajusta o ponto onde o erro aparece, não onde nasce | correção distante da causa apontada |

### MOD-03-CON-07 — Teste adversarial

**Princípio.** Um teste que não pode falhar não é prova de nada. A pergunta a fazer sobre
qualquer teste é: o que precisaria estar errado no código para este teste ficar vermelho?
Se a resposta for "nada relevante", o teste mede apenas a própria existência.

**Prática.** Quebre o código de propósito e confirme que o teste acusa. É a verificação mais
rápida disponível e quase nunca é feita em código gerado. Cobertura mede linhas executadas,
não comportamento demonstrado: uma suíte com cobertura alta e nenhum teste capaz de falhar
é comum quando os testes foram gerados depois da implementação.

**No Cordel.** É a razão de a estratégia de prova ser definida antes da implementação, no
gate — para que o teste não se ajuste ao que o código produziu.

## MOD-03-DEMO — Demonstração: teste verde, evidência parcial

Apresente um teste que confirma a chamada ao serviço de notificação, enquanto o critério
exige que o solicitante correto veja um aviso único após a aprovação concluída.

Analise em voz alta:

- o que o teste demonstra;
- o que não demonstra — destinatário correto, unicidade, momento;
- qual evidência adicional seria necessária;
- se o veredito honesto é "parcial" ou "verificado".

Em seguida, quebre o código de propósito em dois pontos: um que o teste acusa e outro que ele
não acusa. A demonstração do segundo ponto costuma ser o momento em que a turma entende a
diferença entre cobertura e prova.

Feche mostrando uma matriz de rastreabilidade marcada como "coberto" e peça que alguém
localize a prova. Se não houver caminho confirmável, a matriz é alegação, não sustentação.

## MOD-03-LAB — Laboratório: auditoria cruzada e protocolo mínimo

### Cenário

Cada grupo audita o resultado produzido por outro grupo no encontro 2 — código, testes e a
especificação da tarefa. Auditar o trabalho alheio é deliberado: remove o viés de defender a
própria condução.

### Etapa 1 — Classificar afirmações, 15 minutos

Percorrer a análise produzida pelo agente e marcar cada afirmação relevante:

| Afirmação | Natureza | Endereço da evidência | Sustenta o que alega? |
|---|---|---|---|
| | fato / relato / inferência / decisão | | sim / parcial / não |

### Etapa 2 — Confirmar o AS-IS, 15 minutos

Escolher as duas afirmações mais decisivas sobre o comportamento atual e tentar confirmá-las
no código. Registrar o resultado, inclusive quando a confirmação falhar. Buscas sem resultado
são registradas com alcance explícito.

### Etapa 3 — Revisar a diferença, 20 minutos

Sem ler o conteúdo ainda, listar os arquivos alterados e marcar os que não têm motivo no
objetivo declarado. Depois ler as alterações e preencher:

| Arquivo | Motivo no escopo? | Padrão de erro identificado | Gravidade |
|---|---|---|---|

### Etapa 4 — Quebrar os testes, 20 minutos

Para cada teste gerado, introduzir um defeito real no código que ele deveria acusar.
Registrar:

| Teste | Defeito introduzido | Acusou? | Conclusão |
|---|---|---|---|

Testes que não acusam nenhum defeito relevante são reportados como cobertura sem prova.

### Etapa 5 — Devolver e discutir, 10 minutos

Cada grupo apresenta ao grupo auditado o achado mais relevante. O grupo auditado responde se
concorda — divergência é registrada, não resolvida à força.

### Etapa 6 — Protocolo mínimo, 20 minutos

Com base nos três encontros, cada grupo escreve uma página: os controles que considera
indispensáveis para trabalhar com IA. Regras de formato:

- no máximo doze controles;
- cada controle enunciado como ação verificável, não como intenção — "confirmar o
  comportamento atual no código antes de propor mudança", não "ter cuidado com o AS-IS";
- cada controle acompanhado do problema concreto, observado nos encontros 1 a 3, que
  justifica sua existência;
- controles sem problema observado são cortados.

O documento é entregue ao instrutor e devolvido no encontro 5.

## MOD-03-ENT — Entrega

1. tabela de classificação das afirmações;
2. resultado da confirmação do AS-IS, incluindo tentativas frustradas;
3. revisão da diferença com arquivos fora do escopo identificados;
4. tabela de testes quebrados, com veredito de cobertura ou prova;
5. parecer devolvido ao grupo auditado e registro das divergências;
6. **protocolo mínimo do grupo**, com problema observado por controle.

## MOD-03-ROTEIRO — Cronograma de 3 horas

| Tempo | Atividade |
|---:|---|
| 0–10 min | retomada: o que a condução não resolveu |
| 10–30 min | cinco naturezas de afirmação; confirmar o comportamento atual |
| 30–45 min | evidência pertinente e busca negativa |
| 45–60 min | leitura da diferença e padrões típicos de erro |
| 60–75 min | teste adversarial: cobertura não é prova |
| 75–95 min | demonstração: teste verde, evidência parcial |
| 95–105 min | intervalo |
| 105–120 min | laboratório: classificar e confirmar |
| 120–140 min | revisar a diferença |
| 140–155 min | quebrar os testes |
| 155–165 min | devolutiva entre grupos |
| 165–180 min | protocolo mínimo e retrospectiva |

## MOD-03-AVAL — Critérios de avaliação

| Critério | Evidência esperada |
|---|---|
| classifica sem promover | inferência não registrada como fato |
| confirma em fonte | afirmação sobre o AS-IS com endereço verificável |
| delimita a ausência | busca negativa com termos e caminhos declarados |
| revisa contra escopo | arquivo inesperado identificado antes da leitura do conteúdo |
| testa o teste | defeito introduzido e resultado registrado |
| justifica o controle | cada item do protocolo ligado a um problema observado |

Relaciona-se a `OA-05`, `OA-06` e `OA-07`.

## MOD-03-EQUIVOCOS — Equívocos a observar

- "Se os testes passam, está certo." Passar prova que o teste não falhou, e alguns testes não
  conseguem falhar.
- "Cobertura alta é qualidade." Cobertura mede linhas executadas, não comportamento
  demonstrado.
- "Revisar é ler tudo com atenção." Revisar é comparar contra o escopo declarado; atenção sem
  referência cansa e não encontra.
- "O agente citou o arquivo, então confirmou." Citar é endereçar; confirmar exige que o
  conteúdo demonstre a afirmação.
- "Toda inferência é problema." Inferência identificada é trabalho normal; inferência
  disfarçada de fato é o problema.
- "Não achei, logo não existe." Prova apenas o alcance executado.
- "Auditoria é procurar culpado." É calibrar confiança; por isso cada grupo audita outro.

## MOD-03-MAT — Materiais e preparação

- resultados do `MOD-02` de cada grupo, redistribuídos entre grupos;
- exemplo preparado de teste verde com evidência parcial;
- dois defeitos preparados para a demonstração: um detectável, outro não;
- matriz de rastreabilidade fictícia marcada como "coberto" sem prova localizável;
- tabela dos padrões típicos de erro, impressa ou projetada;
- modelo do protocolo mínimo, com um exemplo de controle bem e mal enunciado;
- mecanismo de restauração do laboratório após a introdução de defeitos;
- ambiente em que quebrar o código de um grupo não afete os demais.

## MOD-03-FONTES — Fontes no método

- [`../../method/concepts.md`](../../method/concepts.md)
- [`../../method/traceability.md`](../../method/traceability.md)
- [`../../skill/cordel/references/investigacao.md`](../../skill/cordel/references/investigacao.md)
- [`CURSO-03.md`](CURSO-03.md)
- [`CURSO-06.md`](CURSO-06.md)

## MOD-03-PEND — Pendências

- este módulo é novo nesta revisão do curso e ainda não foi aplicado em turma;
- construir o exemplo de teste verde com evidência parcial no projeto-laboratório;
- preparar os dois defeitos da demonstração e validar que o teste acusa exatamente um;
- definir como os trabalhos serão redistribuídos entre grupos sem perda de tempo;
- garantir isolamento por grupo para a etapa de quebra de testes;
- escrever o modelo do protocolo mínimo e um exemplo comentado;
- decidir se o protocolo é individual ou por grupo — a comparação do encontro 5 pressupõe
  por grupo;
- criar a rubrica de avaliação do protocolo, que é a entrega mais importante do Bloco I;
- testar se seis etapas cabem em 75 minutos, ou fundir as etapas 5 e 6.
