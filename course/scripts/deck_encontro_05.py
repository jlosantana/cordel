#!/usr/bin/env python3
"""Deck de aula do encontro 5 — Cordel como implementação do protocolo.

Fonte do conteúdo: course/topics/MOD-05.md.

É o encontro em que a ferramenta entra. A comparação com o protocolo mínimo
é o conteúdo, não um preâmbulo: conduza-a sem defender o método.
"""

from __future__ import annotations

from deck_theme import (Deck, callout, capa_encontro, checklist, conceito, demo,
                        equivocos, etapa, foot, frase_grande, head, lista_simples,
                        roteiro, statement, tabela, tabela_vazia)

COR = "yellow"


def build() -> Deck:
    d = Deck("Encontro 5", "Cordel como implementação do protocolo")

    d.add("CAPA", "Capa do encontro",
          capa_encontro("5", "II", "Cordel como implementação\ndo protocolo",
                        "O Cordel é uma resposta possível a um conjunto de problemas "
                        "reais, não a única. Quem entende os problemas consegue "
                        "avaliar a resposta."),
          "A ordem importa: a turma passou quatro encontros descobrindo controles por "
          "conta própria. Agora recebe de volta o próprio protocolo e compara.",
          classe="dark divider-yellow")

    d.add("ROTEIRO", "Roteiro das 3 horas",
          head("Encontro 5 · Roteiro", "O que vamos fazer hoje", COR)
          + roteiro([
              ("0–10", "Devolução dos protocolos mínimos"),
              ("10–30", "Demonstração: o confronto"),
              ("30–50", "Do protocolo ao método: ganhos e custo da formalização"),
              ("50–70", "Fontes, artefatos, projeções e tipos de trabalho"),
              ("70–85", "Ciclo de vida, núcleo e adaptador, engenharia de contexto"),
              ("85–95", "O que o método não resolve"),
              ("95–105", "Intervalo"),
              ("105–115", "Demonstração de init, configuração e check"),
              ("115–135", "Laboratório: comparação"),
              ("135–150", "Inventário e inicialização"),
              ("150–172", "Adaptador, índice e classificação"),
              ("172–180", "Check, entrega e retrospectiva"),
          ])
          + foot("MOD-05-ROTEIRO"))

    d.add("DEVOLUCAO", "Devolução dos protocolos",
          head("Encontro 5 · Abertura", "O que vocês escreveram no encontro 3", COR)
          + frase_grande("Cada grupo recebe de volta o próprio protocolo mínimo — "
                         "intacto, como foi entregue.", 30)
          + callout("Leiam antes de qualquer outra coisa. Em quinze minutos vocês vão "
                    "comparar cada item com um método que já existe.")
          + foot("Entrega do MOD-03 · LAB etapa 6"),
          "Devolva impresso, se possível. Ler no papel muda a atenção. Não comente o "
          "conteúdo ainda — a comparação é o exercício.")

    d.add("OBJETIVOS", "Objetivos do encontro",
          head("Encontro 5 · Objetivos", "Ao final deste encontro você consegue", COR)
          + lista_simples([
              "Mapear os controles do próprio protocolo contra as peças do Cordel.",
              "Identificar controles que o método não cobre e seguem sendo trabalho humano.",
              "Distinguir fonte da verdade, artefato e projeção.",
              "Separar requisito, AS-IS, necessidade, story e evidência.",
              "Configurar o adaptador do projeto sem inventar convenções externas.",
              "Organizar um índice curto para carregamento de contexto sob demanda.",
              "Executar init e check até obter GO — sabendo o que esse resultado não significa.",
          ], COR)
          + foot("MOD-05-OBJ · relaciona-se a OA-05 e OA-12"))

    d.add("TESE", "Tese do encontro",
          statement("Um método formaliza controles e os torna revisáveis. Não elimina "
                    "ambiguidade de negócio, não substitui conhecimento de domínio e "
                    "não garante que a fonte esteja correta.", "MOD-05-TESE"),
          "Se a turma sair achando que instalar a ferramenta resolve os problemas dos "
          "encontros 1 a 4, o encontro falhou.",
          classe="dark divider-yellow")

    conceitos = [
        ("MOD-05-CON-01", "Do protocolo ao método", "Conceito 1 de 9",
         "Times que trabalham com IA convergem para um conjunto pequeno e recorrente "
         "de controles. Um método é a formalização desses controles.",
         "Três ganhos: o controle deixa de depender de quem está na sala, vira "
         "revisável por outra pessoa e pode ser parcialmente automatizado. Um custo: "
         "cerimônia.",
         "Um método que exige mais registro do que o risco justifica é abandonado na "
         "primeira semana difícil — e aí o time fica pior do que estava."),

        ("MOD-05-CON-03", "Fonte da verdade", "Conceito 3 de 9",
         "Local autorizado para manter determinado fato. Autoridade depende de "
         "responsável e escopo.",
         "A pergunta que resolve a maioria das disputas: se este fato mudar, qual "
         "arquivo ou sistema precisa ser alterado para que a mudança valha?",
         "Esse é a fonte. Os demais lugares onde o fato aparece são cópias — e cópias "
         "envelhecem."),

        ("MOD-05-CON-04", "Artefato e projeção", "Conceito 4 de 9",
         "Artefato preserva contexto ou decisão e requer revisão. Projeção é "
         "recalculável: índice, matriz, painel.",
         "Quando a projeção diverge, corrige-se a fonte ou o gerador.",
         "Corrigir a projeção à mão é a tentação mais comum e a mais cara: resolve a "
         "aparência, preserva a divergência e destrói o sinal que ela dava."),

        ("MOD-05-CON-06", "Ciclo de vida documental", "Conceito 6 de 9",
         "work/ mantém trabalho ativo · product/ conhecimento atual e durável · "
         "archive/ histórico encerrado · generated/ projeções · local/ notas pessoais.",
         "A separação existe para o agente saber o que pode citar como verdade atual.",
         "Um documento arquivado que continua no meio dos ativos volta como fonte em "
         "alguma investigação futura."),

        ("MOD-05-CON-07", "Núcleo e adaptador", "Conceito 7 de 9",
         "O núcleo define invariantes portáteis. O adaptador declara fontes, comandos, "
         "identificadores e políticas do projeto.",
         "É o mecanismo que responde à pergunta do encontro 8: o que levo comigo "
         "quando mudo de time? O núcleo. O adaptador fica.",
         "Convenções de uma arquitetura não entram silenciosamente no método."),

        ("MOD-05-CON-08", "Engenharia de contexto", "Conceito 8 de 9",
         "O índice aponta para fontes, não as duplica. O agente começa pelo índice e "
         "carrega somente o necessário.",
         "É a resposta estrutural ao problema da janela de contexto, do encontro 1: "
         "em vez de tentar caber tudo, tornar tudo encontrável.",
         "Fonte canônica atual prevalece sobre conversa ou resumo antigo."),

        ("MOD-05-CON-09", "O que o método não resolve", "Conceito 9 de 9",
         "Nenhum método elimina ambiguidade de negócio, substitui conhecimento do "
         "domínio, garante que a fonte canônica esteja correta ou impede que um gate "
         "mal revisado formalize uma premissa ruim.",
         "O que ele faz é tornar essas falhas visíveis e atribuíveis.",
         "Cada grupo termina o encontro sabendo apontar pelo menos dois controles do "
         "próprio protocolo que seguem sendo trabalho humano."),
    ]

    d.add("MOD-05-CON-02", "02 · Manifesto em operação",
          head("MOD-05-CON-02 · Conceito 2 de 9", "Manifesto em operação", COR)
          + lista_simples([
              "Começar pela origem.",
              "Separar fatos de alegações.",
              "Confirmar o comportamento atual.",
              "Preservar decisão humana.",
              "Planejar unidade verificável.",
              "Usar gates com significado.",
              "Reconciliar fontes.",
              "Automatizar mecânica sem delegar julgamento.",
          ], COR, numerada=False)
          + callout("Cada um destes já apareceu no curso como problema, antes de "
                    "aparecer como regra.")
          + foot("MOD-05-CON-02"),
          "Peça que a turma aponte em que momento dos encontros 1 a 4 sentiu a falta "
          "de cada princípio. Se não conseguirem para algum deles, esse princípio "
          "ainda não foi ensinado — anote para o encontro 8.")

    d.add("MOD-05-CON-05", "05 · Tipos de trabalho",
          head("MOD-05-CON-05 · Conceito 5 de 9", "Tipos de trabalho", COR)
          + tabela(["Tipo", "O que registra"], [
              ("Requisito", "Compromisso externo"),
              ("Contexto AS-IS", "Comportamento atual confirmado"),
              ("Necessidade", "Pedido sem destino ou autorização definidos"),
              ("Story", "Unidade de trabalho autorizada"),
              ("Spec", "Desenho do TO-BE, quando necessário"),
              ("Evidência", "Sustentação confirmável de uma afirmação"),
          ])
          + callout("A distinção que mais evita erro: necessidade registra que alguém "
                    "pediu; story registra que alguém autorizou.")
          + foot("MOD-05-CON-05"),
          "Confundir as duas é como o escopo cresce sem que ninguém tenha decidido "
          "nada. Volta com força no encontro 6.")

    for cid, titulo, posicao, principio, pratica, exemplo in conceitos:
        d.add(cid, f"{cid.split('-')[-1]} · {titulo}",
              conceito(cid, posicao, titulo, principio, pratica, exemplo, COR)
              + foot("Fonte: course/topics/MOD-05.md"))

    d.add("DEMO", "Demonstração — o confronto",
          demo("Do protocolo ao método", [
              ("O confronto", "15 min",
               "Protocolo mínimo real e a cadeia do Cordel, lado a lado. Percorra três "
               "categorias, sem defender o método."),
              ("Antes", "5 min",
               "O agente pesquisando um repositório sem configuração: descobre "
               "caminhos, comandos e autoridade misturando busca e inferência."),
              ("Inicialização", "5 min",
               "Execute init. O que foi criado, o que fica vazio, por que não "
               "sobrescreve arquivos existentes."),
              ("Configuração e check", "10 min",
               "Preencha fonte, comando e política. Execute check, corrija e repita "
               "até GO."),
          ], [
              "controles que a turma identificou e o método implementa — costumam ser a maioria",
              "controles que a turma NÃO identificou — em geral origem, autorização e reconciliação",
              "controles que o método resolve de forma diferente — discuta como escolha de projeto",
          ], COR)
          + foot("MOD-05-DEMO"),
          "Se um controle do protocolo não existir no método e for bom, isso é matéria "
          "do encontro 8. Diga isso na hora: valoriza o trabalho da turma e planta a "
          "proposta de evolução.")

    d.add("LAB", "Laboratório — abertura",
          '<div class="cover-body"><p class="eyebrow">Laboratório · 70 minutos</p>'
          '<h1>Comparar e configurar</h1>'
          '<p class="lead">Primeiro a comparação item a item. Depois a configuração do '
          'projeto-laboratório — sem mudar o comportamento funcional dele.</p></div>',
          "Se o tempo apertar, a configuração pode virar pré-trabalho do encontro 6. "
          "A comparação, não: é o conteúdo do encontro.",
          classe="dark divider-yellow")

    d.add("LAB-1", "Etapa 1 — Comparação",
          etapa(1, "Comparação", "20 minutos", [
              "Preencham a tabela para cada controle do próprio protocolo.",
          ], tabela_vazia(["Controle do protocolo", "Problema que o motivou",
                           "Peça do Cordel que o cobre", "Cobertura"], 4)
             + callout("Cobertura: total · parcial · nenhuma · resolvido de outro modo"))
          + foot("MOD-05-LAB · etapa 1"),
          "Ao final, peça duas listas separadas: controles do protocolo sem "
          "correspondência no método, e peças do método sem correspondência no "
          "protocolo — com a hipótese de por que a turma não chegou nelas.")

    d.add("LAB-2", "Etapa 2 — Inventário de fontes",
          etapa(2, "Inventário de fontes", "15 minutos", [
              "Classifiquem os materiais fornecidos por tipo, autoridade, responsável "
              "e escopo.",
              "Itens sem responsável ficam registrados como lacuna.",
          ])
          + foot("MOD-05-LAB · etapa 2"))

    d.add("LAB-3", "Etapa 3 — Inicialização",
          etapa(3, "Inicialização", "10 minutos", [
              "Executem init duas vezes e confirmem a idempotência.",
              "Revisem os arquivos criados antes de editá-los.",
          ])
          + foot("MOD-05-LAB · etapa 3"))

    d.add("LAB-4", "Etapa 4 — Adaptador",
          etapa(4, "Adaptador do projeto", "25 minutos", [
              "Preencham nome, repositórios, fontes, armazenamento, identificadores, "
              "comandos e políticas.",
              "Não criem identificadores que pertencem a uma fonte externa.",
              "Incorporem a política de dados definida no encontro 4.",
          ])
          + foot("MOD-05-LAB · etapa 4"))

    d.add("LAB-5", "Etapa 5 — Índice e classificação",
          etapa(5, "Índice e classificação", "20 minutos", [
              "Criem o índice com rotas para contexto, decisões e trabalho — sem "
              "copiar o conteúdo integral das fontes.",
              "Distribuam os documentos entre product, work, archive, generated e "
              "local, justificando autoridade e ciclo de vida.",
          ])
          + foot("MOD-05-LAB · etapa 5"))

    d.add("LAB-6", "Etapa 6 — Check",
          etapa(6, "Check", "10 minutos", [
              "Executem até GO.",
              "Preservem uma lista separada dos aspectos semanticamente não verificados.",
          ], callout("O que este GO não garante?", "yellow"))
          + foot("MOD-05-LAB · etapa 6"),
          "A pergunta do rodapé é o fecho do encontro. GO significa que invariantes "
          "estruturais passaram — não que o projeto está correto.")

    d.add("ENTREGA", "Entrega do encontro",
          head("Encontro 5 · Entrega", "Comparação e adaptador", COR)
          + checklist([
              "Tabela de comparação entre protocolo mínimo e Cordel",
              "Controles do protocolo sem correspondência no método",
              "Controles que seguem sendo trabalho humano após a configuração",
              "Adaptador do projeto válido",
              "Índice curto e navegável",
              "Estrutura de diretórios coerente",
              "Inventário de fontes com responsável e escopo",
              "Resultado GO do verificador",
              "Lacunas que o verificador estrutural não detecta",
              "Uma informação mantida no adaptador, e não no núcleo, justificada",
          ], COR)
          + foot("MOD-05-ENT"))

    d.add("EQUIVOCOS", "Equívocos a evitar",
          head("Encontro 5 · Fechamento", "Oito leituras erradas deste encontro", COR)
          + equivocos([
              ("O protocolo do grupo era o rascunho; o Cordel é a versão certa.",
               "São respostas ao mesmo problema, com maturidades diferentes."),
              ("Instalar o método resolve os problemas dos encontros 1 a 4.",
               "Ele endereça parte deles e torna o restante visível."),
              ("Fonte da verdade é sempre um arquivo local.",
               "Pode ser sistema externo com responsável."),
              ("URL vira verdade porque está no JSON.",
               "A configuração declara autoridade, não conteúdo."),
              ("Projeção pode ser corrigida rapidamente à mão.",
               "Isso mascara a fonte divergente."),
              ("Tudo deve entrar no contexto do agente.",
               "Contexto demais reduz pertinência e controle."),
              ("GO significa que o projeto está correto.",
               "Significa que invariantes estruturais passaram."),
              ("Notas locais podem sustentar decisão da equipe.",
               "Não possuem autoridade compartilhada."),
          ])
          + foot("MOD-05-EQUIVOCOS"))

    d.add("PONTE", "Próximo encontro",
          '<div class="cover-body"><p class="eyebrow">Encontro 6</p>'
          '<h1>Da demanda<br>à unidade autorizada</h1>'
          '<p class="lead">O projeto está configurado. No próximo encontro percorremos '
          'a cadeia: origem, triagem, comportamento atual confirmado, decisão humana e '
          'a unidade que pode ser implementada sem invenção.</p>'
          '<p class="divider-foot tone-yellow">A demanda ambígua do encontro 1 volta — '
          'agora com fontes.</p></div>',
          classe="dark divider-yellow")

    return d
