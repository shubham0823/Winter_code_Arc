import random
class SnakeWaterGun():
    list = [1,2,3]
    player = int(input(f"input any one (1:-snake , 2:-water, 3:-gun)\n"))
    
    computer_pick = random.choice(list)
    if computer_pick==1 :
        print ("computer pick 1:-snake \nresult")
    elif computer_pick==2 :
        print ("computer pick 2:-water \nresult")
    elif computer_pick==3 :
        print ("computer pick 3:-gun \nresult")
    

    if (computer_pick==player):
        print ("Draw")

    elif (computer_pick==1 and player==2):
        print("You lose")
    
    elif (computer_pick==1 and player==3):
        print("you win")

    elif (computer_pick==2 and player==1):
        print("you lose")

    elif (computer_pick==2 and player==3):
        print("you win")  
    
    elif (computer_pick==3 and player==1):
        print("you lose")

    elif (computer_pick==3 and player==2):
        print("you win")

    else:
        print ("enter correct number")
    