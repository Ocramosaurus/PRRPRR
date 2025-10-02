sentence = "Hej på dig"

"""
for letter in sentence:
    print(letter)
"""


for i in range(1, 11):
    print(i)

gambling = True

"""while gambling:
    print("dollar bill yo")

    if input() == "stop":
        break"""

while True:
    print("mata in nummer")

    number_1 = input()

    try:
        number_1 = int(number_1)
        break
    except:
        print("Försök igen")


