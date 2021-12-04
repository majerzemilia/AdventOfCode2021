import os

numbers = []

with open(os.path.join("data", "day3.txt"), mode="r") as f:
    for line in f:
        numbers.append(line.strip())

number_len = len(numbers[0])

oxygen_generator_rating = numbers[:]

i = 0
while(len(oxygen_generator_rating) > 1 and i < number_len):
    current_digits = [int(entry[i]) for entry in oxygen_generator_rating]
    current_digit = '1' if sum(current_digits) >= 0.5 * len(current_digits) else '0'
    oxygen_generator_rating = list(filter(lambda x: x[i] == current_digit, oxygen_generator_rating))
    i += 1

CO2_scrubber_rating = numbers[:]

i = 0
while(len(CO2_scrubber_rating) > 1 and i < number_len):
    current_digits = [int(entry[i]) for entry in CO2_scrubber_rating]
    current_digit = '1' if sum(current_digits) < 0.5 * len(current_digits) else '0'
    CO2_scrubber_rating = list(filter(lambda x: x[i] == current_digit, CO2_scrubber_rating))
    i += 1

oxygen_generator_rating = int("".join(oxygen_generator_rating), 2)
CO2_scrubber_rating = int("".join(CO2_scrubber_rating), 2)

print(oxygen_generator_rating * CO2_scrubber_rating)
