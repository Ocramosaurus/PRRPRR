print("Miniräknare")
print("Skriv in två nummer")

number_1 = input()
try:
    number_1 = float(number_1)
except:
    print("Endast nummer!")
    exit()

number_2 = input()
try:
    number_2 = float(number_2)
except:
    print("Endast nummer!")
    exit()

print("Vill du addera, subtrahera, multiplicera eller dividera?")

def addera(x, y):
    return x + y

def subtrahera(x, y):
    return x - y

def multiplicera(x, y):
    return x * y

def dividera(x, y):
    if y == 0:
        return "FEL du kan inte dela med noll"
    return round(x / y, 2)

choice = input()

if choice == "addera":
    result = addera(number_1, number_2)
    print(round(result, 2))
elif choice == "subtrahera":
    result = subtrahera(number_1, number_2)
    print(round(result, 2))
elif choice == "multiplicera":
    result = multiplicera(number_1, number_2)
    print(round(result, 2))
elif choice == "dividera":
    result = dividera(number_1, number_2)
    print(result)
