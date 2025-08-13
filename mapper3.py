#!/usr/bin/env python3
import sys
import csv

# Leer CSV desde stdin
reader = csv.DictReader(sys.stdin)

for row in reader:
    try:
        lang = row['original_language'].strip()
        budget = float(row['budget'])
        revenue = float(row['revenue'])
        vote = float(row['vote_average'])
        
        # Emitimos key=language y value=(profit, vote, 1)
        profit = revenue - budget
        print(f"{lang}\t{profit},{vote},1")
    except:
        # Ignorar filas con datos faltantes o inválidos
        continue
