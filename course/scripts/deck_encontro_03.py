#!/usr/bin/env python3
"""Deck de aula do encontro 3 — Verificação: o que a IA produziu merece crédito?

Fonte do conteúdo: course/topics/MOD-03.md.

Regra do Bloco I: o nível "No Cordel" dos conceitos NÃO vai para a tela.
Este é o último encontro antes de o método ser apresentado — a tentação de
antecipar é maior aqui. Não ceda: o protocolo mínimo perde o sentido.
"""

from __future__ import annotations

from deck_theme import (Deck, callout, capa_encontro, checklist, conceito, demo,
                        equivocos, etapa, foot, frase_grande, head, lista_simples,
                        roteiro, statement, tabela, tabela_vazia)

COR = "cyan"
NAO_PROJETAR = "NÃO PROJETAR — antecipação para o instrutor. "


def build() -> Deck:
    d = Deck("Encontro 3", "Verificação: o que a IA produziu merece crédito?")

    d.add("CAPA", "Capa do encontro",
          capa_encontro("3", "I", "Verificação: o que a IA\nproduziu merece crédito?",
                        "Não existe resultado confiável, existe resultado verificado. "
                        "A pergunta não é se o agente acertou, é como você sabe."),
          "Encontro que fecha o Bloco I. A entrega de hoje — o protocolo mínimo — é o "
          "documento mais importante do bloco, e volta no encontro 5.",
          classe="dark")

    d.add("ROTEIRO", "Roteiro das 3 horas",
          head("Encontro 3 · Roteiro", "O que vamos fazer hoje", COR)
          + roteiro([
              ("0–10", "Retomada: o que a condução não resolveu"),
              ("10–30", "Cinco naturezas de afirmação; confirmar o comportamento atual"),
              ("30–45", "Evidência pertinente e busca negativa"),
              ("45–60", "Leitura da diferença e padrões típicos de erro"),
              ("60–75", "Teste adversarial: cobertura não é prova"),
              ("75–95", "Demonstração: teste verde, evidência parcial"),
              ("95–105", "Intervalo"),
              ("105–120", "Laboratório: classificar e confirmar"),
              ("120–140", "Revisar a diferença"),
              ("140–155", "Quebrar os testes"),
              ("155–165", "Devolutiva entre grupos"),
              ("165–180", "Protocolo mínimo e retrospectiva"),
          ])
          + foot("MOD-03-ROTEIRO"))

    d.add("OBJETIVOS", "Objetivos do encontro",
          head("Encontro 3 · Objetivos", "Ao final deste encontro você consegue", COR)
          + lista_simples([
              "Classificar afirmações em fato, relato, inferência, decisão e evidência.",
              "Confirmar o comportamento atual em fonte inspecionável antes de propor mudança.",
              "Avaliar se uma evidência é localizável, autorizada e pertinente.",
              "Delimitar o alcance de uma busca negativa.",
              "Revisar uma diferença contra o escopo declarado.",
              "Reconhecer padrões típicos de erro do agente.",
              "Projetar um teste capaz de falhar — e distinguir cobertura de prova.",
          ], COR)
          + foot("MOD-03-OBJ · relaciona-se a OA-05, OA-06 e OA-07"))

    d.add("TESE", "Tese do encontro",
          statement("A pergunta não é se o agente acertou. É como você sabe.",
                    "MOD-03-TESE"),
          "Esta é a competência que mais escala com o uso de IA: quanto mais código um "
          "time gera, mais a capacidade de revisão vira o gargalo real.",
          classe="dark")

    total = 7
    conceitos = [
        ("MOD-03-CON-02", "Confirmar o comportamento atual",
         "Antes de decidir o que o sistema deve passar a fazer, é preciso saber o que "
         "ele faz hoje — em fonte inspecionável.",
         "O agente é bom nisso, e é exatamente aqui que ele mais engana: pedido a "
         "descrever um comportamento, produz uma descrição coerente misturando o que "
         "leu com o que é plausível. Exija o endereço.",
         "“O envio acontece em notificador.py:88” é verificável. “O sistema já envia "
         "notificações” não é.",
         NAO_PROJETAR + "É o AS-IS confirmado, exigido antes da decisão. Volta como "
         "prática documentada no encontro 6."),

        ("MOD-03-CON-03", "Evidência localizável e pertinente",
         "Uma evidência serve quando pode ser localizada, está no lugar que tem "
         "autoridade sobre aquele fato, e demonstra especificamente a afirmação.",
         "As três condições são independentes, e a terceira é a que mais falha. "
         "`caminho:linha` é endereço, não garantia.",
         "Ao aceitar uma evidência, faça a pergunta inversa: se a afirmação fosse "
         "falsa, esta evidência seria diferente?",
         ""),

        ("MOD-03-CON-04", "Busca negativa",
         "Não encontrar não é o mesmo que não existir. Uma busca só sustenta uma "
         "conclusão quando seu alcance está declarado.",
         "Registre termos, caminhos e revisão consultados. O agente enuncia “o sistema "
         "não notifica” com frequência, a partir de uma busca cujo alcance ele não "
         "relatou.",
         "“Não encontrei notific|aviso|alerta em src/ na revisão atual” é verificável "
         "e refutável. “O sistema não notifica” não é.",
         ""),

        ("MOD-03-CON-05", "Leitura da diferença contra o escopo",
         "Revisar código gerado não é ler linha a linha procurando erro de lógica. É "
         "responder duas perguntas.",
         "Todo arquivo alterado tinha motivo no que foi pedido? Tudo que foi pedido "
         "aparece em algum arquivo alterado? Comece pela lista de arquivos, antes do "
         "conteúdo.",
         "Um arquivo que você não esperava é o sinal mais barato e mais confiável de "
         "escopo excedido. Quando a diferença não cabe em uma leitura atenta, o "
         "problema é o tamanho do passo.",
         NAO_PROJETAR + "Escopo e fora do escopo declarados na story tornam essa "
         "revisão objetiva — existe uma lista contra a qual comparar."),

        ("MOD-03-CON-07", "Teste adversarial",
         "Um teste que não pode falhar não é prova de nada.",
         "A pergunta a fazer sobre qualquer teste: o que precisaria estar errado no "
         "código para este teste ficar vermelho? Se a resposta for “nada relevante”, "
         "o teste mede apenas a própria existência.",
         "Quebre o código de propósito e confirme que o teste acusa. É a verificação "
         "mais rápida disponível e quase nunca é feita em código gerado.",
         NAO_PROJETAR + "É a razão de a estratégia de prova ser definida antes da "
         "implementação, no gate."),
    ]

    # conceito 1 tem forma própria: as cinco naturezas
    d.add("MOD-03-CON-01", "01 · Cinco naturezas de afirmação",
          head("MOD-03-CON-01 · Conceito 1 de 7", "Cinco naturezas de afirmação", COR)
          + tabela(["Natureza", "O que é"], [
              ("Fato", "Sustentado por fonte que qualquer pessoa consegue abrir"),
              ("Relato", "Alguém disse. Verdadeiro ou não, é testemunho, não observação"),
              ("Inferência", "Conclusão provável a partir do que se sabe"),
              ("Decisão", "Escolha que alguém com autoridade fez, ou precisa fazer"),
              ("Evidência", "O material concreto que sustenta um fato"),
          ])
          + callout("Nenhuma se transforma na outra por repetição. Um relato repetido "
                    "três vezes continua relato.")
          + foot("MOD-03-CON-01"),
          "O agente produz as cinco misturadas, no mesmo tom, sem sinalizar a "
          "transição. " + NAO_PROJETAR + "Corresponde à separação entre alegação, "
          "inferência, evidência declarada e confirmada; e ao princípio de que "
          "alegação não promove estado.")

    for pos, (cid, titulo, principio, pratica, exemplo, nota) in enumerate(conceitos, 2):
        posicao = f"Conceito {pos if pos < 6 else pos + 1} de {total}"
        d.add(cid, f"{cid.split('-')[-1]} · {titulo}",
              conceito(cid, posicao, titulo, principio, pratica, exemplo, COR)
              + foot("Fonte: course/topics/MOD-03.md"), nota)

    d.add("MOD-03-CON-06", "06 · Padrões típicos de erro do agente",
          head("MOD-03-CON-06 · Conceito 6 de 7",
               "Padrões típicos de erro do agente", COR)
          + '<p class="intro">Erros de agente não são aleatórios. Concentram-se em um '
            'conjunto pequeno e reconhecível — e conhecê-lo transforma revisão em '
            'busca dirigida.</p>'
          + tabela(["Padrão", "Como se manifesta", "Onde procurar"], [
              ("Teste que confirma a interpretação",
               "Passa porque foi escrito a partir do código, não do critério",
               "Teste que espelha a implementação linha a linha"),
              ("Tratamento de erro decorativo",
               "Captura a exceção, registra e segue como se nada tivesse acontecido",
               "Blocos de exceção que não alteram o fluxo"),
              ("Abstração prematura",
               "Cria camada ou utilitário para um caso único", "Arquivos novos não previstos"),
              ("Alteração fora do pedido",
               "Renomeia, reformata, “melhora” código vizinho",
               "Arquivos sem relação com o objetivo"),
              ("Confiança em API inexistente",
               "Usa método plausível de biblioteca que não o tem",
               "Chamadas não cobertas por teste executado"),
              ("Caso limite silencioso",
               "Lista vazia, nulo, concorrência e repetição não tratados",
               "Ausência de teste, não presença de erro"),
              ("Corrigir o sintoma",
               "Ajusta o ponto onde o erro aparece, não onde nasce",
               "Correção distante da causa apontada"),
          ])
          + foot("MOD-03-CON-06"),
          "Imprima esta tabela e deixe com os grupos durante a auditoria. É a "
          "ferramenta de trabalho da etapa 3.")

    d.add("DEMO", "Demonstração — teste verde, evidência parcial",
          demo("Teste verde, evidência parcial", [
              ("O caso", "5 min",
               "Um teste confirma a chamada ao serviço de notificação. O critério "
               "exige que o solicitante correto veja um aviso único após a aprovação."),
              ("A análise", "7 min",
               "O que o teste demonstra, o que não demonstra, e qual evidência "
               "adicional seria necessária."),
              ("Quebrar o código", "5 min",
               "Introduza dois defeitos: um que o teste acusa e outro que ele não acusa."),
              ("A matriz", "3 min",
               "Mostre uma matriz marcada como “coberto” e peça que alguém localize a "
               "prova."),
          ], [
              "que o veredito honesto aqui é “parcial”, e isso não é fracasso",
              "a diferença entre cobertura e prova, no momento do segundo defeito",
              "que uma matriz sem caminho confirmável é alegação, não sustentação",
          ], COR)
          + foot("MOD-03-DEMO"),
          "A demonstração do segundo defeito costuma ser o momento em que a turma "
          "entende a diferença entre cobertura e prova. Não apresse.")

    d.add("LAB", "Laboratório — abertura",
          '<div class="cover-body"><p class="eyebrow">Laboratório · 75 minutos</p>'
          '<h1>Auditoria cruzada</h1>'
          '<p class="lead">Cada grupo audita o resultado produzido por OUTRO grupo no '
          'encontro 2 — código, testes e especificação.<br>Auditar o trabalho alheio é '
          'deliberado: remove o viés de defender a própria condução.</p></div>',
          "Redistribua o material antes do intervalo. Garanta isolamento por grupo: a "
          "etapa 4 introduz defeitos reais no código.", classe="dark")

    d.add("LAB-1", "Etapa 1 — Classificar afirmações",
          etapa(1, "Classificar afirmações", "15 minutos", [
              "Percorra a análise produzida pelo agente.",
              "Marque cada afirmação relevante.",
          ], tabela_vazia(["Afirmação", "Natureza", "Endereço da evidência",
                           "Sustenta o que alega?"], 4))
          + foot("MOD-03-LAB · etapa 1"))

    d.add("LAB-2", "Etapa 2 — Confirmar o AS-IS",
          etapa(2, "Confirmar o comportamento atual", "15 minutos", [
              "Escolha as duas afirmações mais decisivas sobre o comportamento atual.",
              "Tente confirmá-las no código.",
              "Registre o resultado, inclusive quando a confirmação falhar.",
          ], callout("Buscas sem resultado são registradas com o alcance explícito: "
                     "termos, caminhos e revisão."))
          + foot("MOD-03-LAB · etapa 2"))

    d.add("LAB-3", "Etapa 3 — Revisar a diferença",
          etapa(3, "Revisar a diferença", "20 minutos", [
              "Sem ler o conteúdo ainda: liste os arquivos alterados e marque os que "
              "não têm motivo no objetivo declarado.",
              "Depois leia as alterações e preencha a tabela.",
          ], tabela_vazia(["Arquivo", "Motivo no escopo?", "Padrão de erro",
                           "Gravidade"], 4))
          + foot("MOD-03-LAB · etapa 3"),
          "Insista na ordem: lista de arquivos primeiro, conteúdo depois. Quem lê o "
          "conteúdo primeiro perde o sinal mais barato.")

    d.add("LAB-4", "Etapa 4 — Quebrar os testes",
          etapa(4, "Quebrar os testes", "20 minutos", [
              "Para cada teste gerado, introduza um defeito real que ele deveria acusar.",
              "Registre o que aconteceu.",
          ], tabela_vazia(["Teste", "Defeito introduzido", "Acusou?", "Conclusão"], 4)
             + callout("Testes que não acusam nenhum defeito relevante são reportados "
                       "como cobertura sem prova."))
          + foot("MOD-03-LAB · etapa 4"))

    d.add("LAB-5", "Etapa 5 — Devolver e discutir",
          etapa(5, "Devolver e discutir", "10 minutos", [
              "Cada grupo apresenta ao grupo auditado o achado mais relevante.",
              "O grupo auditado responde se concorda.",
              "Divergência é registrada, não resolvida à força.",
          ])
          + foot("MOD-03-LAB · etapa 5"),
          "Auditoria não é procurar culpado. Se o clima azedar, nomeie: o objetivo é "
          "calibrar confiança, e por isso cada grupo audita outro.")

    d.add("LAB-6", "Etapa 6 — Protocolo mínimo",
          etapa(6, "Protocolo mínimo do grupo", "20 minutos", [
              "Com base nos três encontros, escrevam uma página: os controles que "
              "vocês consideram indispensáveis para trabalhar com IA.",
          ], callout("No máximo doze controles · cada um como ação verificável, não "
                     "como intenção · cada um acompanhado do problema concreto, "
                     "observado nos encontros 1 a 3, que justifica sua existência · "
                     "controles sem problema observado são cortados.", "yellow"))
          + foot("MOD-03-LAB · etapa 6"),
          "Exemplo bom: “confirmar o comportamento atual no código antes de propor "
          "mudança”. Exemplo ruim: “ter cuidado com o AS-IS”. Recolha os protocolos e "
          "guarde intactos: voltam no encontro 5.")

    d.add("ENTREGA", "Entrega do encontro",
          head("Encontro 3 · Entrega", "Auditoria e protocolo mínimo", COR)
          + checklist([
              "Tabela de classificação das afirmações",
              "Resultado da confirmação do AS-IS, incluindo tentativas frustradas",
              "Revisão da diferença, com arquivos fora do escopo identificados",
              "Tabela de testes quebrados, com veredito de cobertura ou prova",
              "Parecer devolvido ao grupo auditado e divergências registradas",
              "PROTOCOLO MÍNIMO do grupo, com o problema observado por controle",
          ], COR)
          + callout("O protocolo mínimo é a entrega mais importante do Bloco I. "
                    "Ele volta no encontro 5.", "yellow")
          + foot("MOD-03-ENT"))

    d.add("EQUIVOCOS", "Equívocos a evitar",
          head("Encontro 3 · Fechamento", "Sete leituras erradas deste encontro", COR)
          + equivocos([
              ("Se os testes passam, está certo.",
               "Passar prova que o teste não falhou — e alguns testes não conseguem falhar."),
              ("Cobertura alta é qualidade.",
               "Cobertura mede linhas executadas, não comportamento demonstrado."),
              ("Revisar é ler tudo com atenção.",
               "É comparar contra o escopo declarado. Atenção sem referência cansa e não encontra."),
              ("O agente citou o arquivo, então confirmou.",
               "Citar é endereçar. Confirmar exige que o conteúdo demonstre a afirmação."),
              ("Toda inferência é problema.",
               "Inferência identificada é trabalho normal; disfarçada de fato é o problema."),
              ("Não achei, logo não existe.",
               "Prova apenas o alcance executado."),
              ("Auditoria é procurar culpado.",
               "É calibrar confiança. Por isso cada grupo audita outro."),
          ])
          + foot("MOD-03-EQUIVOCOS"))

    d.add("PONTE", "Próximo encontro",
          '<div class="cover-body"><p class="eyebrow">Fim do Bloco I · Encontro 4</p>'
          '<h1>Harness, permissões<br>e segurança</h1>'
          '<p class="lead">Três encontros sobre o que uma pessoa faz diante de um '
          'agente. O próximo trata do que o ambiente permite que aconteça — mesmo '
          'quando ninguém está prestando atenção.</p>'
          '<p class="divider-foot tone-cyan">Os protocolos mínimos ficam comigo. '
          'Voltam no encontro 5.</p></div>',
          "Não diga qual método será apresentado no encontro 5, nem que existe um. "
          "A comparação perde força se a turma souber que há resposta pronta.",
          classe="dark")

    return d
