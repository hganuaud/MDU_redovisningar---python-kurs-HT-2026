people = [
    {
        "name": "Anna",
        "age": 28
    },
    {
        "name": "Erik",
        "age": 35
    },
    {
        "name": "Maria",
        "age": 42
    },
    {
        "name": "Lars",
        "age": 19
    },
    {
        "name": "Sofia",
        "age": 55
    }
]

name = input('name > ')

for p in people:  
    if name == p['name']: 
        print(f"{p['name']} is {p['age']} years old.")
        break
else: 
    print('name not found')
        
    
    
        
    