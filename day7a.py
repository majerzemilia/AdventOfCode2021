import os
import statistics

with open(os.path.join("data", "day7.txt")) as f:
    positions = [int(num) for num in f.read().split(',')]

best_position = int(statistics.median(positions))

fuel_spent = sum([abs(position - best_position) for position in positions])

print(fuel_spent)
