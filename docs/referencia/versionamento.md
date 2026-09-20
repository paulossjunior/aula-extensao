# Referência — Tags, SemVer e Conventional Commits

Página de consulta. Descreve o comportamento das tags do Git, as regras do Versionamento Semântico 2.0.0 e o formato Conventional Commits.

O ensino destes temas acontece na [Aula 07](../plano-de-aula/aulas/aula-07-2026-09-21.md); a automação que consome estas convenções está em [Referência — GitHub Actions](github-actions.md).

---

## Tags

Branch e tag apontam para um commit, mas se comportam de forma oposta:

- **Branch é um ponteiro móvel.** A cada commit novo, ela avança sozinha.
- **Tag é um ponteiro fixo.** Ela marca um commit específico e fica lá para sempre.

É por isso que a tag é o instrumento de versão: `v1.2.0` precisa significar o mesmo código hoje e daqui a seis meses.

Existem dois tipos:

| Tipo | Comando | O que guarda | Quando usar |
|------|---------|--------------|-------------|
| **Leve** (*lightweight*) | `git tag v1.2.0` | Só o apontamento para o commit | Marcação temporária e privada |
| **Anotada** (*annotated*) | `git tag -a v1.2.0 -m "..."` | Autor, data, mensagem e — se configurado — assinatura | **Sempre que a tag for uma versão publicada** |

Comandos:

```bash
# criar uma tag anotada no commit atual
git tag -a v0.1.0 -m "Primeira versão navegável do produto"

# criar tag num commit passado
git tag -a v0.1.0 9fceb02 -m "Primeira versão navegável do produto"

# listar, filtrando por padrão
git tag -l "v0.*"

# ver o que a tag guarda, com o commit que ela aponta
git show v0.1.0

# descobrir em que versão o código atual está
git describe --tags

# publicar UMA tag
git push origin v0.1.0

# publicar todas as tags locais que ainda não estão no remoto
git push origin --tags

# apagar localmente e no remoto
git tag -d v0.1.0
git push origin --delete v0.1.0
```

!!! danger "O erro que todo mundo comete uma vez"
    `git push` **não envia tags**. Você cria a tag, dá push, vê tudo verde e a tag não existe no GitHub — então o workflow de release nunca dispara e ninguém entende por quê.

    Use `git push origin v0.1.0` para uma tag específica, ou `git push --follow-tags` para enviar os commits junto com as tags anotadas que os acompanham.

---

## Versionamento Semântico (SemVer 2.0.0)

Um número de versão só é útil se significar a mesma coisa para todo mundo. O **Versionamento Semântico** define esse significado em uma frase:

> Dado um número de versão **MAJOR.MINOR.PATCH**, incremente a versão **MAJOR** quando fizer mudanças incompatíveis na API, a versão **MINOR** quando adicionar funcionalidade mantendo compatibilidade, e a versão **PATCH** quando corrigir bugs mantendo compatibilidade.

A palavra que carrega tudo é **compatibilidade**, não tamanho. Refatorar trinta arquivos sem mudar o comportamento visível é *patch*. Renomear um campo que a API devolve é *major*, mesmo que a mudança tenha três linhas.

| O que aconteceu no produto de comprovantes | Sobe | Fica |
|--------------------------------------------|------|------|
| Upload aceitava só PDF e agora aceita imagem também | MINOR | `1.3.0` |
| O botão de enviar não funcionava no celular e foi corrigido | PATCH | `1.2.1` |
| O endpoint `/comprovantes` passou a se chamar `/documentos` | MAJOR | `2.0.0` |
| O campo `horas` da resposta virou `cargaHoraria` | MAJOR | `2.0.0` |
| Texto de erro reescrito para ficar mais claro | PATCH | `1.2.1` |
| Tela nova de histórico do aluno, sem mexer no que existia | MINOR | `1.3.0` |

Quatro regras que resolvem a maior parte das dúvidas:

- **`0.y.z` é terreno livre.** Enquanto a versão começa com zero, o projeto está em desenvolvimento inicial e *qualquer coisa pode mudar a qualquer momento*. É onde um produto em construção passa a maior parte do tempo.
- **`1.0.0` é um compromisso**, não uma comemoração. Publica-se `1.0.0` quando o produto estiver em uso real e você estiver disposto a tratar quebra de compatibilidade como evento sério.
- **Pré-lançamento** vai depois de um hífen: `1.0.0-rc.1`, `1.0.0-beta.2`. Ele tem precedência **menor** que a versão final — `1.0.0-rc.1` vem antes de `1.0.0`.
- **Metadado de build** vai depois de um sinal de mais: `1.0.0+20260921`. Ele é **ignorado** na comparação de precedência; serve só para rastrear de qual build aquele artefato saiu.

!!! warning "O erro mais comum com SemVer"
    Subir MAJOR porque "foi uma entrega grande". SemVer não mede esforço, mede **quebra de contrato**. A pergunta certa é: *quem usa o que eu publiquei precisa mudar alguma coisa para continuar funcionando?* Se sim, MAJOR. Se não, e há coisa nova, MINOR. Se não, e só corrigiu, PATCH.

---

## Conventional Commits

Se a versão depende do tipo de mudança, e o tipo de mudança está descrito no commit, dá para **calcular a versão a partir do histórico** — desde que a mensagem siga um formato previsível. É o que faz a convenção **Conventional Commits**:

```text
<tipo>[escopo opcional]: <descrição>

[corpo opcional]

[rodapé opcional]
```

| Tipo | Significa | Efeito na versão |
|------|-----------|------------------|
| `feat` | Funcionalidade nova | **MINOR** |
| `fix` | Correção de bug | **PATCH** |
| `docs`, `style`, `refactor`, `test`, `chore`, `ci`, `build`, `perf` | Mudanças que não alteram o comportamento visível | Nenhum |
| Qualquer tipo com `!` ou com rodapé `BREAKING CHANGE:` | Quebra de compatibilidade | **MAJOR** |

Exemplos aplicados ao produto:

```text
feat(upload): aceita imagem JPEG e PNG além de PDF

fix(login): corrige botão de envio que não respondia no Safari do iOS

feat(api)!: renomeia o campo horas para cargaHoraria

BREAKING CHANGE: clientes que liam `horas` na resposta de
/comprovantes precisam passar a ler `cargaHoraria`.
```

!!! abstract "Conexão com a Aula 12"
    Escrever commit assim é o mesmo exercício de comunicação enxuta que a [Aula 12](../plano-de-aula/aulas/aula-12-2026-11-09.md) trabalha com o Caveman: dizer o máximo no mínimo de palavras, num formato que **máquina e humano** conseguem ler. A diferença é que aqui o leitor máquina calcula a sua versão.

---
