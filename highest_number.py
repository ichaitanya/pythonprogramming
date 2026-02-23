numbers = [5, 16, 69, 2, 4, 6]

highest_number = numbers[0]

for number in numbers:
    if number > highest_number:
        highest_number = number
print(highest_number)