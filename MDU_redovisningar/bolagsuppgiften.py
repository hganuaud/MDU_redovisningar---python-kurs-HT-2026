nationality = input("Which country?")
sector = input("Which sector?")

matched = ""

if nationality.lower() == "sweden":
    print("You have chosen Swedish.")
    if sector.lower() == "food":
        matched = "Ica Gruppen AB"
    elif sector.lower() == "build":
        matched = "Skanska AB"
elif nationality.lower() == "usa":
    print("You have chosen American.")
    if sector.lower() == "food":
        matched = "Walmart INC"
    elif sector.lower() == "build":
        matched = "Betchel Group INC"
else: 
    print("The nationality isn't in our database")

if matched == "":
    print("No matches")
else:
    print("The biggest", sector, "supplier in", nationality, "is", matched)