cart = []

while True:
    print("[1] Add Items | [2] Remove Items | [0] Exit")
    answer = int(input("Do you want to add or remove item in your cart? "))

    if answer == 1:
        item = str(input("Add item to cart: ")).lower()
        cart.append(item)
        print("Current Cart List: ", cart)
    elif answer == 2:
        if len(cart) == 0:
            print("Shopping cart is empty!")
            break

            item = str(input("Remove item to cart: ")).lower()
            cart.remove(item)
            print("Current Cart List: ", cart)
    else:
        print("Done editing cart!")
        break