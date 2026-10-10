"""Primeira leitura dos dois datasets, só com a biblioteca padrão (10/10/2026).

Uso: python -X utf8 scripts/01_primeira_leitura.py data/customer_support_tickets.csv data/all_tickets_processed_improved_v3.csv
Objetivo: antes de qualquer análise, conferir se o dado tem sinal.
"""
import csv, sys, statistics as st
from collections import Counter, defaultdict
from datetime import datetime

d1, d2 = sys.argv[1], sys.argv[2]
rows = list(csv.DictReader(open(d1, encoding="utf-8")))
print("D1 linhas:", len(rows))
print("colunas:", list(rows[0].keys()))
for c in ["Ticket Type", "Ticket Status", "Ticket Priority", "Ticket Channel", "Ticket Subject", "Product Purchased"]:
    cnt = Counter(r[c] for r in rows)
    print(f"\n{c}: {len(cnt)} valores ->", cnt.most_common(6))

print("\nAmostra de 3 tickets:")
for r in rows[:3]:
    print(" TYPE:", r["Ticket Type"], "| SUBJ:", r["Ticket Subject"])
    print(" DESC:", r["Ticket Description"][:260].replace("\n", " "))
    print(" RES :", r["Resolution"][:120])
    print(" FRT:", r["First Response Time"], "TTR:", r["Time to Resolution"], "CSAT:", r["Customer Satisfaction Rating"], "\n")

# placeholders e coerência tipo x assunto
ph = sum("{product_purchased}" in r["Ticket Description"] for r in rows)
print("descrições com placeholder {product_purchased}:", ph)
desc = Counter(r["Ticket Description"][:80] for r in rows)
print("aberturas de descrição distintas (80 chars):", len(desc))
ts = defaultdict(Counter)
for r in rows: ts[r["Ticket Subject"]][r["Ticket Type"]] += 1
print("assunto 'Refund request' por tipo:", dict(ts.get("Refund request", {})))

# tempos e CSAT
def p(x):
    try: return datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
    except: return None
fechados = [r for r in rows if r["Ticket Status"] == "Closed"]
print("\nfechados:", len(fechados))
neg = 0; horas = []
for r in fechados:
    a, b = p(r["First Response Time"]), p(r["Time to Resolution"])
    if a and b:
        h = (b - a).total_seconds() / 3600; horas.append(h); neg += h < 0
print("resolução antes da 1ª resposta (negativo):", neg, "de", len(horas))
if horas: print("horas 1ª resp→resolução: mediana", round(st.median(horas), 1), "min", round(min(horas), 1), "max", round(max(horas), 1))
pc = Counter(r["Date of Purchase"][:4] for r in rows) if "Date of Purchase" in rows[0] else {}
print("ano da compra:", dict(pc))
print("ano/mês FRT:", Counter(r["First Response Time"][:7] for r in rows if r["First Response Time"]).most_common(4))
cs = [int(float(r["Customer Satisfaction Rating"])) for r in fechados if r["Customer Satisfaction Rating"]]
print("CSAT dist:", sorted(Counter(cs).items()))
for c in ["Ticket Channel", "Ticket Priority", "Ticket Type"]:
    g = defaultdict(list)
    for r in fechados:
        if r["Customer Satisfaction Rating"]: g[r[c]].append(float(r["Customer Satisfaction Rating"]))
    print(f"CSAT médio por {c}:", {k: round(st.mean(v), 2) for k, v in g.items()})

rows2 = list(csv.DictReader(open(d2, encoding="utf-8")))
print("\nD2 linhas:", len(rows2), "colunas:", list(rows2[0].keys()))
print("Topic_group:", Counter(r["Topic_group"] for r in rows2).most_common())
for r in rows2[:3]: print(" -", r["Topic_group"], "|", r["Document"][:160])
