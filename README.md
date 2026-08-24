# Cordel

**Engenharia de software orientada por contexto, especificações e evidências.**

Cordel reúne práticas que desenvolvi ao trabalhar com agentes de IA em projetos de
software. O objetivo é transformar essa experiência em um método portátil e ensinável,
capaz de manter a ligação entre o pedido original, as decisões tomadas, o código alterado
e a prova de que o resultado funciona.

O núcleo não depende de uma empresa, tecnologia ou domínio de negócio específico. Cada
projeto mantém somente seu adaptador e conhecimento compartilhado em `.cordel/`; a
skill e os scripts do Cordel são instalados separadamente.

## Por que este método existe

Um agente consegue produzir código rapidamente, mas velocidade não garante que ele tenha
entendido a necessidade, confirmado o comportamento atual ou recebido autorização para
alterar o escopo. O método reduz esse risco com uma cadeia rastreável:

```text
demanda -> origem -> classificação -> AS-IS -> decisão -> story/spec
        -> implementação -> prova -> reconciliação
```

A ideia central é simples: afirmações técnicas precisam de evidência; necessidades não são
autorizações; e uma entrega só termina quando documentação, implementação e testes voltam
a concordar.

## Acompanhe uma demanda de ponta a ponta

Imagine o pedido: “o sistema deve avisar quando uma solicitação for aprovada”.

1. **Localize a origem.** Registre quem fez o pedido e qual documento ou decisão o sustenta.
2. **Classifique.** Descubra se é defeito, comportamento já previsto ou escopo novo.
3. **Confirme o AS-IS.** Inspecione código, dados e testes para provar o que acontece hoje.
4. **Obtenha a decisão.** Se for escopo novo, um responsável humano autoriza e delimita a mudança.
5. **Prepare o trabalho.** Escreva story, critérios observáveis e, quando necessário, uma spec.
6. **Implemente e prove.** Relacione cada critério a teste, log, captura ou outra evidência verificável.
7. **Reconcilie.** Atualize as fontes canônicas e confira se código, documentação e projeções concordam.

Antes de implementar, o agente deve declarar um resultado de gate:
`BLOQUEADO`, `PRONTO PARA ESPECIFICAR` ou `PRONTO PARA IMPLEMENTAR`.

## Instale a skill

O instalador cria o diretório de skills quando necessário e copia o Cordel para ele:

```bash
python skill/cordel/scripts/cordel.py install
```

Por padrão, o destino é `CODEX_HOME/skills/cordel` ou `~/.codex/skills/cordel`. Para
usar outro diretório de skills, informe-o como argumento. O comando não substitui uma
instalação existente; remova ou renomeie a versão anterior antes de atualizar.

## Experimente em um projeto-piloto

Requer Python 3.8 ou superior e não possui dependências externas.

```bash
python skill/cordel/scripts/cordel.py init /caminho/do/projeto
```

O comando cria `.cordel/project.json`, um índice de contexto, modelos e pastas por
ciclo de vida. Também cria ou atualiza blocos Cordel delimitados em `AGENTS.md` e
`CLAUDE.md`, preservando as demais instruções existentes. Em seguida:

1. preencha o nome, os repositórios, as fontes da verdade e os comandos do projeto;
2. valide a configuração até obter `GO`:

   ```bash
   python skill/cordel/scripts/cordel.py check /caminho/do/projeto
   ```

3. escolha uma demanda real, pequena e de baixo risco;
4. percorra a cadeia completa e registre onde o método ajudou ou criou atrito;
5. ajuste regras locais no projeto; generalize o núcleo apenas com evidência recorrente.

Em um workspace agregador ou monorepo, execute `init` na raiz comum e liste em
`project.repositories` os caminhos relativos de cada repositório. Assim, uma única
`.cordel/` pode manter necessidades, decisões, specs e evidências transversais, enquanto
o código e as provas locais continuam endereçados pelo caminho de cada repositório.

Por padrão, `init` integra Codex e Claude. Use `--codex`, `--claude` ou `--all` para
escolher os arquivos de agentes; use `--no-agent-files` quando essa integração for
gerenciada por outra ferramenta. Execuções posteriores atualizam somente o bloco entre
`<!-- cordel:start -->` e `<!-- cordel:end -->`.

## Como estudar o Cordel

Uma sequência recomendada para aprender o método:

1. [`method/manifesto.md`](method/manifesto.md): princípios e cadeia mínima;
2. [`method/concepts.md`](method/concepts.md): vocabulário compartilhado;
3. [`method/ai-driven-development.md`](method/ai-driven-development.md): SDD, agentes,
   skills, MCPs, harness e conceitos complementares;
4. [`method/catalog.md`](method/catalog.md): técnicas, padrões e antipadrões;
5. [`method/traceability.md`](method/traceability.md): relações entre artefatos;
6. [`method/adoption.md`](method/adoption.md): roteiro para um piloto.
7. [`method/team-knowledge.md`](method/team-knowledge.md): crescimento documental e uso em equipe.

Depois, consulte os workflows em
[`skill/cordel/references/`](skill/cordel/references/)
e os modelos em
[`skill/cordel/assets/templates/`](skill/cordel/assets/templates/).

## Organização do repositório

- `method/`: manifesto, conceitos, fundamentos de IA, catálogo, rastreabilidade, adoção e schema;
- `skill/`: implementação do método como skill para agentes;
- `skill/assets/templates/`: modelos de necessidade, story, spec, ADR e análise;
- `skill/cordel/scripts/cordel.py`: inicializador e verificador determinístico;
- `example/`: configuração fictícia de referência;
- `source/`: experiências que deram origem ao método e decisões de generalização.

## Limites atuais

Esta é a versão inicial do núcleo. Os validadores cobrem apenas invariantes portáteis.
Regras particulares de arquitetura, frontmatter, CI, banco ou deploy devem ser declaradas
pelo projeto, não incorporadas silenciosamente ao método. O julgamento sobre escopo,
prioridade, risco e ambiguidades de negócio continua sendo responsabilidade humana.

> A configuração v3 usa `.cordel/`. Projetos que adotaram as versões experimentais em
> `.evidence-method/` ou `.ai-dev-kit/` devem migrar os caminhos antes de executar `check`.
