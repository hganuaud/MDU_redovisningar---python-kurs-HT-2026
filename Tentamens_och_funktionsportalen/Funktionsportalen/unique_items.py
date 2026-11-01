

def unique(*items) -> list:
    unique_list = []

    for i in items:
        if i not in unique_list:
            unique_list.append(i)
        else:
            continue

    return unique_list


print(unique(
  -2,
  2.5,
  -1.5,
  "A",
  -1.5,
  "B",
  -2,
  2,
  2.5,
  "B",
  -2.5,
  -1,
  2.5,
  1.5
))

