import random
print("lets play rock, paper scissor!")
choice_list = [0,1,2]
choice = int(input("what do you choose? type 0 for rock, 1 for paper, 2 for scissor : "))
if choice == 0:
    print( '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif choice == 1:
    print( '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif choice == 2:
    print( '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
else:
    print("invalid input")
print("computer choose")
computer_choice = random.choice(choice_list)
if computer_choice == 0:
    print( '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    if choice == 0:
        print("its a tie")
    elif choice == 1:
        print("you win")
    else:
        print("computer wins")
elif computer_choice == 1:
    print( '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
    if choice == 0:
        print("computer wins")
    elif choice == 1:
        print("its a tie")
    else:
        print("you win")
else:
    print( '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    if choice == 0:
        print("you win")
    elif choice == 1:
        print("computer wins")
    else:
        print("computer wins")
    
    
