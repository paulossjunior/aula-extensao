# Publicando o portal do seu grupo

Neste tutorial o seu grupo coloca no ar um **portal de documentação MkDocs**, publicado no GitHub Pages e atualizado sozinho a cada alteração. É a entrega da [Aula 01](../plano-de-aula/aulas/aula-01-2026-08-03.md), e é onde o PRD, a arquitetura e as decisões do produto vão morar até o fim do semestre.

São 30 minutos. Ao final, o grupo terá uma URL pública funcionando.

!!! note "O que o grupo precisa ter antes de começar"
    - Um repositório no GitHub para o **produto do grupo** — um só, compartilhado
    - Python 3 instalado — confirme com `python3 --version`
    - Git instalado

!!! tip "Faça este tutorial uma pessoa por vez, com o grupo junto"
    Uma pessoa executa e empurra; as outras clonam depois. Fazer em paralelo no primeiro dia só produz conflito.

---

## Passo 1 — Clonar o repositório do grupo

```bash
git clone https://github.com/ORGANIZACAO-OU-DONO/repositorio-do-grupo.git
cd repositorio-do-grupo
```

---

## Passo 2 — Instalar o MkDocs num ambiente isolado

Criar um ambiente virtual evita que as dependências do projeto se misturem com as da sua máquina:

```bash
python3 -m venv .venv
.venv/bin/pip install --upgrade pip
```

Agora fixe as versões num arquivo, para que todo o grupo e o servidor de publicação usem exatamente as mesmas:

```bash
cat > requirements.txt <<'TXT'
mkdocs==1.6.1
mkdocs-material==9.5.50
TXT

.venv/bin/pip install -r requirements.txt
```

!!! warning "Não use versões soltas"
    `mkdocs-material` sem número de versão parece prático até o dia em que uma atualização quebra o tema na véspera da apresentação. Versão fixada é o que torna o build reproduzível.

Impeça que o ambiente virtual e o site gerado sejam versionados:

```bash
cat >> .gitignore <<'TXT'
.venv/
site/
TXT
```

---

## Passo 3 — Criar a configuração e a primeira página

O `mkdocs.yml` fica na **raiz** do repositório e descreve o site inteiro:

```bash
cat > mkdocs.yml <<'TXT'
site_name: Nome do Produto do Grupo
site_description: Portal de documentação do produto
docs_dir: docs

theme:
  name: material
  language: pt
  features:
    - navigation.sections
    - navigation.top

plugins:
  - search:
      lang: pt

markdown_extensions:
  - admonition
  - tables
  - toc:
      permalink: true
  - pymdownx.details
  - pymdownx.superfences

nav:
  - Início: index.md
TXT
```

O conteúdo vive em `docs/`. Crie a pasta e a página inicial:

```bash
mkdir -p docs

cat > docs/index.md <<'TXT'
# Nome do Produto

## O problema

(um parágrafo sobre a dor que o produto resolve)

## O grupo

- Integrante 1
- Integrante 2
- Integrante 3
TXT
```

---

## Passo 4 — Ver o site rodando na sua máquina

```bash
.venv/bin/mkdocs serve
```

Abra `http://localhost:8000` no navegador. Você deve ver a página inicial com o tema Material.

Deixe esse comando rodando enquanto edita: ele recarrega o navegador sozinho a cada arquivo salvo. Para encerrar, `Ctrl+C`.

---

## Passo 5 — Publicar automaticamente com GitHub Actions

O site ainda só existe na sua máquina. Este workflow faz o GitHub construir e publicar o portal a cada alteração na `main`:

```bash
mkdir -p .github/workflows

cat > .github/workflows/deploy.yml <<'TXT'
name: Deploy MkDocs

on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7

      - name: Configure Python
        uses: actions/setup-python@v7
        with:
          python-version: 3.x
          cache: pip

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Build site
        run: mkdocs build --strict

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v5
        with:
          path: ./site

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v5
TXT
```

---

## Passo 6 — Ligar o GitHub Pages

Isto é feito **uma vez**, na interface do GitHub:

1. Abra o repositório do grupo no GitHub.
2. Vá em **Settings → Pages**.
3. Em **Source**, selecione **GitHub Actions**.

Não é preciso escolher branch nem pasta: o workflow do passo anterior entrega o site direto.

---

## Passo 7 — Empurrar e conferir

```bash
git add .
git commit -m "feat: portal de documentação do produto"
git push origin main
```

Abra a aba **Actions** do repositório. Você verá o workflow *Deploy MkDocs* rodando. Quando os dois jobs ficarem verdes — primeiro `build`, depois `deploy` —, o endereço aparece em **Settings → Pages**, no formato:

```text
https://SEU-USUARIO.github.io/repositorio-do-grupo/
```

**Essa é a URL que o grupo entrega na Aula 01.**

---

## Se algo deu errado

| Sintoma | Causa provável | O que fazer |
|---------|----------------|-------------|
| Job `build` falha em `pip install` | `requirements.txt` não foi commitado | `git add requirements.txt` e empurre de novo |
| Job `build` falha em `mkdocs build --strict` | Link interno apontando para arquivo ou heading que não existe | Leia a mensagem: ela diz o arquivo e o link. Corrija e empurre |
| Job `deploy` falha com erro de permissão | **Settings → Pages → Source** não está em *GitHub Actions* | Refaça o Passo 6 |
| Site no ar, mas sem estilo | `mkdocs-material` fora do `requirements.txt` | Acrescente a linha e empurre |

!!! tip "O `--strict` é seu aliado, não seu inimigo"
    Ele derruba o build quando um link interno está quebrado. Parece rigor excessivo até a primeira vez que ele impede o grupo de publicar um portal com metade dos links mortos na véspera da apresentação.

---

## Próximos passos

- **O portal não é entrega de uma aula só.** Ele evolui o semestre inteiro: o PRD entra na [Aula 02](../plano-de-aula/aulas/aula-02-2026-08-10.md), a arquitetura e as decisões vêm depois. **Qualidade da documentação vale 10 dos 50 pontos** do trabalho em grupo — critérios em [Avaliação](../avaliacao/avaliacao.md).
- **Rodar `mkdocs build --strict` antes de empurrar** evita descobrir o erro só no CI:

  ```bash
  .venv/bin/mkdocs build --strict
  ```

- **Este site que você está lendo usa exatamente essa configuração.** O código-fonte está em [github.com/paulossjunior/aula-extensao](https://github.com/paulossjunior/aula-extensao) — vale abrir o `mkdocs.yml` de lá quando o grupo quiser acrescentar um recurso novo.
