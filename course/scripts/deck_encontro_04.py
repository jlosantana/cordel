#!/usr/bin/env python3
"""Deck de aula do encontro 4 — Harness, permissões e segurança.

Fonte do conteúdo: course/topics/MOD-04.md.

Abre o Bloco II. O Cordel ainda não entra: aqui se desenha o ambiente, e o
método aparece no encontro 5. Para público de setor regulado, este é o
encontro mais crítico do curso.
"""

from __future__ import annotations

from deck_theme import (Deck, callout, capa_encontro, checklist, conceito, demo,
                        equivocos, etapa, foot, frase_grande, head, lista_simples,
                        roteiro, statement, tabela, tabela_vazia)

COR = "yellow"
NAO_PROJETAR = "NÃO PROJETAR — antecipação para o instrutor. "


def build() -> Deck:
    d = Deck("Encontro 4", "Harness, permissões e segurança")

    d.add("CAPA", "Capa do encontro",
          capa_encontro("4", "II", "Harness, permissões\ne segurança",
                        "Capacidade não é autorização. Um bom ambiente torna a ação "
                        "correta fácil de executar e a ação perigosa difícil por "
                        "acidente."),
          "Abre o Bloco II. Deslocamos o foco do que uma pessoa faz para o que o "
          "ambiente permite que aconteça quando ninguém está olhando.",
          classe="dark divider-yellow")

    d.add("ROTEIRO", "Roteiro das 3 horas",
          head("Encontro 4 · Roteiro", "O que vamos fazer hoje", COR)
          + roteiro([
              ("0–10", "Retomada: do operador para o ambiente"),
              ("10–40", "Modelo, agente, ferramentas, skill, script e MCP"),
              ("40–55", "Harness, contexto, permissões e guardrails"),
              ("55–70", "Instrução hostil em conteúdo lido"),
              ("70–85", "Dados que não podem entrar no contexto"),
              ("85–95", "Observabilidade, evals e risco residual"),
              ("95–105", "Intervalo"),
              ("105–115", "Demonstração dos três ambientes"),
              ("115–145", "Inventário, fluxo e política de operações"),
              ("145–160", "Política de dados"),
              ("160–175", "Cenário adversarial"),
              ("175–180", "Revisão cruzada e entrega"),
          ])
          + foot("MOD-04-ROTEIRO"))

    d.add("OBJETIVOS", "Objetivos do encontro",
          head("Encontro 4 · Objetivos", "Ao final deste encontro você consegue", COR)
          + lista_simples([
              "Distinguir modelo, agente, ferramenta, skill, script, MCP e harness.",
              "Mapear o fluxo entre pedido, contexto, ferramenta, ação e prova.",
              "Classificar operações em leitura, escrita e publicação.",
              "Aplicar permissão mínima por etapa, em vez de permissão global.",
              "Reconhecer instrução hostil embutida em conteúdo lido pelo agente.",
              "Definir o que não pode entrar no contexto por confidencialidade.",
              "Identificar risco residual sem apresentar controle como garantia.",
          ], COR)
          + foot("MOD-04-OBJ · relaciona-se a OA-01, OA-04 e OA-11"))

    d.add("TESE", "Tese do encontro",
          statement("O harness é o único controle que funciona quando ninguém está "
                    "olhando.", "MOD-04-TESE"),
          "Tudo o que depende de a pessoa lembrar de fazer falha em algum momento. "
          "O que está no ambiente, não.",
          classe="dark divider-yellow")

    # -- vocabulário -------------------------------------------------
    d.add("MOD-04-VOCAB-1", "Vocabulário 1 · modelo, agente, ferramenta",
          head("MOD-04-CON-01 a 03 · Vocabulário", "Quem raciocina, quem age, "
               "quem executa", COR)
          + tabela(["Elemento", "O que é", "Limite"], [
              ("Modelo", "Interpreta entradas e produz saídas",
               "Não tem acesso ao repositório nem autoridade para agir"),
              ("Agente", "Usa o modelo para perseguir um objetivo, escolher ações, "
                         "observar e iterar",
               "A autonomia é a extensão desse ciclo antes de alguém olhar"),
              ("Ferramenta", "Capacidade concreta: ler, executar, editar, publicar",
               "Define o que é possível, não o que é autorizado"),
          ])
          + callout("Quando alguém diz “o modelo apagou o arquivo”: o modelo emitiu "
                    "uma ação, o ambiente permitiu e a ferramenta executou. Três elos, "
                    "três pontos de controle.")
          + foot("MOD-04-CON-01 a MOD-04-CON-03"),
          "A pergunta de desenho não é “de que o agente precisa?” e sim “o que ele "
          "consegue fazer se interpretar errado?”. Uma ferramenta disponível será usada.")

    d.add("MOD-04-VOCAB-2", "Vocabulário 2 · skill, script, MCP",
          head("MOD-04-CON-04 e 05 · Vocabulário", "Procedimento, execução e "
               "integração", COR)
          + tabela(["Elemento", "O que é", "Limite"], [
              ("Skill", "Orienta trabalho que exige julgamento",
               "Não garante que a decisão esteja correta"),
              ("Script", "Executa transformação ou validação determinística",
               "Reproduzível e testável — prefira sempre que couber"),
              ("Modelo de documento", "Estrutura inicial a ser preenchida com análise",
               "Preencher não é analisar"),
              ("MCP", "Protocolo que expõe ferramentas, recursos e prompts",
               "Padroniza a conexão; cada servidor é uma fronteira de confiança"),
          ])
          + callout("O que puder ser script deve ser script. Colocar em skill o que "
                    "era determinístico introduz variação onde ela não agrega nada.")
          + foot("MOD-04-CON-04 e MOD-04-CON-05"),
          "Sobre MCP: o que o servidor retorna entra no contexto com o mesmo peso do "
          "resto — e foi escrito por alguém que você talvez não conheça. Conectar um "
          "servidor é decisão de segurança, não de conveniência.")

    conceitos = [
        ("MOD-04-CON-06", "Harness", "Conceito 3 de 8",
         "Infraestrutura que envolve modelo e agente: instruções, contexto, skills, "
         "ferramentas, integrações, permissões, sandbox, limites, registros e "
         "verificações.",
         "É o único controle que funciona quando ninguém está olhando. Tudo o que "
         "depende de a pessoa lembrar de fazer falha em algum momento.",
         "Um bom harness torna ações corretas fáceis de executar e ações perigosas "
         "difíceis por acidente.",
         NAO_PROJETAR + "O adaptador do projeto declara fontes, comandos e políticas: "
         "é a parte do harness que fica versionada junto do código."),

        ("MOD-04-CON-08", "Permissões e guardrails", "Conceito 4 de 8",
         "Permissão define o que a execução pode fazer. Guardrail verifica ou bloqueia "
         "entradas, ações ou saídas. Nenhum dos dois corrige uma decisão errada.",
         "Permissão mínima é por etapa, não por projeto. Investigar exige leitura; "
         "implementar exige escrita no diretório afetado; publicar exige confirmação "
         "própria.",
         "Conceder tudo no início porque “vai precisar depois” anula o controle.",
         ""),

        ("MOD-04-CON-09", "Observabilidade e evals", "Conceito 5 de 8",
         "Sem registro, um erro de agente é irreproduzível e, portanto, incorrigível.",
         "O mínimo útil: o que foi pedido, que arquivos foram lidos e alterados, que "
         "comandos rodaram e com que resultado.",
         "Testes do produto e evals do workflow respondem a perguntas diferentes.",
         ""),

        ("MOD-04-CON-12", "Risco residual", "Conceito 8 de 8",
         "Todo controle deixa resto. Um controle apresentado como garantia é pior que "
         "nenhum, porque desliga a atenção.",
         "Para cada controle do mapa, escreva o que ele não cobre e quem decide quando "
         "ele falhar.",
         "", ""),
    ]

    d.add("MOD-04-CON-07", "07 · Engenharia de contexto",
          conceito("MOD-04-CON-07", "Conceito 6 de 8", "Engenharia de contexto",
                   "Contexto útil é atual, pertinente, rastreável e carregado sob "
                   "demanda. Volume não substitui autoridade.",
                   "Retomada do encontro 2, agora como propriedade do ambiente e não "
                   "do operador: o que o agente carrega por padrão importa mais do que "
                   "o que uma pessoa lembra de incluir.",
                   "", COR) + foot("MOD-04-CON-07"))

    for cid, titulo, posicao, principio, pratica, exemplo, nota in conceitos:
        d.add(cid, f"{cid.split('-')[-1]} · {titulo}",
              conceito(cid, posicao, titulo, principio, pratica, exemplo, COR)
              + foot("Fonte: course/topics/MOD-04.md"), nota)

    # -- segurança ---------------------------------------------------
    d.add("MOD-04-CON-10", "10 · Instrução hostil em conteúdo lido",
          head("MOD-04-CON-10 · Conceito 7 de 8",
               "Instrução hostil em conteúdo lido", COR)
          + '<p class="principio">O agente não distingue, por si, dado de instrução. '
            'Um texto que ele lê para analisar pode conter uma ordem endereçada a ele — '
            'e ser obedecido.</p>'
          + '<div class="pratica accent-yellow"><b>Três controles, em ordem de eficácia</b>'
            '<p>1. Reduzir o alcance da ação — o dano possível é o que as permissões '
            'permitem. &nbsp; 2. Tratar conteúdo lido explicitamente como dado. &nbsp; '
            '3. Confirmar ação sensível fora do canal que a sugeriu.</p></div>'
          + callout("O padrão mais perigoso combina leitura de conteúdo externo com "
                    "capacidade de escrita ou publicação na mesma sessão. Separar as "
                    "duas coisas custa pouco e remove a maior parte do risco.", "red")
          + foot("MOD-04-CON-10 · risco RC-12"),
          "Issue, comentário de código, log, página, README de dependência, resposta "
          "de servidor — qualquer um serve de veículo. Desenhe assumindo que a "
          "instrução será obedecida em algum momento, e pergunte o que aconteceria.")

    d.add("MOD-04-CON-11", "11 · Dados que não podem entrar no contexto",
          head("MOD-04-CON-11 · Segurança",
               "O que entra no contexto sai do seu perímetro", COR)
          + tabela(["Categoria", "Exemplo", "Alternativa"], [
              ("Credenciais", "Token, senha, chave de API, string de conexão",
               "Referência ao cofre; nunca o valor"),
              ("Dados pessoais", "CPF, nome, endereço, dados de cliente",
               "Dados fictícios, como cliente-exemplo.com.br"),
              ("Topologia sensível", "IP interno, nome de host, diagrama de rede",
               "Faixas de documentação, como 192.0.2.0/24"),
              ("Conteúdo contratual", "Proposta, valor, cláusula de terceiro",
               "Descrição genérica do requisito"),
          ])
          + callout("Credencial exposta em log: sinalizar, substituir por marcador e "
                    "ROTACIONAR. Trocar o valor no texto não desfaz a exposição.", "red")
          + foot("MOD-04-CON-11 · risco RC-13"),
          "Defina a lista antes, não durante. Um dado exposto não volta atrás: a "
          "prevenção é o único controle eficaz. " + NAO_PROJETAR + "A política de "
          "dados fica declarada no adaptador do projeto, versionada e revisável.")

    d.add("DEMO", "Demonstração — três ambientes",
          demo("A mesma tarefa, três ambientes", [
              ("Ambiente A", "3 min",
               "Conversa isolada: o modelo recebe apenas a pergunta. Que fontes faltam?"),
              ("Ambiente B", "4 min",
               "Agente com leitura: pesquisa, executa buscas e cita arquivos. Quais "
               "afirmações ainda são inferências?"),
              ("Ambiente C", "3 min",
               "Agente com escrita e execução. Antes de permitir: objetivo, escopo, "
               "reversibilidade, prova e ações que exigem confirmação."),
          ], [
              "que a mesma solicitação produz riscos diferentes conforme o ambiente",
              "em que ponto exato a capacidade passou a exceder a autorização",
          ], COR)
          + foot("MOD-04-DEMO"),
          "O foco não é demonstrar uma ferramenta específica.")

    d.add("LAB", "Laboratório — abertura",
          '<div class="cover-body"><p class="eyebrow">Laboratório · 70 minutos</p>'
          '<h1>Desenhar o harness — e testá-lo</h1>'
          '<p class="lead">Cinco etapas de desenho e uma de ataque. Na etapa 5 o '
          'instrutor planta uma instrução hostil em um arquivo do projeto.</p>'
          '<p class="divider-foot tone-yellow">Ambiente isolado: sem rede, sem escrita '
          'fora do laboratório.</p></div>',
          "Confirme o isolamento antes de começar. A instrução hostil precisa ser "
          "contida e sem efeito real. Em turma de cliente, alinhe previamente com a "
          "área de segurança.", classe="dark divider-yellow")

    d.add("LAB-1", "Etapa 1 — Inventário",
          etapa(1, "Inventário do ambiente", "15 minutos", [
              "Liste os componentes do ambiente do projeto-laboratório.",
          ], tabela_vazia(["Elemento", "Exemplo no projeto", "Responsável",
                           "Limite conhecido"], 5)
             + callout("Modelo · agente · instruções · fontes · skills · ferramentas · "
                       "integrações · permissões · verificações"))
          + foot("MOD-04-LAB · etapa 1"))

    d.add("LAB-2", "Etapa 2 — Fluxo de execução",
          etapa(2, "Fluxo de execução", "15 minutos", [
              "Desenhe o caminho entre pedido, carregamento de contexto, escolha de "
              "ferramenta, observação, decisão, alteração e prova.",
              "Marque onde existe checkpoint humano.",
          ], callout("Um fluxo sem checkpoint marcado é um fluxo sem controle "
                     "identificado."))
          + foot("MOD-04-LAB · etapa 2"))

    d.add("LAB-3", "Etapa 3 — Política de operações",
          etapa(3, "Política de operações", "20 minutos", [
              "Classifique cada operação do ambiente.",
          ], tabela_vazia(["Operação", "Leitura / escrita / publicação", "Impacto",
                           "Reversível?", "Confirmação?"], 4))
          + foot("MOD-04-LAB · etapa 3"))

    d.add("LAB-4", "Etapa 4 — Política de dados",
          etapa(4, "Política de dados", "15 minutos", [
              "Preencham a lista do que não pode entrar no contexto neste projeto, "
              "com a alternativa correspondente.",
              "Revisem os registros produzidos nos encontros 1 a 3.",
          ], callout("Algo que não deveria ter entrado, entrou?", "red"))
          + foot("MOD-04-LAB · etapa 4"),
          "Se algum grupo tiver exposto dado sensível nos encontros anteriores, trate "
          "como aprendizado e não como falta. Tenha o procedimento definido antes.")

    d.add("LAB-5", "Etapa 5 — Cenário adversarial",
          etapa(5, "Cenário adversarial", "20 minutos", [
              "Peçam ao agente uma análise que exija ler o arquivo indicado.",
              "Observem o que acontece.",
          ], callout("O agente seguiu a instrução, mencionou ou ignorou? · Se tivesse "
                     "permissão de escrita ou de rede, qual seria o dano? · Qual "
                     "controle do mapa teria contido, e qual não teria? · O que muda "
                     "na política depois deste teste?", "red"))
          + foot("MOD-04-LAB · etapa 5"),
          "Se o agente ignorar a instrução, ótimo — mas nomeie: o comportamento não é "
          "determinístico, e a proteção é o alcance limitado da ação, não a recusa "
          "observada uma vez.")

    d.add("ENTREGA", "Entrega do encontro",
          head("Encontro 4 · Entrega", "Mapa do harness", COR)
          + checklist([
              "Modelo, agente, skills, scripts, ferramentas e MCPs",
              "Fontes e fronteiras de confiança",
              "Fluxo de contexto e execução, com checkpoints marcados",
              "Operações de leitura, escrita e publicação classificadas",
              "Permissões mínimas por etapa",
              "Lista de dados vedados ao contexto, com alternativas",
              "Resultado do cenário adversarial e o que mudou na política",
              "Registros, testes e evals disponíveis",
              "Risco residual por controle e responsável pela decisão",
          ], COR)
          + foot("MOD-04-ENT"))

    d.add("EQUIVOCOS", "Equívocos a evitar",
          head("Encontro 4 · Fechamento", "Nove leituras erradas deste encontro", COR)
          + equivocos([
              ("O modelo acessa o projeto.",
               "O acesso é oferecido pelo ambiente e pelas ferramentas."),
              ("MCP é a ferramenta.",
               "MCP é o protocolo; servidor e ferramenta são elementos distintos."),
              ("Skill executa a tarefa.",
               "Skill orienta; execução depende do agente e das ferramentas."),
              ("Sandbox resolve qualquer risco.",
               "Limita certos efeitos, não premissas ou decisões."),
              ("Analisar autoriza editar.",
               "Leitura, escrita e publicação exigem distinção explícita."),
              ("Injeção só acontece com conteúdo da internet.",
               "Um comentário no próprio repositório ou o README de uma dependência bastam."),
              ("Se o agente ignorou a instrução hostil, estamos protegidos.",
               "O comportamento não é determinístico. A proteção é o alcance limitado da ação."),
              ("Anonimizar depois resolve.",
               "Trocar o valor no texto não desfaz a exposição. A credencial precisa ser rotacionada."),
          ])
          + foot("MOD-04-EQUIVOCOS"))

    d.add("PONTE", "Próximo encontro",
          '<div class="cover-body"><p class="eyebrow">Encontro 5</p>'
          '<h1>De volta ao<br>protocolo mínimo</h1>'
          '<p class="lead">Vocês escreveram, no encontro 3, os controles que '
          'consideram indispensáveis. No próximo encontro esse documento volta — e vai '
          'ser comparado, item a item, com um método pronto.</p>'
          '<p class="divider-foot tone-yellow">A pergunta será: o que vocês '
          'identificaram sozinhos, e o que faltou?</p></div>',
          "Este é o gancho para o encontro 5. Não diga qual método, nem o nome dele.",
          classe="dark divider-yellow")

    return d
