#******************************************************************************
# Author:           (Alex Maxson)
# Assignment:       (A3)
# Date:             (5-9-2021)
# Description:      A program for an Earthbound(1994) character select screen with small trivia.
#    
# Input:            Prompting user an integer to select.
# Output:           Greeting message.
#                   Prompts user for input of a positive integer.
#                   Explains selections trivia.
#                   Prompts user to try again.
#                   End statement.
#
# Sources:          Assignment 3 specifications, D2L content, #https://earthbound.fandom.com/wiki/List_of_characters_in_EarthBound
#******************************************************************************
#QUIT used as a constant for consistency and stability.
QUIT = 6
#Main Function, prints greeting statement.
def main():
  #Declares needed variables.
  selection = 0
  print('Hello and Welcome!\n')
  
#Character selection while loop.
  while selection != QUIT:
    menu_screen()
    selection = char_return()
    #Poo's Master selection
    if selection == 1:
      print('\nGood choice but, try to select the best character again.')
      print('Trivia: Poo\'s Master doesn\'t have a name in English, but is known as \"Yee-soo-chii\" in the Japanese version. This is derived from the Chinese \"Yi-Si-Qi\" (one-four-seven); a reference to a gameplay concept in mahjong. \n')
    #Tessie selection
    elif selection == 2:
      print('\nGood choice but, try to select the best character again.')
      print('Trivia: Tessie was inspired by Nessie, the Loch Ness Monster. This is referenced in-game when a Hotel employee accidently buys the TwosonStar newspaper instead of the Twoson Tribune, which has the headline "Tessie in Lake Tess is cousin of Nessie".\n')
    #Mr. Saturn election
    elif selection == 3:
      print('\nGood choice but, try to select the best character again.')
      print('Trivia: Despite being able to build the Phase Distorter and modify a Pork Bean to look like one of them (all with no hands), the Mr. Saturns cannot draw a geographically accurate map of Saturn Valley.\n')
    #Master Belch selection
    elif selection == 4:
      print('\nGood choice but, try to select the best character again.')
      print('Trivia: Although his second form is called "Master Barf" he says that he "changed his name to Puke".\n')
    #Brick Road selection
    elif selection == 5:
      print('\nPerfect choice! Brick Road is the best character!\n(Please try the other characters if you\'d like some trivia of them.)')
      print('If not, please feel free to type 6 to quit.')
      print('\nTrivia: While walking around with Dungeon Man in the player\'s party, a song plays called "The Megaton Walk". This song uses a drumbeat directly sampled from "Sgt. Pepper\'s Lonely Hearts Club Band (Reprise)" by The Beatles. \n')
    #Quit selection
    else:
      print('\nThank you and goodbye! \n                    ...Brick Road.\n')
      quit()

#Menu display function.
def menu_screen():
  print('~~Selectable Characters~~')
  print('1.Poo\'s Master')
  print('2.Tessie')
  print('3.Mr.Saturn')
  print('4.Master Belch')
  print('5.Brick Road')
  print('6.Quit. I\'m done with this malarky!')

#User input validation.
def char_return():
  try:
    charSelect = 0
    charSelect = int(input('\nWho/What is your favorite Earthbound character? Select 1-5 or 6 to quit: '))
    #Input Validation. This while loop will check the input to see if its within 1-6 and if its not, it will continue looping. 
    while charSelect <= 0 or charSelect >= 7:
    #Prints to user what happened.
      print('\nOops. Try again with a number between 1-5 and 6 to quit.\n             ...Brick Road.\n')
      #Prints Menu options again.
      menu_screen()
      charSelect = int(input('\nWho/What is your favorite Earthbound character? Select 1-5 or 6 to quit: '))
    return(charSelect)
  except:
    print('\n**Error** Please enter only 1 number between 1-5 or enter 6 if you\'d like to quit')
    main()
main()