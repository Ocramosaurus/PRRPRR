print("Välkommen, vi säljer:")
print("Glass 20kr")
print("Varmkorv 15kr")
print("Läsk 15kr")
print("Godis 10kr")
print("Är det något du är intresserad av?")

wish = input()
wish = str(wish)
price = 0
price = int(price)

if wish == "Glass":
    price = price + 20

if wish == "Varmkorv":
    price = price + 15

if wish == "Läsk":
    price = price + 15

if wish == "Godis":
    price = price + 10

print("Hur många?")

quantity = input()
quantity = int(quantity)

print("Har du en rabbat kod?")

rabbat = input()

if rabbat == "Ja" or rabbat == "ja":
    print("Det kommer bli", (price * quantity) * 0.8, "kr")
elif rabbat != "Ja":
    print("Okej då blir det", price * quantity, "kr")




