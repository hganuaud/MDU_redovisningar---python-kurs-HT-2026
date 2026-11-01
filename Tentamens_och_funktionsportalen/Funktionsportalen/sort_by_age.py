def sort_by_age(people: list[dict]) -> list[str]:
    sorted_list = []
    ages = []
    sorted_ages = []
    
    for p in people:
        ages.append(p['age']) 
        sorted_ages = sorted(ages)
    
    for age in sorted_ages:
        for p in people:
            if p['age'] == age:
                sorted_list.append(p['name'])

      
    return sorted_list

print(sort_by_age(
  [
    {
      "name": "Maja",
      "age": 41
    },
    {
      "name": "Emilia",
      "age": 36
    },
    {
      "name": "Johan",
      "age": 25
    },
    {
      "name": "Lars",
      "age": 40
    },
    {
      "name": "Nils",
      "age": 39
    }
  ]
)
)