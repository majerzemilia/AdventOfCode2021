import os

numbers = []

with open(os.path.join('data', 'day1.txt'), mode='r') as f:
    for line in f:
        numbers.append(int(line.strip()))

result = sum([sum(numbers[i+1:i+4]) > sum(numbers[i:i+3]) for i in range(len(numbers)-3)])

print(result)
