#!/usr/bin/env python3
import sys
import csv

# Leer CSV desde stdin
reader = csv.DictReader(sys.stdin)
for row in reader:
    try:
        runtime = float(row['runtime'])
        if runtime >= 120:
            genres = row['genres'].strip()
            popularity = float(row['popularity'])
            print(f"{genres}\t{popularity},{runtime}")
    except:
        # Ignorar filas con valores faltantes o inválidos
        continue
