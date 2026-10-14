menu = {
    "Burger" : "$15",
    "Taco" : "$10",
    "Soda" : "$2"
}

for each_item in menu:
    print(each_item)

item = input("What do you want to eat?")
if (menu.get(item)):
    print(menu.get(item))

else:
    print("This item is not on the menu")
