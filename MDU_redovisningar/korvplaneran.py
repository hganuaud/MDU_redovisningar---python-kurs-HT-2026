import math 

sausages_2 = int(input("How many students chose 2 sausages?"))
sausages_3 = int(input("How many students chose 3 sausages?"))
vegan_sausages_2 = int(input("How many students chose 2 vegan sausages?"))
vegan_sausages_3 = int(input("How many students chose 3 vegan sausages?"))

amount_in_packet = 8 
amount_in_vpacket = 4
amount_drinks = sausages_2 + sausages_3 + vegan_sausages_2 + vegan_sausages_3
amount_nonvegan = sausages_2 * 2 + sausages_3 * 3
amount_vegan = vegan_sausages_2 * 2 + vegan_sausages_3 * 3

price_sausage = 20.95
price_vegan = 34.95
price_drink = 13.95 

packet_nonvegan = math.ceil(amount_nonvegan/amount_in_packet)
packet_vegan = math.ceil(amount_vegan/amount_in_vpacket)

price_total = packet_nonvegan * price_sausage + price_vegan * packet_vegan + price_drink * amount_drinks

print("Regular sausages:", packet_nonvegan)
print("Vegan sausages:", packet_vegan)
print("Amount of drinks:", amount_drinks)
print("Total price:", price_total, "kr")





