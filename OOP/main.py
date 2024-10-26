""" NOTES:
1. Here init is a default constructor used in python programing that always run when ever
 an instance of class is created init function is run and assigned the value.
2. self command is used to call the class iteself as the python program pass class itself first.
3. Default value of the variable can be set. for example ( quantity = 0 ).
4. Strict data type uses can also be set to the variable so that no other 
data type can be assigned to the variable. for example ( name: str ).
5. Asset keyword is used to validated a given argument. Used as debuging in python that give output in boolean
  if true on error msg if false Assetionerror is shown. We can also add an assertion msg to the terminal using 
  f string in python.
6.class Attribute are defined within classes but outside of methods unlike instance attribute it is same for 
 each instances access and modification can be done using ( Item.pay ).
7. __dict__ command is used to show all the attribute used in a class 
"""

import csv

class Item:

    pay = 0.9
    all = []

    def __init__(self,name:str,price :int ,quantity = 0 ):
        # Run validation to the recived argument
        assert price >= 0 , f"The value of {price} is less than zero!"
        assert quantity >= 0 , f"The value of quantity {quantity} is less than Zero!"

        # Assign self object
        self.name =name
        self.price = price
        self.quantity = quantity
        
        # Append data of each instance in a single array
        Item.all.append(self)

    def calculate_total(self):
        return self.price* self.quantity
    
    def apply_discount(self):
        self.price = self.price* self.pay
    
    @classmethod
    def initantiate(cls):
        with open('item.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),

            )
    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False


    def __repr__(self) -> str:
        return f"Item('{self.name}',{self.price},{self.quantity})"
    
# print(item1.calculate_total())
# print(Item.__dict__) # All the attribute on Class level
# print(item1.__dict__) # All the attribute at instance levelṇ
# print(Item.pay)

# item1.apply_discount()
# print(item1.price)
# item2 = Item('airpod',100,1)
# item2.pay = 0.5
# print(item2.price)
   
Item.instantiate()

print(Item.all)