import csv

class Item:

    pay = 0.9
    all = []

    def __init__(self,name:str,price :int ,quantity = 0 ):
        # Run validation to the recived argument
        assert price >= 0 , f"The value of {price} is less than zero!"
        assert quantity >= 0 , f"The value of quantity {quantity} is less than Zero!"

        # Assign self object
        self.__name =name
        self.price = price
        self.quantity = quantity
        
        # Append data of each instance in a single array
        Item.all.append(self)

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

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
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"