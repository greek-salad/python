import time
import random

def game():
    print('Get ready!')
    computer_choice = ['rock','paper','scissors','witch','lizard']
    beats = {'scissors':'paper','paper':'rock','rock':'lizard','lizard':'witch','witch':'scissors','scissors':'lizard','lizard':'paper','paper':'witch','witch':'rock','rock':'scissors'}
    verbs = {'scissors':'cuts','paper':'suffocates','rock':'crushes','witch':'magics','lizard':'eats'}
    time.sleep(1)
    print('Rock')
    time.sleep(0.75)
    print('Paper')
    time.sleep(0.75)
    print('Scissors')
    time.sleep(0.75)
    print('Shoot')
    player_choice = input('(Type Rock, Paper, Scissors, Witch or Lizard and then press enter)').lower()
    computer_choice = random.choice(computer_choice)
    time.sleep(1)
    if computer_choice == player_choice:
        print('Computer chose ' + computer_choice + '. You tie!')
    elif beats[player_choice] == computer_choice:
        print(player_choice + ' ' + verbs[player_choice] + ' ' + computer_choice)
        print('Computer chose ' + computer_choice + '. You win!')
    elif beats[computer_choice] == player_choice:
        print('Computer chose ' + computer_choice + '. You lose!')
        print(computer_choice + ' ' + verbs[computer_choice] + ' ' + player_choice)
    play_again = input('Press enter to play again or X to end the game')
    if play_again == "":
        game()
    else:
        print('Thank you for playing')

game()
