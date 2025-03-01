# Rock
rock= ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper= ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors =("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_images=[rock,paper,scissors]
import random
User_Choice=int(input("Enter your choice: Type 0 for rock, 1 for paper, 2 for Scissors: "))
if User_Choice >=3 or User_Choice <0:
      print("You have entered an invalid number, you Lose")
else:
      print(game_images[User_Choice])
      computer_choice=random.randint(0,2)
      print("Computer Choice:",computer_choice)
      print(game_images[computer_choice])

if computer_choice == User_Choice:
      print("It's a draw..")
elif computer_choice == 0  and User_Choice == 2:
      print("You lose.. ")
elif User_Choice == 0 and computer_choice == 2:
      print("You win.. ")
elif computer_choice > User_Choice:
      print("You Lose..")
elif User_Choice > computer_choice:
     print("You Win...")


elif computer_choice == 0  and User_Choice == 2:
    print("You lose.. ")
elif User_Choice == 0 and computer_choice == 2:
    print("You win.. ")
