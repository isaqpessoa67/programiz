def mask_credit_card(card_number):
    new_card_number = ''

    for n, _ in enumerate(str(card_number)[:-4]):
        new_card_number += '*'
    new_card_number += str(card_number)[-4:]
    print(new_card_number)
    return new_card_number 

mask_credit_card(7241565286751867)