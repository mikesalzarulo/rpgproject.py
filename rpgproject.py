#
# Michael Salzarulo
#
# rpgproject.py
#
# An rpg game that displays a menu, allows user to choose path, and quit.
#
# Algorithm
# Display Menu.
# Generate: A rules board or initiate game play.
# Input: User selection.
# Processing: 1. Select option (1-3).
#             2. If option 2, enter logic to score points.
#             3. Tally points for different options.
#             4. Display results.
#             5. Ask user to start from beginning or quit.
# Output: Here is the rules or here is your results. Play again?
#

# Import random class.
import random
# Define the main function.
def main():
    
    # Define variables.
    play = 'y'
    name = ''
    userchoice = 0
    userscore = 100
    pathchoice = 0
    highscores = ['', 0]
    highscore = 0

    # Enter Boolean loop.
    while True:

        # Prints intro to user.
        print('Welcome to ... The Tomb of Infinite Loops\n')

        # Display Menu options and valid input.

        userchoice = getMenuChoice()

        # Display Menu if user chooses option 1.
        if userchoice == 1:
            print('Tomb Rules\n'+
                  '1) No running! You might fall.\n'+
                  '2) When choosing a path, think programming.\n'+
                  '3) If Monty asks for food, remind him of his diet.\n\n'+
                  'This game is inpired by the Dutch programmer, Guido van Rossum, who '+
                  ' surprisingly created and named Python after the 1970s hit series,'+
                  ' Monty Python in the year 1991.\n')
        # Enter Game if user chooses option 2.
        elif userchoice == 2:

            # Create variable for user name.
            name = input('Enter name:')
            # Call tomb greeting function.
            tombGreeting(name)
            
            # Dialogue one.
            print('As you enter the tomb, you hear a humming sound. It\'s as if you are not alone...\n'+
                  'Could that sound be a hard drive disk spinning you think to youself? Impossible, it is just too loud.\n')
            print('You proceed to continue without hesitation as you know the Orb of Unlimited Ram is at stake.\n')
            print('Less than 50 steps later, you hear a whoosh and your flashlight flickers. All of a sudden you see what looks\n'+
                  'like a transparent person in front of you. You try to proceed, but you can\'t move.')
            # Interaction one.
            # Validate input until correct.
            while True:
                pathchoice = int(input('Monty - \"Hi! I\'m Monty, and if you want that which you desire, answer me this.\"\n\n'+
                            'What diet did the ghost developer go on?\n'+
                              '1) Atkins\n'+
                              '2) Boolean\n'+
                              '3) Weight Watchers\n'))
                if pathchoice < 1 or pathchoice > 3:
                    print('Invalid entry.')
                else:
                    break
            # Calculate points value and delegate accordingly.
            if pathchoice == 2:
                print('Monty - \"Excellent, maybe you are worthy.\"\n'+
                      'You feel a powerful energy enter your body, but you continue on.\n')
                userscore += 20
                
            elif pathchoice == 3 or pathchoice == 1:
                print('Monty - \"Sorry, not quite.\"\n'+
                      'You feel a stinging sensation on your hands, but you continue on.\n')
                userscore -= 20
            # Display current score.
            print('Current Score:  ', userscore, '\n\n')
            # Dialogue two.
            print('You think to yourself how strange that interaction was and can\'t help but wonder if it was real or not.')
            print('You continue on to deeper depths of the tomb when all of a sudden you hear a whoosh and your flashlight flickers again.')
            print('Who else but the same entity enters, Monty.\n')
            # Interaction two.
            while True:
                pathchoice = int(input('Monty - \"Hello again! I see you have continued to pursue that which you desire. Answer me this!\"\n\n'+
                            'Why did the programmer quit his job?\n'+
                              '1) He didn\'t get arrays\n'+
                              '2) He didn\'t like his schedule\n'+
                              '3) He wanted something challenging\n'))
                if pathchoice < 1 or pathchoice > 3:
                    print('Invalid entry.')
                else:
                    break
            # Calculate points value and delegate accordingly.
            if pathchoice == 1:
                print('Monty - \"Excellent, maybe you are worthy.\"\n'+
                      'You feel a powerful energy enter your body, but you continue on.\n')
                userscore += random.randint(10,40)
                
            else:
                print('Monty - \"Sorry, not quite.\"\n'+
                      'You feel a stinging sensation on your hands, but you continue on.\n')
                userscore -= random.randint(10,40)
            print('Current Score:  ', userscore, '\n\n')
            # Dialogue three.
            print('You realize that the only way to get the Orb of Unlimited Ram is to pass all of Morty\'s tests.\n'+
                  'You can hear the sound of the spinning increasing to an extremely loud volume, but you continue.\n')
            print('You continue on to deeper depths of the tomb when all of a sudden you hear a whoosh and your flashlight flickers again.')
            print('Is that, Morty?\n')
            # Interaction three.
            while True:
                pathchoice = int(input('Monty - \"Hello again! I see you have continued to pursue that which you desire. Seeing as this is my last question, think hard and answer me this!\"\n\n'+
                            'Whats a pirate\'s favorite programming language?\n'+
                              '1) Java\n'+
                              '2) Argghhh!\n'+
                              '3) Python\n'))
                if pathchoice < 1 or pathchoice > 3:
                    print('Invalid entry.')
                else:
                    break
            # Calculate points value and delegate accordingly.
            if pathchoice == 3:
                print('Monty - \"Excellent, maybe you are worthy.\"\n'+
                      'You feel a powerful energy enter your body, but you continue on.\n')
                userscore += random.randint(20,60)
                
            else:
                print('Monty - \"Sorry, not quite.\"\n'+
                      'You feel a stinging sensation on your hands, but you continue on.\n')
                userscore -= random.randint(20,60)
            print('Current Score:  ', userscore, '\n\n')
            # Dialogue four.
            print('You see the entrance to the tomb and almost scream with excitement.\n'+
                  'As you reach for the tomb door, you feel your body freeze. All of a sudden you hear it...')
            # Interaction four.
            while True:
                pathchoice = int(input('Monty - \"Hey uhm, do you remember which diet I\'m on?\"\n\n'+
                              '1) Atkins\n'+
                              '2) Boolean\n'+
                              '3) Weight Watchers\n'))
                if pathchoice < 1 or pathchoice > 3:
                    print('Invalid entry.')
                else:
                    break
            # Calculate points value and delegate accordingly.
            if pathchoice == 2:
                print('Monty - \"Excellent, maybe you are worthy.\"\n'+
                      'You feel a powerful energy enter your body, but you continue on to open the door.\n')
                userscore += 20
                
            else:
                print('Monty - \"Sorry, not quite.\"\n'+
                      'You feel a stinging sensation on your hands, but you continue on to open the door.\n')
                userscore -= 20
            print('You have cleared the tomb. The spinning turns out to have been your imagination all along and all you can hear is the Best Buy associate asking...\n'
                  'Best Buy Associate - \"Will that be credit or debit sir?\"\n')
            print('Roll Credit(s)...\n')
        # Break loop if user decides to quit game.   
        elif userchoice == 3:
            break

        # If user plays game, highscore will be read to list and user score will be displayed.
        if userchoice == 2:

            # Opens and reads current high score values to highscores list.
            scoresfile = open(r'/Users/michaelsalzarulo/Desktop/highscores.txt','r')
            lines = scoresfile.read()
            highscores = lines.splitlines()
            highscore = int(highscores[1])
            # Closes file.
            scoresfile.close()
            
            print('You scored: ', userscore, '!\n')

            # If user beat current high score, user's score will replace old high score. High score will display either way.
            if userscore > highscore:
                # Writes new values to text file.
                scoresfile = open(r'/Users/michaelsalzarulo/Desktop/highscores.txt','w')    
                scoresfile.write(name + '\n')
                scoresfile.write(str(userscore))
                # Closes file.
                scoresfile.close()
                scoresfile = open(r'/Users/michaelsalzarulo/Desktop/highscores.txt','r')
                # Reads new file values and pushes them to highscores list.
                lines = scoresfile.read()
                highscores = lines.splitlines()
                # Closes file.
                scoresfile.close()
            # Call display high scores function.
            displayHighScore(highscores)
    
    
        # Asks user if they would like to play again or select another option.
        play = input('Main Menu?(y/n)\n')
        if play == 'n':
            break


# Define menu choice function.
def getMenuChoice():
    # Enter loop for menu choice input validation.
    while True:
        # Prompt for choice.
        userchoice = int(input('Would you like to\n\n'+
              '1) See Rules\n'+
              '2) Play Game\n'+
              '3) Quit\n'))
        # If out of range, prompt again till in range.
        if userchoice < 1 or userchoice > 3:
                    print('Invalid entry.')
        # Break loop when correct and return choice.
        else:
            break
    return userchoice

# Define high score display function with parameter.
def displayHighScore(score):
    # Prints high score with parameter.
    print('High Score: ', score, '\n')

# Define tomb greeting function with parameter.
def tombGreeting(title):
    # Prints tomb greeting with parameter.
    print('Good luck', title,'...')
    
# Call main function.
main()

