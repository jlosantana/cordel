#!/usr/bin/env python3
"""Deck de aula do encontro 7 — Implementação assistida e prova.

Fonte do conteúdo: course/topics/MOD-07.md.

Encontro mais apertado do curso: funde dois da versão anterior e depende de a
story caber em cerca de quarenta minutos de execução assistida.
"""

from __future__ import annotations

from deck_theme import (Deck, callout, capa_encontro, checklist, conceito, demo,
                        equivocos, etapa, foot, frase_grande, head, lista_simples,
                        roteiro, statement, tabela, tabela_vazia)

COR = "red"


def build() -> Deck:
    d = Deck("Encontro 7", "Implementação assistida e prova")

    d.add("CAPA", "Capa do encontro",
          capa_encontro("7", "III", "Implementação\nassistida e prova",
                        "O gate não encerra o julgamento: ele cria condições para agir. "
                        "E uma entrega só é verificada quando outra pessoa percorre a "
                        "afirmação até uma evidência."),
          "Abre o Bloco III. Encontro mais apertado do curso — cronometre a etapa 2 e "
          "esteja pronto para reduzir a 5.",
          classe="dark divider-red")

    d.add("ROTEIRO", "Roteiro das 3 horas",
          head("Encontro 7 · Roteiro", "O que vamos fazer hoje", COR)
          + roteiro([
              ("0–10", "Retomada do gate e do plano"),
              ("10–25", "Contexto de execução, plano incremental e ferramentas por etapa"),
              ("25–40", "Escopo emergente e observabilidade da execução"),
              ("40–55", "Evidência suficiente, vereditos e estados"),
              ("55–70", "Reconciliação e articulação com branch, pull request e CI"),
              ("70–90", "Demonstração: checkpoints e evidência parcial"),
              ("90–100", "Intervalo"),
              ("100–110", "Laboratório: revalidar o gate e preparar"),
              ("110–150", "Implementar em checkpoints"),
              ("150–160", "Evento de escopo"),
              ("160–172", "Estratégia de prova e revisão entre grupos"),
              ("172–180", "Reconciliação, veredito e entrega"),
          ])
          + foot("MOD-07-ROTEIRO"),
          "Se a implementação atrasar, a etapa 5 vira leitura cruzada de dossiês, sem "
          "execução — mas não corte: é onde a diferença entre implementado e "
          "verificado aparece.")

    d.add("OBJETIVOS", "Objetivos do encontro",
          head("Encontro 7 · Objetivos", "Ao final deste encontro você consegue", COR)
          + lista_simples([
              "Montar contexto mínimo pertinente e transformar critérios em plano incremental.",
              "Conceder ferramentas e permissões compatíveis com a etapa.",
              "Revisar diferenças em checkpoints, contra escopo e fora do escopo.",
              "Distinguir descoberta técnica de escopo funcional novo.",
              "Executar a estratégia de prova e avaliar se a evidência sustenta o critério.",
              "Aplicar os vereditos e diferenciar implementado de verificado.",
              "Promover descobertas duráveis e regenerar projeções.",
              "Articular o rastro com branch, pull request, revisão humana e CI.",
          ], COR)
          + foot("MOD-07-OBJ · relaciona-se a OA-03, OA-06, OA-10 e OA-12"))

    d.add("TESE", "Tese do encontro",
          statement("Uma entrega só pode ser chamada de verificada quando outra pessoa "
                    "consegue percorrer a afirmação até uma evidência atual que "
                    "demonstra especificamente o comportamento.", "MOD-07-TESE"),
          classe="dark divider-red")

    conceitos = [
        ("MOD-07-CON-02", "Plano incremental", "Conceito 1 de 9",
         "Divide a mudança em passos verificáveis, preservando compatibilidade e "
         "feedback.",
         "O tamanho do passo é decisão de revisão, não de produtividade: um passo é "
         "grande demais quando a diferença não cabe em uma leitura atenta.",
         "Cada passo deve permitir observar progresso sem depender de uma longa cadeia "
         "não revisada."),

        ("MOD-07-CON-03", "Ferramentas por etapa", "Conceito 2 de 9",
         "Pesquisa e leitura antes da escrita. Build e testes validam hipóteses. "
         "Publicação permanece separada e exige autorização própria.",
         "Aplicação direta da escala de autonomia do encontro 2 e da política de "
         "permissões do encontro 4.",
         ""),

        ("MOD-07-CON-05", "Escopo emergente", "Conceito 3 de 9",
         "Se a implementação revela necessidade não coberta, essa parte é interrompida "
         "e volta à triagem.",
         "A distinção prática: a descoberta impede cumprir o critério autorizado, ou "
         "acrescenta um resultado novo? A primeira fica; a segunda volta.",
         "Correção estritamente necessária para cumprir o aceite pode permanecer, "
         "quando sustentada pelo escopo e revisada."),

        ("MOD-07-CON-06", "Observabilidade da execução", "Conceito 4 de 9",
         "Registre plano, arquivos alterados, comandos, resultados, decisões e desvios.",
         "O objetivo não é narrar cada tecla, mas permitir reconstruir escolhas "
         "relevantes.",
         ""),

        ("MOD-07-CON-08", "Evidência suficiente", "Conceito 6 de 9",
         "Adequada quando pode ser localizada, está no lugar autorizado, demonstra a "
         "afirmação e distingue ausência de busca incompleta.",
         "Os mesmos critérios do encontro 3, agora aplicados ao fechamento e sujeitos "
         "a revisão por outro grupo.",
         ""),

        ("MOD-07-CON-11", "Reconciliação", "Conceito 8 de 9",
         "Atualiza story, spec, contexto atual, decisões, dependências e projeções "
         "para refletir a entrega.",
         "É a etapa mais pulada em times reais, e a razão de o conhecimento envelhecer.",
         "O sinal de que foi feita: a próxima pessoa que investigar aquele "
         "comportamento encontra a resposta certa sem perguntar a ninguém."),
    ]

    d.add("MOD-07-CON-01", "01 · Contexto de execução",
          conceito("MOD-07-CON-01", "Introdução", "Contexto de execução",
                   "Story, spec, AS-IS, decisões, arquivos afetados, convenções e "
                   "comandos. Materiais não pertinentes ficam fora.",
                   "O contexto pode crescer quando a execução revela uma dependência, "
                   "mas cada inclusão precisa de motivo.",
                   "O índice torna essa seleção barata: aponta-se a rota, o agente "
                   "carrega o que precisa.", COR)
          + foot("MOD-07-CON-01"))

    for cid, titulo, posicao, principio, pratica, exemplo in conceitos:
        d.add(cid, f"{cid.split('-')[-1]} · {titulo}",
              conceito(cid, posicao, titulo, principio, pratica, exemplo, COR)
              + foot("Fonte: course/topics/MOD-07.md"))

    d.add("MOD-07-CON-09", "09 · Vereditos",
          head("MOD-07-CON-09 · Conceito 7 de 9", "Vereditos de rastreabilidade", COR)
          + tabela(["Veredito", "Quando"], [
              ("verificado", "Condições relevantes presentes e provadas"),
              ("parcial", "Parte presente ou provada"),
              ("divergente", "Implementação difere da fonte esperada"),
              ("nao-iniciado", "Busca delimitada não encontrou implementação"),
              ("nao-rastreavel", "O texto não permite verificação objetiva"),
          ])
          + callout("O veredito honesto mais comum, em trabalho real, é PARCIAL. Um "
                    "curso em que todos os grupos declaram verificado provavelmente "
                    "afrouxou o critério de evidência.", "red")
          + foot("MOD-07-CON-09 e CON-10"),
          "implementado indica conclusão técnica com prova insuficiente. verificado "
          "exige evidência confirmável. O estado pode regredir quando a evidência "
          "quebra, envelhece ou perde pertinência.")

    d.add("MOD-07-CON-13", "13 · O rastro e o fluxo existente",
          head("MOD-07-CON-13 · Conceito 9 de 9",
               "O rastro e o fluxo de trabalho que você já tem", COR)
          + '<p class="principio">O rastro do método convive com branch, pull request, '
            'revisão humana e CI — não os substitui nem os duplica.</p>'
          + tabela(["Informação", "Onde vive"], [
              ("Decisão e evidência", "No artefato"),
              ("Discussão da alteração", "No pull request"),
              ("Execução das verificações", "Na CI, com resultado endereçável"),
              ("Revisão humana", "Focada na diferença contra o escopo"),
          ])
          + callout("Duplicar o conteúdo do artefato dentro do pull request cria duas "
                    "versões que divergem na primeira alteração.")
          + foot("MOD-07-CON-13"),
          "Este é o slide que responde à objeção mais comum em time real: “mais uma "
          "camada de burocracia”. Cada informação vive em um lugar só.")

    d.add("DEMO", "Demonstração — checkpoints e prova",
          demo("Checkpoints e evidência parcial", [
              ("Três checkpoints", "12 min",
               "Localizar o ponto de mudança e confirmar a âncora · implementar o "
               "comportamento mínimo e o teste do caminho principal · cobrir a "
               "condição de repetição e verificar."),
              ("O evento de escopo", "incluído",
               "No segundo passo, introduza “aproveitar e enviar e-mail”. Registre a "
               "nova necessidade sem incorporá-la."),
              ("Teste verde, evidência parcial", "8 min",
               "Retome o exemplo do encontro 3, agora com o critério formalizado na "
               "story. Declare PARCIAL sem constrangimento."),
          ], [
              "que após cada passo se compara diferença, teste e critério",
              "o que seria necessário para chegar a verificado — e por que ainda não chegou",
          ], COR)
          + foot("MOD-07-DEMO"))

    d.add("LAB", "Laboratório — abertura",
          '<div class="cover-body"><p class="eyebrow">Laboratório · 80 minutos</p>'
          '<h1>Executar, provar e reconciliar</h1>'
          '<p class="lead">Seis etapas. A implementação é a mais longa, e a revisão '
          'entre grupos é a que não pode ser cortada.</p>'
          '<p class="divider-foot tone-red">Branch por grupo. Falha preexistente '
          'conhecida: separem da introduzida.</p></div>',
          classe="dark divider-red")

    d.add("LAB-1", "Etapa 1 — Revalidar e preparar",
          etapa(1, "Revalidar o gate e preparar", "10 minutos", [
              "Confirmem que fontes, branch, dependências e decisões continuam atuais.",
              "Selecionem o contexto, definam os passos e associem cada passo a um "
              "feedback.",
          ], callout("Drift relevante vira ressalva ou bloqueio."))
          + foot("MOD-07-LAB · etapa 1"))

    d.add("LAB-2", "Etapa 2 — Implementar em checkpoints",
          etapa(2, "Implementar em checkpoints", "40 minutos", [
              "O agente pode editar e executar comandos dentro do escopo.",
              "Revisem diferenças e resultados entre passos.",
              "Evitem acumular grande alteração sem observação.",
          ], callout("Um passo é grande demais quando a diferença não cabe em uma "
                     "leitura atenta."))
          + foot("MOD-07-LAB · etapa 2"),
          "Cronometre. Aos 30 minutos, avise o tempo restante. Grupos que não "
          "terminarem seguem para a etapa 4 com o que tiverem: provar o parcial é "
          "conteúdo tão válido quanto provar o completo.")

    d.add("LAB-3", "Etapa 3 — Evento de escopo",
          etapa(3, "Evento de escopo", "10 minutos", [
              "O instrutor libera uma solicitação adicional plausível.",
              "Decidam se pertence ao critério atual.",
              "Se não pertencer, registrem necessidade separada e sigam apenas o "
              "autorizado.",
          ], callout("A descoberta impede cumprir o critério autorizado, ou acrescenta "
                     "um resultado novo?", "yellow"))
          + foot("MOD-07-LAB · etapa 3"))

    d.add("LAB-4", "Etapa 4 — Executar a prova",
          etapa(4, "Executar a estratégia de prova", "20 minutos", [
              "Para cada critério, executem o teste ou verificação planejada.",
              "Registrem resultado, ambiente, dados e endereço da evidência.",
              "Separem falhas preexistentes das introduzidas pela mudança.",
          ], tabela_vazia(["Critério", "Verificação executada", "Resultado",
                           "Endereço da evidência"], 4))
          + foot("MOD-07-LAB · etapa 4"))

    d.add("LAB-5", "Etapa 5 — Revisão entre grupos",
          etapa(5, "Revisão entre grupos", "20 minutos", [
              "O revisor escolhe pelo menos dois critérios e abre as evidências.",
              "Atribui veredito, registrando condição existente, ausente ou divergente.",
              "Verifica se todo arquivo alterado tem motivo no escopo.",
          ], callout("Se o percurso depende de explicação oral não registrada, há uma "
                     "lacuna no rastro.", "red"))
          + foot("MOD-07-LAB · etapa 5"))

    d.add("LAB-6", "Etapa 6 — Correção e reconciliação",
          etapa(6, "Correção e reconciliação", "15 minutos", [
              "Corrijam prova, texto ou implementação quando autorizado.",
              "Se a revisão revelar escopo novo, registrem necessidade separada.",
              "Atualizem AS-IS, story, spec, decisões e dependências.",
              "Regenerem projeções e executem o comando de reconciliação.",
          ])
          + foot("MOD-07-LAB · etapa 6"))

    d.add("ENTREGA", "Entrega do encontro",
          head("Encontro 7 · Entrega", "Implementação e dossiê de prova", COR)
          + checklist([
              "Plano incremental executado e registro de contexto e ferramentas",
              "Código e testes da story",
              "Diferença revisada contra escopo e fora do escopo",
              "Nova necessidade para o escopo emergente, quando aplicável",
              "Tabela critério-prova executada, com evidências acessíveis",
              "Separação entre falhas preexistentes e introduzidas",
              "Parecer da revisão independente e vereditos por condição",
              "AS-IS atualizado, story e spec reconciliadas, projeções regeneradas",
              "Resultado do comando de reconciliação",
              "Separação entre entrega, dívida e pendência",
              "Estado final justificado entre implementado e verificado",
          ], COR)
          + foot("MOD-07-ENT"))

    d.add("EQUIVOCOS", "Equívocos a evitar",
          head("Encontro 7 · Fechamento", "Leituras erradas deste encontro", COR)
          + equivocos([
              ("Gate pronto impede novas descobertas.",
               "Ele representa o conhecimento no ponto de entrada."),
              ("O agente pode aproveitar para limpar o código.",
               "Só se a limpeza estiver no escopo."),
              ("Contexto mínimo significa informação insuficiente.",
               "Significa pertinência, não privação."),
              ("Checkpoint é aprovação humana de cada linha.",
               "É observação proporcional ao risco."),
              ("Story concluída prova implementação.",
               "Ela registra trabalho, não comportamento."),
              ("Qualquer teste que passa é evidência.",
               "Precisa demonstrar a condição alegada."),
              ("Verificado é estado permanente.",
               "Evidências envelhecem e podem perder validade."),
              ("Reconciliação é atualizar status.",
               "Inclui fontes, conhecimento e projeções."),
              ("O pull request substitui o rastro.",
               "São camadas diferentes; duplicar conteúdo cria divergência."),
          ])
          + foot("MOD-07-EQUIVOCOS"))

    d.add("PONTE", "Próximo encontro",
          '<div class="cover-body"><p class="eyebrow">Encontro 8 · Último</p>'
          '<h1>O que você leva<br>para o seu time</h1>'
          '<p class="lead">Percorremos a cadeia inteira. No próximo encontro a '
          'pergunta muda: o que disso funciona no seu time, que provavelmente não usa '
          'nada disso?</p>'
          '<p class="divider-foot tone-red">Tragam os registros dos sete encontros. '
          'A retrospectiva final é sobre dados, não sobre impressões.</p></div>',
          classe="dark divider-red")

    return d
