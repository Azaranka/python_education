#Players select how many sticks they want to take. The last one to take a stick loses.

gamer_a = input('What is your name, gamer a? ')
gamer_b = input('What is your name, gamer b? ')
gamers_positions = 1 
current_position = ''

def gamer_position(gamers):
    global gamer_a
    global gamer_b
    global current_position
    gamers = [gamer_a, gamer_b]
    if gamers_positions%2 == 0:
        current_position = gamers[1]
        print(f'{current_position} selects now: ')
    else:
        current_position = gamers[0]
        print(f'{current_position} selects now: ')

def sticks_game(sticks_quantity):
    global gamers_positions
    global current_position 
    gamer_choice = 0
    while sticks_quantity > 0:
        who_makes_the_choice = gamer_position(gamers)
        gamer_choice = int(input('How many sticks do you want to take? '))
        if gamer_choice >= 0:
            sticks_quantity -= gamer_choice
            gamers_positions +=1
            print(sticks_quantity)
            if sticks_quantity <= 0:
                print(f'You\'ve lost {current_position}')
                break 
            continue

            
        else:
            print('You should enter a positive number')


sticks_game(10)
