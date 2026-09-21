#!/usr/bin/env python3
"""Confere que as promessas feitas ao aluno batem entre si.

O `mkdocs build --strict` valida link e âncora: ele garante que a página existe.
O que ele não vê é promessa divergente — um exercício com prazo que o cronograma
não tem, uma pasta cobrada no calendário e não descrita em lugar nenhum, uma
frente de nota que sumiu da soma. Esse tipo de erro chega ao aluno em forma de
"não sei o que entregar" ou, pior, de nota que ele não sabia como cumprir.

Cada verificação abaixo existe porque o erro correspondente custa algo concreto.
Rode antes de publicar; o CI roda por você em todo pull request.
"""

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DOCS = RAIZ / "docs"

falhas: list[str] = []
notas: list[str] = []


def ler(caminho: str) -> str:
    return (DOCS / caminho).read_text(encoding="utf-8")


entregas = ler("entregas/index.md")
cronograma = ler("cronograma/cronograma.md")
avaliacao = ler("avaliacao/avaliacao.md")

# O calendário é a fonte das entregas individuais: uma linha por exercício, com
# a página da aula, a pasta cobrada e a data de vencimento.
CALENDARIO = re.compile(r"^\| \[([^\]]+)\]\(([^)]+)\) \|[^|]*\| `([^`]+)`", re.M)
linhas = CALENDARIO.findall(entregas)

if not linhas:
    falhas.append(
        "não encontrei nenhuma linha no calendário de entregas — "
        "o formato da tabela mudou e este script precisa acompanhar"
    )


# 1. Toda linha do calendário aponta uma página de aula que existe.
#    Link morto aqui é aluno que não acha o enunciado do que tem de entregar.
for rotulo, link, _pasta in linhas:
    if not (DOCS / "entregas" / link).resolve().exists():
        falhas.append(f"calendário: a linha [{rotulo}] aponta {link}, que não existe")


# 2. Toda pasta cobrada no calendário é descrita em "Detalhamento por aula",
#    e todo detalhamento corresponde a uma linha do calendário. Pasta cobrada
#    sem descrição é entrega sem enunciado; descrição sem linha é prazo invisível.
detalhamento = entregas.split("## Detalhamento por aula")[-1]
pastas_detalhadas = set(re.findall(r"\*\*Pasta:\*\* `([^`]+)`", detalhamento))
pastas_cobradas = {pasta for _r, _l, pasta in linhas}

for pasta in sorted(pastas_cobradas - pastas_detalhadas):
    falhas.append(f'o calendário cobra `{pasta}`, sem seção em "Detalhamento por aula"')
for pasta in sorted(pastas_detalhadas - pastas_cobradas):
    falhas.append(f'"Detalhamento por aula" descreve `{pasta}`, ausente do calendário')


# 3. Toda página de aula publicada aparece no cronograma. Aula fora do
#    cronograma é conteúdo que existe no site e que ninguém sabe quando acontece.
for aula in sorted((DOCS / "plano-de-aula" / "aulas").glob("*.md")):
    if aula.name not in cronograma:
        falhas.append(f"a aula {aula.name} não é citada no cronograma")


# 4. As frentes da avaliação somam 100. A fórmula da nota depende disso, e o
#    erro só apareceria quando alguém fechasse o semestre.
frentes = re.findall(r"^\| ([^|]+?) \| (\d+) pontos \|", avaliacao, re.M)
if not frentes:
    falhas.append("não encontrei a tabela de frentes em avaliacao.md")
else:
    soma = sum(int(pontos) for _nome, pontos in frentes)
    if soma != 100:
        detalhe = ", ".join(f"{n.strip()}={p}" for n, p in frentes)
        falhas.append(f"as frentes da avaliação somam {soma}, não 100 — {detalhe}")
    else:
        notas.append(f"frentes da avaliação: {len(frentes)}, somando {soma}")


# 5. Toda data de vencimento do calendário existe no cronograma. Vencimento em
#    data sem encontro é prazo que o aluno não tem como cumprir.
vencimentos = sorted(set(re.findall(r"\*\*(Seg|Ter), (\d{2}/\d{2})\*\*", entregas)))
for dia, data in vencimentos:
    if f"{dia}, {data}/2026" not in cronograma:
        falhas.append(f"o vencimento {dia}, {data} não corresponde a nenhuma data do cronograma")


# ---------------------------------------------------------------- relatório
print(f"  {len(linhas)} entregas no calendário, {len(vencimentos)} datas de vencimento")
for nota in notas:
    print(f"  {nota}")

if falhas:
    print(f"\n  {len(falhas)} inconsistência(s) entre as promessas feitas ao aluno:\n")
    for falha in falhas:
        print(f"   ✗ {falha}")
    sys.exit(1)

print("  tudo consistente: calendário, cronograma e avaliação contam a mesma história")
