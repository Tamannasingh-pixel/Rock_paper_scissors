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

print("welcome to rock paper and scissors.")

game = ["rock","paper", "scisssor"]

computer = random.choice(game)

your_input = int(input("enter your choice here (0 for rock) (1 for paper) (2 for scissors): "))
your_choice = game[your_input]

if computer == game[0] and your_choice == game[1]:
    print(f"computer chose {computer}")
    print(rock)
    print(f"you chose {your_choice}")
    print(paper)
    print("you win!")

elif computer == game[0] and your_choice == game[2]:
    print(f"computer chose {computer}")
    print(rock)
    print(f"you chose {your_choice}")
    print(scissors)
    print("you lose!")

elif computer == game[1] and your_choice == game[0]:
    print(f"computer chose {computer}")
    print(paper)
    print(f"you chose {your_choice}")
    print(rock)
    print("you lose!")

elif computer == game[1] and your_choice == game[2]:
    print(f"computer chose {computer}")
    print(paper)
    print(f"you chose {your_choice}")
    print(scissors)
    print("you win!")

elif computer == game[2] and your_choice == game[0]:
    print(f"computer chose {computer}")
    print(scissors)
    print(f"you chose {your_choice}")
    print(rock)
    print("you win!")

elif computer == game[2] and your_choice == game[1]:
    print(f"computer chose {computer}")
    print(scissors)
    print(f"you chose {your_choice}")
    print(paper)
    print("you lose!")

elif computer == your_choice:
    print("it is a draw")

else:
    print("ivalid response!")


