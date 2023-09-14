num = int(input('Enter the number you want to match :'))
match num:
    case 0:
        print("number you entered is zero")
    case 2:
        print("number you entered is two")
    case 4:
        print("number you entered is four")
    case 8:
         print(num)
         # default case with if statment
    case _ if num==6:
        print(num)
    case _ if num==10:
          print("number you entered is ten")
          # default case
    case _:
        print(num)