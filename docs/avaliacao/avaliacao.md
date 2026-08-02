# Critérios de Avaliação

A avaliação deste curso de extensão tem foco prático e está voltada para a aplicação real dos conhecimentos na comunidade. A nota total é de **100 pontos**, distribuídos em três frentes pontuadas e moduladas por uma quarta avaliação.

| Frente | Valor | Natureza |
|--------|-------|----------|
| Atividades individuais — código próprio | 25 pontos | Individual |
| Atividades individuais — mini-curso no YouTube | 25 pontos | Individual |
| Trabalho em grupo — produto em produção | 50 pontos | Coletiva |
| **Checkpoints práticos** | **multiplicador de 0 a 1** | Individual |

!!! danger "Os checkpoints multiplicam tudo"
    Os checkpoints práticos não somam pontos: eles **multiplicam** o total. Quem não souber trabalhar sobre o que entregou perde os pontos do produto do grupo **e também** os das atividades individuais. Detalhes na seção [Checkpoints Práticos](#3-checkpoints-praticos-multiplicador-de-0-a-1).

---

## 🧍 1. Atividades Individuais (50 Pontos)

Duas entregas individuais, de 25 pontos cada: o **código próprio** do aluno e um **mini-curso publicado no YouTube** que explica esse código.

### 1.1 Código próprio (25 pontos)

Cada aluno deve **escrever o seu próprio código** para comprovar que aplicou o conteúdo do curso. A avaliação é individual: não vale apresentar o código do grupo.

- **A dinâmica:** cada aluno mantém um **repositório próprio no GitHub**, na sua conta, com o código produzido ao longo do semestre.
- **O que entra:** exercícios das sessões de terça (EaD) e qualquer implementação que demonstre um conteúdo visto em aula — hipótese e PRD, identificação de clientes, planejamento com DSM, Spec-Driven Development com Spec-Kit, epics e cenários Gherkin, e o que for coberto no segundo bloco do semestre.
- **Como comprovar a aplicação:** cada entrega precisa deixar claro **qual conteúdo ela demonstra**. Um `README.md` curto por exercício, dizendo o que foi aplicado e o que o aluno aprendeu, já resolve.
- **Autoria:** os *commits* devem estar sob a conta do próprio aluno. Uso de agente de IA é permitido e esperado, mas o aluno precisa saber explicar cada decisão do código que entregou.
- **Prazo:** os exercícios propostos na sessão EaD de terça vencem **na aula da segunda-feira seguinte**. As entregas são incrementais ao longo do semestre, e **ter, 08/12/2026** é o último dia para regularizar qualquer pendência. Calendário completo em [Prazos de envio](#prazos-de-envio).

!!! tip "Critério de Sucesso"
    O que pontua não é volume de código, e sim **evidência de aplicação**: dado um conteúdo da disciplina, existe código do aluno que o coloca em prática e uma explicação de por que foi feito daquele jeito.

---

### 1.2 Mini-curso no YouTube (25 pontos)

Cada aluno planeja, grava e publica **um mini-curso individual no YouTube**, aberto à comunidade.

- **É individual.** Cada aluno faz o seu, mesmo estando em grupo.
- **O conteúdo explica o código do próprio aluno.** Não é tema livre: o mini-curso ensina um conteúdo da disciplina mostrando a aplicação que está no repositório individual — o que foi construído, por que aquelas decisões, e como outra pessoa reproduz.
- **Publicação:** vídeo público no YouTube, com o link registrado no `README.md` do repositório individual e informado ao professor.
- **Divulgação:** o curso é publicado e divulgado **no canal do próprio aluno**. É o canal dele que leva o material à comunidade — e o que continua acessível depois do curso.
- **Permanência:** por ficar publicado, o material continua servindo à comunidade depois do fim do semestre — é a contrapartida de extensão da atividade individual.

!!! abstract "A relação entre as duas entregas individuais"
    O código prova que o aluno **sabe fazer**. O mini-curso prova que ele **sabe explicar**. Se o aluno não consegue ensinar o próprio código, o código não está entendido.

---

## 👥 2. Trabalho em Grupo — Produto de Extensão (50 Pontos)

O grande entregável do curso é a criação de um **produto real em produção**, focado em resolver problemas concretos de projetos de extensão.

O grupo entrega a solução desenvolvida e seu portal de documentação (o MkDocs evolutivo criado desde a Aula 02).

Os produtos devem atender **obrigatoriamente** ao seguinte tema:

- **Problema do Campus Escalonável:** identificação de um problema vivido no campus que possua potencial de ser estendido para resolver dores da comunidade externa.

!!! example "Exemplo de problema no escopo"
    **Envio de comprovante de trabalhos complementares.** Hoje o aluno reúne certificados e declarações, envia por e-mail ou entrega em papel na coordenação, e não tem visibilidade do que foi aceito, do que falta e de quantas horas já valeram. A coordenação, do outro lado, controla tudo manualmente. É uma dor concreta do campus, com público bem definido, e que se estende a qualquer instituição que exija carga horária complementar.

!!! tip "Critério de Sucesso"
    Não basta entregar o plano. Os 50 pontos exigem **produto validado e em produção** — rodando e sendo testado pelo público.

---

## 📦 Regras de Entrega

Tudo é entregue por **repositório público no GitHub**. O aluno informa os endereços ao professor uma vez, no início do semestre, e é sempre neles que o trabalho é avaliado.

### Trabalho individual — repositório do aluno

Cada aluno mantém **um repositório na sua própria conta**, com:

- **`README.md` na raiz**, identificando o aluno, listando os exercícios e trazendo o **link do mini-curso no YouTube**
- **Um diretório por exercício**, com o material daquele exercício dentro
- **Um `README.md` em cada diretório**, dizendo qual conteúdo da disciplina o exercício demonstra e o que foi aprendido

```text
meu-repositorio/
├── README.md                     # nome do aluno, disciplina, link do YouTube, índice
├── exercicio-01-problema/
│   ├── README.md                 # o que foi aplicado e o que aprendi
│   └── ...
├── exercicio-02-prototipo/
│   ├── README.md
│   └── ...
└── exercicio-03-clientes/
    ├── README.md
    └── ...
```

!!! warning "Exercício sem pasta e sem README não é avaliado"
    A pasta é o que separa um exercício do outro, e o README é o que comprova **qual conteúdo aquele código aplica**. Código solto na raiz do repositório não tem como ser corrigido.

### Trabalho em grupo — repositório do grupo

O grupo mantém **um repositório único**, com:

- **`README.md` na raiz** contendo o **nome do grupo** e o **nome de todos os integrantes**
- O **código do produto**
- A **documentação do produto** (o portal MkDocs evolutivo)

!!! tip "Os commits identificam quem fez o quê"
    Cada integrante deve commitar sob a própria conta no repositório do grupo. É essa trilha que o professor usa nos checkpoints práticos para propor uma tarefa sobre o código que aquele aluno de fato tocou.

### Mini-curso — canal do aluno no YouTube

- Vídeo **público** no YouTube, **no canal do próprio aluno**
- **Link no `README.md`** do repositório individual, na raiz
- Um mini-curso por aluno, mesmo entre integrantes do mesmo grupo

!!! warning "Sem divulgação, não há extensão"
    Vídeo publicado e não divulgado não alcança ninguém. Divulgar o curso no canal e nos espaços em que o público-alvo está faz parte da entrega — não é opcional.

---

## 🎯 3. Checkpoints Práticos — multiplicador de 0 a 1

Os checkpoints são individuais e **não somam pontos: multiplicam**. Eles existem para responder a uma pergunta simples — *o aluno sabe trabalhar sobre o que foi entregue em nome dele?*

Não é prova escrita nem entrevista: o aluno senta na máquina e **mexe no código que ele ou o grupo entregou**.

### Formato

- **Presencial**, no Lab 207, individual, **30 a 40 minutos** por aluno
- O professor propõe uma **tarefa pequena sobre o repositório do aluno ou do grupo**
- **Uso de IA liberado.** A tarefa é desenhada para exigir conhecimento do repositório específico — o agente não conhece as decisões daquele grupo
- Avalia-se a **decisão**, não a digitação: por que aqui, por que assim, o que quebra se mudar

### Datas e escopo

| Checkpoint | Data | Bloco verificado | Exemplos de tarefa |
|-----------|------|------------------|--------------------|
| **CP1** | Seg, 31/08/2026 | Discovery — Aulas 01 a 04 | Justificar o segmento-alvo a partir das evidências do PRD; reescrever uma hipótese mal formulada do próprio documento; apontar quem é o pagador no mapa de atores e por quê |
| **CP2** | Seg, 28/09/2026 | Definição e planejamento — Aulas 06 e 07 | Encaixar uma feature nova na DSM e dizer o que ela destrava; quebrar uma feature em stories; justificar a ordem de implementação escolhida |
| **CP3** | Seg, 26/10/2026 | Especificação e contexto do agente — Aulas 09 e 10 | Adicionar um campo ponta a ponta no produto; corrigir um bug plantado pelo professor; escrever a spec de uma mudança pequena e rodar o fluxo do Spec-Kit |
| **CP4** | Seg, 30/11/2026 | Comunicação enxuta, épicos, agentes e observabilidade — Aulas 12 a 14 | Escrever o cenário Gherkin de uma regra que já existe no código; derivar uma spec a partir de um épico do grupo; mostrar como o grupo detecta que o produto caiu e qual é o MTTD medido |

Os checkpoints acontecem nas segundas de **apresentação do trabalho**, em paralelo às apresentações dos demais grupos — não consomem aula de conteúdo.

### Como a nota é formada

- Cada checkpoint recebe um fator de **0,0 a 1,0**
- O multiplicador final é a **média dos quatro**
- **Escala:** 1,0 para quem resolve e justifica; valores intermediários para domínio parcial; 0,0 para quem não consegue trabalhar sobre o próprio código
- **Falta sem justificativa** vale 0,0 naquele checkpoint. Com justificativa, a reposição é combinada com o professor

!!! danger "Consequência prática"
    Se a pessoa não souber, **perde os pontos do produto do grupo** — e também os do código próprio e do mini-curso, porque o multiplicador incide sobre o total. Produto em produção e vídeo publicado não garantem nota a quem não consegue sustentar o que fez.

!!! note "Por que quatro, e não um"
    Quatro medidas ao longo do semestre dão sinal cedo: um dia ruim custa um quarto do multiplicador, não o semestre inteiro, e sobra tempo para corrigir. Avaliação única no fim não avisa ninguém a tempo.

    Os três primeiros ficam bem antes do prazo de 08/12 — o CP3, em 26/10, ainda deixa seis semanas de folga. O CP4 fecha a verificação do último bloco de conteúdo.

!!! warning "Checkpoints não entram na política de reenvio"
    Por serem presenciais e pontuais, não podem ser refeitos como as demais entregas. A média dos quatro é justamente o que absorve um desempenho fraco isolado.

!!! note "Por que o multiplicador existe"
    Nota coletiva sem verificação individual premia quem não trabalhou. Os checkpoints ligam a nota do grupo ao que cada integrante realmente entende — e são também o motivo de o uso de agentes de IA ser liberado: a ferramenta pode escrever, mas quem responde é o aluno.

---

## 🧮 Cálculo da Nota

```text
NF = (COD + CUR + PRD) x CP

NF  = Nota Final                (0 a 100)
COD = Código próprio            (0 a 25)    — repositório individual do aluno
CUR = Mini-curso no YouTube     (0 a 25)    — vídeo individual explicando o próprio código
PRD = Produto do grupo          (0 a 50)    — produto em produção + portal de documentação
CP  = Checkpoints Práticos      (0,0 a 1,0) — média dos quatro, multiplicador individual

CP = (CP1 + CP2 + CP3 + CP4) / 4
```

Nota máxima: `(25 + 25 + 50) × 1,0 = 100`.

### Exemplos

| Situação | COD | CUR | PRD | CP | Nota final |
|----------|-----|-----|-----|----|------------|
| Entregou tudo e foi bem nos quatro checkpoints | 25 | 25 | 50 | 1,0 | **100** |
| Entregou tudo, um checkpoint fraco (1,0 · 0,4 · 1,0 · 1,0) | 25 | 25 | 50 | 0,85 | **85** |
| Grupo entregou, mas o aluno não sustentou nenhum checkpoint | 25 | 25 | 50 | 0,0 | **0** |
| Sem código individual, resto completo | 0 | 25 | 50 | 1,0 | **75** |
| Sem mini-curso, resto completo | 25 | 0 | 50 | 1,0 | **75** |
| Produto do grupo não chegou à produção | 25 | 25 | 0 | 1,0 | **50** |
| Faltou ao CP2 sem justificativa (1,0 · 0,0 · 1,0 · 1,0) | 25 | 25 | 50 | 0,75 | **75** |

!!! note "A nota é individual, mesmo com trabalho coletivo"
    `PRD` vem do grupo e é igual para todos os integrantes. Já `COD`, `CUR` e `CP` são individuais — por isso dois alunos do mesmo grupo podem terminar o semestre com notas bem diferentes.

---

## 📝 Prova Final

**Segunda, 14/12/2026 — Lab 207.**

A prova final é uma avaliação **à parte**: ela **não entra na fórmula** `NF = (COD + CUR + PRD) × CP`. Os 100 pontos do semestre são fechados antes dela.

- **Não é prova escrita.** É **outro trabalho, feito individualmente pelo aluno**.
- **Escopo: o conteúdo inteiro da disciplina.** Diferente das atividades individuais, que demonstram um conteúdo por vez, aqui o aluno percorre o ciclo completo sozinho — entender o problema, decidir o que construir, construir e colocar para operar e monitorar.
- **Individual em todos os sentidos:** repositório próprio, problema próprio, decisões próprias. Não é recorte do trabalho de grupo.

!!! tip "O que se espera demonstrar"
    Que o aluno consegue conduzir sozinho o processo que praticou em grupo durante o semestre — e justificar cada decisão tomada ao longo dele.

---

## 🔁 Reenvio de Entregas

Nenhuma entrega deste curso é de uma tentativa só. **Se o aluno ou o grupo não for bem em uma entrega, pode refazê-la e reenviar, e a nota é acertada.**

- **Vale para todas as frentes:** exercícios individuais, mini-curso, código do produto e documentação do portal.
- **A nota é substituída, não somada:** vale a nota da versão reenviada, sem teto e sem desconto por ter reenviado.
- **Quantas vezes forem necessárias**, desde que **cada reenvio respeite o prazo de envio da própria atividade**. Reenviar não cria prazo novo: a versão corrigida entra na mesma janela de entrega das demais submissões.
- **Prazo limite do semestre:** **terça, 08/12/2026**. Depois dessa data não há reenvio — é a última chance de regularizar qualquer pendência.
- **Como funciona:** o aluno ou grupo corrige o que foi apontado no feedback, reenvia e avisa o professor indicando o que mudou.

!!! tip "Por que existe reenvio"
    O curso ensina um processo iterativo: construir, medir, aprender e corrigir. Seria incoerente avaliar com entrega única. O feedback existe para ser aplicado — a nota mede onde você chegou, não onde tropeçou no caminho.

### Prazos de envio

**Regra geral: os exercícios propostos na sessão EaD de terça vencem na aula da segunda-feira seguinte.**

Envio e reenvio seguem o mesmo prazo. Se a segunda-feira seguinte for feriado, o vencimento passa para a próxima aula:

| Exercícios da sessão | Venceria em | **Vence em** | Motivo |
|----------------------|-------------|--------------|--------|
| Ter, 01/09/2026 | Seg, 07/09 | **Seg, 14/09** | Feriado — Independência do Brasil |
| Ter, 06/10/2026 | Seg, 12/10 | **Seg, 19/10** | Feriado — Nossa Senhora Aparecida |
| Ter, 27/10/2026 | Seg, 02/11 | **Seg, 09/11** | Feriado — Finados |
| Ter, 24/11/2026 | Seg, 30/11 | **Seg, 07/12** | 30/11 concentra a apresentação do trabalho e o Checkpoint 4 |

Nas demais sessões vale a regra direta: 04/08 vence em 10/08, 11/08 em 17/08, e assim por diante.

!!! warning "Duas sessões vencendo no mesmo dia"
    Por causa dos feriados, **19/10** recebe os exercícios de 06/10 e de 13/10, e **09/11** recebe os de 27/10 e de 03/11. Planeje-se: são dois conjuntos na mesma data.

!!! note "Dezembro é mês de acerto — não há exercício novo"
    A última sessão EaD que propõe exercício é **ter, 24/11/2026**, com vencimento em **seg, 07/12**.

    De dezembro em diante **não há exercício novo nem conteúdo cobrado**. A Aula 16, em 07/12, é o encerramento, com uma aula extra sem entrega obrigatória; as sessões EaD de **01/12** e **08/12** são reservadas para os alunos **acertarem o trabalho e os exercícios pendentes**, até o prazo final de **ter, 08/12/2026**.
