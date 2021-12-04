import os

numbers = []

with open(os.path.join("data", "day3.txt"), mode="r") as f:
    for line in f:
        numbers.append(line.strip())

number_len = len(numbers[0])

gamma_rate = []

for i in range(number_len):
    current_digits = [int(entry[i]) for entry in numbers]
    gamma_rate.append('1' if sum(current_digits) >= 0.5 * len(current_digits) else '0')

epsilon_rate = ['0' if gamma == '1' else '1' for gamma in gamma_rate]

gamma_rate = int("".join(gamma_rate), 2)
epsilon_rate = int("".join(epsilon_rate), 2)

print(gamma_rate * epsilon_rate)
