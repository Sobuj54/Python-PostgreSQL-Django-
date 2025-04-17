class Admin:
    def __init__(self, name: str):
        self.name = name

    def add_customer(self, restaurant:object, customer: object):
        restaurant.customers.append(customer)
        print("new customer added.")
    
    def remove_customer(self, restaurant: object, customer_name: str):
        restaurant.remove_customer(customer_name)

    def add_item(self, restaurant:object, item: object):
        restaurant.add_item(item)
        print("item added successfully")
    
    def remove_item(self, restaurant: object, item_name: str):
        restaurant.remove_item(item_name)

    def show_items(self, restaurant: object):
        restaurant.show_menu()

    def show_customers(self, restaurant: object):
        restaurant.customer_details()

    def update_item_price(self, restaurant: object,item_name:str, new_price: int):
        restaurant.update_item_price(item_name,new_price)




