
plates = []
while True:
    plate = input('>')
    num = int(plate[3:6])

    if num not in range(1,1000):
        continue

    if len(plates) == 0 and num == 1:
        plates.append(plate)
        print(f'Registered:{plates[0]}')
    elif num == int(plates[-1][3:6]) + 1:
        plates.append(plate)
        print(f'Regsitered:{plates[-1]}')
    elif len(plates) == 998 and num == 999:
        print("Game over!")
        break 


