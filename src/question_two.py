# adult = int(input("Enter the number of Adults: \n"))
# children = int(input("Enter the number of Children: \n"))
# day = input("Enter the Day: \n")
#
# bill = (12 * adult) + (8 * children)
# if day == "Wednesday":
#     bill = bill - 2 * (adult + children)
#
# print(bill)

age = 20
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2

print(price)