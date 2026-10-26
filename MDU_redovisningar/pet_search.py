
pets = [
    { 'name': 'Smulan', 'type': 'cat' },
    { 'name': 'Molly', 'type': 'dog' },
    { 'name': 'Stampe', 'type': 'rabbit' },
    { 'name': 'Bella', 'type': 'cat' },
    { 'name': 'Blubbe', 'type': 'fish' },
    { 'name': 'Morris', 'type': 'dog' }
]

def pet_filter(pets: list) -> list:
        filtered_pets = []
        for p in pets:
            if p["type"] == 'dog' or p["type"] == 'cat':
                filtered_pets.append(p)
        return filtered_pets
    

cat_and_dogs = pet_filter(pets)

for pet in cat_and_dogs:
    print(pet["name"], '(' + pet["type"] + ')')
