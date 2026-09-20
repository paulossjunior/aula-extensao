# Criando o seu repositório de entregas

Neste tutorial você monta, do zero, o **repositório individual** onde todas as suas entregas do semestre vão morar. Ao final, ele estará no ar no GitHub com a estrutura correta, a primeira pasta de aula criada e o índice funcionando.

São 20 minutos. Faça uma vez só, na primeira semana, e use o resto do semestre.

!!! note "O que você precisa ter antes de começar"
    - Uma conta no [GitHub](https://github.com)
    - Git instalado na máquina — confirme com `git --version` no terminal
    - Um editor de texto qualquer

---

## Passo 1 — Criar o repositório no GitHub

1. Entre no GitHub e clique em **New repository**.
2. Em **Repository name**, escreva `extensao-ia-SEU-NOME` — por exemplo, `extensao-ia-maria-silva`.
3. Marque **Public**. O repositório precisa ser público para ser corrigido.
4. Marque **Add a README file**.
5. Clique em **Create repository**.

Pronto: o repositório existe. A barra de endereços agora mostra algo como `github.com/maria-silva/extensao-ia-maria-silva`. Guarde essa URL — é ela que você vai informar ao professor.

---

## Passo 2 — Trazer o repositório para a sua máquina

No terminal, dentro da pasta onde você guarda seus projetos:

```bash
git clone https://github.com/SEU-USUARIO/extensao-ia-SEU-NOME.git
cd extensao-ia-SEU-NOME
```

Se o `clone` funcionou, você está dentro de uma pasta que contém um `README.md`. Confirme:

```bash
ls
```

A saída deve ser `README.md`.

---

## Passo 3 — Criar a pasta da primeira aula

Cada aula ganha **uma pasta**, no formato `aula-NN-tema`. A da Aula 01 se chama `aula-01-processo-de-software`:

```bash
mkdir aula-01-processo-de-software
```

Dentro dela, crie o `README.md` que explica o que foi feito:

```bash
cat > aula-01-processo-de-software/README.md <<'TXT'
# Aula 01 — Visão Geral do Processo de Software

## O que foi feito

(descreva aqui o que você produziu nesta entrega)

## O que eu aprendi

(um parágrafo sobre o que ficou claro e o que ainda não ficou)
TXT
```

!!! warning "A pasta não é detalhe de organização"
    É ela que separa uma entrega da outra, e o README dentro dela é o que comprova qual conteúdo aquela entrega demonstra. **Arquivo solto na raiz do repositório não é avaliado** — não há como corrigir o que não se sabe a que aula pertence.

---

## Passo 4 — Escrever o README da raiz

O `README.md` da raiz é a porta de entrada do seu repositório. Ele precisa de quatro coisas: quem você é, qual disciplina, o link do seu mini-curso no YouTube (mesmo que ainda não exista) e o **índice das entregas**.

Abra o `README.md` no editor e substitua o conteúdo por:

```markdown
# Curso de Extensão — Desenvolvimento de Projetos Suportado por IA

**Aluno:** Seu Nome Completo
**Disciplina:** Curso de Extensão — Desenvolvimento de Projetos Suportado por IA
**Mini-curso no YouTube:** (link será publicado aqui)

## Índice de entregas

| Aula | Pasta | Status |
|------|-------|--------|
| 01 — Visão Geral do Processo de Software | [aula-01-processo-de-software](aula-01-processo-de-software/) | ✅ |
```

A cada entrega nova, você acrescenta uma linha nessa tabela. É assim que o professor encontra o que corrigir.

---

## Passo 5 — Publicar

```bash
git add .
git commit -m "chore: estrutura inicial do repositório de entregas"
git push origin main
```

Recarregue a página do repositório no GitHub. Você deve ver o README novo, com a tabela, e a pasta `aula-01-processo-de-software` na listagem.

**Se você chegou até aqui, o repositório está pronto para o semestre inteiro.**

---

## O que você acabou de construir

```text
extensao-ia-seu-nome/
├── README.md                          # você, disciplina, YouTube, índice
└── aula-01-processo-de-software/
    └── README.md                      # o que foi feito e o que aprendi
```

A cada aula, o movimento é sempre o mesmo: criar a pasta, escrever o README dela, acrescentar a linha no índice, commitar e empurrar.

---

## Próximos passos

- **Entregas que contêm código** precisam de mais três peças — arquitetura, base de conhecimento e comentários que explicam decisão. O que é cada uma e onde ela vive: [Especificação de Entregas](../entregas/index.md#os-tres-requisitos-de-todo-codigo-entregue).
- **A Aula 01 também pede o portal do grupo**, que é outro repositório. O passo a passo está em [Publicando o portal do seu grupo](publicar-portal-do-grupo.md).
- **Os prazos** de cada entrega estão no [calendário de entregas](../entregas/index.md#calendario-de-entregas-exercicios-individuais).

!!! tip "Commite sob a sua própria conta"
    Os commits precisam estar no seu nome — é parte de como a autoria é verificada. Confirme com `git config user.email` e ajuste se necessário:

    ```bash
    git config --global user.name "Seu Nome"
    git config --global user.email "email-da-sua-conta-github@exemplo.com"
    ```
