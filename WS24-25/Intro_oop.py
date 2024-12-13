class Table:

    def __init__(self, number:int, capacity:int):
        self.number = number
        self.capacity = capacity
        self.tab = []

    def calculate_total(self):
        """something"""
        total = 0
        for p in self.tab:
            total += p
        tip = total*.2
        return total + tip
    
    def add_price(self, price:float):
        self.tab.append(price)

class VIPTable(Table):

    def __init__(self, number, capacity, extra):
        super().__init__(number, capacity)
        self.extra = extra

    def calculate_total(self):
        total = 0
        for p in self.tab:
            total += p
        return total * self.extra
    
class ITable:

    def __init__(self, number):
        self.number = number

    def calculate_price():
        raise NotImplementedError
    
    def add_product(product):
        raise NotImplementedError

class SmallTable(ITable):
    
    def __init__(self, number):
        super().__init__()
        self.number = number

table1 = Table(1,1)
table2 = Table(4,1)
vip = VIPTable(1,1,1.5)

table1.add_price(20)
table1.add_price(19)

table2.add_price(5)
vip.add_price(5)

print(table1.calculate_total())

print(table2.calculate_total())

print(vip.calculate_total())