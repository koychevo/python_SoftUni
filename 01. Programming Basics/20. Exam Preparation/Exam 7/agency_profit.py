company_name = input()
adult_tickets_count = int(input())
kid_tickets_count = int(input())
adult_ticket_price = float(input())
service_fee = float(input())

kid_ticket_price = 0.3 * adult_ticket_price

income = adult_tickets_count * (adult_ticket_price + service_fee) + kid_tickets_count * (kid_ticket_price + service_fee)
profit = 0.2 * income
print(f"The profit of your agency from {company_name} tickets is {profit:.2f} lv.")