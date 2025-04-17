from restaurant import Restaurant, Item
from admin import Admin
from customer import Customer

mamar_restaurant = Restaurant("mamar restaurant")

def create_item() -> object:
    name = input("enter item name: ")
    price = int(input("enter item price: "))
    item = Item(name, price)
    return item

def create_customer() -> object:
    name = input("enter customer name: ")
    email = input("enter customer email: ")
    address = input("enter customer address: ")
    customer = Customer(name, email, address)
    return customer

def handle_admin():
    name = input("enter admin name: ")
    admin = Admin(name)
    print(f"welcome admin {name}")
    while True:
        print("\n-------admin panel----------")
        print("1. Create customer account\n2. Remove customer account\n3. View all customers\n4. Manage restaurant Menu\n5. exit")
        choice = int(input("enter your choice: "))
         
        if choice == 1:
            customer = create_customer()
            admin.add_customer(mamar_restaurant, customer)
        elif choice == 2:
            name = input("enter customer name: ")
            admin.remove_customer(mamar_restaurant,name)
        elif choice == 3:
            admin.show_customers(mamar_restaurant)
        elif choice == 4:
            while True:
                print("\n--------admin manage restaurant menu------------")
                print("1. Add item\n2. Remove item\n3. View menu\n4. Update item price\n5. exit")
                n = int(input("enter your choice: "))
                if n == 1:
                    item = create_item()
                    admin.add_item(mamar_restaurant,item)
                elif n == 2:
                    item_name = input("enter item name: ")
                    admin.remove_item(mamar_restaurant, item_name)
                elif n == 3:
                    admin.show_items(mamar_restaurant)
                elif n == 4:
                    item_name = input("enter the item name: ")
                    new_price = int(input("enter new price: "))
                    admin.update_item_price(mamar_restaurant, item_name, new_price)
                else:
                    break
        else:
            print("exit")
            break

def handle_customer():
    name = input("enter customer name: ")
    customer = mamar_restaurant.find_customer(name)
    if not customer:
        print("customer doesn't exist.")
        return
    
    print(f"---------Welcome {name}-----------")
    while True:
        print("\n------------customer panel--------------")
        print("1. View Restaurant menu\n2. View balance\n3. Add Balance\n4. Place order\n5. View past orders\n6. Exit")
        choice = int(input("enter your choice: "))

        if choice == 1:
            customer.show_menu(mamar_restaurant)
        elif choice == 2:
            customer.check_balance()
        elif choice == 3:
            added = int(input("enter balance to add: "))
            customer.add_fund_to_balance(added)
        elif choice == 4:
            item_name = input("enter item name: ")
            customer.place_order(mamar_restaurant, item_name)
        elif choice == 5:
            customer.show_orders()
        else:
            print("exit")
            break

while True:
    print("\n-----------welcome to mamar restaurant----------")
    print("1. Admin login\n2. Customer login\n3. Exit")
    choice = int(input("enter your choice: "))

    if choice == 1:
        handle_admin()
    elif choice == 2:
        handle_customer()
    else:
        print("exit")
        break
