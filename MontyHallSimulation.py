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
        
        # Use for testing, print the doors
        print(doors)
        
        # contestant makes a choice
        # random choice below
        # first_choice = random.randint(0,2)
        # prompt for user input
        print(f"Choose doors 1-{len(doors)}.")
        # choice based on user input
        first_choice = int(input()) - 1
        print(f"First Choice: {first_choice}")
        
        # monty reveals a goat from a door that hasn't
        # been opened by the contestant
        # monty_choice = [x for x in range(3) if x != first_choice and doors[x]==0]

        # list of doors monty can open
        monty_doors = [x for x in range(len(doors)) if x != first_choice and doors[x]==0]
        monty_choice = monty_doors[random.randint(0, len(monty_doors) - 1)]

        # print the door monty reveals
        print(f"Monty reveals door {monty_choice + 1} has a goat.")
        
        # .choice() method from the random module
        # random choice code below
        # second_choice = random.choice(monty_choice)

        '''
        # switch strategy
        if switch_strategy:
            third_choice = next(x for x in range(3) if x != first_choice and x != second_choice)
        
            if doors[third_choice] == 1:
                carcount += 1
            else:
                goatcount += 1
        '''

        # prompt if user wants to change their choice
        print(f"Would you like to change your choice, True or False?")
        # user input for second choice, expected input is True or False
        switch_strategy = False
        switch_strategy_str = input()
        if switch_strategy_str == "True" or switch_strategy_str == "T":
            switch_strategy = True 
        if switch_strategy_str == "False" or switch_strategy_str == "F":
            switch_strategy = False 
        print(f"Switch Strategy: {switch_strategy}")

        # variable to create final choice, assuming that the user did not switch strategy
        final_choice = first_choice
        # if user did choose to switch strategy, then choose the door that is not their original choice nor the one chosen by monty
        if switch_strategy:
            final_choice_doors = [x for x in range(len(doors)) if x != first_choice and x != monty_choice]
            print(f"Final_choice_doors: {final_choice_doors}")
            final_choice = final_choice_doors[0]

        # score count
        print(f"Final Choice:{final_choice}")
        if doors[final_choice] == 1:
            carcount += 1
        else:
            goatcount += 1
        print(f"Car count: {carcount}")

    wining_percentage = (carcount/chances)*100
    return wining_percentage

# sets the number of iterations to 1000
chances = 1

# calls the function monty_game
# switch_win_percentage = monty_game(chances, switch_strategy=True)
switch_win_percentage = monty_game(chances)

# f string
print(f" I won {carcount} times ")
print(f" Win percentage with switching: {switch_win_percentage:.2f}%")
