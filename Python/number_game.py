import random

def rules():
   print("        ---------------Rules---------------\n")
   print("1. Guess the sum of two dice rolled at a same time. \n2. Choose btw 2 to 12. \n3. Ever correct time you get 2X point whereas, you lose for wrong answer. ")

random_number1 =random.randrange(1,7)
random_number2 = random.randrange(1,7)
sum = random_number1 +random_number2
win = 0
def asds(p):
   if p != "n" and p != "N":
     rules()
     amount = int(input("Enter the amount to play with: "))
     bet = int(input("Enter the bet amount: "))
     answer = input("Choose the number btw (2 , 12): ")
     asd(amount, bet , answer)
   else :
     print(f"Thank you for playing {win}")
     quit()

def asd(a,b,c):
   if c ==sum:
      win == a + b*2
      print(win)
   else :
     print(sum)
     print("try again")
          

print("\n\n          Welcome to the game of luck :)\n\n")
play = input("Do you want to play: ")
asds(play)

   



