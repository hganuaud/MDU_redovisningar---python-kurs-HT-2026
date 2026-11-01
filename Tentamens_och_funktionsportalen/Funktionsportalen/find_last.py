def find_last(people: list[dict], age: int) -> str:
    person = ""

    for p in people:
        if p['age'] == age:
            person = p['name']
        else:
            continue
    return person



print(find_last(
  [
    {
      "name": "Elsa",
      "age": 51
    },
    {
      "name": "Sara",
      "age": 50
    },
    {
      "name": "Maja",
      "age": 52
    },
    {
      "name": "Nils",
      "age": 52
    },
    {
      "name": "Anna",
      "age": 51
    },
    {
      "name": "Erik",
      "age": 50
    },
    {
      "name": "Johan",
      "age": 52
    }
  ],
  52
))