def is_weird(n):
    range_not_weird = list(range(2, 6))
    range_weird = list(range(6, 21))

    if n % 2 != 0:
        return 'Weird'
    elif n in range_not_weird:
        return 'Not Weird'
    elif n in range_weird:
        return 'Weird'
    elif n > 20:
        return 'Not Weird'
