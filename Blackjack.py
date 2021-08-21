print(
'''
============================================================================
                    MONTE CARLO BLACKJACK SIMULATOR
============================================================================
                            enjoy it!!!!
============================================================================
''')
    
import random

def bet(): 
    mybet=random.choice(numbers)
    print(' **** Your card is '+ mybet +' ****\n')
    if mybet in ('Jack','Queen','King'):
        mybet=10
    if mybet =='Ace':
        print('\n')
        mybet=input(" **** You got an Ace, would you make it worth 1 or 10  ?:")
    return int(mybet) 
   
#print(random.choice(numbers),random.choice(colors))
total=0

numbers=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']    
colors=['Clubs','Diamons','Hearts','Spades']
hit=1
   
while hit == 1:
    total=bet()+total
    if total > 21:
        print("You got: ",total,"**** DEALER WINS ******\n")
        break
    print("So far your total is: ", total," \n")
    hit = int(input("Enter 1 to hit or 2 to stick with the cards you have: \n"))

total_dealer=0
if total <= 21:
    print("Now lets see how dealer goes \n")
    while total_dealer < total:
        total_dealer=bet()+total_dealer
        if total_dealer > 21:
            print("Dealer got: ", total_dealer,"**** PLAYER WINS ******\n")
            print("\n")
            break
        print("So far your total is: ", total_dealer," \n")
        hit = int(input("Enter 1 to hit or 2 to stick with the cards you have: \n"))

if total == total_dealer:
    print("**** IT IS A DRAW ******\n")
    
print(
'''
============================================================================
                    END OF MONTE CARLO BLACKJACK SIMULATOR
============================================================================
                            Come back !!!!
============================================================================
''')

