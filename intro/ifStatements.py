print("hur gammal är du?")

age = input()
age = int(age)

if age < 18:
    print("du är ett barn")

elif age == 18:
    print("Du är 18")

elif age >= 18 and age < 56:
    print("du är vuxen")

elif age > 55:
    print("du är gammal")