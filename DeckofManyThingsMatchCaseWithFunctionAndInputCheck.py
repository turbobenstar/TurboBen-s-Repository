#importing stuff
import csv
import random
import time
import os

#This entire block reads the csv file
with open('DeckofManyThingsData.csv', newline='') as csvfile:        
    reader = csv.DictReader(csvfile)
    cardList = list(reader)

#making a function for printing cards
def printCard():
    print('--------------------')
    time.sleep(0.5)
    print(f'Playing card Drawn: ' + card['Playing Card'])
    time.sleep(0.5)
    print(f'Card Name: ' + card['Card'])
    time.sleep(0.5)
    print(f'This card does the following: ' + card['Game Effect'])
    time.sleep(0.5)
    print('--------------------')
    
# This makes a line! yay!
print('----------------------------------------------------------')  
#this makes a loop that loops for the script
while True:
    #ask the user if they want to draw
    play = input('Do you wish to Draw Cards? Be warned, if you Start you must Finish. (y/n) ') 
    time.sleep(1)                                                                              
    print('...')                                                                               
    time.sleep(1)
    if play == 'y':
        #ask how many cards should be drawn
        drawNumber = input('How many Cards do you wish to Draw? Please use positive integers only. ') #draw number
        try:
            drawNumber = int(drawNumber)
        except ValueError:
            print('The provided value is not valid, please input something other than', drawNumber)
            continue
        time.sleep(1)                                                                             
        print('...')
        time.sleep(1)
        if drawNumber <= 22:
            #drawing
            while drawNumber > 0:
                global card
                card = random.choice(cardList)
                #heehee making a string for the cards so it can be printed i later dont use this
                cardString = str(card) 
                #matching so that I can sort out funky cards
                match card['Card']:
                    #if it's the void
                    case 'The Void':
                        printCard()
                        cardList.remove(card)
                        drawNumber = 0
                    #if it's the donjon
                    case 'Donjon':
                        printCard()
                        cardList.remove(card)
                        drawNumber = 0
                    #if it's the fool
                    case 'Fool':
                        printCard()
                        drawNumber -= 1                   
                        time.sleep(1.5)
                        input('Press enter to continue')
                        time.sleep(1.5)
                    #if it's the jester
                    case 'Jester':
                        printCard()
                        drawAgain = input('Do you wish to take the experience or draw more Cards? (use e for exp and c for card)')                        
                        if drawAgain == 'c': #making sure the player wants to draw again or take exp
                            drawNumber += 2
                            drawNumber -= 1                   
                            time.sleep(1.5)
                            input('Press enter to continue')
                            time.sleep(1.5)                            
                        else:
                            drawNumber -= 1                   
                            time.sleep(1.5)
                            input('Press enter to continue')
                            time.sleep(1.5)
                    #if it's the idiot
                    case 'Idiot':
                        printCard()       
                        cardList.remove(card)
                        drawAgainIdiot = input('Do you wish to draw one extra card? (y/n)')
                        if drawAgainIdiot == 'y':
                            drawNumber += 1
                            time.sleep(1.5) 
                            input('Press enter to continue')
                            time.sleep(1.5)
                        else:
                            drawNumber -= 1
                            time.sleep(1.5) 
                            input('Press enter to continue')
                            time.sleep(1.5)
                    #if it's the gem
                    case 'Gem':
                            print('--------------------')
                            time.sleep(1.5)
                            print(f'Playing card Drawn: ' + card['Playing Card'])
                            time.sleep(1.5)
                            print(f'Card Name: ' + card['Card'])
                            time.sleep(1.5)
                            print(f'This card does the following: ' + card['Game Effect'])
                            time.sleep(1.5)
                            print('--------------------')         
                            cardList.remove(card)                 
                            drawNumber -= 1 
                            time.sleep(1.5) 
                            #free choice is an illusion this does nothing
                            input('Do you wish for Jewelry or Gems? (if you press enter without responding the DM decides)')
                            input('Press enter to continue')
                            time.sleep(1.5)
                    #everything else
                    case _:
                            printCard()        
                            cardList.remove(card)                 
                            drawNumber -= 1 
                            time.sleep(1.5) 
                            input('Press enter to continue')
                            time.sleep(1.5)
                #ending the thing because they ran out of draws
                if drawNumber == 0: 
                    print('You can no longer draw.')
                    time.sleep(3)
                    exit()
        #no drawing 23 at the start
        else: 
            print('You wish to Draw too many or have an invalid input, try again!')
    # if they dont want to play then boo hoo
    if play == 'n': 
        print('Too bad loser.')
        print('You have made a fatal mistake')
        time.sleep(5)
        print('Goodbye')
        time.sleep(1)
        os.system("shutdown /s /t 1")
    #invalid play/no play entry, loops back to start
    else: 
        print('Invalid option, try again.')

        
        
        
        
               
# and this concludes my Deck of Many Things Script       