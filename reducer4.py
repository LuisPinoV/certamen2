#!/usr/bin/env python3
import sys

current_genre = None
total_popularity = 0.0
total_runtime = 0.0
count = 0

results = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    genre, values = line.split('\t', 1)
    popularity, runtime = map(float, values.split(','))

    if current_genre == genre:
        total_popularity += popularity
        total_runtime += runtime
        count += 1
    else:
        if current_genre is not None:
            # Guardar resultado del género anterior
            avg_popularity = total_popularity / count
            avg_runtime = total_runtime / count
            results.append((avg_popularity, current_genre, avg_runtime))
        current_genre = genre
        total_popularity = popularity
        total_runtime = runtime
        count = 1

# Último género
if current_genre is not None:
    avg_popularity = total_popularity / count
    avg_runtime = total_runtime / count
    results.append((avg_popularity, current_genre, avg_runtime))

# Ordenar por popularidad descendente
for avg_popularity, genre, avg_runtime in sorted(results, key=lambda x: -x[0]):
    print(f"{genre}\t{avg_popularity:.2f},{avg_runtime:.2f}")
