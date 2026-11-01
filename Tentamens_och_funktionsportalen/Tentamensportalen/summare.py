total = 0 

while True:
    try:
        num = int(input('>'))

        if num != 0:
            total += num
        else:
            print('Total:', total)
            break 

    except ValueError:
        print('Not a valid number')