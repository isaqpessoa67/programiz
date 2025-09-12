def character_occurrence(string, char):
    char_occurrence = 0

    for character in string:
        if character == char:
            char_occurrence += 1
    return char_occurrence

character_occurrence('this is a test', 't')