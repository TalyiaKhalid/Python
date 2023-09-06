#Rock Paper Scissors Game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
o = input("What do you choose? Type Rock,  Paper, or  Scissors.")

option = o.lower()

if option == "rock":
  print(rock)
elif option == "paper":
  print(paper)
elif option == "scissors":
  print(scissors)
else:
  print("Please choose something valid")

option_list = [rock,paper,scissors]

comp_rand = random.choice(option_list)
print("Computer chose:\n"+comp_rand)

if (option == "rock" and comp_rand == scissors) or (option == "scissors" and comp_rand == paper) or (option == "paper" and comp_rand == rock):
  print("YOU WINNNN ☺")
elif (option == "rock" and comp_rand == rock) or (option == "paper" and comp_rand == paper) or (option == "scissors" and comp_rand == scissors):
  print("TIE")
else:
  print("LOSER :þ")