import random as rn 

while True:

    opt = input("1)To bet on color\n2)To bet on Even or odd number\n3)To bet on >10 , <10 , =10\n\nEnter your choice =").strip()
    print()

    if(opt == ""):
        print("Please enter your choice")
        break


    elif (int(opt) == 1):
        collor = ['red' , 'black']
        luck = rn.choice(collor)
    
        selcol = input("\nChoose a color (Red/Black) to put money on =").lower().strip()

        if(selcol not in collor ):
            print("\nPlease choose valid color")
            break
        elif(selcol == ""):
            print("Please enter color")
            break

        amt = int(input("Enter amount to bet = "))
        if(selcol == luck):
            print(f"\nYou won {2*amt}\n")
   
        else:
            print("\nyou lose!!\n")

        
    
    elif (int(opt) == 2):
        nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        luck = rn.choice(nums)
        choice = input("1)To bet on even\n2)To bet on odd\nEnter your choice =")
        amt = int(input("\nEnter amount to bet = "))

        if(luck %2 == 0 and int(choice) == 1):
            print(f"\nYou won {1.5*amt}")
        elif(luck %2 !=0 and int(choice) == 2):
            print(f"\nyou won {1.5*amt}")
        else:
            print("\nYou lose!!")

    elif(int(opt) == 3):
        nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        luck = rn.choice(nums)
        choice = input("1)To place your bet on less than 10\n2)To place bet on greater than 10\n3)To place bet on equal to 10\nEnter your choice = ")
        
        amt = int(input("\nEnter amount to bet = "))
        print()
        
        if(int(choice) == 1 and luck < 10):
            print(f"\nYou won {1.5*amt}")

        elif(int(choice) == 2 and luck > 10):
            print(f"\nYou won {1.5*amt}")

        elif(int(choice) == 3 and luck == 10):
            print(f"\nYou won {5*amt}")
        else:
            print("\nYou lose!!")


    else:
        print("\nPlease enter valid choice")
        break


    more = input("\nDo you want to bet more (y/n) = ").lower().strip()
    print()

    if more == 'y':
        continue
    elif more == 'n':
        print("Thank you\n")
        break
    else:
        print("Invalid choice")
        break

        
