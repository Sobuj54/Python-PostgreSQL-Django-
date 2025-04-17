class Customer:
    def __init__(self, name:str, email: str, address: str):
        self.name = name
        self.email = email
        self.address = address
        self.order = []
        self.available_balance = 0

    def show_menu(self, restaurant: object):
        restaurant.show_menu()

    def place_order(self, restaurant: object, item_name:str):
        item = restaurant.find_item(item_name)
        if item:
            if item.price > self.available_balance:
                print("not enough balance")
            else:
                self.order.append(item)
                self.available_balance -= item.price
                print(f"{item_name} ordered successfully.")
        else:
            print("no item found")

    def show_orders(self):
        print("previous orders:")
        print("name\tprice")
        for item in self.order:
            print(f"{item.item_name}\t{item.price}")

    def check_balance(self):
        print(f"{self.name}'s current balance is {self.available_balance}")

    def add_fund_to_balance(self, amount:int):
        self.available_balance += amount
        print(f"{amount} taka added successfully.")


