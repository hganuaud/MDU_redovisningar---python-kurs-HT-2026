def find_first(people: list[dict], age: int) -> str:
    person = ""

    for p in people:
        if p['age'] == age:
            person = p['name']
            break  
    return person

print(find_first(
  [
    {
      "name": "Oskar",
      "age": 22
    },
    {
      "name": "Erik",
      "age": 25
    },
    {
      "name": "Johan",
      "age": 25
    },
    {
      "name": "Maja",
      "age": 23
    },
    {
      "name": "Anna",
      "age": 20
    }
  ],
  20
))