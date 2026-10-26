birds = {}

while True: 
    bird = input('Ange fågel:') 
    if bird not in birds:
        birds[bird] = 0
    birds[bird] += 1 
    total = sum(birds.values())
    print(f'({bird}) {birds[bird]} of {total}')