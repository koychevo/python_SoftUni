town = input()
sales = float(input())
commission = 0
is_error = False

if town == "Sofia":
    if sales < 0:
        is_error = True
    elif sales <= 500:
        commission = 0.05
    elif sales <= 1000:
        commission = 0.07
    elif sales <= 10000:
        commission = 0.08
    else:
        commission = 0.12
elif town == "Varna":
    if sales < 0:
        is_error = True
    elif sales <= 500:
        commission = 0.045
    elif sales <= 1000:
        commission = 0.075
    elif sales <= 10000:
        commission = 0.1
    else:
        commission = 0.13
elif town == "Plovdiv":
    if sales < 0:
        is_error = True
    elif sales <= 500:
        commission = 0.055
    elif sales <= 1000:
        commission = 0.08
    elif sales <= 10000:
        commission = 0.12
    else:
        commission = 0.145
else:
    is_error = True

if is_error:
    print("error")
else:
    print(f"{sales * commission:.2f}")