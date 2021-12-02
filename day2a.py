import os

commands = {
    "forward": 0,
    "down": 0,
    "up": 0
}

with open(os.path.join('data', 'day2.txt'), mode='r') as f:
    for line in f:
        cmd, val = line.split()
        commands[cmd] += int(val)
        
horizontal_pos = commands["forward"]
depth = commands["down"] - commands["up"]

print(horizontal_pos * depth)
