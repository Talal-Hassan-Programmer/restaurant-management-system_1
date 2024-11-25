#Main program
#impprting files from the same devide / folder
import func as f


print("WELCOME TO -----")

while True:
    x = input("New Order, Add to order, remove order (completly)")
    if x == "new order":
        f.create_order_file()
        f.add_to_order()
    elif x == "add to order":
        f.add_to_order()
    elif x == "remove order":
        f.remove_order()
    else:
        pass