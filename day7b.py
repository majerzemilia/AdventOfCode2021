import os
from statistics import mean
from math import floor, ceil

with open(os.path.join("data", "day7.txt")) as f:
    positions = [int(num) for num in f.read().split(',')]

positions_mean = mean(positions)

to_check = [floor(positions_mean), ceil(positions_mean)]

fuel_spent = lambda best_position: sum([sum(range(abs(position - best_position) + 1)) for position in positions])

print(min(map(fuel_spent, to_check)))
