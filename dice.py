import random

def roll_again_one():
    dice_roll = random.randint(1,6)
    print('The dice rolled ' + str(dice_roll))
    roll_again = input('Press enter to roll again')
    if roll_again == '':
        roll_again_one()
    else:
        print('Thanks for using the dice roller.')

def one_dice():
    start = input('Press enter to roll the dice')
    if start == '':
        dice_roll = random.randint(1,6)
        print('The dice rolled ' + str(dice_roll))
    else:
        print('error')
    roll_again = input('Press enter to roll again')
    if roll_again == '':
        roll_again_one()
    else:
        print('Thanks for using the dice roller.')

def two_dice():
    doubles = input('Do you want to have doubles enabled? (Yes or no)')
    doubles = doubles.lower()
    if doubles in ['yes','y']:
        doubles = True
    else:
        doubles = False
    start = input('Press enter to roll the dice')
    if start == '':
        play = True
    else:
        print('error')
    while play == True:
        dice_roll_one = random.randint(1,6)
        dice_roll_two = random.randint(1,6)
        print('The dice rolled ' + str(dice_roll_one) + ' and ' + str(dice_roll_two))
        print('(It equals ' + str(dice_roll_one + dice_roll_two) + '.)')
        if doubles == True and dice_roll_one == dice_roll_two:
            print('You got doubles.')
            dice_roll_one = random.randint(1,6)
            dice_roll_two = random.randint(1,6)
            print('The dice rolled ' + str(dice_roll_one) + ' and ' + str(dice_roll_two))
            print('(It equals ' + str(dice_roll_one + dice_roll_two) + '.)')
        else:
            print('')
            roll_again = input('Press enter to roll again')
            if roll_again == '':
                play = True
            else:
                print('Thanks for using the dice roller.')
                play = False
                break

def roll_again_two():
    dice_roll_one = random.randint(1,6)
    dice_roll_two = random.randint(1,6)
    print('The dice rolled ' + str(dice_roll_one) + ' and ' + str(dice_roll_two))
    print('(It equals ' + str(dice_roll_one + dice_roll_two) + '.)')
    if doubles == True and dice_roll_one == dice_roll_two:
        print('You got doubles.')
        dice_roll_one = random.randint(1,6)
        dice_roll_two = random.randint(1,6)
        print('The dice rolled ' + str(dice_roll_one) + ' and ' + str(dice_roll_two))
        print('(It equals ' + str(dice_roll_one + dice_roll_two) + '.)')
    else:
        print('')
    roll_again = input('Press enter to roll again')
    if roll_again == '':
        roll_again_two()
    else:
        print('Thanks for using the dice roller.')



def start():
    print('Welcome to the dice roller.')
    print('Would you like to roll with one dice or two?')
    type = input('Type 1 or 2 and then hit enter')
    if type == '1':
        one_dice()
    elif type == '2':
        two_dice()
    else:
        restart = input('Error. Press enter to restart')
        if restart == '':
            start()
        else:
            print('Bye')

start()
