# Especificação de Exercícios e Trabalhos

Esta página define **o que entregar, como entregar e até quando**. Ela vale para as duas frentes: os exercícios individuais e o trabalho em grupo.

Os critérios de pontuação estão em [Avaliação](../avaliacao/avaliacao.md); aqui está a mecânica da entrega.

---

## Como entregar

### Um único repositório por aluno

Cada aluno mantém **um repositório público no GitHub**, na própria conta, informado ao professor no início do semestre. **Todos os exercícios do semestre vão nele** — não se cria repositório novo a cada entrega.

- **`README.md` na raiz** com: nome do aluno, disciplina, link do mini-curso no YouTube e o **índice das entregas**
- **Uma pasta por aula**, no formato `aula-NN-tema/`
- **`README.md` dentro de cada pasta**, explicando o que foi feito

!!! warning "Entrega fora da pasta não é avaliada"
    A pasta é o que separa uma entrega da outra, e o README é o que comprova qual conteúdo ela demonstra. Arquivo solto na raiz do repositório não tem como ser corrigido.

### Estrutura do repositório

```text
meu-repositorio/
├── README.md                          # aluno, disciplina, link do YouTube, índice
├── aula-01-processo-de-software/
│   ├── README.md                      # o que foi aplicado e o que aprendi
│   └── ...
├── aula-02-problema-e-mercado/
│   ├── README.md
│   ├── ARQUITETURA.md                 # quando houver código
│   ├── docs/                          # base de conhecimento
│   └── src/                           # código comentado
└── aula-03-prototipacao/
    ├── README.md
    └── ...
```

---

## Os três requisitos de todo código entregue

Sempre que a entrega **contiver código**, ela precisa das três peças abaixo. Sem elas, a entrega é considerada incompleta.

| Requisito | O que é | Onde vive |
|-----------|---------|-----------|
| **Arquitetura** | Os componentes do que foi construído e como se ligam: diagrama, ou descrição em texto se for pequeno. Deve dar para entender o desenho sem abrir o código | `ARQUITETURA.md` na pasta da aula |
| **Base de conhecimento** | O **porquê** daquela arquitetura: decisões tomadas, alternativas descartadas e o motivo, restrições que pesaram, o que você faria diferente | `docs/` na pasta da aula, ou seção no `README.md` |
| **Código comentado** | Comentários que explicam **decisão**, não sintaxe | No próprio código |

!!! tip "O que é um comentário útil"
    Ruim: `// incrementa o contador` — repete o que o código já diz.

    Bom: `// contamos por sessão e não por requisição porque o mesmo usuário reenvia o comprovante várias vezes até acertar o formato`.

    A régua: o comentário deve responder a uma pergunta que o código sozinho não responde.

!!! abstract "Por que exigir arquitetura e base de conhecimento"
    Uso de agente de IA é liberado neste curso. A ferramenta escreve o código; o que ela não faz é **justificar a decisão** em nome de quem entregou. Arquitetura e base de conhecimento são o que separa código gerado de código compreendido — e é isso que a entrevista verifica.

---

## Calendário de entregas — exercícios individuais

**Regra geral:** o exercício proposto na aula de segunda é trabalhado na sessão EaD de terça e vence **na aula da segunda-feira seguinte**. Caindo em feriado, passa para a próxima aula.

| Aula | Data da aula | Exercício | **Vence em** |
|------|--------------|-----------|--------------|
| [01](../plano-de-aula/aulas/aula-01-2026-08-03.md) | Seg, 03/08 | `aula-01-processo-de-software` | **Seg, 10/08** |
| [02](../plano-de-aula/aulas/aula-02-2026-08-10.md) | Seg, 10/08 | `aula-02-problema-e-mercado` | **Seg, 17/08** |
| [03](../plano-de-aula/aulas/aula-03-2026-08-17.md) | Seg, 17/08 | `aula-03-prototipacao` | **Seg, 24/08** |
| [04](../plano-de-aula/aulas/aula-04-2026-08-24.md) | Seg, 24/08 | `aula-04-clientes` | **Seg, 31/08** |
| [06](../plano-de-aula/aulas/aula-06-2026-09-14.md) | Seg, 14/09 | `aula-06-validacao-proposta` | **Seg, 21/09** |
| [07](../plano-de-aula/aulas/aula-07-2026-09-21.md) | Seg, 21/09 | `aula-07-scrum-e-dsm` | **Seg, 28/09** |
| [09](../plano-de-aula/aulas/aula-09-2026-10-05.md) | Seg, 05/10 | `aula-09-spec-driven-development` | **Seg, 19/10** ⚠️ |
| [10](../plano-de-aula/aulas/aula-10-2026-10-19.md) | Seg, 19/10 | `aula-10-agents-md-e-skills` | **Seg, 26/10** |
| [12](../plano-de-aula/aulas/aula-12-2026-11-09.md) | Seg, 09/11 | `aula-12-caveman` | **Seg, 16/11** |
| [13](../plano-de-aula/aulas/aula-13-2026-11-16.md) | Seg, 16/11 | `aula-13-epics-e-gherkin` | **Seg, 23/11** |
| [14](../plano-de-aula/aulas/aula-14-2026-11-23.md) | Seg, 23/11 | `aula-14-langchain` — **opcional** | Seg, 07/12 |
| [16](../plano-de-aula/aulas/aula-16-2026-12-07.md) | Seg, 07/12 | Aula extra — sem entrega | — |

⚠️ A entrega da Aula 09 pula duas semanas porque **12/10 é feriado**.

!!! danger "Prazo final do semestre"
    **Terça, 08/12/2026** é o último dia para entregar ou reenviar qualquer pendência. Depois dessa data nada é aceito.

---

## Detalhamento por aula

### `aula-01-processo-de-software` — vence 10/08

- Ciclo de um produto real preenchido, com o palpite sobre monitoramento justificado
- URL do portal MkDocs do grupo, publicado e acessível
- Os quatro riscos do projeto, um por fase do ciclo

### `aula-02-problema-e-mercado` — vence 17/08

- Parágrafo descrevendo o problema observado
- Tabela de soluções existentes, concorrentes e indicadores de sucesso, com justificativa
- PRD iniciado no portal do grupo

### `aula-03-prototipacao` — vence 24/08

- Requisitos macro do produto e o texto do prompt estruturado
- Link do Figma com as telas geradas, inserido em página do MkDocs
- Parágrafo com o principal aprendizado da validação de corredor

### `aula-04-clientes` — vence 31/08

- Mapa de atores com o usuário principal destacado
- Segmento-alvo escolhido, com justificativa
- Perfil do early adopter
- Seção 2 do PRD (Público-alvo) preenchida

### `aula-06-validacao-proposta` — vence 21/09

- Resumo estruturado da proposta
- Protótipo inicial
- Lista de ajustes apontados pelo professor
- Roteiro da reunião de validação com o cliente

### `aula-07-scrum-e-dsm` — vence 28/09

- Backlog inicial com prioridades
- Lista de features fim a fim priorizadas
- DSM com comentários sobre dependências e ordem de implementação
- Plano inicial de arquitetura e roadmap curto

### `aula-09-spec-driven-development` — vence 19/10

- Repositório com o Spec-Kit inicializado
- `.specify/memory/constitution.md` com os princípios reais do grupo
- `specs/[FEATURE]/spec.md` revisado
- `plan.md` e `tasks.md`, mais reflexão comparando a ordem proposta pelo agente com a DSM

### `aula-10-agents-md-e-skills` — vence 26/10

- `AGENTS.md` commitado, mais o relato do que o agente errou na primeira tentativa
- Constitution e `AGENTS.md` sem sobreposição, com a lista do que foi movido
- `skills-lock.json` e a skill própria versionada

### `aula-12-caveman` — vence 16/11

- Artefato do Spec-Kit anotado, com no mínimo cinco marcações de corte ou preservação
- Três versões da mesma resposta, com contagem de palavras
- Duas revisões reais do fluxo, com decisão do grupo
- Tabela de informação preservada × perdida

### `aula-13-epics-e-gherkin` — vence 23/11

- `docs/epics.md` versionado
- Arquivo de rule criado
- Comando `/epic-to-spec` salvo
- `spec.md`, `plan.md`, `tasks.md` gerados, com nota sobre divergências entre agente, épico e DSM

### `aula-14-langchain` — opcional, até 07/12

Desafio da Aula 14: refazer a crew em LangChain, com a tabela comparativa preenchida e a recomendação escrita.

---

## Trabalho em grupo

O produto de extensão é entregue no **repositório do grupo** — separado dos repositórios individuais.

- `README.md` na raiz com o **nome do grupo** e o **nome de todos os integrantes**
- Código do produto
- Portal de documentação MkDocs, evoluído desde a Aula 02
- Cada integrante commita sob a própria conta

### Os cinco itens avaliados

| Item | Pontos | O que se verifica |
|------|--------|-------------------|
| **Produto entregue** | 10 | O produto existe e funciona |
| **Entrega em ambiente de produção** | 10 | Está no ar, acessível, sendo usado por público real |
| **Qualidade da documentação** | 10 | Portal completo e atualizado: problema, público, arquitetura, decisões |
| **Qualidade do código** | 10 | Organização, legibilidade, comentários que explicam decisão, testes |
| **Apresentação** | 10 | Clareza e evidência nas apresentações mensais |

!!! danger "Produto não entregue zera o trabalho em grupo"
    Se o produto não for entregue, **o grupo recebe 0 nos 50 pontos** — não apenas no item "produto entregue". Documentação e qualidade de código de um produto que não existe não são avaliáveis.

### Apresentações mensais

Toda última segunda-feira do mês, sem conteúdo novo:

| Data | O que acontece |
|------|----------------|
| **Seg, 31/08** | Apresentação 1 · entrega da proposta de produto no Figma Maker · Checkpoint 1 |
| **Seg, 28/09** | Apresentação 2 · Checkpoint 2 |
| **Seg, 26/10** | Apresentação 3 · Checkpoint 3 |
| **Seg, 30/11** | Apresentação 4 · Checkpoint 4 |

### Entrevista — a porteira dos 50 pontos

A entrevista é **individual** e acontece nos quatro checkpoints práticos, nas mesmas datas das apresentações. Cada checkpoint resulta em **passou** ou **não passou**.

**É preciso passar nos quatro.** Falhar em um único checkpoint zera os 50 pontos do trabalho em grupo para aquele aluno — as frentes individuais não são afetadas.

!!! warning "Não há margem para falta"
    Com corte em 4 de 4, faltar a um checkpoint sem justificativa custa os 50 pontos do grupo. Havendo motivo justificado, **combine a reposição com o professor antes da data**.

Formato, datas e o que se avalia em cada checkpoint: [Avaliação](../avaliacao/avaliacao.md#3-entrevista-nos-checkpoints-praticos).

---

## Reenvio

Nenhuma entrega é de tentativa única. Se o aluno ou o grupo não for bem, pode refazer e reenviar, e **a nota é acertada**.

- Vale para exercícios, mini-curso, código do produto e documentação
- A nota da versão reenviada **substitui** a anterior, sem teto e sem desconto
- Quantas vezes forem necessárias, **dentro do prazo da própria entrega**
- Os checkpoints, por serem presenciais e pontuais, **não** entram na política de reenvio

!!! note "Exceções de prazo por feriado"
    | Exercício da aula | Venceria em | **Vence em** | Motivo |
    |---|---|---|---|
    | Aula 09 — 05/10 | Seg, 12/10 | **Seg, 19/10** | Feriado — Nossa Senhora Aparecida |

    As sessões EaD de **01/12** e **08/12** são de regularização: não propõem exercício novo.

