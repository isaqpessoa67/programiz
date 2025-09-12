def replace_vowels(string, char):
    char_to_replace = ['a', 'e', 'i', 'o', 'u']

    new_string = ''

    for i in string:
        if i in char_to_replace:
            i = char
        new_string += i
        print(new_string)
    return new_string

replace_vowels('this is a test', 'y')
replace_vowels('replace vowels', 'z')
replace_vowels('aeiou', 'u')
replace_vowels('hello world', 'x')