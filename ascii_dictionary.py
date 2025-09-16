def ascii_dictionary(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyp'
    ascii_code = 96
    ascii_dict = {}

    for letter in alphabet:
        ascii_code += 1
        for char in string:
            if char == letter:
                ascii_dict.update({char: ascii_code})
    return ascii_code

ascii_dictionary('def')