country = input()
equipment = input()

max_score = 20
score = 0

if country == "Russia":
    if equipment == "ribbon":
        score = 9.1 + 9.4
    elif equipment == "hoop":
        score = 9.3 + 9.8
    else:
        score = 9.6 + 9.0
elif country == "Bulgaria":
    if equipment == "ribbon":
        score = 9.6 + 9.4
    elif equipment == "hoop":
        score = 9.55 + 9.75
    else:
        score = 9.5 + 9.4
else:
    if equipment == "ribbon":
        score = 9.2 + 9.5
    elif equipment == "hoop":
        score = 9.45 + 9.35
    else:
        score = 9.7 + 9.15

print(f"The team of {country} get {score:.3f} on {equipment}.")
print(f"{(1 - score / max_score)  * 100 :.2f}%")