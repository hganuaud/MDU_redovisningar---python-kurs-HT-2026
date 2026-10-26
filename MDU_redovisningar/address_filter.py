def get_name(adress: str) -> str:
    for p in people: 
        if address.lower() == p['address'].lower():
            return p['name']
    else: 
        raise KeyError
    


people = [
    {
        'address': 'Funktionstorget 2',
        'name': 'Lena Eriksson'
    },
    {
        'address': 'Listgatan 1',
        'name': 'Erik Olsson'
    },
    {
        'address': 'Strängvägen 3',
        'name': 'Emma Johansson'
    }
]

while True:
    address = input('address > ')

    try:
        print('MATCH:', get_name(address))
    except KeyError:
        print('ERROR: no such address')

    print()