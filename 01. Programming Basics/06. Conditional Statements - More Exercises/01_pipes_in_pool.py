pool_volume = int(input())
capacity_first_pipe = int(input())
capacity_second_pipe = int(input())
hours = float(input())

water_from_first_pipe = hours * capacity_first_pipe
water_from_second_pipe = hours * capacity_second_pipe

water = water_from_first_pipe + water_from_second_pipe
water_difference = water - pool_volume

if water_difference > 0:
    print(f"For {hours} hours the pool overflows with {water_difference} liters.")
else:
    print(f"The pool is {water / pool_volume * 100:.2f}% full. \
    Pipe 1: {water_from_first_pipe / water * 100:.2f}%. \
    Pipe 2: {water_from_second_pipe / water * 100:.2f}%.")
