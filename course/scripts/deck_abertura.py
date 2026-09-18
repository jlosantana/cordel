#!/usr/bin/env python3
"""Deck de abertura — apresenta o curso: estrutura, objetivos, avaliação.

Usado nos primeiros minutos do encontro 1 e como material de apresentação do
treinamento. Não é material de aula: o conteúdo de cada encontro está nos decks
`encontro-01` a `encontro-08`.

Fonte do conteúdo: course/ementa.md.
"""

from __future__ import annotations

from deck_theme import BLOCOS, Deck, callout, card, e, foot, head, tabela

PERGUNTAS = [
    ("PROB-01", "Origem", "Qual necessidade deu origem à mudança?"),
    ("PROB-02", "Natureza", "O que é fato, relato, inferência ou decisão?"),
    ("PROB-03", "AS-IS", "O que o sistema realmente faz hoje?"),
    ("PROB-04", "Autoridade", "Quem autorizou a mudança de escopo?"),
    ("PROB-05", "Observação", "Como o resultado esperado será observado?"),
    ("PROB-06", "Prova", "Qual evidência sustenta a conclusão?"),
    ("PROB-07", "Concordância", "Como fontes, código e testes voltam a concordar?"),
]

IDENTIFICACAO = [
    ("Carga horária", "24 horas, em 8 encontros de 3 horas."),
    ("Formato", "Prático, presencial ou remoto: exposição curta, demonstração, "
                "laboratório e retrospectiva."),
    ("Público-alvo", "Desenvolvimento, liderança técnica, arquitetura, qualidade "
                     "e produto."),
    ("Pré-requisitos", "Desenvolvimento, Git, leitura de código e testes. IA em "
                       "profundidade não é necessária."),
    ("Projeto-laboratório", "Aplicação pequena, versionada e executável, com "
                            "demandas deliberadamente incompletas."),
    ("Ferramenta", "O Cordel entra no 5º encontro. Os quatro primeiros usam "
                   "qualquer agente, sem método instalado."),
]

OBJETIVOS_A = [
    ("OA-01", "Mecânica", "Explicar como um agente transforma uma solicitação em "
                          "ação, e por que o resultado não é determinístico."),
    ("OA-02", "Limites", "Reconhecer onde a IA gera ganho real e quando a decisão "
                         "correta é não usá-la."),
    ("OA-03", "Condução", "Decompor a demanda, declarar objetivo, restrições e "
                          "critério de pronto."),
    ("OA-04", "Autonomia", "Calibrar autonomia e permissões conforme risco e "
                           "reversibilidade (Cordel: harness)."),
    ("OA-05", "Epistemologia", "Separar fato, relato, inferência, decisão e evidência."),
    ("OA-06", "Verificação", "Revisar diferenças contra o escopo e projetar um teste "
                             "capaz de falhar (Cordel: estratégia de prova)."),
]

OBJETIVOS_B = [
    ("OA-07", "AS-IS", "Confirmar o comportamento atual em fonte inspecionável antes "
                       "de propor a mudança."),
    ("OA-08", "Origem", "Localizar a origem da demanda e distinguir necessidade de "
                        "autorização."),
    ("OA-09", "Unidade", "Transformar o pedido em unidade verificável, com critérios "
                         "que tenham forma de prova."),
    ("OA-10", "Autorização", "Decidir e registrar, de modo contestável, se há "
                             "informação suficiente para autorizar."),
    ("OA-11", "Segurança", "Reconhecer instrução hostil em conteúdo lido e exposição "
                           "de dados e credenciais."),
    ("OA-12", "Transferência", "Reconciliar fontes e levar os controles ao próprio "
                               "time, com ou sem a ferramenta do curso."),
]

CADEIA = [
    ("pedido incompleto", "cyan"), ("condução deliberada", "cyan"),
    ("auditoria", "cyan"), ("protocolo mínimo", "cyan"),
    ("ambiente", "yellow"), ("método", "yellow"), ("decisão", "yellow"),
    ("prova", "red"), ("transferência", "red"),
]

CICLO = [
    ("MET-01", "Conceitos", "45 min", "Vocabulário e critérios para o problema do dia."),
    ("MET-02", "Demonstração", "30 min", "O instrutor trabalha em voz alta, com incertezas visíveis."),
    ("MET-03", "Laboratório", "90 min", "Duplas ou trios, papéis rotativos, decisão do grupo."),
    ("MET-04", "Retrospectiva", "15 min", "Decisão, evidência, erro evitado e incerteza restante."),
]

RISCOS_A = [
    ("RC-01", "Pesquisa rápida", "Fonte errada ou antiga",
     "Declarar autoridade por fonte e exigir evidência endereçável",
     "A fonte canônica também pode errar"),
    ("RC-02", "Compreensão de legado", "Lacunas preenchidas por suposição",
     "Confirmar o comportamento atual em fonte inspecionável",
     "Busca negativa não prova ausência"),
    ("RC-03", "Geração de código", "Problema errado implementado depressa",
     "Decisão humana e unidade verificável antes do código",
     "Gate ruim formaliza premissa ruim"),
    ("RC-04", "Detalhamento", "Solução tratada como autorização",
     "Distinguir necessidade, requisito, unidade e detalhamento",
     "Ambiguidade exige decisão humana"),
    ("RC-05", "Geração de testes", "Teste confirma o próprio agente",
     "Projetar a prova antes do código e garantir que possa falhar",
     "Oráculos exigem julgamento"),
    ("RC-06", "Documentação", "Propagação de informação falsa",
     "Fonte única por fato e projeções regeneradas",
     "Conhecimento envelhece sem responsável"),
    ("RC-07", "Integrações", "Ação externa sem autoridade",
     "Permissão mínima por etapa e confirmação para operação mutável",
     "Depende da configuração do harness"),
]

RISCOS_B = [
    ("RC-08", "Procedimentos reutilizáveis", "Skill obsoleta ou específica demais",
     "Separar julgamento de execução determinística e versionar",
     "Skills exigem avaliação e manutenção"),
    ("RC-09", "Autonomia", "Deriva de objetivo e automação de erro",
     "Passos observáveis e interrupção no escopo novo",
     "Agentes seguem não determinísticos"),
    ("RC-10", "Síntese de status", "Artefato tratado como prova",
     "Promover estado só com evidência acessível e pertinente",
     "Evidência pode envelhecer"),
    ("RC-11", "Produção em volume", "A revisão passa a confirmar aparência",
     "Revisar a diferença contra o escopo, em passos pequenos",
     "Revisão cansa; lotes grandes derrotam o revisor"),
    ("RC-12", "Leitura de conteúdo externo", "Instrução hostil no que o agente lê",
     "Tratar conteúdo lido como dado e reduzir o alcance da ação",
     "Recusa observada uma vez não é garantia"),
    ("RC-13", "Uso de dados reais", "Exposição de dados e credenciais",
     "Definir antes o que não entra no contexto, com alternativa",
     "Exposição é irreversível; rotacionar credencial"),
]

MODULOS = [
    ("01", "I", "Como um agente funciona e por que erra",
     ["O que o modelo enxerga do problema · janela de contexto · corte de conhecimento",
      "Não determinismo · custo e latência · produtividade local versus resultado do sistema",
      "Plausibilidade não é evidência · o duplo efeito da aceleração · as sete perguntas"],
     ["Responder a uma demanda ambígua sem método e sem preparo.",
      "Executar a mesma solicitação três vezes e medir a divergência.",
      "Auditar as premissas de uma das respostas."],
     ["Diagnóstico com benefícios, riscos e perguntas ausentes.",
      "Tabela de divergência entre execuções.",
      "Ação que o grupo considera autorizada agora."],
     "Pergunta de fechamento do laboratório: qual das três respostas você teria "
     "implementado se tivesse executado apenas uma vez?"),

    ("02", "I", "Condução: da intenção à tarefa executável",
     ["Decomposição · especificação de tarefa: objetivo, restrições, fora do escopo, critério de pronto",
      "Seleção de contexto · exemplos e contraexemplos · refinar ou reiniciar a sessão",
      "Autonomia proporcional ao risco · quando não usar IA"],
     ["Refazer a demanda do encontro 1 com condução deliberada.",
      "Registrar cada intervenção, sua causa e se era evitável."],
     ["Especificação da tarefa e comparação com a condução ingênua.",
      "Um caso concreto em que não usar IA seria melhor."],
     "O campo mais negligenciado é o fora do escopo, e é o que mais economiza "
     "revisão. Insista nele."),

    ("03", "I", "Verificação: o que a IA produziu merece crédito?",
     ["Fato, relato, inferência, decisão e evidência · confirmar o comportamento atual",
      "Evidência pertinente · busca negativa · leitura da diferença contra o escopo",
      "Padrões típicos de erro do agente · teste adversarial: este teste consegue falhar?"],
     ["Auditar o trabalho de OUTRO grupo: classificar e revisar a diferença.",
      "Introduzir defeitos reais e verificar se os testes acusam."],
     ["Relatório de auditoria com o que foi alterado fora do escopo.",
      "PROTOCOLO MÍNIMO: até doze controles, cada um com o problema que o justifica."],
     "Entrega mais importante do Bloco I. Recolha os protocolos e devolva intactos "
     "no encontro 5."),

    ("04", "II", "Harness, permissões e segurança",
     ["Modelo, agente, ferramenta, skill, script, MCP e harness · engenharia de contexto",
      "Permissões e guardrails · observabilidade e evals · risco residual",
      "Instrução hostil em conteúdo lido · dados que não podem entrar no contexto"],
     ["Desenhar o harness: inventário, fluxo e política de operações e dados.",
      "Cenário adversarial: instrução hostil plantada em um arquivo do projeto."],
     ["Mapa do ambiente e política mínima de permissões.",
      "Lista de dados vedados ao contexto e o que o adversarial mudou nela."],
     "Ambiente isolado, sem rede nem escrita externa. Alinhe o cenário adversarial "
     "com a área de segurança do cliente antes de executá-lo."),

    ("05", "II", "Cordel como implementação do protocolo",
     ["Confronto entre o protocolo mínimo e o método · manifesto · fonte da verdade",
      "Artefato e projeção · tipos de trabalho · ciclo de vida documental",
      "Núcleo portátil e adaptador do projeto · o que o método NÃO resolve"],
     ["Mapear cada controle do próprio protocolo contra as peças do Cordel.",
      "Inicializar, preencher o adaptador, organizar o índice e obter GO."],
     ["Adaptador versionável e inventário de fontes.",
      "Protocolo anotado: o que a ferramenta cobre e o que segue humano."],
     "Conduza a comparação em três categorias: o que a turma identificou e o método "
     "implementa; o que ela não identificou; o que o método resolve de forma "
     "diferente. Não defenda o método."),

    ("06", "II", "Da demanda à unidade autorizada",
     ["Origem · filtros de triagem · investigação · busca negativa · promoção de descoberta",
      "Decisão antes da unidade · objetivo observável · escopo e fora do escopo · critérios",
      "Estratégia de prova · impactos · quando criar spec · gate com três resultados"],
     ["Confirmar o AS-IS a partir de um dossiê parcial e aplicar os filtros.",
      "Simular a decisão de produto e preparar a unidade, com prova por critério."],
     ["Triagem, AS-IS confirmado e unidade rastreável.",
      "Gate: BLOQUEADO, PRONTO PARA ESPECIFICAR ou PRONTO PARA IMPLEMENTAR."],
     "Funde dois encontros da versão anterior. O dossiê parcial existe para caber no "
     "tempo — calibre: entregar demais esvazia a investigação."),

    ("07", "III", "Implementação assistida e prova",
     ["Contexto de execução · plano incremental e checkpoints · escopo emergente",
      "Evidência suficiente · vereditos · implementado versus verificado · reconciliação",
      "Revisão independente · articulação com branch, pull request e CI"],
     ["Implementar em checkpoints e separar uma mudança de escopo surpresa.",
      "Executar a prova, revisar o dossiê de outro grupo e reconciliar."],
     ["Alteração funcional, dossiê de evidências e contexto reconciliado.",
      "Decisão justificada entre implementado e verificado."],
     "Encontro mais apertado do curso. Se a implementação atrasar, a revisão entre "
     "grupos vira leitura cruzada de dossiês — mas não corte: é onde a diferença "
     "entre implementado e verificado aparece."),

    ("08", "III", "Transferência e evolução",
     ["Núcleo portátil e adaptador · conhecimento federado · sinais de evolução",
      "Hipótese e forma de refutação · evals · versionamento · adoção incremental",
      "Tradução dos controles para as ferramentas do time · o que não se transfere"],
     ["Propor uma melhoria avaliável, classificada como local ou portátil.",
      "TESTE DE TRANSFERÊNCIA, individual: traduzir cada controle para o seu time."],
     ["Proposta com hipótese e forma de refutação; plano de 30 dias.",
      "Três controles prioritários e o problema que cada um resolve."],
     "O teste de transferência contém informação sobre o time de origem de cada "
     "pessoa. Em turma fechada de cliente, o padrão é que fique com quem escreveu."),
]

LABORATORIO = [
    ("Aplicação", "Dois ou três componentes executáveis."),
    ("Contradição", "Código que contradiz a alegação inicial."),
    ("Dados", "Integração ou persistência simples."),
    ("Identidade", "Identificadores controlados, que ninguém pode inventar."),
    ("Testes", "Suíte parcialmente útil, mas imperfeita."),
    ("Projeção", "Visão gerada divergente da fonte."),
    ("AS-IS", "Documentação com lacuna intencional."),
    ("Surpresa", "Drift ou mudança de escopo durante a implementação."),
    ("Origem", "Requisito válido e decisão histórica."),
    ("Adversário", "Instrução hostil plantada, contida, para o encontro 4."),
    ("Ambiguidade", "Demanda que parece defeito e revela escopo novo."),
    ("Confidencialidade", "Dados fictícios em tudo; nenhuma credencial real."),
]

ARTEFATOS = [
    ("01 · Diagnóstico", "Uso ingênuo de IA e divergência entre execuções."),
    ("06 · Configuração", "project.json, índice e protocolo anotado."),
    ("02 · Condução", "Especificação de tarefa e análise comparativa."),
    ("07 · Unidade e gate", "Triagem, AS-IS, story, spec e veredito."),
    ("03 · Auditoria", "Revisão da produção do agente e testes quebrados."),
    ("08 · Código", "Implementação, testes e diferenças revisadas."),
    ("04 · Protocolo mínimo", "Controles indispensáveis, escritos pelo grupo."),
    ("09 · Prova", "Relação critério-evidência e contexto reconciliado."),
    ("05 · Harness", "Mapa, permissões e dados vedados ao contexto."),
    ("10 · Transferência", "Retrospectiva, plano de adoção e três controles."),
]

AVALIACAO = [
    ("20%", "Condução do agente",
     "Tarefa decomposta, fronteiras declaradas, autonomia proporcional."),
    ("20%", "Verificação do que a IA produziu",
     "Diferenças revisadas, afirmações classificadas, testes capazes de falhar."),
    ("15%", "Rastreabilidade da decisão",
     "Origem, AS-IS confirmado, autorização explícita e bloqueios honestos."),
    ("15%", "Implementação e qualidade técnica",
     "Mudança coerente, testes proporcionais, sem escopo não autorizado."),
    ("15%", "Segurança e limites de operação",
     "Permissões mínimas, dados sensíveis fora do contexto, reação ao adversarial."),
    ("15%", "Transferência para o próprio contexto",
     "Controles enunciados sem o vocabulário do Cordel, adaptados ao time real."),
]

CONCLUSAO = [
    ("Participação", "Participar das decisões e revisões."),
    ("Cadeia", "Entregar o rastro até o fechamento, mesmo parcial ou bloqueado."),
    ("Demonstração", "Explicar ganho, risco e o controle que mudou uma decisão."),
    ("Independência", "Responder às sete perguntas sem o vocabulário do Cordel."),
    ("Continuidade", "Propor adoção preservando núcleo e adaptador."),
    ("Indicador do Bloco I",
     "Quantos controles cada grupo identificou sozinho antes do encontro 5."),
]


# ---------------------------------------------------------------- montagem

def build() -> Deck:
    d = Deck("Abertura", "Engenharia de software com agentes de IA")

    d.add("CAPA", "Capa", """
      <div class="cover-body">
        <p class="eyebrow">Curso · 24 horas · 8 encontros</p>
        <h1>Engenharia de software<br>com agentes de IA</h1>
        <p class="lead">Contexto, decisão e evidência.<br>Aplicando o método Cordel.</p>
        <ul class="chips">
          <li class="tone-cyan">3 blocos</li>
          <li class="tone-yellow">1 projeto-laboratório</li>
          <li class="tone-red">princípio antes da ferramenta</li>
        </ul>
      </div>""",
          "Deck gerado por course/scripts/build_deck.py a partir de course/ementa.md. "
          "Não edite o HTML à mão.", classe="dark")

    perguntas = "".join(
        f'<li><span class="tag">{e(rot)} · {e(pid)}</span>'
        f'<span class="txt">{e(txt)}</span></li>'
        for pid, rot, txt in PERGUNTAS)
    d.add("CURSO-03", "Problema orientador",
          head("CURSO-03 · Problema orientador",
                    "As sete perguntas que o curso responde") + f"""
      <p class="intro">A IA reduz o custo de pesquisar, planejar, escrever e testar.
      O mesmo ganho reduz o intervalo entre uma premissa errada e uma alteração concreta.</p>
      <ul class="qgrid">{perguntas}</ul>
      {callout("O Cordel é uma resposta possível a essas perguntas — não a única. "
                    "Quem conclui o curso deve saber respondê-las em um time que não o use.")}
      """ + foot("Detalhe: course/topics/CURSO-03.md"),
          "Estas sete perguntas são o currículo real. Volte a elas ao abrir cada "
          "encontro. No MOD-01 elas são usadas SEM nomear o Cordel.")

    colunas = ""
    dados_blocos = [
        ("I", "Encontros 1 a 3", "Como se trabalha com um agente sem se enganar?",
         ["Como o agente funciona e por que erra", "Condução da tarefa",
          "Verificação do que a IA produziu"]),
        ("II", "Encontros 4 a 6", "Como transformar isso em prática de time?",
         ["Harness, permissões e segurança", "Cordel como implementação",
          "Da demanda à unidade autorizada"]),
        ("III", "Encontros 7 e 8", "Como provar o resultado e levar ao meu time?",
         ["Implementação assistida e prova", "Transferência e evolução"]),
    ]
    for chave, encontros, pergunta, itens in dados_blocos:
        rotulo, cor, ferramenta = BLOCOS[chave]
        lis = "".join(f"<li>{e(i)}</li>" for i in itens)
        colunas += f"""
        <article class="block accent-{cor}">
          <p class="block-name">{e(rotulo)}</p>
          <p class="block-when">{e(encontros)}</p>
          <h3>{e(pergunta)}</h3>
          <ul>{lis}</ul>
          <p class="block-tool">{e(ferramenta)}</p>
        </article>"""
    d.add("BLO-00", "Os três blocos",
          head("BLO-00 · Estrutura", "Três blocos, três perguntas") + f"""
      <div class="blocks">{colunas}</div>
      {callout("A entrega que liga os blocos é o protocolo mínimo: uma página "
                    "escrita por cada grupo no encontro 3, confrontada com o Cordel "
                    "no encontro 5.")}
      """ + foot("Detalhe: course/topics/CURSO-05.md"),
          "O Cordel só entra no encontro 5. Não antecipe: a partir do momento em que a "
          "turma sabe que existe resposta pronta, para de construir a sua.")

    cards = "".join(
        card(rot, [txt], "cyan" if pos % 2 == 0 else "blue")
        for pos, (rot, txt) in enumerate(IDENTIFICACAO))
    d.add("CURSO-01", "O curso em uma página",
          head("CURSO-01 · Identificação", "O curso em uma página")
          + f'<div class="grid-3">{cards}</div>'
          + foot("Detalhe: course/ementa.md"))

    for faixa, objetivos, cor in [("1 de 2", OBJETIVOS_A, "cyan"),
                                  ("2 de 2", OBJETIVOS_B, "blue")]:
        linhas = "".join(
            f'<li><span class="oid tone-{cor}">{e(oid)}</span>'
            f'<span class="obody"><b>{e(rot)}</b>{e(txt)}</span></li>'
            for oid, rot, txt in objetivos)
        d.add(f"CURSO-04-{faixa[0]}", f"Objetivos {faixa}",
              head(f"CURSO-04 · Objetivos de aprendizagem {faixa}",
                        "Competência primeiro, ferramenta depois", cor) + f"""
          <p class="intro">Cada objetivo é independente de ferramenta. Onde o Cordel
          oferece uma implementação direta, ela aparece entre parênteses.</p>
          <ul class="olist accent-{cor}">{linhas}</ul>
          """ + foot("Detalhe: course/topics/CURSO-04.md"))

    passos = "".join(f'<li class="tone-{cor}">{e(t)}</li>' for t, cor in CADEIA)
    ciclo = "".join(
        f'<article class="card accent-blue"><h3>{e(rot)} · {e(tempo)}</h3>'
        f'<p>{e(txt)}</p><p class="mid">{e(mid)}</p></article>'
        for mid, rot, tempo, txt in CICLO)
    d.add("CURSO-05", "Metodologia",
          head("CURSO-05 · Metodologia", "Uma demanda atravessa os 8 encontros")
          + f"""
      <ol class="chain">{passos}</ol>
      <div class="grid-4">{ciclo}</div>
      <div class="callout tone-yellow big">
        <b>Princípio antes da ferramenta</b>
        Nos três primeiros encontros a turma trabalha sem método instalado e escreve o
        próprio protocolo mínimo. Antecipar o Cordel destrói o mecanismo pedagógico:
        a turma para de construir a própria resposta.
      </div>
      """ + foot("Detalhe: course/topics/CURSO-05.md"),
          "Indicador de que a ordem funcionou: quantos controles cada grupo identificou "
          "sozinho antes do encontro 5. Registre por turma.")

    for faixa, linhas, cor in [("1 de 2", RISCOS_A, "cyan"),
                               ("2 de 2", RISCOS_B, "red")]:
        d.add(f"CURSO-06-{faixa[0]}", f"Riscos {faixa}",
              head(f"CURSO-06 · Riscos e controles {faixa}",
                        "O controle vem primeiro; a ferramenta, depois", cor)
              + tabela(["ID", "Ganho da IA", "Risco introduzido",
                             "Controle ensinado", "Risco residual"], linhas, "riscos")
              + foot("Detalhe: course/topics/CURSO-06.md · catálogo completo "
                          "RC-01 a RC-13"))

    divisores = {
        "I": ("Fundamentos",
              "Como se trabalha com um agente sem se enganar?<br>"
              "Nenhum método instalado. A turma constrói o próprio protocolo."),
        "II": ("Controle e método",
               "Como transformar esses controles em prática repetível de time?<br>"
               "O ambiente primeiro; o Cordel a partir do encontro 5."),
        "III": ("Prova e transferência",
                "Como provar o resultado e levar isso para o meu time?<br>"
                "A pergunta que decide se o curso valeu."),
    }
    encontros_bloco = {"I": "Encontros 1 a 3", "II": "Encontros 4 a 6",
                       "III": "Encontros 7 e 8"}
    bloco_atual = None
    for num, chave, titulo, conceitos, pratica, entrega, nota in MODULOS:
        if chave != bloco_atual:
            bloco_atual = chave
            rotulo, cor, ferramenta = BLOCOS[chave]
            nome, sub = divisores[chave]
            d.add(f"BLOCO-{chave}", f"▸ {rotulo}", f"""
          <div class="cover-body">
            <p class="eyebrow">{e(rotulo)}</p>
            <h1>{e(nome)}</h1>
            <p class="lead">{sub}</p>
            <p class="divider-foot tone-{cor}">{e(encontros_bloco[chave])} · {e(ferramenta)}</p>
          </div>""", classe=f"dark divider-{cor}")

        rotulo, cor, _ = BLOCOS[chave]
        d.add(f"MOD-{num}", f"MOD-{num} · {titulo}",
              head(f"MOD-{num} · Encontro {int(num)} · {rotulo}", titulo, cor)
              + card("Conceitos", conceitos, cor)
              + '<div class="grid-2">'
              + card("Prática", pratica, "blue")
              + card("Entrega", entrega, "cyan")
              + "</div>"
              + foot(f"Detalhe: course/topics/MOD-{num}.md"), nota)

    d.add("LAB-00", "Projeto-laboratório",
          head("LAB-00 · Projeto-laboratório",
                    "Pequeno para caber no curso, real para conter decisões")
          + '<ul class="dgrid">' + "".join(
              f'<li class="tone-cyan"><b>{e(rot)}</b>{e(txt)}</li>'
              for rot, txt in LABORATORIO) + "</ul>"
          + foot("Detalhe: course/ementa.md"))

    d.add("ART-00", "Artefatos da turma",
          head("ART-00 · Artefatos da turma",
                    "O rastro que a turma produz nos oito encontros", "blue")
          + '<ul class="dgrid">' + "".join(
              f'<li class="tone-blue"><b>{e(rot)}</b>{e(txt)}</li>'
              for rot, txt in ARTEFATOS) + "</ul>"
          + foot("Detalhe: course/ementa.md"))

    d.add("AVA-00", "Avaliação",
          head("AVA-00 · Avaliação", "Avalia-se o rastro, não o volume de código")
          + '<p class="intro">As dimensões são independentes de ferramenta. Os '
            'artefatos do Cordel entram como evidência, não como critério.</p>'
          + tabela(["Peso", "Dimensão", "Evidência esperada"], AVALIACAO, "aval")
          + callout("Reproduzir o procedimento do Cordel sem saber explicar qual "
                         "risco ele mitiga não caracteriza domínio. Manter o gate "
                         "BLOQUEADO quando faltam condições reais, sim.", "yellow")
          + foot("Detalhe: course/topics/CURSO-04.md"))

    d.add("CON-00", "Conclusão e evolução",
          head("CON-00 · Conclusão e evolução",
                    "O que fecha o curso — e o que fecha a próxima turma", "yellow")
          + '<p class="intro">A conclusão é individual; o indicador do Bloco I mede o '
            'desenho do curso, não a turma.</p>'
          + '<ul class="dgrid one">' + "".join(
              f'<li class="tone-yellow"><b>{e(rot)}</b>{e(txt)}</li>'
              for rot, txt in CONCLUSAO) + "</ul>"
          + foot("Detalhe: course/ementa.md · course/topics/CURSO-05.md"))

    d.add("FIM", "Fechamento", """
      <div class="cover-body">
        <p class="eyebrow">Fechamento</p>
        <h1>O que você leva<br>para o seu time</h1>
        <p class="lead">Três controles, na ferramenta que o time já usa, cada um ligado
        a um problema concreto que você viu acontecer neste curso.</p>
        <p class="divider-foot tone-red">Se o método precisar ser trocado, os controles
        continuam valendo. É isso que torna o aprendizado portátil.</p>
      </div>""",
          "Encerre com o teste de transferência do MOD-08, não com um resumo do Cordel.",
          classe="dark divider-red")

    return d
