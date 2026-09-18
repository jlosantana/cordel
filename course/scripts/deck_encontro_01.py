#!/usr/bin/env python3
"""Deck de aula do encontro 1 — Como um agente funciona e por que erra.

Fonte do conteúdo: course/topics/MOD-01.md.

Regra do Bloco I: o nível "No Cordel" dos conceitos NÃO vai para a tela. Ele
aparece apenas nas notas do apresentador, marcado como antecipação. Projetar
a resposta pronta faz a turma parar de construir a sua — que é o mecanismo
pedagógico do bloco inteiro.
"""

from __future__ import annotations

from deck_theme import (Deck, callout, capa_encontro, checklist, conceito, demo,
                        equivocos, etapa, foot, frase_grande, head, lista_simples,
                        roteiro, statement, tabela, tabela_vazia)

COR = "cyan"          # Bloco I
NAO_PROJETAR = "NÃO PROJETAR — antecipação para o instrutor. "


def build() -> Deck:
    d = Deck("Encontro 1", "Como um agente funciona e por que erra")

    # ---------------------------------------------------------- abertura
    d.add("CAPA", "Capa do encontro",
          capa_encontro("1", "I", "Como um agente funciona\ne por que erra",
                        "A IA encurta o caminho até uma alteração concreta. O trabalho "
                        "de engenharia precisa garantir que esse caminho continue "
                        "ligado à necessidade, à decisão e à prova."),
          "Não prometa que o curso ensina a usar uma ferramenta. Ele ensina a "
          "trabalhar com agentes. A ferramenta aparece no encontro 5.",
          classe="dark")

    d.add("ROTEIRO", "Roteiro das 3 horas",
          head("Encontro 1 · Roteiro", "O que vamos fazer hoje", COR)
          + roteiro([
              ("0–15", "Apresentação do curso, dos três blocos e da demanda condutora"),
              ("15–30", "Respostas espontâneas e discussão inicial"),
              ("30–55", "Como o modelo enxerga o problema: contexto, janela, corte de conhecimento"),
              ("55–70", "Não determinismo, custo e latência"),
              ("70–85", "Produtividade local, plausibilidade e duplo efeito"),
              ("85–100", "Demonstração: primeira passagem e três execuções"),
              ("100–110", "Intervalo"),
              ("110–125", "Laboratório: resposta imediata"),
              ("125–140", "Medição de divergência"),
              ("140–165", "Auditoria de premissas e sete perguntas"),
              ("165–180", "Comparação, entrega e retrospectiva"),
          ])
          + foot("Fonte: course/topics/MOD-01.md · MOD-01-ROTEIRO"),
          "Deixe o roteiro visível no intervalo. A turma precisa saber que 70 dos "
          "180 minutos são de laboratório.")

    d.add("OBJETIVOS", "Objetivos do encontro",
          head("Encontro 1 · Objetivos", "Ao final deste encontro você consegue", COR)
          + lista_simples([
              "Descrever o ciclo de observação e ação de um agente, e o que ele enxerga do seu problema.",
              "Explicar o efeito prático da janela de contexto sobre trabalhos longos.",
              "Reconhecer que o resultado não é determinístico — e medir essa variação.",
              "Identificar tarefas em que o agente reduz esforço ou tempo de forma real.",
              "Reconhecer premissas não confirmadas em uma resposta tecnicamente plausível.",
              "Explicar por que código e testes não provam, sozinhos, que o problema certo foi resolvido.",
          ], COR)
          + foot("MOD-01-OBJ · relaciona-se a OA-01 e OA-02"))

    d.add("TESE", "Tese do encontro",
          statement("A IA encurta o caminho até uma alteração concreta. "
                    "O trabalho de engenharia é garantir que esse caminho continue "
                    "ligado à necessidade, à decisão e à prova.",
                    "MOD-01-TESE"),
          "Leia em voz alta e deixe no ar. Volte a esta frase no fechamento, depois "
          "que a turma tiver visto três respostas diferentes para a mesma pergunta.",
          classe="dark")

    d.add("DEMANDA", "A demanda condutora",
          head("Caso condutor", "Uma frase, oito encontros", COR)
          + frase_grande("“O sistema deve avisar quando uma solicitação for aprovada.”")
          + '<p class="intro" style="margin-top:22px">Esta frase atravessa o curso '
            'inteiro. Hoje ela vai direto para o agente, sem preparo — para vermos o '
            'que acontece.</p>'
          + callout("Parece suficiente para implementar uma notificação. Guarde essa "
                    "impressão: vamos testá-la em quinze minutos.")
          + foot("Fonte: course/topics/CURSO-03.md · caso condutor"),
          "Não antecipe as perguntas que a frase esconde. Deixe a turma descobrir na "
          "primeira execução. Se alguém já apontar as lacunas, registre no quadro e "
          "siga — vai ser útil na etapa 3.")

    # ---------------------------------------------------------- conceitos
    total = 10
    conceitos = [
        ("MOD-01-CON-01", "O que o modelo enxerga do seu problema",
         "O modelo não tem acesso ao seu projeto. Ele recebe um texto e produz uma "
         "continuação provável desse texto.",
         "Tudo o que não estiver nesse texto, ou não puder ser buscado por uma "
         "ferramenta, não existe para ele. Antes de julgar uma resposta, pergunte o "
         "que o agente tinha em mãos quando a produziu.",
         "Um comportamento óbvio para a equipe e não escrito em lugar nenhum é "
         "invisível para o agente.",
         ""),

        ("MOD-01-CON-02", "Janela de contexto",
         "Existe um limite para quanto texto entra em uma interação. Quando ele se "
         "aproxima, informação antiga é resumida ou descartada — e o agente continua "
         "respondendo com a mesma segurança.",
         "Trabalhos longos degradam de forma silenciosa: uma restrição combinada no "
         "início deixa de ser respeitada, um arquivo já corrigido volta ao estado "
         "anterior, uma decisão é reaberta.",
         "O controle é manter o que importa em arquivo, não na conversa — e recomeçar "
         "a sessão apontando para esse arquivo.",
         NAO_PROJETAR + "É a razão de existir um índice curto que aponta para fontes "
         "em vez de duplicá-las, com carregamento sob demanda."),

        ("MOD-01-CON-03", "Corte de conhecimento",
         "O modelo foi treinado até certa data. O que veio depois é desconhecido — e "
         "ele não sinaliza a diferença.",
         "Para qualquer afirmação sobre biblioteca, versão, sintaxe ou comportamento "
         "de ferramenta, exija a fonte. O que o projeto usa está no arquivo de "
         "dependências, não na memória do modelo.",
         "Ele responde sobre a versão que conhece com a mesma naturalidade com que "
         "responderia sobre a versão atual.",
         ""),

        ("MOD-01-CON-04", "Não determinismo",
         "A mesma solicitação pode produzir resultados diferentes em execuções "
         "diferentes. Não é falha: é como o modelo gera texto.",
         "Um resultado que você não consegue reproduzir não pode ser a base de uma "
         "decisão. O que precisa ser estável — a decisão, o critério, o comando — vai "
         "para um arquivo versionado.",
         "Duas execuções podem escolher arquivos distintos, estruturas distintas e "
         "até conclusões distintas sobre o mesmo código.",
         NAO_PROJETAR + "É por isso que o método registra decisão e evidência em "
         "artefatos, e não trata a conversa com o agente como fonte."),

        ("MOD-01-CON-05", "Custo e latência",
         "Cada execução consome tempo e dinheiro. Uma tarefa com três tentativas e "
         "uma revisão longa pode custar mais do que fazer à mão.",
         "Estime antes de delegar: quanto tempo levaria fazer, quanto tempo levará "
         "revisar. Quando a revisão for mais cara que a execução, a delegação não "
         "compensa.",
         "", ""),

        ("MOD-01-CON-06", "Produtividade local e resultado do sistema",
         "Uma tarefa localmente eficiente pode aumentar retrabalho ou risco no fluxo "
         "completo.",
         "Produtividade local mede quanto uma etapa ficou mais rápida. Resultado do "
         "sistema considera se a mudança atende à necessidade, respeita decisões, não "
         "cria impacto indevido e pode ser provada.",
         "“Escrevi o teste em dois minutos” e “a mudança está pronta” são afirmações "
         "de naturezas diferentes.",
         ""),

        ("MOD-01-CON-07", "Plausibilidade não é evidência",
         "Uma explicação pode parecer completa porque preenche lacunas de modo "
         "provável. Coerência interna não é sinal de correção.",
         "Toda afirmação técnica importante precisa ser ligada a uma fonte ou "
         "permanecer marcada como inferência. As duas coisas são aceitáveis; a mistura "
         "silenciosa das duas, não.",
         "", NAO_PROJETAR + "Corresponde à separação entre alegação, inferência, "
         "evidência declarada e evidência confirmada. É o tema do encontro 3."),

        ("MOD-01-CON-08", "O duplo efeito da aceleração",
         "Onde a aceleração é maior, o controle precisa ser mais próximo. Não o "
         "contrário.",
         "Pesquisa, planejamento, código, testes e documentação ficam mais rápidos. Os "
         "mecanismos de falha também: escolher fonte errada, consolidar suposição, "
         "implementar escopo indevido, testar a própria interpretação.",
         "O intervalo entre uma premissa errada e uma alteração concreta encurta na "
         "mesma proporção.",
         ""),

        ("MOD-01-CON-09", "Necessidade, autorização e prova",
         "Uma necessidade justifica investigação. Uma decisão autoriza escopo. Uma "
         "implementação materializa. Uma evidência sustenta. Nenhuma substitui a outra.",
         "A confusão mais comum e mais cara é tratar necessidade como autorização: "
         "alguém pediu, logo está aprovado. O agente reproduz essa confusão porque não "
         "tem como perceber a diferença.",
         "", NAO_PROJETAR + "É a cadeia mínima do método, estudada a partir do "
         "encontro 6."),
    ]

    for pos, (cid, titulo, principio, pratica, exemplo, nota) in enumerate(conceitos, 1):
        d.add(cid, f"{cid.split('-')[-1]} · {titulo}",
              conceito(cid, f"Conceito {pos} de {total}", titulo, principio, pratica,
                       exemplo, COR)
              + foot("Fonte: course/topics/MOD-01.md"), nota)

    d.add("MOD-01-CON-10", "10 · As sete perguntas",
          head("MOD-01-CON-10 · Conceito 10 de 10", "As sete perguntas", COR)
          + '<p class="intro">Voltam em todos os encontros. São o currículo real '
            'do curso.</p>'
          + '<ul class="qgrid">' + "".join(
              f'<li><span class="tag">{r}</span><span class="txt">{t}</span></li>'
              for r, t in [
                  ("Origem", "Qual necessidade deu origem à mudança?"),
                  ("Natureza", "O que é fato, relato, inferência ou decisão?"),
                  ("AS-IS", "O que o sistema realmente faz hoje?"),
                  ("Autoridade", "Quem autorizou a mudança de escopo?"),
                  ("Observação", "Como o resultado será observado?"),
                  ("Prova", "Qual evidência sustentará a conclusão?"),
                  ("Concordância", "Como fontes, código e testes voltam a concordar?"),
              ]) + "</ul>"
          + foot("MOD-01-CON-10 · quadro completo em course/topics/CURSO-03.md"),
          "Este quadro fica visível durante o laboratório. A turma vai usá-lo na "
          "etapa 4. Não entregue as respostas: várias delas ninguém consegue responder "
          "hoje, e perceber isso é o objetivo.")

    # ------------------------------------------------------ demonstração
    d.add("DEMO", "Demonstração — roteiro",
          demo("A mesma pergunta, três respostas", [
              ("Primeira passagem", "8 min",
               "Peça um plano de implementação. Não forneça requisito, canal, "
               "destinatário, estado nem política. Preserve a resposta."),
              ("Três execuções", "7 min",
               "Repita a mesma solicitação, do zero, mais duas vezes. Coloque as três "
               "lado a lado."),
              ("Leitura crítica", "15 min",
               "Marque uma das respostas com as quatro categorias do próximo slide."),
              ("Fechamento", "5 min",
               "Mostre que o plano pode ser razoável e ainda depender de várias "
               "decisões."),
          ], [
              "o que variou entre as três: arquivos, canal presumido, estrutura, profundidade",
              "quantas decisões de negócio o agente tomou sem avisar",
              "quais afirmações têm fonte e quais são preenchimento provável",
          ], COR)
          + foot("MOD-01-DEMO"),
          "Não ridicularize a primeira resposta. O valor dela é revelar como uma "
          "solicitação insuficiente produz uma solução convincente. A turma costuma "
          "esperar variação de redação e encontrar variação de conclusão.")

    d.add("DEMO-MARCAS", "Demonstração — as quatro marcas",
          head("Demonstração", "Quatro marcas para ler qualquer resposta", COR)
          + tabela(["Marca", "Significado", "Exemplo nesta resposta"], [
              ("F", "Fato sustentado", "arquivo efetivamente localizado"),
              ("A", "Alegação recebida", "“o sistema não avisa”"),
              ("I", "Inferência", "“o canal deve ser e-mail”"),
              ("D", "Decisão necessária", "destinatário e momento do envio"),
          ])
          + callout("O problema não é a inferência. É a inferência que atravessa o "
                    "texto vestida de fato e chega ao código como premissa.")
          + foot("MOD-01-DEMO · leitura crítica"),
          "Marque ao vivo, na resposta real, e não em um exemplo preparado. Se a "
          "turma discordar de uma marca, discuta — a fronteira entre I e F é "
          "exatamente o que se está aprendendo a enxergar.")

    # -------------------------------------------------------- laboratório
    d.add("LAB", "Laboratório — abertura",
          '<div class="cover-body"><p class="eyebrow">Laboratório · 70 minutos</p>'
          '<h1>Diagnóstico sem método</h1>'
          '<p class="lead">Grupos de duas ou três pessoas. Uma demanda ambígua por '
          'grupo, acesso de leitura ao repositório.<br>O agente pode ler, pesquisar e '
          'propor — não deve alterar arquivos.</p></div>',
          "Distribua as demandas antes do intervalo, para os grupos já voltarem "
          "lendo. Confirme que cada grupo consegue abrir sessões limpas com rapidez: "
          "a etapa 2 depende disso.",
          classe="dark")

    d.add("LAB-1", "Etapa 1 — Resposta imediata",
          etapa(1, "Resposta imediata", "15 minutos", [
              "Peça análise e plano ao agente, como você faria normalmente.",
              "Guarde a solicitação, as fontes usadas e a resposta.",
              "Não corrija nada durante esta primeira execução.",
          ], callout("O objetivo é registrar o comportamento natural do grupo, não o "
                     "melhor comportamento possível."))
          + foot("MOD-01-LAB · etapa 1"),
          "Circule ouvindo, sem intervir. Anote quem já começou a refinar o prompt "
          "sozinho — vira material para a discussão do encontro 2.")

    d.add("LAB-2", "Etapa 2 — Medição de divergência",
          etapa(2, "Medição de divergência", "15 minutos", [
              "Execute a mesma solicitação mais duas vezes, em sessões novas.",
              "Preencha a tabela comparando as três execuções.",
          ], tabela_vazia(["Aspecto", "Execução 1", "Execução 2", "Execução 3",
                           "Divergiu?"], 4)
             + callout("Qual das três respostas você teria implementado se tivesse "
                       "executado apenas uma vez?"))
          + foot("MOD-01-LAB · etapa 2"),
          "Linhas sugeridas para a tabela: arquivos consultados, causa apontada, "
          "solução proposta, decisões assumidas. A pergunta do rodapé é o fecho da "
          "etapa — faça em voz alta, para a turma toda.")

    d.add("LAB-3", "Etapa 3 — Auditoria de premissas",
          etapa(3, "Auditoria de premissas", "25 minutos", [
              "Escolha uma das três respostas.",
              "Classifique cada afirmação relevante e registre o que falta para "
              "sustentá-la.",
          ], tabela_vazia(["Afirmação", "Tipo (F / A / I / D)", "Fonte disponível",
                           "O que falta"], 4))
          + foot("MOD-01-LAB · etapa 3"),
          "O erro típico é classificar tudo como fato porque “está no código”. Peça o "
          "endereço: caminho e linha. Sem endereço, é alegação.")

    d.add("LAB-4", "Etapa 4 — As sete perguntas",
          etapa(4, "Aplicação das sete perguntas", "20 minutos", [
              "Responda cada uma das sete perguntas apenas com o que consegue confirmar.",
              "Resposta desconhecida vira busca pendente ou decisão pendente — nunca "
              "suposição.",
          ], callout("Quantas das sete vocês conseguem responder agora? Quantas "
                     "dependem de alguém que não está nesta sala?", "yellow"))
          + foot("MOD-01-LAB · etapa 4"),
          "É comum um grupo responder duas ou três das sete. Isso é o resultado "
          "esperado, não fracasso. Nomeie isso explicitamente antes de seguir.")

    d.add("LAB-5", "Etapa 5 — Comparação e entrega",
          etapa(5, "Comparação e preparação da entrega", "15 minutos", [
              "Ganho real oferecido pelo agente.",
              "Primeira ação que teria sido executada cedo demais.",
              "Fonte que deveria ter sido consultada.",
              "Decisão que pertence a uma pessoa.",
              "Prova que ainda não poderia ser definida.",
          ], callout("Escolham um exemplo claro para apresentar à turma, preservando "
                     "as respostas originais como evidência."))
          + foot("MOD-01-LAB · etapa 5"),
          "Peça que cada grupo apresente UM item, não os cinco. Quinze minutos não "
          "comportam mais que isso, e a repetição entre grupos é o que consolida.")

    d.add("ENTREGA", "Entrega do encontro",
          head("Encontro 1 · Entrega", "Diagnóstico inicial", COR)
          + checklist([
              "Demanda recebida e contexto disponível",
              "As três respostas originais do agente",
              "Tabela de divergência entre execuções",
              "Mapa de fatos, relatos, inferências e decisões",
              "Benefícios observados, ligados a tarefas concretas",
              "Riscos e perguntas ausentes",
              "Ação que o grupo considera autorizada neste momento",
              "Justificativa, sem antecipar conteúdo ainda não visto",
          ], COR)
          + callout("Este diagnóstico volta nos encontros 3, 6 e 8. Guardem os "
                    "arquivos originais.")
          + foot("MOD-01-ENT"),
          "Cobre a preservação das respostas originais. Sem elas, a auditoria "
          "cruzada do encontro 3 não tem material.")

    # ---------------------------------------------------------- fechamento
    d.add("EQUIVOCOS", "Equívocos a evitar",
          head("Encontro 1 · Fechamento", "Seis leituras erradas deste encontro", COR)
          + equivocos([
              ("O objetivo é provar que o agente é ruim.",
               "O objetivo é calibrar confiança e controle."),
              ("Toda inferência é proibida.",
               "Inferência identificada é trabalho normal. Disfarçada de fato, é o problema."),
              ("Mais prompt resolveria tudo.",
               "Parte das lacunas depende de fonte, acesso ou decisão. Encontro 2 mostra até onde a condução vai."),
              ("Se compila, está correto.",
               "Compilação não prova necessidade, autorização nem aceite."),
              ("A variação some com temperatura zero.",
               "Reduz, não elimina — e o problema de fundo é decidir sobre um resultado não reproduzido."),
              ("O modelo sabe qual versão da biblioteca usamos.",
               "Ele sabe o que estava no treino, ou o que uma ferramenta buscou agora."),
          ])
          + foot("MOD-01-EQUIVOCOS"),
          "Se algum desses apareceu no laboratório, cite o grupo sem expor: “ouvi "
          "hoje que...”. Funciona melhor que apresentar como lista abstrata.")

    d.add("RETRO", "Retrospectiva",
          head("Encontro 1 · Retrospectiva", "15 minutos, por grupo", COR)
          + lista_simples([
              "Uma decisão que vocês tomaram hoje.",
              "A evidência que a sustenta — ou a ausência dela.",
              "Um erro que vocês evitaram por terem parado para olhar.",
              "Uma incerteza que continua aberta.",
          ], COR)
          + callout("O registro desta retrospectiva alimenta o encontro 8. Não é "
                    "conversa: é dado.")
          + foot("MOD-01 · MET-04"),
          "Abra o registro acumulativo hoje e mantenha até o encontro 8: tempo por "
          "etapa, bloqueios, erros evitados, redescobertas, decisões alteradas.")

    d.add("PONTE", "Próximo encontro",
          '<div class="cover-body"><p class="eyebrow">Encontro 2</p>'
          '<h1>Condução:<br>da intenção à tarefa executável</h1>'
          '<p class="lead">Hoje entregamos a intenção ao agente e vimos o que '
          'acontece.<br>No próximo encontro, vamos entregar uma tarefa — e refazer '
          'exatamente a mesma demanda para comparar.</p>'
          '<p class="divider-foot tone-cyan">Traga o diagnóstico de hoje. '
          'Ele é o ponto de partida.</p></div>',
          "Feche voltando à tese do início. A turma agora viu três respostas "
          "diferentes para a mesma pergunta: a frase sobre necessidade, decisão e "
          "prova significa outra coisa depois disso.",
          classe="dark")

    return d
