from datetime import date
today = date.today()

birthYear = int(input("Your BirthYear? "))
age = today.year - birthYear

if age >= 15 and age < 20:
    print("teenager")

print("Your age : %d" %age)

# teenager in korea : 15 ~ 20 -> use if~else
# print("teenager")
