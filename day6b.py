import os


def how_many_fish(lantern_fish_cnts, days_to_check):
    while days_to_check > 0:
        lantern_fish_cnts = {k: lantern_fish_cnts[k+1] for k in lantern_fish_cnts if k != 9}
        lantern_fish_cnts.update({9: 0})
        lantern_fish_cnts[8] += lantern_fish_cnts[-1]
        lantern_fish_cnts[6] += lantern_fish_cnts[-1]
        lantern_fish_cnts[-1] = 0
        days_to_check -= 1
    return sum(lantern_fish_cnts.values())


lantern_fish_cnts = {k: 0 for k in range(-1, 9)}
lantern_fish_cnts[9] = 0

with open(os.path.join("data", "day6.txt")) as f:
    for num in f.read().split(','):
        lantern_fish_cnts[int(num)] += 1

after_256 = how_many_fish(lantern_fish_cnts, 256)
print(after_256)
