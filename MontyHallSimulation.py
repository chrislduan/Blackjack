# in-built module that generates
# random numbers
import random

# def monty_game(chances, switch_strategy=True):
def monty_game(chances):
    
    global goatcount
    global carcount
    
    carcount = 0
    goatcount = 0

    for i in range(chances):
        doors = [0, 0, 0]
        # randomly replaces one of the goats with a car
        car_door = random.randint(0,2)
        doors[car_door] = 1
        
        # contestant makes a choice
        # random choice below
        # first_choice = random.randint(0,2)
        # choice based on user input
        first_choice = int(input()) - 1
        
        # monty reveals a goat from a door that hasn't
        # been opened by the contestant
        # monty_choice = [x for x in range(3) if x != first_choice and doors[x]==0]
        monty_choice = x for x in range(3) if x != first_choice and doors[x]==0
        
        # .choice() method from the random module
        # random choice code below
        second_choice = random.choice(monty_choice)

        '''
        # switch strategy
        if switch_strategy:
            third_choice = next(x for x in range(3) if x != first_choice and x != second_choice)
        
            if doors[third_choice] == 1:
                carcount += 1
            else:
                goatcount += 1
        '''

        # user input for second choice, expected input is True or False
        switch_strategy = input()

        # variable to create final choice, assuming that the user did not switch strategy
        final_choice = first_choice
        # if user did choose to switch strategy, then choose the door that is not their original choice nor the one chosen by monty
        if switch_strategy:
            final_choice = [x for x in range(3) if x != first_choice and x != monty_choice]

        # score count
        if doors[final_choice] == 1:
            carcount += 1
        else:
            goatcount += 1

    wining_percentage = (carcount/chances)*100
    return wining_percentage

# sets the number of iterations to 1000
chances = 2

# calls the function monty_game
# switch_win_percentage = monty_game(chances, switch_strategy=True)
switch_win_percentage = monty_game(chances)

# f string
print(f" I won {carcount} times ")
print(f" Win percentage with switching: {switch_win_percentage:.2f}%")
