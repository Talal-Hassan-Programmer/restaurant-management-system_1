# all funcs for this projects 
#for main file

menu = {
    "pizza":20,
    "burgerr":50,
    "pasta":25
}


#adding a order 
def add_to_order():
    nm = int(input("ORDER NUMBER"))
    m_k = menu.keys()
    order = input("Order Pls {m_k}").lower()
    if order in menu:
        if nm:
            with open(f"{nm}].txt","a") as f:
                f.write(f"{order}{price}.\n")
        else:
            print("No order with that number.")
    else:
        print("This is not avalibal in our restaurant")

#removing a order
def remove_order():
    pass

#creating a order file
def create_order_file():
    nm = int(input("Please enter the order number: "))
    with open(f"{nm}.txt", "w") as f:
        f.write(f"This order file is for {nm}.\n")

