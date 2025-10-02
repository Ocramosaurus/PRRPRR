print("hej, hur gammal är du?")

age = input()
age = int(age)

if age < 5:
    print("Vart är dina föräldrar pojk.")
elif age > 4 and age < 8:
    print("det kostar 100 kr.")
elif age > 7 and age < 65:
    print("det kostar 130 kr.")
elif age >= 65:
    print("det kostar 85 kr.")



while True and age < 20 and age > 5:

    print("Är du student?")

    student = input()
    student = str(student)

    if student == "Ja":
        print("Då kostar det bara 60 kr. Ha en bra resa..")
        break
    elif student == "Nej":
        print("Aha okej. Ha en bra resa..")
        break
    elif student != "Nej" or student != "Ja":
        print("Jag förstår inte..")
    