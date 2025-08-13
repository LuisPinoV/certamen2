#!/usr/bin/env python3
import sys

movies = []

for line in sys.stdin:
    try:
        title, runtime, budget, revenue, profit = line.strip().split("\t")
        movies.append((float(profit), title, runtime, budget, revenue))
    except:
        continue

# Ordenar por profit ascendente
movies.sort(key=lambda x: x[0])

# Imprimir solo los 10 primeros
for profit, title, runtime, budget, revenue in movies[:10]:
    print(f"{title}\t{runtime}\t{budget}\t{revenue}\t{profit}")
