import random
Rock='''

    _ _ _ _ _ _ _ 
---'       _ _ __)
        (_ _ _ _ _)
        (_ _ _ _ _)
        (_ _ _ _ )
----._ _(_ _ _ _)

'''
paper='''

    _ _ _ _ _ _
---'     _ _ _ )_ _ _      
               _ _ _ _) _
               _ _ _ _ _ )
            _ _ _ _ _ _)
---._ _ _ _ _ _ _ _ _)

'''
scissors='''


    _ _ _ _ _ _
---'     _ _ _ )_ _ _
            _ _ _ _ _ )
            _ _ _ _ _ _)
          (_ _ _ _ )
---._ _ _ (_ _ _ _)


'''

game_images=[Rock,paper,scissors]
print("0:Rock")
print("1:Paper")
print("2:scissors")
user_choice=int(input("Enter You Choice:"))
if user_choice>=3:
    print("You Enter a Wrong Number!",user_choice,"You Lose.")
else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print("The computer_choice is:",computer_choice)
    print(game_images[computer_choice])
    if user_choice==0  and computer_choice==2:
        print("You Win.")
    elif user_choice==2 and computer_choice==0:
        print("You Lost.")
    elif user_choice<computer_choice:
        print("You Lose.")
    elif user_choice>computer_choice:
        print("You Win.")
    elif user_choice==computer_choice:
        print("IT's a Tie.")
