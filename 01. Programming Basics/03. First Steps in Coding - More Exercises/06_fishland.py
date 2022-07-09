mackerel_price = float(input())
sprat_price = float(input())
bonito_kilos = float(input())
scad_kilos = float(input())
mussels_kilos = float(input())

bonito_price = 1.6 * mackerel_price
scad_price = 1.8 * sprat_price
mussels_price = 7.5

total_costs = bonito_kilos * bonito_price + scad_kilos * scad_price + mussels_kilos * mussels_price
print(f"{total_costs:.2f}")