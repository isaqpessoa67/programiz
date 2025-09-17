def maximize_first_number(numbers):
    number_to_rearrange = numbers[0]
    numbers.remove(numbers[0])

    number_to_rearrange_str = str(number_to_rearrange)
    number_to_rearrange_ord = sorted(number_to_rearrange_str, reverse=True)
    str_number_ord = "".join(number_to_rearrange_ord)
    number_ord = int(str_number_ord)
    

    numbers.insert(0, number_ord)
    print(numbers)
    return numbers

maximize_first_number([1234, 7890])