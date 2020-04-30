import time
import random

def game():
    print('Get ready!')
    computer_choice = ['Rock','Paper','Scissors']
    time.sleep(1)
    print('Rock')
    time.sleep(1)
    print('Paper')
    time.sleep(1)
    print('Scissors')
    time.sleep(1)
    print('Shoot')
    player_choice = input('(Type Rock, Paper or Scissors and then press enter)')
    if player_choice in ['Rock','rock','rocks','Rocks','r','R']:
        player_choice = 'Rock'
    elif player_choice in ['Paper','paper','Papers','papers','p','P']:
        player_choice = 'Paper'
    elif player_choice in ['Scissors','scissors','Scissor','scissor','S','s']:
        player_choice = 'Scissors'
    else:
        print('No')
    computer_choice = random.choice(computer_choice)
    time.sleep(1)
    if computer_choice == 'Rock' and player_choice == 'Paper':
        print('Computer chose rock. You win!')
    elif computer_choice == 'Paper' and player_choice == 'Rock':
        print('Computer chose paper. You lose!')
    elif computer_choice == 'Rock' and player_choice == 'Rock':
        print('Computer chose rock. You tie!')
    elif computer_choice == 'Paper' and player_choice == 'Scissors':
        print('Computer chose paper. You win!')
    elif computer_choice == 'Scissors' and player_choice == 'Rock':
        print('Computer chose scissors. You win!')
    elif computer_choice == 'Paper' and player_choice == 'Paper':
        print('Computer chose paper. You tie!')
    elif computer_choice == 'Scissors' and player_choice == 'Scissors':
        print('Computer chose scissors. You tie!')
    elif computer_choice == 'Scissors' and player_choice == 'Paper':
        print('Computer chose scissors. You lose!')
    elif computer_choice == 'Rock' and player_choice == 'Scissors':
        print('Computer chose rock. You lose!')
    else:
        print('error')
    play_again = input('Press enter to play again or X to end the game')
    if play_again == "":
        game()
    else:
        print('Thank you for playing')


loop = True
while loop == True:
    while loop == True:
        start = input('press enter to begin')
        if start == "":
            loop = False
            game()
        else:
            print('restart initiated')
            break
