def numeric_seesaw(n):
    numbers_list = []
    counter = 0

    while counter < n:
        counter += 1
        numbers_list.append(counter)
        continue
    while counter == n or counter < n:
        counter -= 1
        if counter == 0:
            break
        numbers_list.append(counter)
        continue
    return numbers_list