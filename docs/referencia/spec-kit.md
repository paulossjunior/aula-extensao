# Referência — Spec-Kit e contexto do agente

Página de consulta. Reúne o que se digita e o que se escreve para dar contexto a um agente de IA: os comandos do **Spec-Kit**, o esqueleto do **`AGENTS.md`**, os comandos do **skills.sh**, e a rule e o comando `/epic-to-spec` que ligam os épicos ao fluxo de especificação.

O ensino destes temas está distribuído em quatro aulas — [09](../plano-de-aula/aulas/aula-09-2026-10-05.md) (Spec-Driven Development), [10](../plano-de-aula/aulas/aula-10-2026-10-19.md) (AGENTS.md e skills), [12](../plano-de-aula/aulas/aula-12-2026-11-09.md) (comunicação enxuta) e [13](../plano-de-aula/aulas/aula-13-2026-11-16.md) (épicos e Gherkin). Esta página existe para não obrigar ninguém a lembrar em qual delas cada comando foi visto.

---

## Instalação e fases do Spec-Kit

A instalação típica usa o gerenciador `uv`:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z
specify init meu-produto --integration claude
```

Também é possível rodar de forma efêmera com `uvx`, sem instalar globalmente. Depois do `init`, o projeto ganha uma pasta `.specify/` com os arquivos do toolkit.

A partir daí o trabalho acontece em fases, cada uma disparada por um slash-command dentro do agente:

1. **`/speckit.constitution`** — registra os **princípios do projeto**: padrões de qualidade, política de testes, expectativas de UX, restrições de performance. Gera `.specify/memory/constitution.md`. Pense nela como o "contrato" que o agente deve respeitar em todas as fases seguintes. Para um produto de envio de comprovantes de trabalhos complementares, por exemplo, a constitution pode dizer "todo envio gera protocolo rastreável com data e hora" e "o fluxo completo precisa funcionar em tela de celular".
2. **`/speckit.specify`** — descreve **o quê** e **por quê** da feature, sem decidir stack. Gera `specs/[FEATURE]/spec.md` com user stories e requisitos. Para a feature *"o pescador registra um pedido e acompanha seu status"*, esta fase produziria as histórias, os atores e os critérios de aceitação.
3. **`/speckit.clarify`** *(opcional, mas recomendado)* — faz perguntas estruturadas para reduzir ambiguidade antes do plano técnico. As respostas são registradas no próprio spec. É a parte que mais costuma puxar o time para fora do "achismo".
4. **`/speckit.plan`** — agora sim entra o **como**: stack, arquitetura, contratos, modelo de dados. Gera `plan.md`, `research.md`, `data-model.md` e uma pasta `contracts/`.
5. **`/speckit.tasks`** — quebra o plano em tarefas ordenadas, com dependências explícitas e marcadores `[P]` para o que pode rodar em paralelo, organizadas por user story e em estilo TDD.
6. **`/speckit.implement`** — executa as tarefas em ordem, gerando o código.
7. **Validação opcional** — `/speckit.analyze` checa consistência entre os artefatos gerados; `/speckit.checklist` aplica listas de qualidade sobre o conjunto.

Não é obrigatório usar todas as fases. Em features simples, ir direto de `/speckit.specify` para `/speckit.implement` pode ser suficiente. Em features grandes, pular fases costuma cobrar caro depois.

---

## Esqueleto do `AGENTS.md`

```markdown
# AGENTS.md

## Sobre o projeto
Sistema de envio de comprovantes de trabalhos complementares.
Aluno fotografa o comprovante pelo celular; a coordenação valida e o
sistema devolve protocolo rastreável.

## Stack
- Back-end: FastAPI + PostgreSQL, em `api/`
- Front-end: React + Vite, em `web/`
- Deploy: Docker Compose, `docker/`

## Comandos
- Testes: `make test`
- Lint: `make lint`
- Subir local: `make up`

## Convenções
- Conventional Commits em português
- Branch: `feat/<descricao-curta>`
- Toda rota nova precisa de teste de integração

## Restrições
- Nunca commitar `.env`
- Nunca alterar migrations já aplicadas — criar uma nova
- Todo envio precisa gerar protocolo com data e hora
```

!!! tip "Regra de ouro: escreva o que você repetiria"
    Se você já explicou a mesma coisa ao agente duas vezes, ela pertence ao `AGENTS.md`. Se está lá e o agente ignora, o texto está longo demais ou ambíguo demais — corte, não aumente.

---

## `AGENTS.md` e constitution: camadas diferentes

A constitution do Spec-Kit e o `AGENTS.md` não competem: cobrem camadas diferentes.

| | `AGENTS.md` | Constitution do Spec-Kit |
|---|---|---|
| Responde | *Como se trabalha neste repositório?* | *Que princípios o produto não pode violar?* |
| Escopo | Operacional — comandos, pastas, convenções | Qualidade — testes, performance, UX, restrições |
| Quem lê | Qualquer agente, a qualquer momento | O fluxo do Spec-Kit, em todas as fases |
| Exemplo | "testes rodam com `make test`" | "toda tela precisa funcionar em conexão fraca" |

O encaixe prático:

```text
AGENTS.md          →  contexto permanente do repositório
    ↓
/speckit.constitution  →  princípios do produto
    ↓
/speckit.specify       →  o que construir  (entra o épico da Aula 13)
    ↓
/speckit.plan          →  como construir
    ↓
/speckit.tasks         →  em que ordem      (aqui entra a DSM da EaD 07)
    ↓
/speckit.implement     →  código
```

!!! warning "Duplicar é pior que não ter"
    Se a mesma regra aparece no `AGENTS.md` e na constitution com redações diferentes, o agente segue uma delas, e não há como saber qual. **Uma regra, um lugar.** Convenção de repositório vai no `AGENTS.md`; princípio de produto vai na constitution.

---

## skills.sh — capacidades instaláveis

Uma **skill** é um pacote de instruções para uma tarefa específica: revisar PR, escrever changelog, gerar documentação, montar um deploy. O [skills.sh](https://www.skills.sh/) é o catálogo onde essas skills são publicadas e de onde são instaladas por comando.

```bash
npx skills find docs mkdocs        # buscar skills por palavra-chave
npx skills add <owner/repo@skill>  # instalar
npx skills check                   # verificar atualizações
npx skills update                  # atualizar todas
npx skills init minha-skill        # criar a sua
```

A instalação grava um `skills-lock.json`, com origem e *hash* de cada skill — o mesmo princípio de `package-lock.json` ou `uv.lock`: **a capacidade do agente vira dependência versionada e reproduzível**.

!!! abstract "Este repositório usa exatamente isso"
    O curso tem uma skill instalada, `find-skills`, registrada em [`skills-lock.json`](https://github.com/paulossjunior/aula-extensao/blob/main/skills-lock.json) com origem `vercel-labs/skills` e hash de verificação. Qualquer pessoa que clone o repositório reproduz o mesmo conjunto de capacidades.

### As três camadas juntas

| Camada | Granularidade | Vive em | Muda com que frequência |
|--------|---------------|---------|--------------------------|
| `AGENTS.md` | O repositório inteiro | Raiz do projeto | Raramente |
| Constitution | O produto | `.specify/memory/` | Raramente |
| Skills | Uma tarefa | `skills-lock.json` + pasta de skills | Conforme a necessidade |

!!! tip "O teste para saber onde uma instrução vai"
    Pergunte **com que frequência ela muda** e **a quantas tarefas se aplica**.

    - Vale para tudo e quase nunca muda → `AGENTS.md`
    - É princípio de qualidade do produto → constitution
    - Serve a uma tarefa específica, repetida → skill

---

## Rule de projeto — epics como fonte

Uma **rule** é uma instrução persistente do projeto. Dependendo da ferramenta, ela pode viver em `AGENTS.md`, `CLAUDE.md`, `.cursor/rules/`, `.github/copilot-instructions.md` ou outro arquivo equivalente.

Texto da rule:

```markdown
# Project Rule — Epics como Fonte de Produto

Antes de especificar, planejar ou implementar uma feature, leia `docs/epics.md`.

Regras:
- Use `docs/epics.md` como fonte primária de escopo de produto.
- Trabalhe em apenas um épico por vez.
- Não implemente requisitos de outros épicos.
- Se o épico estiver ambíguo, marque como `[NEEDS CLARIFICATION]`.
- Não invente regra de negócio fora do épico sem pedir confirmação.
- Preserve rastreabilidade citando o ID/nome do épico na spec.
- Separe requisito funcional de detalhe técnico.
- Preserve os cenários Gherkin como critérios de aceitação.
- Não converta `Given/When/Then` em detalhes de implementação.
```

A rule não executa nada sozinha: muda o comportamento padrão do agente. Funciona como lembrete permanente de consultar a fonte de produto antes de especificar.

## Comando `/epic-to-spec`

O comando `/epic-to-spec` é um pré-processador. Ele lê `docs/epics.md`, encontra um único épico e transforma esse trecho em uma entrada limpa para o Spec-Kit.

O que o comando faz:

1. localizar o épico solicitado
2. ignorar todos os outros épicos
3. extrair objetivo, atores, user stories, regras, cenários Gherkin e fora de escopo
4. marcar lacunas com `[NEEDS CLARIFICATION]`
5. gerar um texto pronto para `/speckit.specify`

Texto do comando, em Markdown:

```markdown
# /epic-to-spec

Leia `docs/epics.md`.

Entrada esperada:
- ID ou nome do épico

Tarefa:
- Localizar o épico solicitado.
- Ignorar todos os outros épicos.
- Converter o épico em entrada para `/speckit.specify`.
- Separar requisitos funcionais de detalhes técnicos.
- Preservar user stories e cenários Gherkin.
- Marcar lacunas com `[NEEDS CLARIFICATION]`.
- Criar uma spec pequena, revisável e rastreável.

Formato da saída:
Epic:
Objetivo:
Atores:
User Stories:
Regras de negócio:
Cenários Gherkin:
Fora de escopo:
Dúvidas:
Prompt sugerido para /speckit.specify:
```

Uso esperado:

```text
/epic-to-spec Epic 01 — Cadastro e autenticação
```

Saída esperada:

```markdown
Epic: Epic 01 — Cadastro e autenticação

Objetivo:
Permitir que usuários criem conta e acessem o sistema.

Atores:
- visitante
- usuário cadastrado

User Stories:
- US-01 — Como visitante, quero criar conta com nome, e-mail e senha, para acessar o sistema.
- US-02 — Como usuário cadastrado, quero entrar com e-mail e senha, para acessar minha área autenticada.

Regras de negócio:
- e-mail deve ser único
- senha deve ter no mínimo 8 caracteres

Cenários Gherkin:

```gherkin
Feature: Cadastro de usuário

Scenario: Cadastro com dados válidos
  Given que sou um visitante na tela de cadastro
  When preencho nome, e-mail único e senha válida
  And envio o formulário
  Then minha conta deve ser criada
  And devo ser redirecionado para o painel

Scenario: Cadastro com e-mail já usado
  Given que existe um usuário cadastrado com o e-mail "ana@email.com"
  When tento criar uma conta com o e-mail "ana@email.com"
  Then o cadastro deve ser bloqueado
  And devo ver a mensagem "E-mail já cadastrado"
```

Fora de escopo:
- login social
- recuperação de senha

Dúvidas:
- [NEEDS CLARIFICATION] haverá confirmação de e-mail?

Prompt sugerido para /speckit.specify:
Crie uma spec para o Epic 01 — Cadastro e autenticação usando apenas as informações acima. Preserve as user stories e os cenários Gherkin como critérios de aceitação. Não implemente. Marque ambiguidades como [NEEDS CLARIFICATION].
```
