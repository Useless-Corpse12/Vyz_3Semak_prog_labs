class Product:
    _id_counter = 0

    def __init__(self):
        Product._id_counter += 1
        self.id = Product._id_counter

class SavingsAccount(Product):
    def operate(self):
        return f'{self.id}-й накапливает'

class CreditAccount(Product):
    def operate(self):
        return f'{self.id}-й кредитует'

class Deposit(SavingsAccount):
    pass

class Loan(CreditAccount):
    pass

#старт
items = [SavingsAccount(),CreditAccount(), Deposit(), Loan()]
for item in items:
    print(item.operate())