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

#Write your code below this line 👇
import random
game_images = [rock , paper , scissors]
opponent_choice = int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
if opponent_choice >= 3 or opponent_choice <0:
  print(" Invalid number , LOSER!")
else:
  print(game_images [opponent_choice])
  
  computer_choice = random.randint(0,2)
  print("Computer chose:")
  print(game_images[computer_choice])
  
  if opponent_choice == 0 and computer_choice == 2:
    print("you win!")
  elif computer_choice == 0 and opponent_choice == 2:
    print("loser!")
  elif opponent_choice > computer_choice:
    print('you win!')
  elif computer_choice > opponent_choice:
    print("loser!")
  elif computer_choice == opponent_choice:
    print("draw")


