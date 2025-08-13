#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)

# Omitir encabezado si está presente
header = True

for row in reader:
    if header:
        header = False
        continue

    try:
        budget = float(row[1])                 # budget
        revenue = float(row[9])                # revenue
        runtime = float(row[10])               # runtime
        production_companies = row[7]          # production_companies

        if runtime < 90 and budget > 0 and production_companies != '[]':
            profit = revenue - budget
            print(f"{production_companies}\t{profit}")
    except:
        continue
