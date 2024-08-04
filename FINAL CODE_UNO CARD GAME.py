#UNO GAME

#importing modules
import random
import numpy as np
import cv2
from matplotlib import pyplot as plt

#print("UNO GAME")

plt.rcParams["figure.figsize"] = [15,15]
plt.rcParams["figure.autolayout"] = True
imgc=plt.imread(r'F:\GITHUB PROJECTS\CS UNO CARD GAME\UNO CARDS\Uno-Cover Image.jpg')
plt.subplot(1,3,2)
plt.imshow(imgc)
plt.axis('off')
plt.show()

#Game Rules
rules=input("Do you want to check the rules of the game? (Y/N): ")
display=True
while display:
    if rules in "Yy":
        print()
        print("OFFICIAL RULES")
        print(".To start a hand, five cards are dealt to each player.\n.Top card of the remaining deck is flipped over to start the game.\n.Play one card matching the top card of the discard pile in terms of the same colour,")
        print(" number or symbol.\n.Play a wild to change the colour of the discard pile.\nCan be played as wish.\n.Wild draw 4 enables the next person in turn to draw 4 cards. Can be played as wish.")
        print(". Skip- Skips the next player’s turn. Only the same coloured skip as the card on top of the discard pile can be played.\n. Reverse-Reverses the order of play from the player who has played the card. Only the")
        print("same coloured reverse as the card on top of the discard pile can be played.\n.Draw 2 enables the next person in turn to draw 2 cards. Only the same coloured draw 2 can ")
        print("be played on top of a normal card.\n. Draw 2 cards can be stacked irrespective of the colour.\n.UNO shown on screen when a player has one card remaining.")
        print(".First person with no cards remaining wins the game.")
        display=False
        break
    elif rules in "Nn":
        display=False
        break
    else:
        print("Invalid input!!!")


#Building a Deck

'''
d1,d2-->list
deck-->Main list with all the cards
colours,values,wilds--> list
'''

d1=[]
deck=[]
d2=[]
colours=["Red","Blue","Yellow","Green"]
values=[0,1,2,3,4,5,6,7,8,9,"Draw Two","Skip","Reverse"]
Wilds=["Wild","Wild-Draw Four"]

for i in colours:
    for j in values:
        card=(i+"-"+str(j))
        d1.append(card)
#print(d1)
values.remove(0)
for c in colours:
    for v in values:
        card2=(c+"-"+str(v))
        d2.append(card2)
#print(d2)
deck=d1+d2
deck.extend(Wilds*4)
#print(deck)
#print(len(deck))


#Shuffling the deck

'''
pos --> index values of list deck
rpos --> random index values of list deck
'''

for pos in range(108):
    rpos=random.randint(0,107)
    deck[pos],deck[rpos]=deck[rpos],deck[pos]
   
#print(deck)

#Checking if the current card is valid

ccpos=random.randint(0,107)
print("Index value of top card(ccpos):",ccpos)
currentcard=deck[ccpos]
while "Wild" in currentcard or "Skip" in currentcard or "Reverse" in currentcard or "Draw Two" in currentcard:
    ccpos=random.randint(0,107)
    currentcard=deck[ccpos]
#print(ccpos)
#print(currentcard)

#Number of players
print()  
n=int(input("Enter a number of players: "))
while True:
    if n<=1:
        n=int(input("Pleas enter a number greater than 1: "))
    if n>4:
        n=int(input("Too many players!\nEnter a number of players less than 4: "))
    else:
        break

#Dealing the cards

players={}
for p in range(1,n+1):
    cards=[]
    for x in range(5):
        cards.append(deck.pop(0))
    players[p]=cards
#print(players)
#print(len(deck))
#print(deck)

game=True
play=True
stack=1
used=False
currentplayer=1
direction=1
discardpile=[]
discardpile.append(currentcard)
end=True
winner=False
 
while game:
    print()
    print("The card on top is:")
   
    #Displaying current card
    plt.rcParams["figure.figsize"] = [2.7,2.7]
    plt.rcParams["figure.autolayout"] = True
    plt.rcParams["font.size"]=15
    imgcc=plt.imread(r'F:\GITHUB PROJECTS\CS UNO CARD GAME\UNO CARDS\{}.jpg'.format(currentcard))
    plt.imshow(imgcc)
    plt.title(currentcard)
    plt.axis('off')
    plt.show()
   
    print("Player {}'s Turn:".format(currentplayer))
    print("Your cards:\n")
    currentlist=players[currentplayer]
   
    #Displaying players cards
    for c in range(len(currentlist)):
        plt.rcParams["figure.figsize"] = [8.5,2.7]
        plt.rcParams["figure.autolayout"] = True
        plt.rcParams["font.size"]=9
        imgc=plt.imread(r'F:\GITHUB PROJECTS\CS UNO CARD GAME\UNO CARDS\{}.jpg'.format(currentlist[c]))
        plt.subplot(1,len(currentlist),c+1)
        plt.imshow(imgc)
        t=str(c+1)+") "+currentlist[c]
        plt.title(t)
        plt.axis('off')
    plt.show()

    if currentcard=="Wild":
        split1=["Wild",""]
    else:
        split1=currentcard.split("-")
    if split1[0] in colours:
        if split1[1] not in ["Draw Two","Skip","Reverse"]:
            #It is a normal colour-number card

            #Checking if the player has a card that matches either the colour or number or has a "Wild"
            chck=[]
            for pc in currentlist:
                if split1[0] in pc or split1[1] in pc:
                    chck.append("True")
                elif "Wild" in pc:
                    chck.append("True")
                else:
                    pass
            if "True" in chck:
                canplay=True
                while canplay:
                    cpnum=int(input("Enter the card you want to play: "))
                    #cpnum ---> integer entered by user indicating the card they wish to play
                    cardplayed=currentlist[cpnum-1]
                    #cardplayed ---> card the user has played
                   
                    if cardplayed!="Wild":
                        split2=cardplayed.split("-")
                    else:
                        split2=['Wild','']
                       
                    if split2[0]==split1[0] or split2[1]==split1[1]:
                        currentcard=currentlist.pop(cpnum-1)
                        print("You played:",currentcard)
                       
                        if "Skip" in currentcard:
                            #skip has been used
                            if direction>0:
                                if currentplayer==n:
                                    currentplayer=1
                                else:
                                    currentplayer+=direction
                            else:
                                if currentplayer==1:
                                    currentplayer=n
                                else:
                                    currentplayer+=direction
                                   
                        elif "Reverse" in currentcard:
                            direction=direction*-1                        
                           
                        discardpile.append(currentcard)
                        #print(currentlist)
                        canplay=False
                        break
                   
                    elif "Wild" in cardplayed:
                        currentcard=currentlist.pop(cpnum-1)
                        print("You played:",currentcard)
                        discardpile.append(currentcard)
                        for cc in range(4):
                            print(cc+1,")",colours[cc],sep="")
                        ccpos=int(input("Which colour do you want to change to? "))
                        colourchange=colours[ccpos-1]
                        print("You chose:",colourchange)
                        #print(currentlist)
                        canplay=False
                        break
                    else:
                        print("Invalid Card!!!")
                       
            else:
                #The player doesn't have a card with required colour or number
                currentlist.append(deck.pop(0))
                print("You don't have a playable card!\nYou had to draw a card")
                #print(currentlist)
        else:
            #it is a special colour card
           
            if split1[1]=="Draw Two":
               
                #stack=-1 when card "Draw Two" is already used and is on top just to indicate colour
                #stack=1 when it is a fresh "Draw Two" card and the stack can further increase
               
                if stack==-1:
                    chck=[]
                    for pc in currentlist:
                        #Over a used "Draw Two" card one can play either a card with same colour or one of the wilds
                        if split1[0] in pc or "Wild" in pc:
                            chck.append("True")
                        else:
                            pass
                    if "True" in chck:
                        canplay=True
                        while canplay:
                            cpnum=int(input("Enter a card you want to play: "))
                            cardplayed=currentlist[cpnum-1]
                            if split1[0] in cardplayed:
                                currentcard=currentlist.pop(cpnum-1)
                                print("You played:",currentcard)
                                discardpile.append(currentcard)
                               
                                if "Skip" in currentcard:
                                    #skip has been used
                                    if direction>0:
                                        if currentplayer==n:
                                            currentplayer=1
                                        else:
                                            currentplayer+=direction
                                    else:
                                        if currentplayer==1:
                                            currentplayer=n
                                        else:
                                            currentplayer+=direction
                                           
                                elif "Reverse" in currentcard:
                                    direction=direction*-1
                               
                                #print(currentlist)
                                stack=1
                                #stack is changed to one so that whenever it is a "Draw Two" card agin it indicates it is a fresh one
                                canplay=False
                                break
                               
                            elif "Wild" in cardplayed:
                                currentcard=currentlist.pop(cpnum-1)
                                print("You played:",currentcard)
                                discardpile.append(currentcard)
                                for cc in range(4):
                                    print(cc+1,")",colours[cc],sep="")
                                ccpos=int(input("Which colour do you want to change to? "))
                                colourchange=colours[ccpos-1]
                                print("You chose:",colourchange)
                                #print(currentlist)
                                stack=1
                                #stack is changed to one so that whenever it is a "Draw Two" card agin it indicates it is a fresh one
                                canplay=False
                                break
                               
                            else:
                                print("Invalid Card!!!")
                    else:
                        currentlist.append(deck.pop(0))
                        print("You don't have a playable card!\nYou had to draw a card")
                        #print(currentlist)
                       
                else:
                    #stack>=1 i.e. the "Draw Two" card has not been applied yet
                    chck=[]
                    for pc in currentlist:
                        if "Draw Two" in pc:
                            chck.append("True")
                        else:
                            pass
                    if "True" in chck:
                        canplay=True
                        while canplay:
                            choice=input("Do you want to stack? (Y/N): ")
                            if choice in "Yy":
                                cp=int(input("Enter the card you want to stack: "))
                                if "Draw Two" in currentlist[cp-1]:
                                    currentcard=currentlist.pop(cp-1)
                                    discardpile.append(currentcard)
                                    #increasing stack value to increase number of cards to be drawn
                                    stack+=1
                                    canplay=False
                                    break
                                else:
                                    print("Invalid Card!!!")
                            elif choice in "Nn":
                                #If they do not wish to stack
                                for add in range(2*stack):
                                    currentlist.append(deck.pop(0))
                                print("You had to Draw",2*stack,"Cards")
                                #print(currentlist)
                                stack=-1
                                #Changing stack=-1 to show that cards have been drawn and "Draw Two" has been used
                                canplay=False
                                break
                            else:
                                print("Invalid Input!!!")
                           
                    else:
                        for add in range(2*stack):
                            currentlist.append(deck.pop(0))
                        print("You had to Draw",2*stack,"Cards")
                        #print(currentlist)
                        stack=-1
                        #Changing stack=-1 to show that cards have been drawn and "Draw Two" has been used

           
            elif split1[1]=='Skip':
                chck=[]
                for c in currentlist:
                    if split1[0] in c or "Wild" in c:
                        chck.append('True')
                    else:
                        pass
                if len(chck)>0:
                    canplay=True
                    while canplay:
                        cpc=int(input("Enter a card you want to play:"))
                        cardplayed=currentlist[cpc-1]
                        if split1[0] in cardplayed:
                            currentcard=currentlist.pop(cpc-1)
                            print("You played:",currentcard)
                            discardpile.append(currentcard)
                            canplay=False
                            used=False
                            break
                        elif "Wild" in cardplayed:
                            currentcard=currentlist.pop(cpc-1)
                            print("You played:",currentcard)
                            discardpile.append(currentcard)
                            for cc in range(4):
                                print(cc+1,")",colours[cc],sep="")
                            ccpos=int(input("Which colour do you want to change to? "))
                            colourchange=colours[ccpos-1]
                            print("You chose:",colourchange)
                            discardpile.append(currentcard)
                            canplay=False
                            used=False
                            break
                        else:
                            print("Invalid Card!!!")
                else:
                    print("You do not have a card,draw a card from the deck")
                    a=deck.pop(0)
                    currentlist.append(a)
                       
            elif split1[1]=='Skip':
                chck=[]
                for c in currentlist:
                    if split1[0] in c or "Wild" in c:
                        chck.append('True')
                    else:
                        pass
                if len(chck)>0:
                    canplay=True
                    while canplay:
                        cpc=int(input("Enter a card you want to play:"))
                        cardplayed=currentlist[cpc-1]
                        if split1[0] in cardplayed:
                            currentcard=currentlist.pop(cpc-1)
                            print("You played:",currentcard)
                            discardpile.append(currentcard)
                            canplay=False
                            used=False
                            break
                        elif "Wild" in cardplayed:
                            currentcard=currentlist.pop(cpc-1)
                            print("You played:",currentcard)
                            discardpile.append(currentcard)
                            for cc in range(4):
                                print(cc+1,")",colours[cc],sep="")
                            ccpos=int(input("Which colour do you want to change to? "))
                            colourchange=colours[ccpos-1]
                            print("You chose:",colourchange)
                            canplay=False
                            used=False
                            break
                        else:
                            print("Invalid Card!!!")
                else:
                    print("You do not have a card,draw a card from the deck")
                    a=deck.pop(0)
                    currentlist.append(a)

    elif "Wild" in currentcard:
        if split1[1]=="Draw Four":
            if stack==-1:
                print("The current colour is:",colourchange)
                chck=[]
                for pc in currentlist:
                    #Over a used "Wild-Draw Four" card one can play either a card with new colour or one of the Wilds
                    if colourchange in pc or "Wild" in pc:
                        chck.append("True")
                    else:
                        pass
                if "True" in chck:
                    canplay=True
                    while canplay:
                        cpnum=int(input("Enter a card you want to play: "))
                        cardplayed=currentlist[cpnum-1]
                        if colourchange in cardplayed:
                            currentcard=currentlist.pop(cpnum-1)
                            print("You played:",currentcard)
                            
                            if "Skip" in currentcard:
                            #skip has been used
                                if direction>0:
                                    if currentplayer==n:
                                        currentplayer=1
                                    else:
                                        currentplayer+=direction
                                else:
                                    if currentplayer==1:
                                        currentplayer=n
                                    else:
                                        currentplayer+=direction
                                   
                            elif "Reverse" in currentcard:
                                direction=direction*-1      
                            
                            discardpile.append(currentcard)
                            #print(currentlist)
                            stack=1
                            #stack is changed to one so that whenever it is a "Wild-Draw Four" card agin it indicates it is a fresh one
                            canplay=False
                            break
                        elif "Wild" in cardplayed and "Draw Four" not in cardplayed:
                            currentcard=currentlist.pop(cpnum-1)
                            print("You played:",currentcard)
                            discardpile.append(currentcard)
                            for cc in range(4):
                                print(cc+1,")",colours[cc],sep="")
                            ccpos=int(input("Which colour do you want to change to?"))
                            colourchange=colours[ccpos-1]
                            print("You chose:",colourchange)
                            #print(currentlist)
                            stack=1
                            #stack is changed to one so that whenever it is a "Draw Two" card agin it indicates it is a fresh one
                            canplay=False
                            break
                               
                        else:
                            print("Invalid Card!!!")
                else:
                    currentlist.append(deck.pop(0))
                    print("You don't have a playable card!\nYou had to draw a card")
                    #print(currentlist)
                       
            else:
                #stack>=1 i.e. the "Wild-Draw Four" card has not been applied yet
                for add in range(4):
                        currentlist.append(deck.pop(0))
                print("You had to Draw 4 Cards")
                #print(currentlist)
                stack=-1
                #Changing stack=-1 to show that cards have been drawn and "Draw Two" has been used
        else:
            #It is a plain "Wild"
            print("The current colour is:",colourchange)
            chck=[]
            for pc in currentlist:
                #Over a used "Wild" card one can play either a card with new colour or one of the Wilds
                if colourchange in pc or "Wild" in pc:
                    chck.append("True")
                else:
                    pass
            if "True" in chck:
                canplay=True
                while canplay:
                    cpnum=int(input("Enter a card you want to play: "))
                    cardplayed=currentlist[cpnum-1]
                    if colourchange in cardplayed:
                        currentcard=currentlist.pop(cpnum-1)
                        print("You played:",currentcard)
                        if "Skip" in currentcard:
                            #skip has been used
                            if direction>0:
                                if currentplayer==n:
                                    currentplayer=1
                                else:
                                    currentplayer+=direction
                            else:
                                if currentplayer==1:
                                    currentplayer=n
                                else:
                                    currentplayer+=direction
                                   
                        elif "Reverse" in currentcard:
                            direction=direction*-1 
                            
                        discardpile.append(currentcard)
                        #print(currentlist)
                        canplay=False
                        break
                    elif "Wild" in cardplayed:
                        currentcard=currentlist.pop(cpnum-1)
                        print("You played:",currentcard)
                        discardpile.append(currentcard)
                        for cc in range(4):
                            print(cc+1,")",colours[cc],sep="")
                        ccpos=int(input("Which colour do you want to change to?"))
                        colourchange=colours[ccpos-1]
                        print("You chose:",colourchange)
                        #print(currentlist)
                        canplay=False
                        break
                               
                    else:
                        print("Invalid Card!!!")
                
            else:
                print("You do not have a card,draw a card from the deck")
                a=deck.pop(0)
                currentlist.append(a)

    #Checking if deck is empty
    if len(deck)==0:
        for pos in range(108):
            rpos=random.randint(0,107)
            discardpile[pos],discardpile[rpos]=discardpile[rpos],discardpile[pos]
        deck=discardpile
    else:
        pass        

    #checking for player with one card or no cards remaining
    if len(currentlist)==1:
        print("UNO!!!")
        print("You have one card remaining!!!")
        #Increasing/Decreasing CurrentPlayer
        if direction>0:
            if currentplayer==n:
                currentplayer=1
            else:
                currentplayer+=direction

        elif direction<0:
            if currentplayer==1:
                currentplayer=n
            else:
                currentplayer+=direction

    elif len(currentlist)==0:
        game=False
        winner=True
        break
    else:
        #Increasing/Decreasing CurrentPlayer
        if direction>0:
            if currentplayer==n:
                currentplayer=1
            else:
                currentplayer+=direction

        elif direction<0:
            if currentplayer==1:
                currentplayer=n
            else:
                currentplayer+=direction

print("GAME OVER")
if winner==True:
    print("WINNER")
    print("Player {} ".format(currentplayer),"WINS!!!!!!!")
else:
    pass

plt.rcParams["figure.figsize"] = [15,15]
plt.rcParams["figure.autolayout"] = True
imgc=plt.imread(r'F:\GITHUB PROJECTS\CS UNO CARD GAME\UNO CARDS\Winner.gif')
plt.subplot(1,3,2)
plt.imshow(imgc)
plt.axis('off')
plt.show()