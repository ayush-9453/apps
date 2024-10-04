import random

user_wins =0
computer_win =0

opt = ["rock","paper","scissors"]
while True:
    user_input = input("Type Rock/Paper/scissors or quit: ").lower()
    if user_input == "q":
        break

    if user_input not in opt:
        continue
    
    random_number = random.randint(0,2)
    pick = opt[random_number]
    print("computer Picked ", pick + ".")
    
    if user_input =="rock" and pick == "scissors":
      print("You won!")
      user_wins +=1
    
    elif user_input =="scissors" and pick == "paper":
      print("You won!")
      user_wins +=1
  
    elif user_input =="paper" and pick == "rock":
      print("You won!")
      user_wins +=1
    
    else :
       print("You lost")
       computer_win +=1
    
print(f"Your wins {user_wins}")
print(f"Computer wins {computer_win}")
print("Goodbye")