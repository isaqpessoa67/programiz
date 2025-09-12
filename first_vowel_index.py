def first_vowel_index(s):
    vowel_list = 'aeiouAEIOU'
    for i, char in enumerate(s):
        if char in vowel_list:
            return i
        
first_vowel_index('world')
