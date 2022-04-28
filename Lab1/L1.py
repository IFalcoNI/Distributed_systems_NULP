import datetime


def factorial(n):
    fact = 1
    for i in range(1, n+1, 1):
        fact = fact * i
    return fact


print("HELLo World!")
name = input("Please, enter your name: ")
print("Hello, " + name + "!")
nameLength = len(name)
print("Your name has " + str(nameLength) + " letters.")
print(str(nameLength) + "! = " + str(factorial(nameLength)))

day, month, year = input(
    "Please, enter your birth date in format (DD.MM.YYYY): ").split('.')
today = datetime.datetime.today()
birthday = datetime.datetime(year=int(year), month=int(month), day=int(day))
diff = today - birthday
diffYear = int(diff.days/365)
print("Today is " + today.strftime("%d.%m.%Y"))
print("You are " + str(diffYear) + " year (" + str(diff.days) + " days) old.")
