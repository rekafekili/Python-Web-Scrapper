age = int(input("How old are you? "))

print("user answer :", age)
print("user input type :", type(age))

if age < 18:
    print("You can't drink.") 
elif age >= 18 and age <= 35:
    print("You drink beer!")
elif age == 60 or age == 70:
    print("Birthday party!")
else:
    print("Go ahead!")