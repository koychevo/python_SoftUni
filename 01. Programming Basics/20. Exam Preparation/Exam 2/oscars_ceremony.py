hall_rent = int(input())

statuette_costs = 0.7 * hall_rent
catering_costs = 0.85 * statuette_costs
music_costs = 0.5 * catering_costs

total_costs = hall_rent + statuette_costs + catering_costs + music_costs
print(f"{total_costs:.2f}")