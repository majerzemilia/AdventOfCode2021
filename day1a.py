import os

numbers = []

with open(os.path.join('data', 'day1.txt'), mode='r') as f:
    for line in f:
        numbers.append(int(line.strip()))
		
result = sum([numbers[i+1] > numbers[i] for i in range(len(numbers)-1)])

print(result)
