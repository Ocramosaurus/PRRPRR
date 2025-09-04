print("hej, hur gammal är du?")

age = input()
age = int(age)

if age < 7:
    print("det kostar 85 kr.")
elif age > 6 and age < 20:
    print("det kostar 100 kr.")
elif age > 19 and age < 65:
    print("det kostar 130 kr.")
elif age >= 65:
    print("det kostar 85 kr.")



while True:

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