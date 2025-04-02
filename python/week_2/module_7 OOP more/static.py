"""
    Python provides three types of attributes and methods at the class level:

    1. Static Attribute (Shared class variable)
    2. Static Method (Independent method inside a class)
    3. Class Method (Method that works on the class, not instances)
"""

class Shopping:
    cart = []  # static attribute
    """
         Static Attribute (Class Variable):

        1. Belongs to the class, not individual instances.
        2. Shared among all instances of the class.
        3. Defined outside the constructor (__init__).
    """

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def purchase(self, item, price, amount):
        self.cart.append(item)
        print(f"buying: {item} for price: {price} and remaining: {amount - price} {self.cart}")

    # static method
    """
        Static Method (@staticmethod):

        1. Belongs to the class, not instances.
        2. Cannot access instance (self) or class (cls) attributes.
        3. Used for utility/helper functions inside the class.
    """
    @staticmethod
    def add(a,b):
        print("sum ", a+b)

    # class methods can be called without an object
    """
        Class Method (@classmethod):

        1. Works on class level instead of instance level.
        2. Uses cls (class reference) instead of self (instance reference).
        3. Can modify class attributes but not instance attributes.
    """
    @classmethod
    def hudai_dekhi(cls):
        cls.cart.append("boi")
        print(f"kinum na tao dekhi {cls.cart}")

jomuna = Shopping("jomuna", "dhaka")
jomuna.purchase("shirt",500,1000)

Shopping.hudai_dekhi()
Shopping.add(2,3)