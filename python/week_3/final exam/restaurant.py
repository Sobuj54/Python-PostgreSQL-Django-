class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []
        self.customers = []

    def show_menu(self):
        print("item\tprice")
        for food in self.menu:
            print(f"{food.item_name}\t{food.price}")

    def find_item(self, item_name: str):
        for item in self.menu:
            if item.item_name.lower() == item_name.lower():
                return item
        return None

    def add_item(self, item: object):
        self.menu.append(item)

    def remove_item(self, item_name:str):
        item = self.find_item(item_name)
        if item:
            self.menu.remove(item)
        else:
            print("No item found.")

    def customer_details(self):
        print("All customers:")
        print("name\temail\taddress")
        for customer in self.customers:
            print(f"{customer.name}\t{customer.email}\t{customer.address}")

    def find_customer(self, name: str):
        for customer in self.customers:
            if customer.name.lower() == name.lower():
                return customer
        return None

    def remove_customer(self, customer_name: str):
        customer = self.find_customer(customer_name)
        if customer:
            self.customers.remove(customer)
            print(f"{customer_name} removed successfully.")
        else:
            print("No customer found with this name")

    def update_item_price(self, item_name:str, new_price: int):
        item = self.find_item(item_name)
        if item: 
            item.price = new_price
            print(f"{item_name} price is updated successfully.")
        else:
            print("no matching item found")

class Item:
    def __init__(self, item_name: str, price: int):
        self.item_name = item_name
        self.price = price