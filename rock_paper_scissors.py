import random

def get_choices():
  player_choice = input("Enter a Choice, rock, paper, or scissors : ")
  computer_options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(computer_options)
  choices = {"player": player_choice, "computer": computer_choice}

  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  
  if player == computer:
    print("its a tie")
    
  elif player == "rock":
    if computer == "scissors":
      print("player win")
    else:
      print("player lose")

  elif player == "scissors":
    if computer == "paper":
      print("player win")
    else:
      print("player lose")

  elif player == "paper":
    if computer == "rock":
      print("player win")
    else:
      print("player lose")

choices = get_choices()
result = check_win(choices["player"], choices["computer"])