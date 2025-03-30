class Phone:
    brand = "samsung"
    price = 90000

    # all class methods must have a self parameter
    def show(self):
        print("just print")

    def discount(self, dis):
        return dis
    
new_phone = Phone()

new_phone.show()

new_price = new_phone.discount(1000)
print(new_price)