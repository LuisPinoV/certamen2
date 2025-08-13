#!/usr/bin/env python3
import sys

current_company = None
total_profit = 0

for line in sys.stdin:
    company, profit = line.strip().split("\t", 1)
    try:
        profit = float(profit)
    except:
        continue

    if current_company == company:
        total_profit += profit
    else:
        if current_company is not None:
            print(f"{current_company}\t{total_profit}")
        current_company = company
        total_profit = profit

# Última compañía
if current_company is not None:
    print(f"{current_company}\t{total_profit}")
