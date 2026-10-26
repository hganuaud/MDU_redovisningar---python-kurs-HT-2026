list_a = [4, 1, 9, 4, 7, 9, 3, 8, 5, 8]
list_b = [4, 1, 1, 4, 7, 9, 6, 8, 5, 8]

i = 0 

while i < len(list_a):
    x = list_a[i]
    y = list_b[i]
    print(f'({i})', end=' ')

    if x == y: 
        print(f'{x} - {y}')
    else: 
        print(f'{x} - {y} --> DIFF')

    i += 1


    


