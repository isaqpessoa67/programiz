def eliminate_odd_numbers(numbers):
    
    for number in numbers:
        if number % 2 != 0:
            del numbers[numbers.index(number)]
    return numbers