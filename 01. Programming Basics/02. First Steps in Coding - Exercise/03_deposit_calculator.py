deposit = float(input())
months = int(input())
interest = float(input()) / 100

money = deposit + months * deposit * interest / 12
print(money)