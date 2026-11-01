def find(people: list[dict], age: int) -> list[str]:
    result = []

    for attr in people:
        if attr['age'] == age:
            result.append(attr['name'])
        else:
            continue 
    
    return result 

print(find(
  [
    {
      "name": "Sara",
      "age": 30
    },
    {
      "name": "Oskar",
      "age": 30
    },
    {
      "name": "Emilia",
      "age": 32
    },
    {
      "name": "Anna",
      "age": 30
    }
  ],
  30
))