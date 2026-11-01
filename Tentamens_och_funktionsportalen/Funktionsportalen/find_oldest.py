def find_oldest(people: list[dict]) -> str:
    oldest = ""
    current_age = 0 

    for person in people:

        if person['age'] > current_age:
            current_age = person['age']
            oldest = person['name']
        else:
            continue 

    return oldest 


print(find_oldest(
  [
    {
      "name": "Elsa",
      "age": 27
    },
    {
      "name": "Oskar",
      "age": 46
    },
    {
      "name": "Lars",
      "age": 54
    },
    {
      "name": "Anna",
      "age": 44
    }
  ]
))