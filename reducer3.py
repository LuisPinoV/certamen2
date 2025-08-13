#!/usr/bin/env python3
import sys

current_lang = None
total_profit = 0
total_votes = 0
count_votes = 0

results = []

for line in sys.stdin:
    line = line.strip()
    lang, values = line.split('\t')
    profit, vote, count = values.split(',')
    
    profit = float(profit)
    vote = float(vote)
    count = int(count)
    
    if current_lang == lang:
        total_profit += profit
        total_votes += vote
        count_votes += count
    else:
        if current_lang:
            avg_vote = total_votes / count_votes if count_votes > 0 else 0
            results.append((current_lang, total_profit, avg_vote))
        current_lang = lang
        total_profit = profit
        total_votes = vote
        count_votes = count

# Último idioma
if current_lang:
    avg_vote = total_votes / count_votes if count_votes > 0 else 0
    results.append((current_lang, total_profit, avg_vote))

# Ordenar resultados: profit descendente, avg_vote descendente
results.sort(key=lambda x: (x[1], x[2]), reverse=True)

# Imprimir
for lang, profit, avg_vote in results:
    print(f"{lang}\t{profit}\t{avg_vote:.2f}")
