# Sobre o PSM CID Measurement Framework

Explicação de apoio. Descreve o framework de medição que o curso usa para responder a uma pergunta que atravessa as quatro fases do processo: **como saber se o que estamos fazendo está funcionando**.

Não é conteúdo de uma aula só. Ele é apresentado na [Aula 01](../plano-de-aula/aulas/aula-01-2026-08-03.md), volta na [Aula 14](../plano-de-aula/aulas/aula-14-2026-11-23.md) para medir orquestração e observabilidade, e de novo na [Aula 16](../plano-de-aula/aulas/aula-16-2026-12-07.md) para medir a operação.

---


Descrever o processo é metade do trabalho. A outra metade é **saber se ele está funcionando**, e isso exige medida. O material de referência do curso é o **PSM Continuous Iterative Development (CID) Measurement Framework**, versão 2.1 (2021), produzido em conjunto por três organizações: *Practical Software and Systems Measurement* (PSM), *National Defense Industrial Association* (NDIA) e *International Council on Systems Engineering* (INCOSE).

O framework define **Desenvolvimento Contínuo e Iterativo (CID)** como o método de gerenciar desenvolvimento, teste e liberação de software de modo a entregar, contínua ou iterativamente, sistemas funcionais de capacidade crescente. É o guarda-chuva que cobre Agile, DevOps, DevSecOps e SAFe.

Três características tornam esse material útil para este curso:

- **É agnóstico de metodologia.** Foi escrito para ser adaptado, não seguido à risca.
- **Cobre o ciclo inteiro**, incluindo o que acontece depois do deploy — exatamente a fase que este curso não deixa de fora.
- **Separa três perspectivas** de quem precisa da informação: **time**, **produto** e **empresa**. A mesma medida-base pode servir às três, agregada em níveis diferentes.

!!! warning "O erro clássico de medição"
    O framework é direto: o maior problema com medidas é elas **não serem usadas**. A recomendação é escolher um **conjunto mínimo**, cada medida com um responsável identificado, que informe uma decisão concreta e provoque uma ação. Medida que ninguém olha deve ser descartada ou substituída.

---

## Decomposição do trabalho

![Figura 1 — CID Work Decomposition](../assets/psm-cid/fig1-cid-work-decomposition.png)

Requisitos de missão viram **capacidades** (*capabilities*), que se quebram em **features**, que se quebram em **stories**, que se quebram em **tasks**. Cada nível se organiza em um horizonte de tempo diferente:

| Nível | Horizonte | O que é |
|-------|-----------|---------|
| Capability | Roadmap | Solução de alto nível, atravessa várias releases |
| Feature | Release | Serviço ou característica que atende uma necessidade, com critério de aceitação, dentro de uma release |
| Story | Iteração | Comportamento pequeno, baseado em cenário de usuário, implementável e demonstrável em uma iteração |
| Task | — | Passos necessários para satisfazer uma story |

É o mesmo vocabulário das Aulas 07 e 12, quando montarmos backlog, épicos e user stories.

---

## Contexto de medição: onde cada medida nasce

![Figura 2 — Measurement Context Diagram](../assets/psm-cid/fig2-measurement-context.png)

É a figura mais importante para o curso, porque mostra as **quatro fases do nosso ciclo com as medidas encaixadas em cada transição**:

- **Backlog** — coleção de itens propostos: necessidades novas e defeitos de releases anteriores. Só vira trabalho o que for priorizado e aceito (*committed work*).
- **Factory** — a fábrica: requisitos, design, implementação e teste do trabalho aceito, culminando no deploy. Trabalho planejado e executado iterativamente.
- **Operations** — o que sai da fábrica é implantado em operação interna ou externa: ambiente de integração do time, teste operacional ou uso final.
- **Rework** — a release implantada precisa de correção por defeito, vulnerabilidade ou anomalia. A operação pode seguir em **modo degradado** (contorno, caminho redundante) até o serviço ser restaurado.

Os intervalos de tempo marcados na figura são as medidas:

| Medida | O que mede |
|--------|------------|
| **Lead Time** | Do momento em que o trabalho é identificado até a solicitação ser satisfeita |
| **Cycle Time** | Do momento em que o trabalho entra em execução até estar concluído |
| **MTTD** (*Mean Time to Detect*) | Tempo até detectar e diagnosticar a falha |
| **MTTR** (*Mean Time to Restore*) | Tempo total de restauração: detectar, diagnosticar, corrigir e implantar |
| **Change Failure Rate** | Proporção de mudanças implantadas que precisaram de *rollback* |

!!! tip "Por que MTTD e MTTR importam para o trabalho de extensão"
    O critério dos 50 pontos exige produto em produção. Se o sistema do grupo cair e ninguém perceber por três dias, o MTTD é de três dias — e isso é um resultado mensurável, não uma impressão. É a diferença entre "está no ar" e "sabemos que está no ar".

O framework ainda distingue **quatro ambientes** onde a medição pode ocorrer, e nem toda organização tem os quatro separados:

1. Desenvolvimento/Integração
2. Representativo de produção
3. Operacionalmente relevante
4. Operacional

A empresa costuma olhar as medidas do ambiente operacional; o time e o produto começam a medir nos ambientes anteriores.

---

## Terminologia de defeitos: contido x escapado

![Figura 3 — Defect Terminology](../assets/psm-cid/fig3-defect-terminology.png)

A distinção central e a mais cobrada em revisão de qualidade:

- **Defeito contido** (*contained*, também chamado *save*) — detectado e resolvido **antes** da release. É o sistema de qualidade funcionando.
- **Defeito escapado** (*escaped*) — detectado ou resolvido **depois** da release que o continha. Escapes são rastreados separadamente para releases internas e externas.

**Defeito**, na definição do framework, é qualquer condição do produto que não atende ao requisito ou à expectativa do usuário, faz o produto funcionar mal, produzir resultado incorreto ou inesperado, comportar-se de modo não intencional, ou gerar prejuízo de qualidade, custo, prazo ou desempenho. Documentação também pode conter defeito.

A figura mostra onde cada tipo aparece: iterações internas (defeitos originados) → releases internas (entregues, com escapes) → releases externas (implantadas em campo, com escapes). Tudo à esquerda do limite é *Factory*; à direita é *Operations*.

---

## O processo CID ao longo do tempo

![Figura 4 — Continuous Iterative Development Process](../assets/psm-cid/fig4-cid-process.png)

A espiral mostra iterações sucessivas (v0.1, v0.n, v1.1, v1.2 …) acumulando capacidade. Nem toda iteração vira release externa: um subconjunto é **candidate release**, e um subconjunto desses é efetivamente liberado para uso operacional.

Os patamares horizontais são limiares de maturidade do produto:

| Termo | Significado |
|-------|-------------|
| **MVP** (*Minimum Viable Product*) | Versão inicial que entrega capacidades básicas a usuários para avaliação e feedback. O aprendizado do MVP molda escopo, requisitos e design das releases seguintes. |
| **MVCR** (*Minimum Viable Capability Release*) | Conjunto de features adequado para ir a um ambiente operacional, entregando valor real ao usuário final. Equivale ao *Minimum Marketable Product* da indústria. |
| **NVP** (*Next Viable Product*) | Próximo conjunto de features na entrega seguinte. |

E os tipos de release (*release style*):

- **Cadenciada** — por tempo, por exemplo trimestral
- **Por feature** — libera quando o conjunto está pronto, por exemplo o MVP
- **Deploy contínuo** — exige disciplina e maturidade altas

!!! note "Expectativa realista para o semestre"
    O framework observa que deploy contínuo exige maturidade significativa e que **a maioria dos programas adota alguma forma de cadência**. Para o nosso curso, cadência mensal amarrada às apresentações é uma escolha honesta: cada última segunda do mês é uma release.

---

## Vocabulário essencial

Termos do framework que passam a valer como vocabulário comum da disciplina:

| Termo | Definição resumida |
|-------|--------------------|
| **Roadmap** | Descrição de alto nível da visão e direção do produto ao longo do tempo; descreve metas e capacidades das releases externas |
| **Backlog do produto** | Lista priorizada de necessidades detalhadas. Contém features novas, mudanças, correções de defeito e mudanças de infraestrutura. Defeitos achados em desenvolvimento **e em operação** entram aqui |
| **Backlog da iteração** | Decomposição dos itens do backlog do produto priorizados para o ciclo curto |
| **Story Points** | Valor subjetivo, sem unidade, atribuído pelo time como medida relativa de esforço e complexidade. **Não é comparável entre times** |
| **Iteração / Sprint** | Bloco curto de tempo em que o time desenvolve e demonstra um conjunto de stories |
| **Release** | Agrupamento de capacidades ou features utilizável para demonstração, avaliação ou entrega |
| **Release interna** | Pronta para uso fora do time de desenvolvimento — integração, teste ou demonstração |
| **Candidate release** | Passou pelo pipeline e pelo teste de sistema; pronta para transição ao usuário |
| **Release operacional** | Aprovada para uso operacional |
| **Problem Report** | Registro de problema no produto — também chamado *trouble ticket* |
| **Change Request** | Solicitação de mudança no produto |
| **Stakeholder** | Indivíduo ou organização com direito, participação ou interesse no sistema (ISO/IEC/IEEE 15288) |
| **Product Value** | Grau em que o produto entregue satisfaz as necessidades dos stakeholders — inclui melhoria de missão, eficiência, redução de risco e custo |

---

## Do dado à decisão

Medir não é coletar número: é ligar um **dado** a uma **necessidade de informação** que sustenta uma decisão. O framework usa o modelo da ISO/IEC/IEEE 15939.

![Figura 5 — Information Model, visão de alto nível](../assets/psm-cid/fig5-information-model.png)

A leitura é de baixo para cima: **entidades** têm **atributos** mensuráveis (tamanho, esforço, número de defeitos); o **construto de medição** define como quantificar esses atributos; o **conceito mensurável** descreve ideias que satisfazem a necessidade; o **produto de informação** entrega medida e interpretação a quem decide.

![Figura 6 — Measurement Information Model](../assets/psm-cid/fig6-measurement-information-model.png)

Detalhando, existem três níveis de medida:

| Nível | O que é |
|-------|---------|
| **Base measure** | Medida de um único atributo por um método específico |
| **Derived measure** | Quantidade definida como função de duas ou mais medidas |
| **Indicator** | Estimativa ou avaliação que fornece base para decisão, combinando medidas e critérios de decisão |

![Figura 7 — Mapping Data to Measures](../assets/psm-cid/fig7-mapping-data-to-measures.png)

O exemplo concreto da Figura 7 percorre o modelo inteiro para uma pergunta real:

1. **Necessidade de informação:** quantos defeitos foram liberados para o cliente?
2. **Medidas-base:** contar defeitos contidos, escapados internamente e escapados externamente
3. **Função de medição:** defeitos escapados ÷ total de defeitos
4. **Medida derivada:** *External Escape Ratio*
5. **Modelo de análise:** a razão está abaixo do critério de decisão?
6. **Indicador e interpretação:** menos de 1% dos defeitos escapou externamente

---

## Princípios de medição

![Figura 8 — Speed-Quality Sweet Spot](../assets/psm-cid/fig8-speed-quality-sweet-spot.png)

O princípio que mais interessa a um time iniciante: **existe um ponto de equilíbrio entre velocidade e qualidade**. Ênfase excessiva em velocidade custa qualidade do produto; ênfase excessiva em qualidade derruba a velocidade de entrega. Algumas melhorias — automação, principalmente — deslocam as duas curvas ao mesmo tempo e melhoram os dois lados.

Os demais princípios:

- As medidas do framework são **exemplos**, identificados por survey e revisão de especialistas, não uma lista obrigatória
- Medidas de time, produto e empresa coexistem, e **nem todas podem ser agregadas** entre níveis
- Selecione um **conjunto mínimo prático**, adaptado às circunstâncias, ferramentas e processos do grupo
- Toda medida escolhida precisa ter stakeholder identificado, informar decisão e **provocar ação**, dando visibilidade cedo o suficiente para correção de rumo
- **Automatize a coleta** sempre que praticável, integrada ao fluxo de trabalho

As onze medidas com especificação detalhada no framework:

| | |
|---|---|
| Automated Test Coverage | Defect Resolution |
| Burndown | MTTR / MTTD |
| Committed vs. Completed Progress | Release Frequency |
| Cumulative Flow | Team Velocity |
| Cycle Time / Lead Time | Product Value |
| Defect Detection | |

---

## Como isso se encaixa no ciclo do curso

| Fase do nosso ciclo | Elemento do PSM CID | Medidas candidatas para o trabalho de extensão |
|---------------------|---------------------|------------------------------------------------|
| 1 — Entender o problema | Roadmap, capacidades | Product Value |
| 2 — Decidir o que construir | Backlog, decomposição em features e stories | Committed vs. Completed, Burndown |
| 3 — Construir | Factory, iterações, releases | Cycle Time, Defect Detection, Automated Test Coverage |
| 4 — Operar e monitorar | Operations, rework | **MTTD, MTTR**, Change Failure Rate, Release Frequency |

!!! quote "Atribuição e direitos"
    Figuras 1 a 8 e definições reproduzidas de *Practical Software and Systems Measurement — Continuous Iterative Development Measurement Framework, Part 1: Concepts, Definitions, Principles, and Measures*, Versão 2.1, 15 de abril de 2021. Editores: Cheryl L. Jones, Geoff Draper, Bill Golaz e Paul Janusz. Produtos nº PSM-2021-03-001 e INCOSE-TP-2020-001-06.

    Desenvolvido e publicado por membros do **Practical Software & Systems Measurement (PSM)**, da **National Defense Industrial Association (NDIA)** e do **International Council on Systems Engineering (INCOSE)**.

    *Copyright Notice — General Use:* "Permission to reproduce, use this document or parts thereof, and to prepare derivative works from this document is granted, with attribution to PSM, NDIA, and INCOSE, and the original author(s), provided this copyright notice is included with all reproductions and derivative works."

    Documento original: *Unclassified — Distribution Statement A: Approved for Public Release; Distribution is Unlimited.*

---
