
def map_square(numbers: list[int]) -> list[int]:
    squared_numbers = []

    for num in numbers:
        squared_numbers.append(num*num)

    return squared_numbers


print(map_square(
  [
    19,
    9,
    -5,
    -3,
    18,
    5,
    15,
    -7,
    -8
  ]
))