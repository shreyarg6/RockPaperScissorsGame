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

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
comp_choice = random.randint(0,2)

if user_choice == 0 and comp_choice == 0:
    print("You chose: "+ rock)
    print("Computer chose: " +rock)
    print("You tied")
elif user_choice == 0 and comp_choice == 1:
    print("You chose: "+ rock)
    print("Computer chose: " +paper)
    print("Computer")
elif user_choice == 0 and comp_choice == 2:
    print("You chose: "+ rock)
    print("Computer chose: " +scissors)
    print("You won")
elif user_choice == 1 and comp_choice == 0:
    print("You chose: "+ paper)
    print("Computer chose: " +rock)
    print("You won")
elif user_choice == 1 and comp_choice == 1:
    print("You chose: "+ paper)
    print("Computer chose: " +paper)
    print("You tied")
elif user_choice == 1 and comp_choice == 2:
    print("You chose: "+ paper)
    print("Computer chose: " +scissors)
    print("computer won")
elif user_choice == 2 and comp_choice == 0:
    print("You chose: "+ scissors)
    print("Computer chose: " +rock)
    print("Computer won")
elif user_choice == 2 and comp_choice == 1:
    print("You chose: "+ scissors)
    print("Computer chose: " +paper)
    print("You won")
else:
    print("You chose: "+ scissors)
    print("Computer chose: " +scissors)
    print("You tied")
