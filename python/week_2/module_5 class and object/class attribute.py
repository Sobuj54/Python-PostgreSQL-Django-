class Shop:
    # here cart is a class attribute
    # class attribute can be accessed by all the objects
    cart = []

    def __init__ (self, name):
        # here name is is instance attribute
        # instance attribute can only be accessed by specific objects
        self.name = name

    def addToCart(self, item):
        self.cart.append(item)

ali = Shop("ali baba")
ali.addToCart("Phone")
ali.addToCart("watch")
print(ali.cart)

gali = Shop("galli boy")
gali.addToCart("tupi")
gali.addToCart("kupi")
print(gali.cart)