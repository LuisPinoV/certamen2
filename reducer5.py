#!/usr/bin/env python3
import sys

movies = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    title, values = line.split('\t', 1)
    try:
        profit, runtime = map(float, values.split(','))
        movies.append((profit, title, runtime))
    except:
        continue

# Ordenar por profit descendente
for profit, title, runtime in sorted(movies, key=lambda x: -x[0]):
    print(f"{title}\t{profit:.2f},{runtime:.2f}")
