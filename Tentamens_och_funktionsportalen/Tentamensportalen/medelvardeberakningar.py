turns = 0 
var = 0 

while True:
    number = input('>')
    if number.lower() == 'exit': 
        break
    else:
        try: 
            num = int(number)
            var += num
            turns += 1
        except ValueError:
            print('dat no number')

if turns != 0:
    print(var/turns)
else: 
    print('Error no values')
        

