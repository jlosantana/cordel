#!/usr/bin/env python3
"""Deck de aula do encontro 2 — Condução: da intenção à tarefa executável.

Fonte do conteúdo: course/topics/MOD-02.md.

Regra do Bloco I: o nível "No Cordel" dos conceitos NÃO vai para a tela.
Aparece apenas nas notas do apresentador, marcado como antecipação.
"""

from __future__ import annotations

from deck_theme import (Deck, callout, capa_encontro, checklist, conceito, demo,
                        equivocos, etapa, foot, frase_grande, head, lista_simples,
                        roteiro, statement, tabela, tabela_vazia)

COR = "cyan"
NAO_PROJETAR = "NÃO PROJETAR — antecipação para o instrutor. "


def build() -> Deck:
    d = Deck("Encontro 2", "Condução: da intenção à tarefa executável")

    d.add("CAPA", "Capa do encontro",
          capa_encontro("2", "I", "Condução: da intenção\nà tarefa executável",
                        "A maior parte do que se atribui à qualidade do modelo é, na "
                        "verdade, qualidade da tarefa que foi entregue a ele."),
          "Abra retomando a divergência medida ontem. A pergunta do dia: quanto "
          "daquilo era o modelo e quanto era a tarefa que entregamos a ele?",
          classe="dark")

    d.add("ROTEIRO", "Roteiro das 3 horas",
          head("Encontro 2 · Roteiro", "O que vamos fazer hoje", COR)
          + roteiro([
              ("0–10", "Retomada do diagnóstico do encontro 1"),
              ("10–35", "Decomposição e especificação de tarefa"),
              ("35–55", "Seleção de contexto, exemplos e contraexemplos"),
              ("55–70", "Refinar ou reiniciar; autonomia proporcional ao risco"),
              ("70–85", "Quando não usar IA"),
              ("85–100", "Demonstração das duas conduções"),
              ("100–110", "Intervalo"),
              ("110–125", "Laboratório: decompor"),
              ("125–145", "Especificar"),
              ("145–165", "Executar e decidir sobre reinício"),
              ("165–180", "Comparar, entregar e retrospectiva"),
          ])
          + foot("MOD-02-ROTEIRO"))

    d.add("OBJETIVOS", "Objetivos do encontro",
          head("Encontro 2 · Objetivos", "Ao final deste encontro você consegue", COR)
          + lista_simples([
              "Decompor uma demanda em tarefas com resultado observável.",
              "Escrever uma especificação com objetivo, restrições, fora do escopo e critério de pronto.",
              "Escolher deliberadamente o que entra no contexto — e justificar cada inclusão.",
              "Usar exemplos e contraexemplos para fixar formato e convenção.",
              "Decidir entre refinar a sessão atual e reiniciá-la.",
              "Calibrar autonomia conforme risco e reversibilidade.",
              "Reconhecer quando a decisão correta é não usar IA.",
          ], COR)
          + foot("MOD-02-OBJ · relaciona-se a OA-02, OA-03 e OA-04"))

    d.add("TESE", "Tese do encontro",
          statement("Uma tarefa mal delimitada não é salva por um modelo melhor.",
                    "MOD-02-TESE"),
          "Provocação útil: peça que levantem a mão quem já culpou o modelo por um "
          "resultado ruim. Depois pergunte o que estava escrito na solicitação.",
          classe="dark")

    d.add("ENQUADRAMENTO", "Não é sobre prompt",
          head("Encontro 2 · Enquadramento", "Isto não é sobre escrever prompts", COR)
          + frase_grende_pt()
          + callout("É a mesma competência exigida para delegar trabalho a uma pessoa "
                    "recém-chegada ao time — com uma diferença: essa pessoa pergunta "
                    "quando não entende, e o agente não.")
          + foot("MOD-02-INT"),
          "Se a turma esperava técnicas de redação de prompt, nomeie a diferença "
          "agora. Condução é delimitar trabalho; o texto é consequência.")

    total = 7
    conceitos = [
        ("MOD-02-CON-01", "Decomposição",
         "Uma demanda não é uma tarefa. Quebre até que cada parte tenha um resultado "
         "que você consegue observar ao final.",
         "Se você não sabe dizer como saberá que a parte terminou, ela ainda não é uma "
         "tarefa. Tarefas de investigação e de alteração não se misturam: a primeira "
         "produz informação, a segunda produz mudança.",
         "“Fazer o sistema avisar quando aprovar” contém pelo menos quatro tarefas — e "
         "o agente resolverá três por suposição para chegar à quarta.",
         NAO_PROJETAR + "A unidade de trabalho verificável, do encontro 6, é a forma "
         "documentada dessa decomposição."),

        ("MOD-02-CON-02", "Especificação de tarefa",
         "Quatro elementos tornam uma tarefa executável sem invenção: objetivo, "
         "restrições, fora do escopo e critério de pronto.",
         "O campo mais negligenciado é o fora do escopo, e é o que mais economiza "
         "revisão. O agente tende a “aproveitar e melhorar”: renomear, extrair função, "
         "ajustar formatação, corrigir um erro vizinho.",
         "Cada uma dessas iniciativas é plausível e nenhuma foi pedida. Declarar a "
         "fronteira custa uma linha.",
         NAO_PROJETAR + "Objetivo observável, escopo, fora do escopo e critérios de "
         "aceite são campos da story."),

        ("MOD-02-CON-03", "Seleção do contexto",
         "Contexto útil é pertinente e atual, não volumoso.",
         "Material irrelevante compete por espaço com o que importa e sugere caminhos "
         "falsos: um arquivo antigo incluído “por garantia” será tratado como se "
         "descrevesse o presente. Para cada item incluído, saiba dizer por que.",
         "Prefira apontar o caminho e deixar o agente ler a fonte a colar um trecho "
         "que pode estar desatualizado.",
         NAO_PROJETAR + "É a engenharia de contexto: um índice curto que aponta para "
         "fontes, com carregamento sob demanda."),

        ("MOD-02-CON-04", "Exemplos e contraexemplos",
         "Descrever um formato em palavras é caro e ambíguo. Mostrar um caso pronto é "
         "barato e preciso.",
         "Aponte um arquivo existente que já segue o padrão desejado, em vez de "
         "descrever o padrão. Para convenções abandonadas, mostre o caso antigo e diga "
         "explicitamente que ele não deve ser seguido.",
         "Sem esse aviso, o agente encontrará o arquivo antigo sozinho e o tratará "
         "como referência.",
         ""),

        ("MOD-02-CON-05", "Refinar ou reiniciar",
         "Quando uma sessão entra em caminho errado, corrigir por cima costuma sair "
         "pior que recomeçar.",
         "Refine quando o desvio é pontual. Reinicie quando o entendimento do problema "
         "está errado, quando a mesma correção já foi pedida duas vezes, ou quando as "
         "restrições iniciais começaram a ser esquecidas.",
         "O sintoma clássico: o agente conserta o que você apontou e reintroduz o "
         "problema anterior. Ao reiniciar, leve o que aprendeu — escrito, não de memória.",
         NAO_PROJETAR + "É a razão de a decisão e o critério viverem em arquivo: "
         "reiniciar a sessão não pode custar o conhecimento acumulado."),
    ]

    for pos, (cid, titulo, principio, pratica, exemplo, nota) in enumerate(conceitos, 1):
        d.add(cid, f"{cid.split('-')[-1]} · {titulo}",
              conceito(cid, f"Conceito {pos} de {total}", titulo, principio, pratica,
                       exemplo, COR) + foot("Fonte: course/topics/MOD-02.md"), nota)

    d.add("MOD-02-CON-06", "06 · Autonomia proporcional ao risco",
          head("MOD-02-CON-06 · Conceito 6 de 7", "Autonomia proporcional ao risco", COR)
          + '<p class="intro">Autonomia não é configuração da ferramenta. É escolha '
            'por tarefa, com base em custo do erro e reversibilidade.</p>'
          + tabela(["Nível", "Quando usar", "O que o agente faz"], [
              ("Consulta", "Dúvida, exploração, leitura", "Responde; nada é alterado"),
              ("Proposta", "Alteração de baixo risco", "Propõe a diferença; a pessoa aplica"),
              ("Execução com checkpoint", "Trabalho reversível, escopo definido",
               "Executa em passos, com revisão entre eles"),
              ("Execução contínua", "Tarefa mecânica, verificável por comando",
               "Executa e reporta ao final"),
          ])
          + callout("Ação irreversível ou externa não entra em nenhum nível sem "
                    "confirmação própria.")
          + foot("MOD-02-CON-06"),
          NAO_PROJETAR + "Esta escala vira a política de permissões e os checkpoints "
          "no encontro 4. Aqui ela é decisão de quem conduz, não do ambiente.")

    d.add("MOD-02-CON-07", "07 · Quando não usar IA",
          head("MOD-02-CON-07 · Conceito 7 de 7", "Quando não usar IA", COR)
          + '<p class="principio">A delegação compensa quando o custo de executar '
            'supera o custo de revisar. Quando se inverte, o agente vira despesa '
            'disfarçada de produtividade.</p>'
          + lista_simples([
              "A alteração é menor que o esforço de descrevê-la.",
              "Você não saberia reconhecer um resultado errado — e aceitar sem revisar não é opção.",
              "O código é crítico e revisar exigiria a mesma atenção de escrevê-lo.",
              "Os dados necessários não podem entrar no contexto por confidencialidade.",
              "A tarefa depende de julgamento que só a pessoa responsável pode exercer.",
          ], COR, numerada=False)
          + foot("MOD-02-CON-07"),
          "O último caso não é sobre capacidade técnica. Uma decisão de negócio "
          "delegada a um agente continua sem dono. O caso de confidencialidade volta "
          "com força no encontro 4.")

    d.add("DEMO", "Demonstração — duas conduções",
          demo("A mesma demanda, duas conduções", [
              ("Condução A", "5 min",
               "Repita a solicitação direta do encontro 1. Use a resposta preservada, "
               "não execute de novo."),
              ("Condução B", "15 min",
               "Construa em voz alta: decomposição, escolha da primeira tarefa, "
               "especificação, seleção de contexto, nível de autonomia, execução."),
              ("Comparação", "10 min",
               "As duas lado a lado. Quanto do ganho veio do modelo e quanto veio "
               "da tarefa?"),
          ], [
              "pelo menos uma suposição que a condução B eliminou",
              "pelo menos uma que ela NÃO eliminou — nem tudo é problema de condução",
              "quanto tempo a mais custou preparar, e se compensou",
          ], COR)
          + foot("MOD-02-DEMO"),
          "O segundo item de observação é o mais importante: parte das lacunas "
          "depende de fonte, acesso ou decisão. É a ponte para o encontro 3.")

    d.add("LAB", "Laboratório — abertura",
          '<div class="cover-body"><p class="eyebrow">Laboratório · 70 minutos</p>'
          '<h1>Refazer com condução deliberada</h1>'
          '<p class="lead">A mesma demanda do encontro 1. O agente pode ler e propor; '
          'alteração de arquivos apenas na etapa 3, e apenas na tarefa escolhida.</p>'
          '</div>',
          "Cada grupo precisa das próprias respostas do encontro 1 em mãos. Sem elas "
          "a etapa 5 não fecha.", classe="dark")

    d.add("LAB-1", "Etapa 1 — Decompor",
          etapa(1, "Decompor", "15 minutos", [
              "Quebre a demanda em tarefas com resultado observável.",
              "Classifique cada uma como investigação ou alteração.",
              "Escolha a primeira tarefa a executar e justifique a ordem.",
          ], callout("Se você não sabe como saberá que a tarefa terminou, ela ainda "
                     "não é uma tarefa."))
          + foot("MOD-02-LAB · etapa 1"),
          "Erro típico: decompor por camada técnica (banco, serviço, tela) em vez de "
          "por resultado observável. Aponte quando vir.")

    d.add("LAB-2", "Etapa 2 — Especificar",
          etapa(2, "Especificar", "20 minutos", [
              "Preencha a especificação da tarefa escolhida.",
          ], tabela_vazia(["Campo", "Conteúdo"], 6)
             + callout("Objetivo observável · restrições · fora do escopo · critério "
                       "de pronto · contexto incluído e por quê · nível de autonomia "
                       "e por quê"))
          + foot("MOD-02-LAB · etapa 2"),
          "Cobre o fora do escopo com itens plausíveis. “Não fazer mais nada” não "
          "protege: o campo precisa nomear o que um leitor razoável inferiria que "
          "faz parte.")

    d.add("LAB-3", "Etapa 3 — Executar",
          etapa(3, "Executar", "25 minutos", [
              "Acione o agente com a especificação.",
              "Registre cada intervenção necessária e sua causa.",
          ], tabela_vazia(["Intervenção", "Causa", "Era evitável na especificação?"], 4)
             + callout("Causas possíveis: lacuna de contexto · fronteira ausente · "
                       "decisão de negócio · limite do modelo"))
          + foot("MOD-02-LAB · etapa 3"),
          "A última coluna é o coração do exercício: separa o que a condução resolve "
          "do que exige fonte, decisão ou verificação. É o que o encontro 3 vai tratar.")

    d.add("LAB-4", "Etapa 4 — Refinar ou reiniciar",
          etapa(4, "Refinar ou reiniciar", "15 minutos", [
              "Ao surgir o primeiro desvio relevante, decida entre corrigir na sessão "
              "e recomeçar com o que aprendeu.",
              "Registre a decisão com a justificativa.",
              "Se houver tempo, compare o resultado das duas abordagens.",
          ])
          + foot("MOD-02-LAB · etapa 4"),
          "Se nenhum grupo tiver desvio relevante, provoque um: peça uma alteração "
          "adicional ambígua e observe o que acontece com as restrições iniciais.")

    d.add("LAB-5", "Etapa 5 — Comparar",
          etapa(5, "Comparar com o encontro 1", "15 minutos", [
              "O que a condução deliberada eliminou.",
              "O que ela não eliminou.",
              "Quanto tempo custou a mais, e se compensou.",
              "Em que ponto desta tarefa fazer à mão teria sido melhor.",
          ], callout("A lista do que ela NÃO eliminou é o insumo do encontro 3. "
                     "Guardem.", "yellow"))
          + foot("MOD-02-LAB · etapa 5"))

    d.add("ENTREGA", "Entrega do encontro",
          head("Encontro 2 · Entrega", "Especificação e comparação", COR)
          + checklist([
              "Decomposição da demanda em tarefas observáveis",
              "Especificação completa da tarefa executada",
              "Registro das intervenções, com causa e evitabilidade",
              "Decisão de refinar ou reiniciar, justificada",
              "Análise comparativa entre condução ingênua e deliberada",
              "Lista do que a condução não resolve",
              "Um caso em que não usar IA seria a decisão correta",
          ], COR)
          + foot("MOD-02-ENT"))

    d.add("EQUIVOCOS", "Equívocos a evitar",
          head("Encontro 2 · Fechamento", "Sete leituras erradas deste encontro", COR)
          + equivocos([
              ("Condução é escrever prompts melhores.",
               "É delimitar trabalho. O texto é consequência."),
              ("Especificar demais engessa o agente.",
               "Restrição reduz invenção, não capacidade."),
              ("Fora do escopo é óbvio.",
               "O que é óbvio para quem conhece o projeto é invisível para quem vê só o texto."),
              ("Reiniciar é desperdiçar o que já foi feito.",
               "Desperdício maior é arrastar um entendimento errado por mais dez interações."),
              ("Mais contexto sempre ajuda.",
               "Contexto irrelevante compete com o pertinente e sugere caminhos falsos."),
              ("Autonomia é configuração da ferramenta.",
               "É decisão por tarefa, baseada em risco e reversibilidade."),
              ("Se a condução foi boa, o resultado está certo.",
               "Condução reduz invenção; não substitui verificação. É o encontro seguinte."),
          ])
          + foot("MOD-02-EQUIVOCOS"))

    d.add("PONTE", "Próximo encontro",
          '<div class="cover-body"><p class="eyebrow">Encontro 3</p>'
          '<h1>Verificação:<br>o que a IA produziu merece crédito?</h1>'
          '<p class="lead">Hoje reduzimos a invenção do agente. No próximo encontro, '
          'vamos auditar o que ele produziu — e cada grupo vai revisar o trabalho de '
          'outro grupo.</p>'
          '<p class="divider-foot tone-cyan">Tragam o código, os testes e a '
          'especificação de hoje. Vão para as mãos de outra equipe.</p></div>',
          "Avise agora que o material será redistribuído. Isso muda o cuidado com que "
          "os grupos registram o que fizeram.", classe="dark")

    return d


def frase_grende_pt() -> str:
    return frase_grande(
        "É uma competência de engenharia: decompor trabalho, declarar fronteiras, "
        "escolher o que entra no contexto e decidir quanta autonomia a tarefa merece.",
        28)
