chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15
delivery_costs = 2.50

chicken_menu_count = int(input())
fish_menu_count = int(input())
vegetarian_menu_count = int(input())

menus_costs = chicken_menu_count * chicken_menu_price + fish_menu_count * fish_menu_price + vegetarian_menu_count * vegetarian_menu_price
dessert_costs = 0.2 * menus_costs

total_costs = menus_costs + dessert_costs + delivery_costs
print(total_costs)