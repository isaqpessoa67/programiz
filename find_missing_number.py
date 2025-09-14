def find_missing_number(numbers):
    complete_numbers = [1, 2, 3, 4, 5]
    missing_number = 0

    for n in complete_numbers:
        if n not in numbers:
            missing_number = n
            return missing_number
        continue

find_missing_number([1, 2, 3, 5])