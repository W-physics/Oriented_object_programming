class Item: 
    #Métodos
    def calculate_total_price(self,item_price,item_quantity):#El método siempre va a tomar como primer argumento al objeto en sí
        return item_price*item_quantity

item1 = Item() # item 1 va a pertenecer a la clase de item
item2 = Item()

# Atributos

item1.name = "phone"
item1.price = 500
item1.quantity = 5
x = item1.calculate_total_price(item1.price,item1.quantity)

item2.name = "computer"
item2.name = 1000
item2.quantity = 20



print(x) #<class> "__main__Item"

# Cambiamos el tipo de dato que es Item1