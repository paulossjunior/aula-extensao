# AGENTS.md — Curso de Extensão: Desenvolvimento de Projetos Suportado por IA

Instruções para agentes de IA que trabalham neste repositório. Este é um repositório de **conteúdo**, não de aplicação: o produto é um site estático de material didático.

---

## Sobre o projeto

Site do curso de extensão **Desenvolvimento de Projetos Suportado por IA**, publicado em <https://paulossjunior.github.io/aula-extensao/>.

- **Idioma:** português do Brasil, em todo o conteúdo
- **Público:** alunos de graduação em curso de extensão
- **Semestre vigente:** 29/07/2026 a 11/12/2026

---

## Stack

| Item | Valor |
|------|-------|
| Gerador | [MkDocs](https://www.mkdocs.org/) `1.6.1` |
| Tema | [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) `9.5.50` |
| Diagramas | Mermaid, pelo suporte nativo do Material (lib carregada de CDN em runtime) |
| Deploy | GitHub Actions → GitHub Pages nativo, sem branch `gh-pages` |

Versões fixadas em `requirements.txt`. **Não atualize sem necessidade** — o tema quebra com facilidade entre majors.

Extensões Markdown habilitadas: `admonition`, `tables`, `toc`, `pymdownx.details`, `pymdownx.superfences` com fence `mermaid`.

!!! warning "O que NÃO está habilitado"
    `pymdownx.tabbed` não está na configuração. Blocos de aba (`=== "Título"`) renderizam como texto solto. Use seções normais, ou habilite a extensão antes de usar.

---

## Estrutura do repositório

```text
aula-extensao/
├── AGENTS.md               # este arquivo
├── Makefile                # automação local
├── mkdocs.yml              # configuração, nav e validação
├── requirements.txt        # dependências fixadas
├── skills-lock.json        # skills instaladas via skills.sh
├── .agents/skills/         # conteúdo real das skills
├── .agent/skills/          # symlink para .agents/skills — shim do skills CLI, não apague
├── .github/workflows/      # deploy.yml
└── docs/
    ├── index.md            # porta de entrada, mapeia os quatro territórios
    ├── assets/psm-cid/     # figuras do framework PSM CID
    ├── comece-aqui/        # TUTORIAL — passo a passo guiado, faz uma vez
    ├── plano-de-aula/
    │   ├── index.md        # metodologia e estrutura da semana
    │   └── aulas/          # uma página por aula
    ├── entregas/           # GUIA PRÁTICO — o que entregar, como e até quando
    ├── cronograma/         # REFERÊNCIA — datas e prazos
    ├── avaliacao/          # REFERÊNCIA — critérios e fórmula da nota
    ├── referencia/         # REFERÊNCIA — comandos e sintaxe consultados o semestre todo
    ├── explicacoes/        # EXPLICAÇÃO — o porquê por trás do que se ensina
    ├── materiais/          # mapa da documentação, agrupado pelos quatro territórios
    └── modelos/            # templates e exemplos preenchidos
```

---

## Convenções de conteúdo

### Nomes de arquivo

- kebab-case minúsculo, sem acento
- páginas de aula: `aula-NN-AAAA-MM-DD.md`, com a data real da aula
- ao remarcar uma aula, **renomeie o arquivo** e atualize a data no corpo, a `nav` e todos os links

### Estrutura de uma página de aula

Fonte única da verdade: **[`docs/modelos/template.md`](docs/modelos/template.md)**. A sequência é:

```text
# Aula NN — Título
**Data:** … | **Horário:** … | **Local:** … | **Modalidade:** …
[⬇️ Baixar / Copiar Código Fonte da Aula](raw.githubusercontent…)
## Introdução            → contexto e o objetivo da aula, em prosa
## Materiais de Apoio    → opcional
## Discovery do Projeto  → o conteúdo
## Tarefas               → atividades com duração, formato e entregável
## Encerramento          → síntese + próxima aula + tarefa de casa
## Referências           → links verificados
```

!!! important "O objetivo da aula vive na Introdução"
    Toda aula precisa declarar, na Introdução, **o que o aluno sai sabendo fazer**. Não use seção separada de "Objetivos de Aprendizagem": as doze aulas seguem o padrão de objetivo em prosa, e a página [Entregas](docs/entregas/index.md) já nomeia o objetivo de cada aula em uma linha.

### Cada conteúdo tem um território — não escreva tudo na aula

A documentação segue o framework [Diátaxis](https://diataxis.fr). Antes de escrever, decida em qual dos quatro territórios o conteúdo vive:

| Território | Pasta | O que é | Marca de linguagem |
|-----------|-------|---------|--------------------|
| **Tutorial** | `docs/comece-aqui/` | Passo a passo guiado, do zero a um resultado que funciona. Feito uma vez | "Neste tutorial você…", passos numerados |
| **Guia prático** | `docs/entregas/` | Receita para quem já sabe o básico e tem um objetivo concreto | "Como fazer X" |
| **Referência** | `docs/referencia/`, `docs/cronograma/`, `docs/avaliacao/` | Descrição austera: comandos, tabelas, parâmetros. Consultada, não lida | Terceira pessoa, sem imperativo |
| **Explicação** | `docs/explicacoes/` | Por que existe, o que foi descartado, como se conecta | "Sobre X", "Por que Y" |

A **página de aula é um tutorial**: ela conduz o aluno pelo conteúdo daquele dia. Ela **não** é o depósito de tudo sobre o tema.

!!! danger "O erro que este repositório já cometeu"
    A Aula 07 chegou a 642 linhas porque acumulou tabela de comandos `git`, especificação do SemVer e dois workflows YAML inteiros — **referência presa dentro de tutorial**, alcançável só por quem lembrasse a data da aula. O sintoma que denuncia isso: um índice que precisa apontar para âncora no meio de uma aula.

    Ao escrever uma aula, pergunte de cada bloco: *o aluno vai voltar aqui depois da aula?* Se sim, ele é referência — crie ou amplie a página em `docs/referencia/` e deixe na aula o ensino mais um link.

!!! warning "Regra única, lugar único"
    Regra de nota vive em `docs/avaliacao/`. Mecânica de entrega vive em `docs/entregas/`. Datas vivem em `docs/cronograma/`. Nenhuma das três se repete nas outras: o `mkdocs build --strict` valida links, **não** detecta duas versões divergentes da mesma regra.

### Admonitions

Use os blocos do Material para separar níveis de atenção:

```markdown
!!! tip "Dica"
!!! note "Observação"
!!! warning "Atenção"
!!! danger "Risco de perder nota"
!!! abstract "Conexão com outra aula"
!!! example "Exemplo concreto"
```

### Links e referências

- **Verifique todo link externo antes de publicar.** Vários links herdados do material antigo estavam mortos
- Links internos sempre relativos, terminando em `.md`
- Ao citar outra aula, use o caminho relativo real do arquivo — os números de aula já mudaram várias vezes

---

## Regras operacionais

1. **Leia este arquivo antes de agir.**
2. **Apresente um plano e aguarde aprovação explícita** antes de criar arquivos, mover conteúdo ou rodar comandos que alterem o repositório.
3. **Atualize a `nav` do `mkdocs.yml`** ao adicionar ou renomear página.
4. **Rode `mkdocs build --strict` antes de considerar o trabalho pronto.** A configuração valida âncoras: link para heading inexistente derruba o build, e o CI usa o mesmo comando.
5. **Não crie arquivo de conteúdo fora de `docs/`.**
6. **Consistência entre páginas é obrigação.** Mudar data, título ou numeração de aula exige varrer cronograma, avaliação, entregas, `nav` e as referências cruzadas entre aulas.
7. **Não invente número, data nem referência.** Calcule datas contra o calendário real e verifique URLs.

---

## Comandos

```bash
make install    # cria .venv e instala as dependências fixadas
make serve      # servidor local com hot-reload em :8000
make build      # gera site/ estático
make clean      # remove .venv e site/
make run        # install + serve
```

Para validar como o CI valida:

```bash
.venv/bin/mkdocs build --strict
```

---

## Skills

O repositório usa o ecossistema [skills.sh](https://www.skills.sh/), com as skills registradas em `skills-lock.json` — origem e hash de cada uma.

```bash
npx skills find <termo>            # buscar
npx skills add <owner/repo@skill>  # instalar
npx skills check                   # verificar atualizações
npx skills update
npx skills init <nome>             # criar uma skill própria
```

!!! note "Sobre os dois diretórios de skills"
    O conteúdo real fica em `.agents/skills/`. O diretório `.agent/skills/` contém um **symlink** para ele, criado pelo skills CLI para compatibilidade com agentes que procuram nesse caminho. **Não é duplicação e não deve ser removido.**

---

## Deploy

Push na `main` dispara `.github/workflows/deploy.yml`, que roda `mkdocs build --strict` e publica no GitHub Pages. Build com warning **falha** o deploy — é intencional.
