class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount
        self.last_transaction = 0
        
    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for i in range(quantity):
            self.items.append(title)
        self.last_transaction = price * quantity

    def add_item_optional_quantity(self, title, price, quantity=1):
        self.add_item(title, price, quantity)
   
    def apply_discount(self):
        if self.discount > 0:
            self.total -= self.total * (self.discount / 100)
            print("After the discount, the total comes to ${:.0f}.".format(self.total))
        else:
            print("There is no discount to apply.")
            
    def void_last_transaction(self):
        if self.last_transaction > 0:
            self.total -= self.last_transaction
            self.last_transaction = 0
            
