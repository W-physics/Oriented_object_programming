class Item():
    #Esta función nos servirá para darle atributos a los objetos de forma más efectiva
    def __init__(self,name,price,quantity):
        self.name = name #atributo "nombre" creado
        self.price = price
        self.quantity = quantity
        print(f"Un objeto ha sido creado: {name}") #Método format útil para reemplazar nombres de variables en texto
    
item_1 = Item("phone",500,5)
item_2 = Item("computer",1000,7)

print(item_1.__dict__) #Otorga todos los atributos del item como un diccionario

