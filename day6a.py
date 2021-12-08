import os


def how_many_fish(lantern_fish, days_to_check):
    while days_to_check > 0:
        lantern_fish = list(map(lambda x: x - 1, lantern_fish))
        new_fish = len(list(filter(lambda x: x == -1, lantern_fish)))
        lantern_fish = list(map(lambda x: 6 if x == -1 else x, lantern_fish))
        lantern_fish += [8] * new_fish
        days_to_check -= 1
    return len(lantern_fish)


with open(os.path.join("data", "day6.txt")) as f:
    lantern_fish = [int(num) for num in f.read().split(',')]

after_80 = how_many_fish(lantern_fish, 80)
print(after_80)
