from menu import Menu
from item import Item
from orders import Order
from restaurants import Restaurant
from users import Customer, Employee, Admin

haji_biriyani = Restaurant("haji biriyani")

def customer_menu():
    name = input("enter your name: ")
    email = input("enter your email: ")
    phone = input("enter your phone: ")
    address = input("enter your address: ")
    customer = Customer(name=name, phone=phone, email=email,address=address)

    while True:
        print(f"welcome {name}")
        print("1. View menu\n2. add item to cart\n3. view cart\n4. pay bill\n5. exit")

        choice = int(input("enter your choice: "))
        if choice == 1:
            customer.view_menu(haji_biriyani)
        elif choice == 2:
            item_name = input("enter item name: ")
            quantity = int(input("enter quantity: "))
            customer.add_to_cart(haji_biriyani,item_name,quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        else:
            break

def admin_menu():
    name = input("enter your name: ")
    email = input("enter your email: ")
    phone = input("enter your phone: ")
    address = input("enter your address: ")
    admin = Admin(name=name, phone=phone, email=email,address=address)

    while True:
        print(f"welcome {name}")
        print("1. Add new Item\n2. add new employee\n3. view employees\n4. view items\n5. delete item\n6. exit")

        choice = int(input("enter your choice: "))
        if choice == 1:
            item_name = input("enter item name: ")
            price = int(input("enter price: "))
            quantity = int(input("enter quantity: "))
            item = Item(item_name, price, quantity)
            admin.add_new_item(haji_biriyani,item)
        elif choice == 2:
            name = input("enter employee name: ")
            phone = input("enter phone number: ")
            email = input("enter email: ")
            address = input("enter address: ")
            age = input("enter age: ")
            designation = input("enter designation: ")
            salary = input("enter salary: ")
            employee = Employee(name,phone,email,address,age,designation,salary)
            admin.add_employee(haji_biriyani,employee)
        elif choice == 3:
            admin.view_employee(haji_biriyani)
        elif choice == 4:
            admin.view_menu()
        elif choice == 5:
            item_name = input("enter item name: ")
            admin.remove_item(haji_biriyani, item_name)
        else:
            break

while True:
    print("welcome")
    print("1. Admin\n2. Customer\n3. exit")
    choice = int(input("enter your choice: "))

    if choice == 1:
        admin_menu()
    elif choice == 2:
        customer_menu()
    else:
        break

