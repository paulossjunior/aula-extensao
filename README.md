# Curso de Extensão: Desenvolvimento de Produto Baseado em Hipótese

Repositório principal de material, cronograma e estruturação do curso de extensão focado em Lean Startup, Design Centrado no Humano e Validação Rápida.

🔗 **[Visite a Documentação Oficial](https://paulossjunior.github.io/aula-extensao/)** 

## 📖 Sobre o Curso

O objetivo deste curso é guiar os alunos desde a identificação de um problema real até a prototipação e validação de um produto (MVP) utilizando Inteligência Artificial e metodologias ágeis como o *Build-Measure-Learn*. 

## 🏗 Estrutura do Repositório

Este site é estático e gerado automaticamente através da ferramenta acadêmica **MkDocs** com o tema **Material for MkDocs**.

```text
aula-extensao/
├── Makefile                # Automação de comandos locais
├── mkdocs.yml              # Configuração global de menus e temas
└── docs/
    ├── index.md            # Landing Page do material
    └── plano-de-aula/
        ├── index.md        # Resumo da metodologia
        ├── cronograma.md   # Datas e aulas do curso
        └── aulas/          # Páginas individuais por aula
```

## 🛠 Como executar localmente

Se deseja fazer modificações ou rodar os arquivos localmente:

1. **Clone este repositório**
   ```bash
   git clone https://github.com/paulossjunior/aula-extensao.git
   ```

2. **Execute via Makefile** (Isso criará o `.venv` e instalará o mkdocs automaticamente)
   ```bash
   make run
   ```

3. **Acesse no navegador**  
   Abra `http://localhost:8000`

## 🚀 Deploy Automático (CI/CD)

O deploy é gerido pelo **GitHub Actions**. Todas as atualizações feitas na branch `main` são compiladas pela Action configurada (`.github/workflows/deploy.yml`) e publicadas no GitHub Pages nativamente sem uso de branch orfã (`gh-pages`).
