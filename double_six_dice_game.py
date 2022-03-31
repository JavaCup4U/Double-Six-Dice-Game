
from random import randint



print('________________________\n|                       |\n|  Double Six Dice Game |\n|_______________________|')


# Keep track of the number of rolls for each player 
player_one_rolls = 0
player_two_rolls = 0




# A fucntion to decide who wins the game 
def who_won(player_one_rolls,player_two_rolls,player1,player2):
    if player_one_rolls < player_two_rolls:             # If player one has less attempts (rolls) player one wins 
        print(f"{player1} Wins! with {player_one_rolls} rolls!") 
        
    else:                                               # Otherwise player two wins with less attempts (rolls) 
        print(f"{player2} Wins! with {player_two_rolls} rolls!")
         
    if player_one_rolls == player_two_rolls:            # If player one attempts is equal to player twos attempts 
        print("It's a Draw!")                           # Print It is a draw to console 
        

# -------------- Main Code ----------

# Keep rolling the dice until 
# Player1 hits a double six 
running = True
while running:
    # Ask first player their name 
    player1 = input("What is your name?: ")
    
    # Ask First player to roll first try 
    player_one_roll = input("Player one's turn: press 'R' to roll the dice!")
    # Create two unique random numbers for each dice 
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    print(dice1)
    print(dice2)
    if dice1 == 6 and dice2 == 6:                       # If they roll a double six on the first try 
        player_one_rolls += 1                           # Add a roll 
        print("You rolled a double six!\n")             
        print(f"Number of rolls: {player_one_rolls}")   # Show their current count of rolls 
    else:                                              # Add a roll regardless if they roll a double six or not 
        player_one_rolls += 1
            
    
    # Player one's turn keeps going until players turn is False
    player_one_turn = True
    while player_one_turn:
        # Create a new set of random numbers for the next roll
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        # Ask First player to roll
        player_one_new_try = input("No luck! Roll again!: press 'R' to roll the dice!")
        if player_one_new_try.upper(): # If player rolls we print the random values
            print(dice1)        # And increment the number of rolls for that player 
            print(dice2)
            player_one_rolls += 1
        
        if dice1 == 6 and dice2 == 6:           # If the player rolls a double six 
            print("You rolled a double six!\n") 
            print(f"Number of rolls: {player_one_rolls}")
            player_one_turn = False             # Set the players turn to False to get out of the while loop 
    
    # Ask second player their name 
    player2 = input("What is your name?: ")
    # Create a new set of random numbers for the next player 
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    # Ask player two to roll
    player_two_roll = input("Player two's turn: press 'R' to roll the dice!")
    print(dice1)
    print(dice2)
    if dice1 == 6 and dice2 == 6:               # if they get it on first try 
        player_two_rolls += 1                   # Add a roll 
        print("You rolled a double six!\n")
        print(f"Number of rolls: {player_two_rolls}")
        who_won(player_one_rolls,player_two_rolls,player1,player2)    # decide who wins  end the game 
        running = False                               # End the game 
    else:
        player_two_rolls += 1                       # Add a roll regardless if they roll a double on first try 
                                                    # Or not 

    # Player two's turn 
    player_two_turn = True 
    while player_two_turn:
        # Create new set of random numbers for the next roll
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        # Ask player two to roll
        player_two_new_try= input("No luck! Roll again!: press 'R' to roll the dice!")

        if player_two_new_try.upper(): # If player rolls we print the two random values
            print(dice1)            # for the dice roll and increment the player rolls 
            print(dice2)
            player_two_rolls += 1
        
        if dice1 == 6 and dice2 == 6:
            print("You rolled a double six!\n")
            print(f"Number of rolls: {player_two_rolls}")
            player_two_turn = False
    
    # Decide who is the winner with the least rolls 
    who_won(player_one_rolls,player_two_rolls,player1,player2)

    # End the game
    running = False
    

