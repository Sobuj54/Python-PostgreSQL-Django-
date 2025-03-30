class Phone:
    manufactured = "china"

    # constructor
    def __init__ (self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price
    
new_phone = Phone("sobuj", "samsung", 10000)

print(new_phone.owner, new_phone.brand, new_phone.price)