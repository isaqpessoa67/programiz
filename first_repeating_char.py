def first_repeating_char(s):
    first_repeating = ''
    seen_chars = []

    for char in s:
        if char in seen_chars:
            first_repeating = char
            return first_repeating
        seen_chars += char
    return "No repeating characters"

v = first_repeating_char('leila')
print(v)