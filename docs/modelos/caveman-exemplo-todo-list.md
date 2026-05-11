# Exemplo — TODO List usando Caveman

> **Exemplo preenchido:** Este material mostra como usar Caveman em um projeto simples de lista de tarefas. A ideia não é substituir o exemplo de SDD com Spec-Kit, mas mostrar como pedir respostas mais curtas para revisar spec, tasks, bugs, commits e PRs.

[Baixar / Copiar Código Fonte do Exemplo](https://raw.githubusercontent.com/paulossjunior/aula-extensao/main/docs/modelos/caveman-exemplo-todo-list.md)

---

## 1. Cenário

| Campo | Descrição |
|-------|-----------|
| Produto | ListaJá |
| Tipo | TODO List simples |
| Stack sugerida | React + Vite + TypeScript no front; API REST opcional |
| Objetivo da feature | Usuário cria, conclui, edita e remove tarefas |
| Objetivo didático | Usar Caveman para reduzir verbosidade sem perder informação técnica |

Neste exemplo, vamos imaginar que o grupo já tem uma feature definida:

> Como usuário, quero registrar tarefas com título, status e prazo opcional, para acompanhar o que preciso fazer.

O Caveman será usado em quatro momentos:

1. resumir a spec
2. revisar tasks
3. explicar e corrigir bug
4. gerar review e commit

---

## 2. Ativando o modo conciso

Se o Caveman estiver instalado:

```text
/caveman lite
```

ou, no Codex:

```text
$caveman
```

Se o grupo não instalou o Caveman, use o prompt manual:

```text
Responda de forma concisa.
Preserve: causa, ação, teste e risco.
Remova: cortesia, repetição e explicação genérica.
```

!!! tip "Quando usar cada nível"
    Use `lite` para explicações em sala, `full` para bugs e revisão técnica, e `ultra` para checklist rápido. Se a decisão envolver arquitetura, segurança ou dados sensíveis, peça expansão pontual antes de implementar.

---

## 3. Exemplo 1 — Resumir a Spec

### Pedido ao agente

```text
/caveman lite
Resuma esta spec de TODO List em até 8 linhas.
Formato:
Objetivo:
Atores:
Fluxo:
Regras:
Dados:
Riscos:
```

### Spec de entrada

```text
O usuário precisa criar tarefas com título obrigatório, descrição opcional,
prazo opcional e status. A tela deve listar tarefas pendentes e concluídas.
O usuário pode marcar uma tarefa como concluída, reabrir, editar título e
excluir tarefas. Tarefas sem título não podem ser salvas. O sistema deve
preservar as tarefas ao recarregar a página.
```

### Resposta esperada em modo conciso

```text
Objetivo: gerenciar tarefas com criação, edição, conclusão e exclusão.
Atores: usuário final.
Fluxo: criar tarefa, listar, alterar status, editar, excluir.
Regras: título obrigatório; descrição e prazo opcionais.
Dados: id, título, descrição, status, prazo, criadoEm.
Persistência: manter tarefas após recarregar página.
Riscos: perder dados no refresh; salvar tarefa vazia; status inconsistente.
```

### O que observar

- A resposta preserva objetivo e regras.
- A resposta corta explicações óbvias.
- O grupo consegue revisar a feature antes de gerar plano técnico.

---

## 4. Exemplo 2 — Revisar Tasks

### Tasks geradas pelo agente

```markdown
- [ ] Criar componente TodoForm
- [ ] Criar componente TodoList
- [ ] Salvar tarefas no localStorage
- [ ] Implementar filtro por status
- [ ] Adicionar botão de concluir tarefa
- [ ] Criar teste de renderização da lista
```

### Pedido ao agente

```text
/caveman full
Revise estas tasks contra a spec.
Liste apenas lacunas.
Formato: problema — correção.
```

### Resposta esperada

```text
Sem validação de título — adicionar task para bloquear título vazio.
Sem edição — adicionar task para editar título/descrição/prazo.
Sem exclusão — adicionar task para remover tarefa.
Teste fraco — adicionar testes para criar, concluir, editar, excluir e persistir.
Filtro não está na spec — manter só se grupo decidir como requisito.
```

### Versão ajustada das tasks

```markdown
- [ ] Criar modelo `Todo`
- [ ] Criar componente `TodoForm`
- [ ] Validar título obrigatório
- [ ] Criar componente `TodoList`
- [ ] Criar ação de concluir/reabrir tarefa
- [ ] Criar ação de editar tarefa
- [ ] Criar ação de excluir tarefa
- [ ] Persistir tarefas no localStorage
- [ ] Testar criação com título válido
- [ ] Testar bloqueio de título vazio
- [ ] Testar concluir, reabrir, editar e excluir
- [ ] Testar persistência após recarregar
```

### O que observar

A resposta curta não implementa nada, mas melhora a lista de trabalho. Esse é um bom uso do Caveman: revisão rápida antes de codar.

---

## 5. Exemplo 3 — Explicar Bug

### Bug encontrado

Ao clicar duas vezes rápido em "Adicionar", a mesma tarefa aparece duplicada.

### Pedido ao agente

```text
/caveman full
Explique este bug e sugira correção.
Formato:
Causa:
Correção:
Teste:
Risco:
```

### Resposta esperada

```text
Causa: submit dispara duas vezes antes do estado atualizar.
Correção: desabilitar botão durante submit ou impedir submit duplicado por id/título+timestamp.
Teste: duplo clique em "Adicionar" deve criar uma tarefa só.
Risco: bloquear submit para sempre se erro não reativar botão.
```

### Correção sugerida no front

```tsx
import { FormEvent, useState } from "react";

type Todo = {
  id: string;
  title: string;
  done: boolean;
};

type TodoFormProps = {
  onAdd: (todo: Todo) => void;
};

export function TodoForm({ onAdd }: TodoFormProps) {
  const [title, setTitle] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    const normalizedTitle = title.trim();
    if (!normalizedTitle || isSubmitting) {
      return;
    }

    setIsSubmitting(true);

    onAdd({
      id: crypto.randomUUID(),
      title: normalizedTitle,
      done: false,
    });

    setTitle("");
    setIsSubmitting(false);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={title}
        onChange={(event) => setTitle(event.target.value)}
        placeholder="Nova tarefa"
      />
      <button type="submit" disabled={isSubmitting || !title.trim()}>
        Adicionar
      </button>
    </form>
  );
}
```

### Revisão crítica

Essa correção resolve parte do problema, mas ainda merece atenção: em React, duas chamadas síncronas podem ocorrer antes de a UI refletir `disabled`. Para um caso simples, isso costuma bastar. Para uma API real, a proteção também deve existir no servidor, usando idempotência ou regra de unicidade.

Boa continuação para o agente:

```text
Expanda só o risco.
Esta proteção no front basta se houver API?
Responda com: risco, correção no back, teste.
```

Resposta esperada:

```text
Risco: front não garante unicidade; requisições duplicadas ainda podem chegar.
Back: aceitar `clientRequestId` único ou aplicar regra de duplicidade por usuário+título+janela.
Teste: enviar duas requisições iguais em paralelo; API deve criar uma só.
```

---

## 6. Exemplo 4 — Revisão de PR

### Pedido ao agente

```text
/caveman-review
Revise este PR da TODO List.
Procure bugs de validação, estado e persistência.
Formato: arquivo:linha — problema — correção.
```

### Resposta esperada

```text
TodoForm.tsx:18 — título com espaços passa. Usar `trim()` antes de validar.
TodoList.tsx:34 — `index` usado como key. Usar `todo.id`.
useTodos.ts:22 — localStorage parse pode quebrar. Tratar JSON inválido.
useTodos.ts:41 — edição não persiste. Salvar após atualizar estado.
```

### O que observar

Esse formato é útil porque cada comentário vira uma ação clara. Se o agente responder com recomendações genéricas, peça:

```text
Reescreva em comentários acionáveis.
Cada linha deve ter arquivo, problema e correção.
```

---

## 7. Exemplo 5 — Commit

### Pedido ao agente

```text
/caveman-commit
Gere uma mensagem Conventional Commit para:
- bloqueia tarefa sem título
- evita duplicidade por duplo clique
- adiciona teste de criação
Assunto com até 50 caracteres.
```

### Resposta esperada

```text
fix: prevent invalid todo creation
```

### Versão com corpo

```text
fix: prevent invalid todo creation

Blocks blank titles, reduces double-submit, and adds creation test.
```

---

## 8. Exemplo 6 — Checklist Final

### Pedido ao agente

```text
/caveman ultra
Crie checklist final antes do PR.
Máximo 8 itens.
```

### Resposta esperada

```markdown
- [ ] título vazio bloqueado
- [ ] criar tarefa funciona
- [ ] concluir/reabrir funciona
- [ ] editar tarefa funciona
- [ ] excluir tarefa funciona
- [ ] refresh preserva dados
- [ ] JSON inválido não quebra app
- [ ] testes passam
```

---

## 9. Comparação: Resposta Normal x Caveman

| Situação | Resposta normal tende a | Resposta Caveman deve |
|----------|--------------------------|------------------------|
| Bug | explicar muito contexto | mostrar causa, correção, teste e risco |
| Spec | reescrever tudo | resumir decisões verificáveis |
| Tasks | elogiar e sugerir melhorias genéricas | apontar lacunas acionáveis |
| PR | fazer comentários longos | produzir linha com arquivo, problema e correção |
| Commit | narrar mudanças | gerar mensagem curta e rastreável |

---

## 10. Prompt Base para o Grupo

Use este bloco quando quiser aplicar o estilo Caveman sem instalar nada:

```text
Responda de forma concisa, técnica e acionável.
Preserve:
- causa
- decisão
- ação
- teste
- risco

Remova:
- cortesia
- repetição
- contexto óbvio
- explicação genérica

Formato:
Contexto:
Causa:
Ação:
Teste:
Risco:
```

---

## 11. Entregável sugerido

Cada grupo deve aplicar este fluxo em uma feature real do projeto e registrar no MkDocs:

1. prompt usado
2. resposta original do agente
3. versão concisa
4. informação preservada
5. informação perdida
6. decisão final do grupo

O objetivo não é falar menos por falar menos. É chegar mais rápido à decisão certa, com menos ruído e mais rastreabilidade.
