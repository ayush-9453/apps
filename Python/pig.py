import random

def roll():
    min_value = 1 
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while(True):
    players = input("Enter the number of players (2-4):")
    if players.isdigit():
        players=int(players)
        if 1<=players <=4:
            print("Must be between 1-4 players.")
            break
    else:
        print("Invalid, try again.")

max_score=50 
player_score = [ 0 for _ in range(players)]

while max(player_score)< max_score:
    for player_idk in range(players):
       print("\nPlayer", player_idk+1 ,"turn has just started!\n")
       print("your total score is :", player_score[player_idk],"\n")
       current_score = 0

    while True:
        should_roll = input("would you like to roll (y)?")
        if should_roll.lower() !="y":
         break
        value = roll()
        if value ==1:
          print("You rolled 1! Trun done!")
          current_score=0
          break
        else:
           current_score += value
           print("You rolled a:" ,value)
        print("Your score is:", current_score)

    player_score[player_idk] += current_score
    print("Your total score is :",player_score[player_idk])