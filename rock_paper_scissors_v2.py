import time
import random

def game():
    print('Get ready!')
    computer_choice = ['rock','paper','scissors']
    beats = {'rock':'scissors','scissors':'paper','paper':'rock'}
    time.sleep(1)
    print('Rock')
    time.sleep(0.75)
    print('Paper')
    time.sleep(0.75)
    print('Scissors')
    time.sleep(0.75)
    print('Shoot')
    player_choice = input('(Type Rock, Paper or Scissors and then press enter)').lower()
    computer_choice = random.choice(computer_choice)
    time.sleep(1)
    if computer_choice == player_choice:
        print('Computer chose ' + computer_choice + '. You tie!')
    elif beats[player_choice] == computer_choice:
        print('Computer chose ' + computer_choice + '. You win!')
    elif beats[computer_choice] == player_choice:
        print('Computer chose ' + computer_choice + '. You lose!')
    else:
        print('error')
    play_again = input('Press enter to play again or X to end the game')
    if play_again == "":
        game()
    else:
        print('Thank you for playing')

game()
