num = int(input('Write number:'))

def is_even(num: int) -> bool:
    state = False
    if num % 2 == 0:
        state = True
    else:
        state = False
    return state

print(is_even(num))
