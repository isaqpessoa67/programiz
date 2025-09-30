def check_result(marks):
    while marks <= 100 and marks >= 0:
        if marks >= 40:
            return 'Pass'
        return 'Fail'
    return 'Invalid'

print(check_result(0))