shape = input('shape: ')
try: 
    height = int(input('height: '))
    if shape.lower() == "rectangle":
        width = int(input('width:'))
        sh = '#' * int(width/2)
        for h in range(height):
            print(sh * height)
    elif shape.lower() == "triangle":
        for num in range(height + 1):
            print('#' * num)
    else: 
        print('Shape no avaliable')
except ValueError:
    print('Height must be a number')