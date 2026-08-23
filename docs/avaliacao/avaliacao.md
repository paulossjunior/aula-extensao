# Critérios de Avaliação

A avaliação deste curso tem foco prático e está voltada para a aplicação real dos conhecimentos na comunidade. A nota total é de **100 pontos**.

| Frente | Valor | Natureza |
|--------|-------|----------|
| Código próprio | 25 pontos | Individual |
| Mini-curso no canal do aluno | 25 pontos | Individual |
| Trabalho em grupo | 50 pontos | Coletiva |
| Observabilidade do produto — **opcional** | +10 pontos | Coletiva |
| **Entrevista** | **0 ou 1** — porteira dos 50 pontos do grupo | Individual |

!!! danger "Aprovação: 60 pontos ou mais"
    O aluno precisa de **NF ≥ 60** na soma geral. Abaixo disso, vai para a [prova final](#prova-final).

    Duas coisas derrubam a nota de uma vez: **produto não entregue** zera os 50 do grupo para todo mundo, e **reprovar na entrevista** zera os 50 do grupo para aquele aluno.

A mecânica das entregas — repositórios, estrutura de pastas, calendário e prazos — está em [Especificação de Exercícios e Trabalhos](../entregas/index.md).

---

## 🧍 1. Atividades Individuais (50 Pontos)

Duas entregas individuais, de 25 pontos cada: o **código próprio** do aluno e um **mini-curso** que explica esse código.

### 1.1 Código próprio (25 pontos)

Cada aluno deve **escrever o seu próprio código** para comprovar que aplicou o conteúdo do curso. A avaliação é individual: não vale apresentar o código do grupo.

- **A dinâmica:** cada aluno mantém um **repositório próprio no GitHub**, na sua conta, com o código produzido ao longo do semestre.
- **O que entra:** exercícios das sessões de terça (EaD) e qualquer implementação que demonstre um conteúdo visto em aula — incluindo o trabalho [Recreio Arcade](../trabalho/recreio-arcade.md), construído pela turma em quatro grupos mas com o código no repositório de cada aluno.
- **Como comprovar:** todo código entregue precisa de **arquitetura**, **base de conhecimento** e **comentários que expliquem decisão** — detalhes em [Especificação de Entregas](../entregas/index.md#os-tres-requisitos-de-todo-codigo-entregue).
- **Autoria:** os *commits* devem estar sob a conta do próprio aluno. Uso de agente de IA é permitido e esperado, mas o aluno precisa saber explicar cada decisão do código que entregou.

!!! tip "Critério de Sucesso"
    O que pontua não é volume de código, e sim **evidência de aplicação**: dado um conteúdo da disciplina, existe código do aluno que o coloca em prática e uma explicação de por que foi feito daquele jeito.

### 1.2 Mini-curso no canal do aluno (25 pontos)

Cada aluno planeja, grava e publica **um mini-curso individual**, aberto à comunidade.

- **É individual.** Cada aluno faz o seu, mesmo estando em grupo.
- **O conteúdo explica o código do próprio aluno.** Não é tema livre: o mini-curso ensina um conteúdo da disciplina mostrando a aplicação que está no repositório individual.
- **Publicação:** vídeo público no YouTube, **no canal do próprio aluno**, com o link no `README.md` do repositório individual.
- **Divulgação:** o curso é divulgado no canal do aluno e nos espaços em que o público-alvo está.

!!! abstract "A relação entre as duas entregas individuais"
    O código prova que o aluno **sabe fazer**. O mini-curso prova que ele **sabe explicar**. Se o aluno não consegue ensinar o próprio código, o código não está entendido.

---

## 👥 2. Trabalho em Grupo — Produto de Extensão (50 Pontos)

O grande entregável do curso é a criação de um **produto real em produção**, focado em resolver problemas concretos de projetos de extensão.

### Os cinco itens avaliados

| Item | Pontos | O que se verifica |
|------|--------|-------------------|
| **Produto entregue** | 10 | O produto existe e funciona |
| **Entrega em ambiente de produção** | 10 | Está no ar, acessível e sendo usado por público real |
| **Qualidade da documentação** | 10 | Portal completo e atualizado: problema, público, arquitetura e decisões |
| **Qualidade do código** | 10 | Organização, legibilidade, comentários que explicam decisão, testes |
| **Apresentação** | 10 | Clareza e evidência nas quatro apresentações mensais |

!!! danger "Produto não entregue zera o trabalho em grupo"
    Se o produto não for entregue, **o grupo recebe 0 nos 50 pontos** — não apenas no item "produto entregue". Documentação e qualidade de código de um produto que não existe não são avaliáveis.

### Tema obrigatório

- **Problema do Campus Escalonável:** identificação de um problema vivido no campus que possua potencial de ser estendido para resolver dores da comunidade externa.

!!! example "Exemplo de problema no escopo"
    **Envio de comprovante de trabalhos complementares.** Hoje o aluno reúne certificados e declarações, envia por e-mail ou entrega em papel na coordenação, e não tem visibilidade do que foi aceito, do que falta e de quantas horas já valeram. A coordenação, do outro lado, controla tudo manualmente. É uma dor concreta do campus, com público bem definido, e que se estende a qualquer instituição que exija carga horária complementar.

---

## 🎯 3. Entrevista nos Checkpoints Práticos

A entrevista é **individual** e vale **0 ou 1**. Ela não soma pontos: **libera ou bloqueia os 50 pontos do trabalho em grupo**.

Ela existe para responder a uma pergunta simples — *o aluno sabe trabalhar sobre o que foi entregue em nome dele?* Não é prova escrita: o aluno senta na máquina e **mexe no código que ele ou o grupo entregou**.

### Formato

- **Presencial**, no Lab 207, individual, **30 a 40 minutos** por aluno
- Acontece nas quatro segundas de apresentação, em paralelo às apresentações dos demais grupos — não consome aula de conteúdo
- O professor propõe uma **tarefa pequena sobre o repositório do aluno ou do grupo**
- **Uso de IA liberado.** A tarefa exige conhecimento do repositório específico, que o agente não tem
- Avalia-se a **decisão**, não a digitação: por que aqui, por que assim, o que quebra se mudar

### Datas e escopo

| Checkpoint | Data | Bloco verificado | Exemplos de tarefa |
|-----------|------|------------------|--------------------|
| **CP1** | Seg, 31/08/2026 | Discovery — Aulas 01 a 04 | Justificar o segmento-alvo a partir das evidências do PRD; reescrever uma hipótese mal formulada; apontar quem é o pagador no mapa de atores |
| **CP2** | Seg, 28/09/2026 | Definição e planejamento — Aulas 06 e 07 | Encaixar uma feature nova na DSM e dizer o que ela destrava; quebrar uma feature em stories; justificar a ordem de implementação |
| **CP3** | Seg, 26/10/2026 | Especificação e contexto do agente — Aulas 09 e 10 | Adicionar um campo ponta a ponta; corrigir um bug plantado pelo professor; rodar o fluxo do Spec-Kit para uma mudança pequena |
| **CP4** | Seg, 30/11/2026 | Comunicação enxuta, épicos e agentes — Aulas 12 a 14 | Escrever o cenário Gherkin de uma regra existente; derivar uma spec a partir de um épico; justificar por que o trabalho foi ou não dividido entre agentes |

### Como o resultado é apurado

- Cada checkpoint resulta em **passou** ou **não passou**
- **É preciso passar nos quatro.** `ENT = 1` apenas com **4 de 4**
- Falhar em um único checkpoint faz `ENT = 0` e o aluno **perde os 50 pontos do trabalho em grupo**
- As frentes individuais — código próprio e mini-curso — **não são afetadas**
- **Falta sem justificativa** conta como não passou

!!! warning "Não há margem para falta — combine a reposição antes"
    Com corte em 4 de 4, faltar a um checkpoint custa os 50 pontos do grupo. Havendo motivo justificado, **combine a reposição com o professor antes da data**, não depois.

!!! note "Por que a entrevista existe"
    Nota coletiva sem verificação individual premia quem não trabalhou. A entrevista liga a nota do grupo ao que cada integrante realmente entende — e é também o motivo de o uso de agentes de IA ser liberado: a ferramenta pode escrever, mas quem responde é o aluno.

!!! warning "A entrevista não entra na política de reenvio"
    Por ser presencial e pontual, não pode ser refeita como as demais entregas.

---

## 🎁 Pontos Extras — Observabilidade (até 10 pontos)

**Opcional.** O grupo que colocar o próprio produto sob observação ganha até **10 pontos extras**.

Estar em produção não é só ter feito o deploy: é o grupo **saber** que o produto está de pé. Três peças, cumulativas:

| Peça | Pontos | O que é |
|------|--------|---------|
| **Health check** | 3 | Uma rota que responde 200 quando o sistema está sadio, tocando as dependências críticas — banco, fila, serviço externo |
| **Log de erro estruturado** | 3 | Uma linha por evento, com nível, momento e contexto suficiente para diagnosticar sem reproduzir |
| **Verificação externa agendada** | 4 | Algo que consulte o health check periodicamente e **avise o grupo num canal** quando falhar |

A ferramenta é escolha do grupo: cron, GitHub Action agendada, serviço de *uptime* gratuito ou um agente. O que não vale é depender de alguém lembrar de olhar.

!!! tip "O que comprova a entrega"
    O grupo informa o **MTTD** medido do próprio produto — o tempo entre uma falha provocada de propósito e o alerta chegar. É o número que separa "achamos que está no ar" de "sabemos que está no ar".

!!! note "Por que vale a pena mesmo sendo opcional"
    Um dos itens dos 50 pontos é **entrega em ambiente de produção**. Se o sistema cai na sexta e o grupo descobre na apresentação de segunda, foram três dias fora do ar. A observabilidade não é só bônus: é o que protege a nota principal.

    Conteúdo na [Aula 14](../plano-de-aula/aulas/aula-14-2026-11-23.md), em formato expositivo.

---

## 🧮 Cálculo da Nota

```text
NF = min(100, COD + CUR + (GRP + EXT) x ENT)

NF  = Nota Final              (0 a 100)   — aprovado com 60 ou mais
COD = Código próprio          (0 a 25)    — individual
CUR = Mini-curso              (0 a 25)    — individual
GRP = Trabalho em grupo       (0 a 50)    — cinco itens de 10; zera se o produto não for entregue
EXT = Observabilidade         (0 a 10)    — opcional, do grupo
ENT = Entrevista              (0 ou 1)    — individual; 1 apenas com 4 de 4 checkpoints
```

Os pontos extras entram na soma antes da porteira e servem para **compensar perdas em outras frentes** — não ultrapassam o teto de 100.

### Exemplos

| Situação | COD | CUR | GRP | EXT | ENT | Nota final | |
|----------|-----|-----|-----|-----|-----|-----------|---|
| Entregou tudo e passou nos quatro checkpoints | 25 | 25 | 50 | 0 | 1 | **100** | ✅ |
| Tudo, mais observabilidade (teto aplicado) | 25 | 25 | 50 | 10 | 1 | **100** | ✅ |
| Sem mini-curso, mas com observabilidade | 25 | 0 | 50 | 10 | 1 | **85** | ✅ |
| Sem código próprio, resto completo | 0 | 25 | 50 | 0 | 1 | **75** | ✅ |
| Só o trabalho de grupo, com observabilidade | 0 | 0 | 50 | 10 | 1 | **60** | ✅ |
| **Reprovou em um checkpoint** | 25 | 25 | 50 | 10 | **0** | **50** | ❌ |
| **Produto do grupo não foi entregue** | 25 | 25 | **0** | 0 | 1 | **50** | ❌ |
| Sem código próprio e reprovou na entrevista | 0 | 25 | 50 | 0 | 0 | **25** | ❌ |

!!! danger "As duas quedas de 50 pontos"
    Reprovar na entrevista e não entregar o produto têm o mesmo efeito numérico — tiram os 50 pontos do grupo — mas alcances diferentes:

    - **Produto não entregue** atinge **todos** os integrantes do grupo
    - **Reprovar na entrevista** atinge **só aquele aluno**

    Nos dois casos, com as frentes individuais completas o aluno fica em 50 e **não atinge os 60 da aprovação**.

!!! note "A nota é individual, mesmo com trabalho coletivo"
    `GRP` e `EXT` vêm do grupo e são iguais para todos. Já `COD`, `CUR` e `ENT` são individuais — por isso dois alunos do mesmo grupo podem terminar o semestre com notas bem diferentes.

---

## 📝 Prova Final

**Segunda, 14/12/2026 — Lab 207.**

Destinada a quem **não atingiu os 60 pontos** na soma geral. É uma avaliação **à parte**: não entra na fórmula `NF`.

- **Não é prova escrita.** É **outro trabalho, feito individualmente pelo aluno**.
- **Escopo: o conteúdo inteiro da disciplina.** Diferente das atividades individuais, que demonstram um conteúdo por vez, aqui o aluno percorre o ciclo completo sozinho — entender o problema, decidir o que construir, construir e colocar para operar e monitorar.
- **Individual em todos os sentidos:** repositório próprio, problema próprio, decisões próprias. Não é recorte do trabalho de grupo.

!!! tip "O que se espera demonstrar"
    Que o aluno consegue conduzir sozinho o processo que praticou em grupo durante o semestre — e justificar cada decisão tomada ao longo dele.

---

## 📦 Entregas, prazos e reenvio

Toda a mecânica de entrega vive em uma página própria:

- **[Especificação de Exercícios e Trabalhos](../entregas/index.md)** — estrutura do repositório, os três requisitos de todo código, o calendário com a data de cada entrega, o detalhamento por aula e a política de reenvio.

Em resumo: exercício proposto na terça vence **na aula da segunda seguinte**; o reenvio é ilimitado dentro do prazo da própria entrega; e **terça, 08/12/2026** é o último dia para regularizar qualquer pendência do semestre.
