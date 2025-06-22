inventory = {}
while True:
    item = input("Enter the item name: ")
    quantity = input("Enter the item quantity: ")
    inventory[item] = quantity

    if quantity == "":
        print("0")
        break
    print(inventory)
    break    
                          
    