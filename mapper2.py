#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
header = True

for row in reader:
    if header:
        header = False
        continue

    try:
        budget = float(row[1])   # budget
        revenue = float(row[9])  # revenue
        runtime = float(row[10]) # runtime
        title = row[11]          # title

        if runtime > 180 and revenue <= budget and revenue > 0 and budget > 0:
            profit = revenue - budget
            print(f"{title}\t{runtime}\t{budget}\t{revenue}\t{profit}")
    except:
        continue
