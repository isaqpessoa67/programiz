def same_parity(numbers):
    if numbers[0] % 2 != 0:
        for number in numbers:
            if number % 2 == 0:
                del numbers[numbers.index(number)]
    else:
        for number in numbers:
            if number % 2 != 0:
                del numbers[numbers.index(number)]
    return numbers