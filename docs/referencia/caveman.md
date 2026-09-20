# Referência — Caveman

Página de consulta. Descreve a instalação do Caveman, os comandos disponíveis, os três níveis de concisão e os prompts prontos para cada fase do Spec-Kit.

O ensino deste tema acontece na [Aula 12](../plano-de-aula/aulas/aula-12-2026-11-09.md). O exemplo aplicado ponta a ponta está em [Exemplo de TODO List usando Caveman](../modelos/caveman-exemplo-todo-list.md).

---

## Instalação

O README do projeto apresenta uma instalação por script:

```bash
# macOS / Linux / WSL / Git Bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash
```

No Windows PowerShell:

```powershell
irm https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.ps1 | iex
```

Para instalação manual em vários agentes, o projeto também usa `npx skills add JuliusBrussee/caveman -a <agente>`. No Codex, o acionamento pode aparecer como `$caveman`; em outros agentes, como `/caveman` ou por instruções do tipo "responda em modo caveman".

!!! warning "Cuidado antes de rodar scripts remotos"
    Mesmo quando o repositório parece confiável, nunca execute `curl | bash` sem ler o script ou entender o que ele altera. A instalação é opcional no curso: o comportamento pode ser simulado com prompts de concisão.

---

## Comandos

O Caveman traz comandos e habilidades auxiliares. Nem todos funcionam em todos os agentes, a matriz de compatibilidade fica no README do projeto.

| Comando/Recurso | Para que serve | Exemplo de uso |
|---|---|---|
| `/caveman lite` | Reduz enrolação, mantendo escrita profissional | explicação curta para o grupo |
| `/caveman full` | Resposta fragmentada e direta | depuração, revisão, próximos passos |
| `/caveman ultra` | Máxima compressão | checklist rápido ou diagnóstico simples |
| `/caveman-commit` | Sugere mensagem de commit curta | `fix: block duplicate cpf` |
| `/caveman-review` | Produz comentários curtos de PR | `UserForm.tsx:42 — CPF sem validação. Adicionar schema.` |
| `/caveman-stats` | Mostra economia de tokens em ambientes suportados | acompanhar redução de saída |
| `/caveman:compress <arquivo>` | Comprime arquivo de memória ou notas | reduzir tamanho de `CLAUDE.md` |
| `caveman-shrink` | Comprime descrições de ferramentas MCP | diminuir custo de contexto de ferramentas |

Os comandos principais do curso são os três níveis de resposta (`lite`, `full`, `ultra`) e a simulação manual por prompt. Os recursos de commit, review, stats e compressão entram como extensão para quem quiser experimentar no projeto.

## Níveis de concisão

O Caveman organiza a concisão em níveis. Três deles são usados no curso:

1. **Lite** — remove enrolação, mas mantém gramática normal. Bom para respostas profissionais.
2. **Full** — usa frases curtas e fragmentos. Bom para depuração rápida e revisão técnica.
3. **Ultra** — resposta telegráfica. Bom para comandos, diagnósticos simples e listas de ação.

O desafio é perceber que "mais curto" não é sempre "melhor". Uma resposta ultra curta pode ser excelente para um bug óbvio e ruim para uma decisão arquitetural com trade-offs.

---

## Prompts prontos para cada fase do Spec-Kit

Um prompt por fase do Spec-Kit, para colar depois que o artefato daquela fase é gerado.

### Revisar constitution

```text
/caveman lite
Revise .specify/memory/constitution.md.
Liste apenas:
- princípio ambíguo
- princípio impossível de verificar
- conflito entre princípios
- princípio faltante para este projeto
Formato: problema — correção sugerida.
```

### Revisar spec

```text
/caveman full
Compare spec.md com o backlog/epic original.
Liste apenas divergências.
Formato:
Tipo: inventado | faltante | ambíguo | fora de escopo
Item:
Correção:
```

### Revisar plano técnico

```text
/caveman lite
Revise plan.md.
Separe:
Decisões técnicas:
Trade-offs:
Riscos:
Dependências externas:
Perguntas antes de codar:
```

### Revisar tasks

```text
/caveman full
Compare tasks.md com spec.md e plan.md.
Liste:
- tasks faltantes
- tasks fora de escopo
- tasks sem teste
- dependências em ordem errada
- tarefas que podem ser paralelas
Não explique além do necessário.
```

### Revisar implementação

```text
/caveman-review
Compare o código implementado com spec.md.
Formato: arquivo:linha — divergência — teste necessário.
Priorize bugs e critérios de aceitação não atendidos.
```

### Relatório final da feature

```text
/caveman ultra
Gere relatório final da feature.
Formato:
Feito:
Faltando:
Riscos:
Testes:
Próximo passo:
```
