def product_of_list(*args):
    index_counter = 1

    for number in args:
        while index_counter < len(args):
            number *= args[index_counter]
            index_counter += 1
        return number

n = product_of_list(2, 3, 4)
print(n)