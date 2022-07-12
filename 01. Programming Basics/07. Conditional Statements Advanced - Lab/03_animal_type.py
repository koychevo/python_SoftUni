animal = input()

if animal == "dog":
    animalType = "mammal"
elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
    animalType = "reptile"
else:
    animalType = "unknown"

print(animalType)