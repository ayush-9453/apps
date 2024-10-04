a = input("Enter the number: ")
print(f"Multiplication tabel of {a} is: ")

try:
  for i in range(1, 11):
      print(f"{int(a)} X {i} = {int(a)*i}")
except :
   print("Invalid Input")
finally:
   print("always executed")