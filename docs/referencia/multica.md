# Referência — Multica

Página de consulta. Descreve a instalação do Multica, os comandos da CLI, os campos de um agente, os estados e limites do runtime e as regras de skills.

O ensino deste tema acontece na curiosidade [Orquestração e Observabilidade](../curiosidades/orquestracao-e-observabilidade.md). O porquê dos conceitos está em [Sobre o Multica](../explicacoes/multica.md).

Fonte de tudo o que segue: a [documentação oficial](https://multica.ai/docs). Flags variam entre versões; a fonte final é `multica <comando> --help`.

---

## Requisitos

- Conta no Multica, criada em [multica.ai](https://multica.ai)
- Pelo menos **uma ferramenta de código com IA** instalada **e com login feito** no computador
- A ferramenta precisa ter sido aberta ao menos uma vez sozinha no terminal, para concluir o login ou a configuração do provedor

O daemon só sobe se detectar pelo menos uma ferramenta suportada. Abaixo da versão mínima, a ferramenta não vira runtime.

| Ferramenta | Comando detectado | Versão mínima |
|-----------|-------------------|---------------|
| Claude Code | `claude` | 2.0.0 |
| Codex CLI | `codex` | 0.100.0 |
| GitHub Copilot CLI | `copilot` | 1.0.0 |
| OpenCode | `opencode` | 1.1.54 |
| Qwen Code | `qwen` | 0.20.0 |

A lista completa, com mais de trinta ferramentas, está em [Install AI coding tools](https://multica.ai/docs/install-agent-runtime). "Suportada" significa que o Multica consegue acionar a ferramenta — não que ele forneça conta ou cota.

Conferir se a ferramenta está no `PATH`:

```bash
# macOS / Linux / WSL
command -v claude
claude --version
```

```powershell
# Windows PowerShell
Get-Command claude
claude --version
```

---

## Instalação

Há dois caminhos.

| Caminho | Quando usar | Como |
|---------|-------------|------|
| **Multica Desktop** | Computador pessoal, com interface gráfica | Baixar em [multica.ai/download](https://multica.ai/download). Ao entrar, o Desktop sobe o daemon, registra o computador e detecta as ferramentas |
| **Multica CLI** | Servidor, máquina remota ou sem interface | Comandos abaixo |

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash

# ou, com Homebrew
brew install multica-ai/tap/multica

multica version
```

!!! warning "Cuidado antes de rodar scripts remotos"
    Nunca execute `curl | bash` sem ler o script. O comando para Windows está na [página da CLI](https://multica.ai/docs/cli).

### Primeira conexão

```bash
multica setup          # salva o servidor, abre o navegador para login e sobe o daemon
multica auth status
multica daemon status

multica login          # só refaz o login, sem sobrescrever o resto
multica login --token  # máquina sem navegador: cola um token pessoal criado na web
```

---

## Daemon

| Comando | Efeito |
|---------|--------|
| `multica daemon start` | Sobe o daemon em segundo plano |
| `multica daemon start --foreground` | Sobe preso ao terminal, útil para depurar |
| `multica daemon status` | Estado atual |
| `multica daemon logs -f` | Acompanha o log |
| `multica daemon restart` | Reinicia — **necessário depois de instalar ferramenta nova** |
| `multica daemon stop` | Para |
| `multica daemon autostart enable` | Volta sozinho depois de reiniciar o computador |
| `multica daemon autostart status` | Mostra se o autostart está ativo |
| `multica daemon autostart disable` | Desliga o autostart |
| `multica config set workspaces_root <caminho>` | Muda a pasta de trabalho. Padrão: `~/multica_workspaces` |

!!! note "Daemon iniciado pela CLI não volta sozinho"
    Sem `autostart enable`, o daemon não sobe de novo depois de um reboot. No Desktop ele sobe junto com o aplicativo.

### Estados e limites do runtime

| Item | Valor padrão |
|------|--------------|
| Heartbeat do daemon | a cada 15 s |
| Marcado como offline após saída inesperada | em cerca de 3 min |
| Rótulo nos primeiros 5 min sem contato | *Recently lost*, depois *Offline* |
| Tolerância antes de falhar runs em andamento (`MULTICA_RUNTIME_RECONNECT_GRACE`) | 3 h — depois disso o run falha com `runtime_offline` |
| Runs simultâneos por daemon (`MULTICA_DAEMON_MAX_CONCURRENT_TASKS`) | 20 |
| Runs simultâneos por agente | 6 |
| Limpeza da pasta de run de issue fechada | após 24 h sem atualização |

O limite efetivo é o **menor** entre o do daemon e o do agente. Runtime local é **privado por padrão**; só o dono pode torná-lo público ou compartilhar com pessoas específicas.

---

## Comandos usados no tutorial oficial

| Comando | Para que serve |
|---------|----------------|
| `multica repo add` | Registra um repositório no workspace |
| `multica agent update` | Altera a configuração de um agente — inclusive o próprio agente, a partir de um pedido no chat |
| `multica env start web` | Sobe o ambiente de desenvolvimento ligado à issue |
| `multica skill import --file ./review-helper.skill` | Importa uma skill a partir de arquivo |
| `multica skill refresh <skill-id>` | Atualiza uma skill importada de fonte hospedada |

---

## Campos de um agente

| Campo | Regra |
|-------|-------|
| **Name** | Obrigatório, único no workspace |
| **Runtime** | Obrigatório |
| Description | Aparece só na lista e no detalhe — **nunca** vai para o prompt |
| Instructions | Enviadas em **todo** run |
| Model / thinking level | Em branco usa o padrão do runtime ou da CLI local |
| Access | *Only me* (padrão), *Entire workspace* ou *Specific people*. Só o dono muda |
| Concurrency limit | Padrão 6 |
| Environment variables | Guardadas em **texto puro** no servidor. `PATH`, `HOME` e `MULTICA_*` não podem ser sobrescritas |
| Custom arguments | Passados item a item, sem expansão de shell. Argumentos reservados, como `--permission-mode`, são recusados |
| MCP | Por agente ou a partir da biblioteca do workspace |
| Conversation starters | Até três pares rótulo/prompt |

Duplicar um agente copia quase tudo, **exceto** valores de variáveis de ambiente e configuração de MCP.

---

## Skills

| Forma de criar | Origem |
|----------------|--------|
| Create manually | Escrita na interface |
| Import from local | Pasta com `SKILL.md`, ou arquivo `.skill` / `.zip` |
| Import from URL | GitHub, ClawHub, [skills.sh](https://www.skills.sh/) |
| Copy from a runtime | Cópia de uma skill já presente no computador |

| Limite | Valor |
|--------|-------|
| Tamanho por arquivo | 1 MiB, UTF-8 |
| Arquivos de apoio | até 512, somando no máximo 8 MiB |
| Caminho reservado | `SKILL.md` |

- Um agente usa várias skills, e uma skill serve a vários agentes
- Prefira **desativar** o vínculo a apagar a skill: apagar é definitivo e remove de todos os agentes
- Quem criou e os donos/admins do workspace editam; os demais só usam
- Skills do repositório, como `.claude/skills/` e `.agents/skills/`, são lidas direto por algumas ferramentas, mas **não** viram skills do workspace automaticamente

!!! danger "Skill importada não é revisada"
    O Multica não revisa, não assina e não isola skills importadas. Leia o `SKILL.md` antes de anexar a um agente.

---

## Espaços da interface

| Espaço | O que reúne |
|--------|-------------|
| **Work** | Inbox, Views, Projects |
| **Team** | Agents, Squads, Skills, Runtimes, Analytics |
| **Chat** | Conversas com agentes fora de issue |
| **Auto** | Autopilots: agenda (cron), fuso, modo *Create issue* ou *Run only*, botão *Run now* |

| Atalho | Ação |
|--------|------|
| `C` | Nova issue |
| `⌘K` | Busca |
| `⌘J` | *Ask Multica* — chat rápido |

### Papéis de pessoas no workspace

| Papel | Escopo |
|-------|--------|
| Member | Workspace inteiro |
| Admin | Workspace inteiro, com configuração |
| Guest | Só os projetos compartilhados, sem ocupar vaga |
