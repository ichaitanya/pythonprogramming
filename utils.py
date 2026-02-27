def find_max(numbers):
    highest_number = numbers[0]

    for number in numbers:
        if number > highest_number:
            highest_number = number
    return highest_number