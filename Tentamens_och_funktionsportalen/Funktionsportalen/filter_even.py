def filter_even(numbers: list[int]) -> list[int]:
    result = []

    for num in numbers:
        if num % 2 == 0:
            result.append(num)
        else:
            continue 
    return result


print(filter_even(
  [
    4,
    -15,
    -16,
    -4,
    -1,
    -5,
    13,
    2,
    -16,
    20
  ]
))