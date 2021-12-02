import os

horizontal_pos = 0
depth = 0
aim = 0

with open(os.path.join('data', 'day2.txt'), mode='r') as f:
    for line in f:
        cmd, val = line.split()
        val = int(val)
        if cmd == "down":
            aim += val
        elif cmd == "up":
            aim -= val
        else:
            horizontal_pos += val
            depth += aim * val

print(horizontal_pos * depth)
