print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print(     "welcome to treasure island")
print("    you are a pirate finding your own stolen treasure")
scene1 = input ("    Ahoy! matey! you are at a crossroad , left smells like fish and right leads to a forest choose your destiny \"left\" or right\" remember your life depends upon your choices!    ")
if scene1 == "left":
   scene2= input(    'I see you have made it! you come across a fish market beyond which a river stands still , type "swim" to swim across or "wait" to wait for a boat     ')
   if scene2 == "wait":
      scene3 = input('    you arrive to the shore in the comfort of company and safety , you notice an abondoned villa , you step in it with hopes of finding your lost treasure in there you find 3 doors labeled "red" like blood "yellow" like sun and "blue" like water , now is your final choice to make think wisely    ')
      if scene3 == "blue":
         print("     you drowned in a pool full of water. GAME OVER XD  ")
      elif scene3 == "yellow":
         print ( "      Yo-ho-ho-ho! you find the treasure ! INDEED it is as bright and yellow as the sun    ")
      elif scene3 == "red":
         print("      oh no , the flames of the red room only left your ashes. GAME OVER XD    ")
   else:
       print("      the hungry crocodiles chewed him up till his bones , GAME OVER.   ")
else:
   print("       the agony of being clawed by a tiger was so deep you coudn\'t make it. GAME OVER XD    ")

print("THE END")


