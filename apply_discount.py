#Crear y llamar un método que tome un item y le aplique descuento de 20% a su precio

class Item():
    def __init__(self,name, price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_discount(self,price): #La funcion también toma a self
        return self.price * 0.8

item1 = Item("phone",200,5)

print(item1.calculate_discount(item1.price))
