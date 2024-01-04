import random

def game_win(computer,player):

  if((computer.lower() == "s") and (player.lower() == "w")):
    print("Computer wins")
  elif((computer.lower() == "w") and (player.lower() == "s")):
    print("Player wins")
  elif((computer.lower() == "w") and (player.lower() == "g")):
    print("Computer wins")
  elif((computer.lower() == "g") and (player.lower() == "w")):
    print("player wins")
  elif((computer.lower() == "g") and (player.lower() == "s")):
    print("computer wins")
  elif((computer.lower() == "s") and (player.lower() == "g")):
    print("Player wins")
  else:
    print("Invalid Entry")


num = random.randint(0,2)
if(num == 0):
  comp_entry = "s"
elif(num == 1):
  comp_entry = "w"
else:
  comp_entry = "g"

print("Computer Entry",comp_entry)
player_entry = input("Enter snake(s) , water(w) and gun(g) :")
game_win(comp_entry,player_entry)
