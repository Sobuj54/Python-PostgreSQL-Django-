class Shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, quantity, price):
        product = {
            "item": item.lower(),
            "quantity": quantity,
            "price" :price
        }
        self.cart.append(product)

    def remove_from_cart(self, item):
        idx = -1
        for i,product in enumerate(self.cart):
            if product["item"] == item.lower():
                idx = i

        if idx != -1:
            popped = self.cart.pop(idx)
            return f"removed item: {popped} \nnew cart: {self.cart}"
        else:
            return "no matching item found"

    def checkout(self):
        total = 0
        for product in self.cart:
            total += product["quantity"] * product["price"]
        return total


alan = Shopping("alan")
alan.add_to_cart("alu",3, 50)
alan.add_to_cart("chal",5, 70)
alan.add_to_cart("chini",1, 120)

print("alan's total spending: ", alan.checkout())
print(alan.remove_from_cart("Chal"))
print("alan's total spending: ", alan.checkout())