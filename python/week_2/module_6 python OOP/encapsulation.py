"""
    Encapsulation: Hide details

    Access modifiers: Public, Private, Protected
"""

class Bank:
    def __init__(self, name, initial_balance):
        self.name = name
        self._pro = False
        self.__balance = initial_balance
        """
            public:
                name is public attribute.It can be accessed and modified from outside.
            
            private:
                __balance is a private attribute.It can not be accessed or modified from outside the class. __ makes an attribute private
            
            protected:
                _pro is protected attribute.Although it's actually not protected.Its just used as convention in python.Many languages support protected attribute but python doesn't. _ (single underscore) is used to show protected.
        """
    
    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

rafsan = Bank("rafa", 10000)
print(rafsan.name)
rafsan.deposit(500)
print(rafsan.get_balance())
print("protected: ",rafsan._pro)
        