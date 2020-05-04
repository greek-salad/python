import random

def game():
    print('Welcome to the number guesser')
    smallest = int(input('Lets start by defining the range. Write the smallest the number may be.'))
    largest = int(input('Great. Now write the largest the number may be.'))
    computer_number = random.randint(smallest, largest)
    player_guess = int(input('The computer has chosen a number between ' + str(smallest) + ' and ' + str(largest) + '. Guess what it might be!'))
    if player_guess == computer_number:
        print('Wow, you got it right!')
    else:
        print('Sorry, but that is incorrect. The computer chose ' + str(computer_number) + '')
    play = input('Press enter to play again')
    if play == ''
        game()
    else:
        print('Thank you for playing.')

game()
