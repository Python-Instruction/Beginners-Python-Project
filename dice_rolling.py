#using random library
#importing random
import random
def dice_simulate():
    number = random.randint(1,6)
    #print(number)
    while(1):
       #if user want to continue
       flag = str(input("Do you want to dice it up again:Enter Y and if not enter N\n"))
       if flag == 'Y': 
         number = random.randint(1,6)
         print("YOU GOT :",number)
       elif flag == 'y': 
         number = random.randint(1,6)
         print("YOU GOT :",number)
       else:
         print("ending the game")
         return 0

dice_simulate() 
