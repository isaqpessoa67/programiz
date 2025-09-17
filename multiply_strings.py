def multiply_strings(num1, num2):
    if num1.isdigit() and num2.isdigit():
        num1_int = int(num1)
        num2_int = int(num2)

        multiply_str = num1_int * num2_int
    return str(multiply_str)
