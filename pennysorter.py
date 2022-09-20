pennies = int(input("how many pennies do you have "))

dollars = pennies // 100
pennies = pennies % 100
quarters = pennies // 25
pennies = pennies % 25
dime = pennies // 10
pennies = pennies % 10
nickels = pennies // 5
pennies = pennies % 5

print("your change once counting pennies is")
print(("dollars ") + str(dollars))
print(("quarters ") + str(quarters))
print(("dimes ") + str(dime))
print(("nickels ") + str(nickels))
print(("pennies ") + str(pennies))