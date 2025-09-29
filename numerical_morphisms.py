def numerical_morphisms(n):
    n_string = str(n)
    final_number = ''
    
    for char in n_string:
        char_int = int(char)
        char_int += 1
        char_int_str = str(char_int)
        final_number += char_int_str
    return final_number
        
numerical_morphisms(1234)