class Shop:
    shopping_mall = "jamuna park"

    def __init__ (self, name):
        self.name = name
        # here cart is is instance attribute
        # instance attribute can only be accessed by specific objects
        self.cart = []

    def addToCart(self, item):
        self.cart.append(item)

ali = Shop("ali baba")
ali.addToCart("Phone")
ali.addToCart("watch")
print(f"{ali.name} cart items: ",ali.cart)

gali = Shop("galli boy")
gali.addToCart("tupi")
gali.addToCart("kupi")
print(f"{gali.name} cart items: ",gali.cart)