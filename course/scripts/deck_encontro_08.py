#!/usr/bin/env python3
"""Deck de aula do encontro 8 — Transferência e evolução.

Fonte do conteúdo: course/topics/MOD-08.md.

O teste de transferência é a atividade que revela se o curso ensinou princípio
ou procedimento. É individual, e contém informação sobre o time de origem de
cada pessoa: decida antes o destino desse documento.
"""

from __future__ import annotations

from deck_theme import (Deck, callout, capa_encontro, checklist, conceito, demo,
                        equivocos, etapa, foot, frase_grande, head, lista_simples,
                        roteiro, statement, tabela, tabela_vazia)

COR = "red"


def build() -> Deck:
    d = Deck("Encontro 8", "Transferência e evolução")

    d.add("CAPA", "Capa do encontro",
          capa_encontro("8", "III", "Transferência\ne evolução",
                        "O que se aprende aqui precisa sobreviver à troca de "
                        "ferramenta, de time e de empresa."),
          "Último encontro. A pergunta que decide se o curso valeu: o que cada pessoa "
          "leva para o próprio time, que provavelmente não usa o Cordel?",
          classe="dark divider-red")

    d.add("ROTEIRO", "Roteiro das 3 horas",
          head("Encontro 8 · Roteiro", "O que vamos fazer hoje", COR)
          + roteiro([
              ("0–20", "Núcleo, adaptador e conhecimento federado"),
              ("20–35", "Sinais de evolução, hipótese e refutação"),
              ("35–50", "Evals, versionamento e adoção incremental"),
              ("50–70", "Tradução para o contexto real e o que não se transfere"),
              ("70–85", "Demonstração dos três destinos"),
              ("85–95", "Intervalo"),
              ("95–125", "Inventário, classificação e proposta"),
              ("125–140", "Eval"),
              ("140–165", "Teste de transferência, individual"),
              ("165–180", "Plano de 30 dias, apresentações e fechamento"),
          ])
          + foot("MOD-08-ROTEIRO"))

    d.add("OBJETIVOS", "Objetivos do encontro",
          head("Encontro 8 · Objetivos", "Ao final deste encontro você consegue", COR)
          + lista_simples([
              "Distinguir núcleo, adaptador e contexto local.",
              "Identificar atrito útil, desperdício e lacuna de controle.",
              "Formular hipótese de evolução com evidência de uso.",
              "Desenhar eval para skill ou workflow.",
              "Traduzir cada controle do curso para as ferramentas que seu time já usa.",
              "Identificar o que é inegociável, o que é adaptável e o que não se aplica hoje.",
              "Planejar um piloto de 30 dias com condições de sucesso e de abandono.",
          ], COR)
          + foot("MOD-08-OBJ · relaciona-se a OA-02, OA-04 e OA-12"))

    d.add("TESE", "Tese do encontro",
          statement("Se o método precisar ser trocado, os controles continuam valendo. "
                    "É isso que torna o aprendizado portátil.", "MOD-08-TESE"),
          classe="dark divider-red")

    conceitos = [
        ("MOD-08-CON-01", "Núcleo portátil", "Conceito 1 de 7",
         "Invariantes que resolvem o mesmo problema em contextos diferentes: origem, "
         "AS-IS, autorização, unidade verificável, evidência e reconciliação.",
         "Teste de portabilidade: o controle continua fazendo sentido em um time que "
         "usa outra linguagem, outro processo e outra ferramenta de IA?",
         "Se depender de um nome de arquivo ou de um comando, é adaptador."),

        ("MOD-08-CON-03", "Conhecimento federado", "Conceito 3 de 7",
         "Contexto local ao serviço fica perto do código; requisitos e decisões "
         "transversais podem viver em sistemas especializados.",
         "Cada fonte registra responsável e escopo.",
         "Integração não substitui autoridade."),

        ("MOD-08-CON-05", "Hipótese e avaliação", "Conceito 5 de 7",
         "Uma proposta descreve problema, evidência, alcance, alternativa, efeito "
         "esperado e forma de refutação.",
         "Sem forma de refutação, a proposta é opinião.",
         "A pergunta que fecha qualquer proposta: que observação me faria concluir que "
         "isto não funcionou?"),

        ("MOD-08-CON-07", "Adoção incremental", "Conceito 6 de 7",
         "Comece tornando o projeto legível, escolha uma demanda pequena, percorra a "
         "cadeia mínima, registre o atrito e só então amplie.",
         "O erro típico é começar pelo projeto mais crítico, para “provar valor”.",
         "Um piloto pequeno separa problemas do método de problemas do produto. Um "
         "piloto grande mistura os dois, e o método leva a culpa."),
    ]

    d.add("MOD-08-CON-02", "02 · Núcleo e adaptador",
          head("MOD-08-CON-02 · Conceito 2 de 7", "O que fica e o que vai com você", COR)
          + tabela(["Nível", "O que declara", "Portátil?"], [
              ("Núcleo", "Invariantes: origem, AS-IS, autorização, prova, reconciliação",
               "Sim — vai com você"),
              ("Adaptador", "Caminhos, comandos, arquitetura, prefixos, políticas locais",
               "Não — fica com o projeto"),
              ("Contexto local", "Notas pessoais, sem autoridade compartilhada",
               "Não — fica com você, sem valer para o time"),
          ])
          + callout("É o mecanismo que responde à pergunta de hoje: o que levo comigo "
                    "quando mudo de time?")
          + foot("MOD-08-CON-02"))

    d.add("MOD-08-CON-04", "04 · Sinais para evolução",
          head("MOD-08-CON-04 · Conceito 4 de 7", "Quando mudar o método", COR)
          + lista_simples([
              "Decisão errada recorrente.",
              "Informação redescoberta em vários trabalhos.",
              "Risco relevante não coberto.",
              "Campo ou gate que nunca altera decisão.",
              "Regra local repetida em contextos independentes.",
              "Execução inconsistente da mesma skill.",
          ], COR, numerada=False)
          + callout("Um caso isolado não é sinal. Preferência pessoal não é sinal. A "
                    "ausência de sinal é motivo suficiente para não mudar nada.")
          + foot("MOD-08-CON-04"))

    for cid, titulo, posicao, principio, pratica, exemplo in conceitos:
        d.add(cid, f"{cid.split('-')[-1]} · {titulo}",
              conceito(cid, posicao, titulo, principio, pratica, exemplo, COR)
              + foot("Fonte: course/topics/MOD-08.md"))

    d.add("MOD-08-CON-08", "08 · Tradução para o contexto real",
          head("MOD-08-CON-08 · Conceito 7 de 7",
               "O controle não depende do artefato que o carrega", COR)
          + tabela(["Controle", "Onde pode viver sem o Cordel"], [
              ("Origem preservada", "Campo de origem no item de backlog; link para o incidente"),
              ("AS-IS confirmado", "Seção do pull request com endereços verificáveis"),
              ("Autorização explícita", "Quem aprovou e com que limites, registrado no item"),
              ("Escopo e fora do escopo", "Descrição do item, revisada antes de começar"),
              ("Estratégia de prova", "Critérios de aceite com forma de verificação, antes do código"),
              ("Revisão contra escopo", "Política que compara arquivos alterados ao pedido"),
              ("Reconciliação", "Atualização de documentação no critério de pronto"),
          ])
          + callout("A maior parte dos times não adotará um método inteiro. Adotará "
                    "dois ou três controles, nas ferramentas que já usa.", "yellow")
          + foot("MOD-08-CON-08"),
          "Este slide é a preparação direta do teste de transferência. Deixe visível "
          "durante a etapa 5 — mas como ponto de partida, não como resposta.")

    d.add("MOD-08-CON-09", "09 · O que não se transfere",
          conceito("MOD-08-CON-09", "Limite", "O que não se transfere",
                   "Alguns controles dependem de condições que nem todo time tem: "
                   "autoridade para bloquear, tempo de investigação antes de "
                   "implementar, fonte canônica com responsável.",
                   "Fingir que se aplicam produz cerimônia sem efeito. Reconhecer o "
                   "que não se aplica hoje, e sob que condição passaria a se aplicar, "
                   "é resposta melhor que uma adoção completa e falsa.",
                   "", COR)
          + foot("MOD-08-CON-09"))

    d.add("DEMO", "Demonstração — três destinos",
          demo("Três destinos para uma melhoria", [
              ("A proposta", "3 min",
               "“Toda story deve incluir o campo schema Oracle afetado.”"),
              ("Os três destinos", "7 min",
               "No projeto Oracle: possível regra do adaptador. Em projetos sem "
               "Oracle: sem aplicabilidade. No núcleo: inadequada, por ser tecnologia "
               "específica."),
              ("O problema portátil", "3 min",
               "Impactos em dados precisam ser avaliados quando aplicáveis. Essa "
               "formulação pode pertencer ao núcleo; o campo permanece no adaptador."),
              ("Controle ou cerimônia", "2 min",
               "Como testar se um novo checklist evita omissões ou apenas aumenta "
               "preenchimento."),
          ], [
              "que a proposta original não estava errada — estava no nível errado",
              "que extrair o problema portátil é o trabalho, não descartar a proposta",
          ], COR)
          + foot("MOD-08-DEMO"))

    d.add("LAB", "Laboratório — abertura",
          '<div class="cover-body"><p class="eyebrow">Laboratório · 85 minutos</p>'
          '<h1>Retrospectiva, proposta<br>e transferência</h1>'
          '<p class="lead">Primeiro olhamos para dentro do método: o que ele deveria '
          'passar a fazer. Depois para fora: o que cada um leva para o próprio '
          'time.</p>'
          '<p class="divider-foot tone-red">A etapa 5 é individual. O contexto de cada '
          'pessoa é diferente.</p></div>',
          classe="dark divider-red")

    d.add("LAB-1", "Etapa 1 — Inventário de evidências",
          etapa(1, "Inventário de evidências", "15 minutos", [
              "Reúnam os registros dos sete encontros: bloqueios, redescobertas, erros "
              "evitados, campos sem efeito, correções do agente, decisões alteradas.",
              "Incluam a divergência medida no encontro 1.",
              "Incluam a medida do Bloco I: quantos controles do protocolo mínimo o "
              "grupo identificou sozinho antes do encontro 5.",
          ])
          + foot("MOD-08-LAB · etapa 1"),
          "A última linha é o indicador do desenho do curso, não do desempenho da "
          "turma. Registre por turma e acompanhe entre edições.")

    d.add("LAB-2", "Etapa 2 — Classificar problemas",
          etapa(2, "Classificar problemas", "15 minutos", [
              "Para cada item, decidam o que é.",
          ], lista_simples([
              "Falha do cenário ou da infraestrutura do curso.",
              "Regra local do projeto.",
              "Problema recorrente candidato ao núcleo.",
              "Necessidade de skill, script, modelo ou documentação.",
              "Preferência sem evidência suficiente.",
          ], COR, numerada=False))
          + foot("MOD-08-LAB · etapa 2"))

    d.add("LAB-3", "Etapa 3 — Formular proposta",
          etapa(3, "Formular proposta", "20 minutos", [
              "Preencham a proposta de evolução.",
          ], tabela_vazia(["Campo", "Conteúdo"], 5)
             + callout("Problema observado · evidência · frequência ou risco · alcance "
                       "(núcleo / adaptador / local) · mudança · resultado esperado · "
                       "custo e risco · avaliação · critério de adoção"))
          + foot("MOD-08-LAB · etapa 3"),
          "Propostas vindas de controles do protocolo mínimo sem correspondência no "
          "método, identificados no encontro 5, são candidatas naturais. Lembre a "
          "turma disso.")

    d.add("LAB-4", "Etapa 4 — Desenhar eval",
          etapa(4, "Desenhar eval", "15 minutos", [
              "Criem ao menos três casos: comum, limite e adversarial.",
              "Definam comportamento esperado e critério mensurável.",
          ], callout("Evitem avaliar somente estilo textual. Eval não é perguntar se a "
                     "resposta parece boa."))
          + foot("MOD-08-LAB · etapa 4"))

    d.add("LAB-5", "Etapa 5 — Teste de transferência",
          etapa(5, "Teste de transferência — INDIVIDUAL", "25 minutos", [
              "Descreva o seu time. Depois preencha, para cada controle do curso:",
          ], tabela_vazia(["Controle do curso", "Onde viveria no meu time", "Ferramenta",
                           "Classificação"], 4)
             + callout("Classificação: inegociável · adaptável · não se aplica hoje. "
                       "Para cada “não se aplica hoje”, registre a condição que "
                       "precisaria mudar.", "yellow"))
          + foot("MOD-08-LAB · etapa 5"),
          "Individual, não em grupo. Este documento contém informação sobre o "
          "empregador de quem está na sala: em turma fechada de cliente, o padrão é "
          "que fique com quem escreveu.")

    d.add("LAB-5B", "Etapa 5 — Os três controles",
          head("Encontro 8 · Teste de transferência", "Escolha três", COR)
          + frase_grande("Quais três controles você introduziria primeiro no seu "
                         "time — e qual problema concreto espera resolver com cada um?",
                         30)
          + callout("Três é deliberado. Uma lista de doze não é adotada por ninguém.",
                    "yellow")
          + foot("MOD-08-LAB · etapa 5, fecho"),
          "Peça duas frases por controle. A segunda — o problema concreto — é a que "
          "revela se a pessoa entendeu ou está repetindo.")

    d.add("LAB-6", "Etapa 6 — Plano de 30 dias",
          etapa(6, "Plano de 30 dias", "10 minutos", [
              "Projeto-piloto, demanda inicial, responsáveis, fontes, comandos, "
              "checkpoints e métricas.",
              "Decisão de continuidade — incluindo o que faria o piloto ser abandonado.",
          ], callout("Um plano sem critério de abandono não é um plano; é uma "
                     "intenção."))
          + foot("MOD-08-LAB · etapa 6"))

    d.add("ENTREGA", "Entrega do encontro",
          head("Encontro 8 · Entrega", "Evolução e transferência", COR)
          + checklist([
              "Retrospectiva baseada no rastro dos oito encontros",
              "Classificação entre núcleo, adaptador e local",
              "Proposta de evolução com hipótese, evidência e forma de refutação",
              "Conjunto inicial de evals",
              "Riscos e custo da própria mudança",
              "Teste de transferência individual, com os três controles prioritários",
              "Plano de adoção de 30 dias, com critério de abandono",
              "Apresentação final ligando problema, controle, resultado e aprendizado",
          ], COR)
          + callout("A apresentação final tem uma exigência: responder às sete "
                    "perguntas SEM o vocabulário do Cordel.", "yellow")
          + foot("MOD-08-ENT · critério de conclusão do curso"))

    d.add("EQUIVOCOS", "Equívocos a evitar",
          head("Encontro 8 · Fechamento", "Leituras erradas deste encontro", COR)
          + equivocos([
              ("Todo atrito deve ser removido.",
               "Alguns pontos existem para preservar decisão ou segurança."),
              ("Se funcionou no laboratório, entra no núcleo.",
               "Um caso não demonstra portabilidade."),
              ("Mais campos tornam o método completo.",
               "Campos sem decisão associada criam ruído."),
              ("Eval é perguntar se a resposta parece boa.",
               "Precisa de tarefa e critério observável."),
              ("Adoção começa pelo maior projeto.",
               "Um piloto pequeno separa problemas do método e do produto."),
              ("Transferir é convencer o time a adotar o Cordel.",
               "É levar os controles, na ferramenta que o time já usa."),
              ("Se meu time não me deixa bloquear, nada disso se aplica.",
               "Parte se aplica. Identificar o que não se aplica hoje é resposta válida."),
              ("O curso acabou.",
               "O plano de 30 dias começa segunda-feira. Sem ele, isto foi entretenimento."),
          ])
          + foot("MOD-08-EQUIVOCOS"))

    d.add("FIM", "Fechamento do curso",
          '<div class="cover-body"><p class="eyebrow">Fim do curso</p>'
          '<h1>O que você leva<br>para o seu time</h1>'
          '<p class="lead">Três controles, na ferramenta que o time já usa, cada um '
          'ligado a um problema concreto que você viu acontecer nestes oito '
          'encontros.</p>'
          '<p class="divider-foot tone-red">Se o método precisar ser trocado, os '
          'controles continuam valendo. É isso que torna o aprendizado portátil.</p>'
          '</div>',
          "Encerre com o teste de transferência, não com um resumo do Cordel. Se a "
          "última coisa que a turma ouvir for a ferramenta, o curso voltou a ser sobre "
          "ela.", classe="dark divider-red")

    return d
