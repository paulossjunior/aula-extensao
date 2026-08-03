# Curso de Extensão: Desenvolvimento de Projetos Suportado por IA

Repositório de material, cronograma, avaliação e especificação de entregas do curso de extensão.

🔗 **[Visite a documentação oficial](https://paulossjunior.github.io/aula-extensao/)**

## 📖 Sobre o curso

O objetivo é **desenvolver projetos de software suportados por Inteligência Artificial**, do entendimento do problema até o produto rodando e sendo monitorado em produção.

O curso percorre quatro fases: entender o problema, decidir o que construir, construir e operar. Cada grupo entrega um **produto real em produção** que resolve um problema concreto do campus, com potencial de escalar para a comunidade externa.

- **Período:** 29/07/2026 a 11/12/2026
- **Segundas, 11h20–13h00:** aula de conteúdo, presencial no Lab 207
- **Terças, 13h50–16h30:** exercícios e trabalho de grupo, a distância

## 🏗 Estrutura do repositório

Site estático gerado com **MkDocs** e tema **Material for MkDocs**.

```text
aula-extensao/
├── AGENTS.md               # instruções para agentes de IA que editam este repo
├── Makefile                # automação local
├── mkdocs.yml              # configuração, nav e validação de links
├── requirements.txt        # dependências fixadas
├── skills-lock.json        # skills instaladas via skills.sh
├── .github/workflows/      # deploy.yml — build strict + GitHub Pages
└── docs/
    ├── index.md            # landing page
    ├── assets/psm-cid/     # figuras do framework PSM CID
    ├── plano-de-aula/
    │   ├── index.md        # metodologia e estrutura da semana
    │   └── aulas/          # uma página por aula
    ├── cronograma/         # datas, feriados e apresentações
    ├── avaliacao/          # critérios e fórmula da nota
    ├── entregas/           # exercícios, prazos e regras de entrega
    ├── materiais/          # catálogo de apoio
    └── modelos/            # templates e exemplos preenchidos
```

## 🛠 Como executar localmente

```bash
git clone https://github.com/paulossjunior/aula-extensao.git
cd aula-extensao
make run          # cria o .venv, instala as dependências e sobe o servidor
```

Acesse `http://localhost:8000`.

Outros alvos: `make install`, `make serve`, `make build`, `make clean`.

## ✅ Antes de abrir PR

```bash
.venv/bin/mkdocs build --strict
```

É o mesmo comando do CI. A configuração valida links internos **e âncoras**: apontar para um heading que não existe derruba o build.

## 🚀 Deploy

Push na `main` dispara o [workflow de deploy](.github/workflows/deploy.yml), que roda o build estrito e publica no GitHub Pages nativamente, sem branch órfã.

## 🤖 Editando com agente de IA

Leia o [`AGENTS.md`](AGENTS.md) primeiro. Ele documenta a stack, as convenções de página de aula, o que **não** está habilitado no Markdown e as regras de consistência entre cronograma, avaliação e entregas.
