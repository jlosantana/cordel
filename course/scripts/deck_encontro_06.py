#!/usr/bin/env python3
"""Deck de aula do encontro 6 — Da demanda à unidade autorizada.

Fonte do conteúdo: course/topics/MOD-06.md.

Este encontro funde dois da versão anterior do curso. O cronograma é apertado:
o dossiê parcial de fontes existe para caber no tempo.
"""

from __future__ import annotations

from deck_theme import (Deck, callout, capa_encontro, checklist, conceito, demo,
                        equivocos, etapa, foot, frase_grande, head, lista_simples,
                        roteiro, statement, tabela, tabela_vazia)

COR = "yellow"


def build() -> Deck:
    d = Deck("Encontro 6", "Da demanda à unidade autorizada")

    d.add("CAPA", "Capa do encontro",
          capa_encontro("6", "II", "Da demanda\nà unidade autorizada",
                        "Antes de desenhar o que o sistema deve fazer, confirme por "
                        "que a demanda existe e o que o sistema faz hoje."),
          "Encontro que funde dois da versão anterior. Vigie o relógio: as etapas 5 e "
          "6 são as que mais estouram.",
          classe="dark divider-yellow")

    d.add("ROTEIRO", "Roteiro das 3 horas",
          head("Encontro 6 · Roteiro", "O que vamos fazer hoje", COR)
          + roteiro([
              ("0–10", "Retomada: da configuração para a cadeia"),
              ("10–30", "Origem, filtros de triagem e investigação"),
              ("30–45", "Evidência, busca negativa e promoção de descoberta"),
              ("45–60", "Decisão, objetivo observável, escopo e critérios"),
              ("60–75", "Estratégia de prova, impactos, spec e gate"),
              ("75–95", "Demonstração: quatro classificações e refinamento"),
              ("95–105", "Intervalo"),
              ("105–115", "Laboratório: preservar e reconciliar"),
              ("115–140", "Confirmar o AS-IS"),
              ("140–150", "Filtros e decisão simulada"),
              ("150–170", "Story, aceites, prova e gate"),
              ("170–180", "Revisão cruzada e entrega"),
          ])
          + foot("MOD-06-ROTEIRO"))

    d.add("OBJETIVOS", "Objetivos do encontro",
          head("Encontro 6 · Objetivos", "Ao final deste encontro você consegue", COR)
          + lista_simples([
              "Preservar origem, relato, ambiente e anexos.",
              "Classificar a demanda em defeito, lacuna documental, detalhamento ou escopo novo.",
              "Confirmar o AS-IS registrando evidências e buscas negativas com alcance.",
              "Distinguir necessidade de story autorizada.",
              "Registrar objetivo observável, escopo e fora do escopo.",
              "Formular critérios de aceite com estratégia de prova por critério.",
              "Avaliar impactos e decidir quando criar spec e ADR.",
              "Declarar o gate com pendências e próxima ação.",
          ], COR)
          + foot("MOD-06-OBJ · relaciona-se a OA-07, OA-08, OA-09 e OA-10"))

    d.add("TESE", "Tese do encontro",
          statement("Uma unidade está pronta quando o agente pode implementá-la sem "
                    "inventar uma decisão — e a equipe sabe, antes do código, como "
                    "observará o resultado.", "MOD-06-TESE"),
          classe="dark divider-yellow")

    d.add("CADEIA", "A cadeia mínima",
          head("Encontro 6 · Enquadramento", "A cadeia que vamos percorrer hoje", COR)
          + '<ol class="chain" style="grid-template-columns:repeat(5,1fr)">'
          + "".join(f'<li class="tone-yellow">{t}</li>' for t in
                    ["origem", "classificação", "AS-IS confirmado", "decisão humana",
                     "story / spec"])
          + "</ol>"
          + frase_grande("Cada elo evita uma substituição indevida.", 26)
          + tabela(["Elemento", "Não substitui"], [
              ("Necessidade", "Autorização"),
              ("Requisito", "Confirmação do comportamento atual"),
              ("Story", "Prova de implementação"),
              ("Spec", "Origem ou decisão de negócio"),
              ("Agente", "Responsável por decisão de produto"),
          ])
          + foot("Fonte: course/topics/CURSO-03.md · CURSO-03-CADEIA"),
          "Etapas simples podem ter poucos artefatos. O que não pode desaparecer é a "
          "distinção que cada elo protege.")

    conceitos = [
        ("MOD-06-CON-01", "Origem", "Conceito 1 de 10",
         "Pedido, documento, incidente, reunião ou decisão que explica por que a "
         "análise existe.",
         "A pergunta prática: se este trabalho for questionado daqui a três meses, o "
         "que eu mostro?",
         "Sem origem, não há como distinguir “alguém importante pediu” de “isto foi "
         "decidido”."),

        ("MOD-06-CON-03", "Investigação do geral ao específico", "Conceito 3 de 10",
         "Comece por drift de ambiente e contexto atual, delimite o sintoma, depois "
         "abra código, configuração, migrações, dados e testes nos pontos afetados.",
         "O erro típico, humano e do agente, é saltar para o primeiro arquivo cujo "
         "nome parece relacionado.",
         "É rápido e frequentemente leva ao lugar errado: o nome reflete a intenção de "
         "quem criou, não o comportamento atual."),

        ("MOD-06-CON-06", "Decisão antes da unidade", "Conceito 5 de 10",
         "Escopo novo precisa de responsável competente. A story preserva essa "
         "decisão; não a cria.",
         "Quando não há quem decida disponível, o estado correto é bloqueado.",
         "Fabricar a decisão para não travar o trabalho é a falha mais cara do método "
         "inteiro, porque produz um rastro que parece íntegro."),

        ("MOD-06-CON-07", "Objetivo observável", "Conceito 6 de 10",
         "Descreve resultado percebido, não atividade técnica.",
         "“Enviar um aviso único ao solicitante quando a aprovação for concluída” é "
         "observável. “Alterar o serviço X” é meio de solução.",
         "Objetivo escrito como atividade fecha a solução antes da análise e impede "
         "que o agente encontre um caminho melhor dentro do mesmo resultado."),

        ("MOD-06-CON-09", "Critérios de aceite", "Conceito 8 de 10",
         "Condições específicas e testáveis, cobrindo caminho principal, condições "
         "relevantes e restrições.",
         "Critério não é tarefa. “Implementar o envio” é tarefa; “o solicitante recebe "
         "exatamente um aviso por aprovação concluída” é critério.",
         "Sem antecipar detalhes técnicos que ainda não foram decididos."),

        ("MOD-06-CON-10", "Estratégia de prova", "Conceito 9 de 10",
         "Para cada critério: teste ou verificação, ambiente, dados e evidência "
         "esperada — planejados ANTES da implementação.",
         "É a resposta direta ao problema demonstrado no encontro 3: um teste escrito "
         "depois, a partir do código, tende a confirmar a implementação em vez do "
         "critério.",
         "Definir a prova antes remove esse grau de liberdade."),
    ]

    d.add("MOD-06-CON-02", "02 · Triagem em filtros",
          head("MOD-06-CON-02 · Conceito 2 de 10", "Triagem em filtros", COR)
          + '<p class="principio">Classifique nesta ordem. A ordem evita criar '
            'funcionalidade fictícia para algo que já existe, e evita tratar '
            'divergência de implementação como melhoria.</p>'
          + lista_simples([
              "É defeito? Há compromisso e o comportamento diverge dele.",
              "É lacuna documental? O comportamento existe, a documentação omite.",
              "É detalhamento de compromisso existente? O requisito cobre, falta precisar.",
              "É escopo novo? Nenhuma cobertura válida após busca delimitada.",
          ], COR)
          + callout("A mesma frase pode cair em qualquer um dos quatro. O que "
                    "determina não é o texto do pedido: é a relação entre origem, "
                    "compromisso existente e comportamento atual.")
          + foot("MOD-06-CON-02"))

    d.add("MOD-06-CON-04", "04 · Evidência e busca negativa",
          conceito("MOD-06-CON-04", "Conceito 4 de 10", "Evidência e busca negativa",
                   "Retomada do encontro 3, agora como registro obrigatório.",
                   "Toda busca negativa que sustente uma classificação precisa declarar "
                   "termos, caminhos e revisão. Uma classificação de “escopo novo” "
                   "apoiada em busca sem alcance declarado é rejeitada na revisão "
                   "cruzada.",
                   "“Não encontrei no alcance X” é mais preciso, e mais útil, que "
                   "“não existe”.", COR)
          + foot("MOD-06-CON-04"))

    d.add("MOD-06-CON-08", "08 · Escopo e fora do escopo",
          conceito("MOD-06-CON-08", "Conceito 7 de 10", "Escopo e fora do escopo",
                   "Escopo enumera resultados incluídos. Fora do escopo protege "
                   "fronteiras que poderiam ser inferidas.",
                   "É o mesmo campo praticado no encontro 2, agora com autorização "
                   "anexada. Ambos devem ser compatíveis com a decisão registrada.",
                   "Um fora do escopo genérico — “não fazer mais nada” — não protege. "
                   "Ele precisa nomear o que um leitor razoável inferiria que faz parte.",
                   COR) + foot("MOD-06-CON-08"))

    for cid, titulo, posicao, principio, pratica, exemplo in conceitos:
        d.add(cid, f"{cid.split('-')[-1]} · {titulo}",
              conceito(cid, posicao, titulo, principio, pratica, exemplo, COR)
              + foot("Fonte: course/topics/MOD-06.md"))

    d.add("MOD-06-CON-13", "13 · Gate com três resultados",
          head("MOD-06-CON-13 · Conceito 10 de 10", "Gate com três resultados", COR)
          + tabela(["Resultado", "Significado"], [
              ("BLOQUEADO", "Falta origem, evidência, autorização ou decisão"),
              ("PRONTO PARA ESPECIFICAR", "Trabalho válido, desenho incompleto"),
              ("PRONTO PARA IMPLEMENTAR", "Unidade verificável, sem decisão bloqueante"),
          ])
          + '<div class="pratica accent-yellow"><b>Na prática</b><p>O gate formaliza '
            'uma pergunta que qualquer pessoa deveria fazer antes de começar: sei o '
            'suficiente para agir, e outra pessoa concordaria com essa avaliação?</p>'
            '</div>'
          + callout("O valor está em ser revisável, não em ser um carimbo.")
          + foot("MOD-06-CON-13"),
          "Quando criar spec: alteração de contrato, dados existentes, estados, "
          "integração, segurança, concorrência, vários componentes ou decisão técnica "
          "relevante. Mudança simples exige critérios e prova, não documentação "
          "excessiva — o custo da cerimônia é real, como visto no encontro 5.")

    d.add("DEMO", "Demonstração — classificar e refinar",
          demo("Quatro classificações, uma frase", [
              ("As quatro variantes", "15 min",
               "“O sistema deve avisar quando aprovado” em quatro cenários: defeito, "
               "lacuna documental, detalhamento e escopo novo."),
              ("Refinar sem inventar", "15 min",
               "Com a decisão simulada em mãos: objetivo, escopo, três critérios, "
               "prova de cada um, impactos, spec ou não, gate."),
          ], [
              "que a frase não determina a classificação",
              "o momento em que surge uma dúvida de negócio — e o instrutor PARA e marca "
              "decisão pendente em vez de completar por plausibilidade",
          ], COR)
          + foot("MOD-06-DEMO"),
          "O segundo item é o momento mais didático da demonstração. Force-o mesmo que "
          "precise inventar a dúvida.")

    d.add("LAB", "Laboratório — abertura",
          '<div class="cover-body"><p class="eyebrow">Laboratório · 75 minutos</p>'
          '<h1>Da triagem ao gate</h1>'
          '<p class="lead">Cada grupo recebe a demanda, a origem preservada e um '
          'dossiê parcial de fontes já localizadas.</p>'
          '<p class="divider-foot tone-yellow">A busca completa não cabe no tempo. O '
          'objetivo é a classificação e a decisão.</p></div>',
          classe="dark divider-yellow")

    d.add("LAB-1", "Etapa 1 — Preservar e reconciliar",
          etapa(1, "Preservar e reconciliar", "10 minutos", [
              "Registrem origem, data, autor, ambiente, relato e anexos.",
              "Separem o que foi recebido da interpretação do grupo.",
              "Executem o comando de reconciliação de ambiente, ou registrem por que "
              "não está disponível.",
          ])
          + foot("MOD-06-LAB · etapa 1"))

    d.add("LAB-2", "Etapa 2 — Confirmar o AS-IS",
          etapa(2, "Confirmar o AS-IS", "25 minutos", [
              "Consultem o dossiê, o requisito integral e o contexto atual.",
              "Inspecionem código, configuração e testes nos pontos afetados.",
          ], tabela_vazia(["Afirmação", "Evidência ou busca negativa",
                           "Alcance declarado", "Sustenta?"], 4))
          + foot("MOD-06-LAB · etapa 2"))

    d.add("LAB-3", "Etapa 3 — Aplicar filtros",
          etapa(3, "Aplicar filtros", "15 minutos", [
              "Respondam, em ordem: é defeito? lacuna documental? compromisso "
              "existente? escopo novo?",
              "Uma resposta positiva precisa de sustentação na tabela anterior.",
          ])
          + foot("MOD-06-LAB · etapa 3"))

    d.add("LAB-4", "Etapa 4 — Decisão simulada",
          etapa(4, "Decisão simulada", "10 minutos", [
              "O responsável de produto recebe os fatos da triagem.",
              "Escolhe entre rejeitar, adiar, autorizar com limites ou pedir "
              "especificação adicional.",
              "A decisão fica registrada com autor e limites.",
          ], callout("Quem conduz o agente não pode ser quem decide o escopo.", "red"))
          + foot("MOD-06-LAB · etapa 4"))

    d.add("LAB-5", "Etapa 5 — Necessidade, story e prova",
          etapa(5, "Necessidade, story e prova", "25 minutos", [
              "Atualizem a necessidade e criem a story apenas para o escopo autorizado.",
              "Cada critério precisa de uma forma de prova.",
          ], tabela_vazia(["Critério", "Teste ou verificação", "Dados / ambiente",
                           "Evidência esperada"], 4))
          + foot("MOD-06-LAB · etapa 5"))

    d.add("LAB-6", "Etapa 6 — Impactos, spec e gate",
          etapa(6, "Impactos, spec e gate", "15 minutos", [
              "Percorram o checklist de impactos.",
              "Se alguma condição justificar desenho adicional, criem a spec.",
              "Revisem tudo e declarem uma das três saídas do gate.",
          ], callout("Um gate BLOQUEADO bem justificado vale mais que um PRONTO PARA "
                     "IMPLEMENTAR fabricado.", "yellow"))
          + foot("MOD-06-LAB · etapa 6"))

    d.add("ENTREGA", "Entrega do encontro",
          head("Encontro 6 · Entrega", "Triagem, unidade e gate", COR)
          + checklist([
              "Origem e relato preservados",
              "Escopo da investigação e fontes consultadas",
              "Afirmações, evidências e buscas negativas com alcance",
              "Resultado de cada filtro e classificação com grau de confiança",
              "Regra durável a promover ao AS-IS, quando houver",
              "Decisão humana registrada, com autor e limites",
              "Necessidade atualizada",
              "Story com objetivo observável, escopo e fora do escopo",
              "Critérios com estratégia de prova por critério",
              "Impactos, spec e ADR quando necessários",
              "Gate completo, com pendências e próxima ação",
          ], COR)
          + foot("MOD-06-ENT"))

    d.add("EQUIVOCOS", "Equívocos a evitar",
          head("Encontro 6 · Fechamento", "Leituras erradas deste encontro", COR)
          + equivocos([
              ("Se há relato de erro, é defeito.",
               "É preciso comportamento esperado e divergência."),
              ("Se existe código, está coberto.",
               "Código pode divergir do requisito ou estar inativo."),
              ("Busca sem resultado prova ausência.",
               "Prova apenas o alcance executado."),
              ("Escopo novo deve ser rejeitado.",
               "Deve ser registrado e levado à decisão competente."),
              ("Necessidade aprovada é story pronta.",
               "Ainda exige unidade verificável."),
              ("Critério é uma tarefa.",
               "Critério descreve comportamento ou restrição observável."),
              ("Spec é obrigatória para tudo.",
               "É proporcional a complexidade e risco."),
              ("Pronto significa que alguém vai começar.",
               "Significa ausência de decisão bloqueante."),
          ])
          + foot("MOD-06-EQUIVOCOS"))

    d.add("PONTE", "Próximo encontro",
          '<div class="cover-body"><p class="eyebrow">Fim do Bloco II · Encontro 7</p>'
          '<h1>Implementação<br>assistida e prova</h1>'
          '<p class="lead">O gate autoriza. No próximo encontro implementamos dentro '
          'dele, em checkpoints — e provamos o resultado.</p>'
          '<p class="divider-foot tone-yellow">Grupos com gate BLOQUEADO recebem uma '
          'story de referência para não perderem o encontro.</p></div>',
          "Tenha a story de referência pronta. Um grupo bloqueado honestamente não "
          "pode ser penalizado com a perda do encontro seguinte.",
          classe="dark divider-yellow")

    return d
