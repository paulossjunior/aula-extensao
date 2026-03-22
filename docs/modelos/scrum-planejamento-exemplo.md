# Exemplo de Planejamento Scrum — Plataforma de Pedidos para Pescadores

> **Exemplo preenchido:** Este arquivo demonstra como usar o template de planejamento Scrum com um caso fictício inspirado no contexto da comunidade e dos pescadores.

[⬇️ Baixar / Copiar Código Fonte do Exemplo](https://raw.githubusercontent.com/paulossjunior/aula-extensao/main/docs/modelos/scrum-planejamento-exemplo.md)

---

## 1. Visão Geral do Planejamento

| Campo              | Descrição |
|-------------------|-----------|
| Nome do Produto   | RedePesca |
| Equipe            | Grupo 02 |
| Product Owner     | Ana |
| Scrum Master      | Carlos |
| Data de Início    | 06/04/2026 |
| Objetivo Geral    | Criar uma solução digital simples para registrar pedidos de pescado, organizar entregas e melhorar a comunicação entre pescadores e compradores locais. |

---

## 2. Backlog do Produto

| ID | US/EPIC | Descrição | Importância | Status |
|----|---------|-----------|-------------|--------|
| EP-01 | EPIC | Cadastro e autenticação de usuários | Alta | Em andamento |
| EP-02 | EPIC | Gestão de pedidos de pescado | Alta | Em andamento |
| EP-03 | EPIC | Acompanhamento de status do pedido | Média | Pendente |
| US-01 | US | Como pescador, quero criar uma conta para acessar a plataforma | Alta | Concluído |
| US-02 | US | Como pescador, quero fazer login para acessar meu painel | Alta | Concluído |
| US-03 | US | Como pescador, quero registrar um novo pedido de pescado | Alta | Em andamento |
| US-04 | US | Como comprador, quero visualizar o status do meu pedido | Média | Pendente |
| US-05 | US | Como administrador, quero atualizar o status dos pedidos | Média | Pendente |

---

## 3. Planejamento Geral de Sprints

| Sprint | EPCs | US | Task |
|--------|------|----|------|
| Sprint 1 | EP-01 | US-01, US-02 | Criar cadastro, login e validação básica |
| Sprint 2 | EP-02 | US-03 | Criar formulário de pedido, salvar no banco e listar pedidos |
| Sprint 3 | EP-03 | US-04, US-05 | Exibir status, atualizar pedido e testar fluxo completo |
| Sprint 4 | EP-02, EP-03 | US-03, US-04, US-05 | Refinar interface, corrigir bugs e preparar demonstração |

---

## 4. Sprint 1

### Objetivo da Sprint

Disponibilizar o acesso inicial à plataforma por meio de cadastro e login.

### Itens Planejados

| EPC | US | Task | Responsável | Status |
|-----|----|------|-------------|--------|
| EP-01 | US-01 | Criar tela de cadastro | Ana | Concluído |
| EP-01 | US-01 | Implementar persistência do usuário | Carlos | Concluído |
| EP-01 | US-02 | Criar tela e fluxo de login | João | Concluído |

### Critérios de Conclusão

- [x] Usuário consegue criar conta
- [x] Usuário consegue fazer login
- [x] Dados básicos são armazenados corretamente

### Observações

> A equipe percebeu que será necessário validar o tipo de usuário no futuro, mas isso não entrou nesta sprint.

---

## 5. Sprint 2

### Objetivo da Sprint

Permitir que o pescador registre novos pedidos de pescado no sistema.

### Itens Planejados

| EPC | US | Task | Responsável | Status |
|-----|----|------|-------------|--------|
| EP-02 | US-03 | Criar formulário de pedido | Ana | Em andamento |
| EP-02 | US-03 | Criar tabela de pedidos no banco | Carlos | Em andamento |
| EP-02 | US-03 | Listar pedidos no painel | João | Pendente |

### Critérios de Conclusão

- [ ] Pedido pode ser cadastrado
- [ ] Pedido aparece no painel do pescador
- [ ] Informações básicas ficam registradas

### Observações

> O grupo decidiu começar com poucos campos no formulário para simplificar a primeira entrega.

---

## 6. Sprint 3

### Objetivo da Sprint

Permitir o acompanhamento e atualização do status dos pedidos.

### Itens Planejados

| EPC | US | Task | Responsável | Status |
|-----|----|------|-------------|--------|
| EP-03 | US-04 | Mostrar status do pedido no painel | Ana | Pendente |
| EP-03 | US-05 | Criar ação para atualizar status | Carlos | Pendente |
| EP-03 | US-04 | Validar fluxo completo com usuário teste | João | Pendente |

### Critérios de Conclusão

- [ ] Usuário visualiza o status do pedido
- [ ] Administrador atualiza o status
- [ ] Fluxo completo é testado

### Observações

> Esta sprint depende da estabilidade da Sprint 2.

---

## 7. Sprint 4

### Objetivo da Sprint

Refinar o produto para demonstração e validação final.

### Itens Planejados

| EPC | US | Task | Responsável | Status |
|-----|----|------|-------------|--------|
| EP-02 | US-03 | Melhorar usabilidade do formulário | Ana | Pendente |
| EP-03 | US-04 | Ajustar tela de acompanhamento | Carlos | Pendente |
| EP-02 | US-03 | Corrigir bugs e preparar demo | João | Pendente |

### Critérios de Conclusão

- [ ] Fluxo principal está funcional
- [ ] Interface está compreensível
- [ ] Produto pode ser demonstrado

### Observações

> A prioridade será garantir uma demonstração estável, mesmo que funcionalidades secundárias fiquem para depois.

---

## 8. Riscos e Dependências

| Item | Tipo | Impacto | Ação sugerida |
|------|------|---------|---------------|
| Tela de pedidos depende do login | Dependência técnica | Alto | Finalizar Sprint 1 antes de ampliar Sprint 2 |
| Falta de validação com usuários reais | Risco de produto | Alto | Marcar teste rápido com pescador ou representante |
| Mudanças no escopo do pedido | Risco de escopo | Médio | Priorizar apenas campos essenciais |

---

## 9. Revisão Geral

### O que foi concluído

Cadastro e login foram definidos como primeira entrega funcional do produto.

### O que precisa ser replanejado

A equipe ainda precisa decidir se o painel do comprador entra junto com o painel do pescador ou em sprint posterior.

### Próximos passos

Concluir o fluxo de cadastro de pedido, validar a experiência com usuários e atualizar o backlog conforme o aprendizado.
