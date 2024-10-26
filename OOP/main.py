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



from item import Item

item1 = Item("MyItem", 750)

# Setting an Attribute
item1.name = "OtherItem"

# Getting an Attribute
print(item1.name)