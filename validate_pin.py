def validate_pin(pin):
    pin_len = len(pin)
    print(pin_len)

    if pin.isdigit() and (pin_len == 4 or pin_len == 6):
        return True
    else:
        return False

validate_pin('1234')