
largest_num = 0
condition = True 

while condition == True:
    num = int(input("Number:"))
    if num>largest_num:
        largest_num = num
        continue
    elif num == 0:
        print("Largest number:", largest_num)
        break
    elif num<0:
        print("NOOOOOOOOOO")
    else:
        print("WRITE A NUMBER, IDIOT")
        continue 

    

