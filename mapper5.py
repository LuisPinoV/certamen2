#!/usr/bin/env python3
import sys
import csv

reader = csv.DictReader(sys.stdin)
for row in reader:
    try:
        budget = float(row['budget'])
        revenue = float(row['revenue'])
        runtime = float(row['runtime'])
        if budget > 0 and revenue > 0 and 0 < runtime <= 60:
            title = row['original_title'].strip()
            profit = revenue - budget
            print(f"{title}\t{profit},{runtime}")
    except:
        continue
