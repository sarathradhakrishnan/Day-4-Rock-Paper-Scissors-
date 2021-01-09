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
random_num =random.randint(1,3)
if random_num==1:
    comp =rock
elif random_num==2:
    comp =paper
else:
    comp =scissors


inp =input("Rock,Paper or Scissors??\n")
if inp=="Rock":
    print(rock)
    print(comp)
    if comp ==rock:
        print("Its a Tie")
    elif comp ==paper:
        print("You Lose")
    elif comp ==scissors:
        print("You Win")
    else:
        print("Invalid Input")            
    
elif inp=="Paper":
    print(paper)
    print(comp)
    if comp ==rock:
        print("You Win")
    elif comp ==paper:
        print("Its a Tie")
    elif comp ==scissors:
        print("You lose")    
    else:
        print("Invalid Input")
elif inp=="Scissors":
    print(scissors)
    print(comp)
    if comp ==rock:
        print("You Lose")
    elif comp ==paper:
        print("You Win")
    elif comp==scissors:
        print("Its a Tie")    
    else:
        print("Invalid Input")
else:
     print("Invalid Input")       



       
    

