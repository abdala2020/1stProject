""" This is a simple dice game with two players. who scores 50 points winns.
    if the player rolls 1, they will lose the scores the earn in that turn."""

import random # for generating random numbers for die slides
import os # incase file handling is needed

player1_turn_score = 0 #stores scores earned during a turn
player2_turn_score = 0 ##stores scores earned during a turn
player1_turns_Played= 0 # number of turns player1 played during the game
player2_turns_played = 0 # number of turns player2 played during the game
turn = 1 # for tracking turns

def main():# this is the entry point of the program
    global player1_turn_score
    global player2_turn_score
    print("Welcome To The Game! We Are So Excited To Have You Here!")
    print("---------------------------------------------------")

    ans = input("would you like to start the game? y/n ")
    ans = ans.lower()
    while ans == "y":
        slashes()
        start()
        ans = input("Do you want to quit or play again? y/n ")
        if ans == 'y':
            player1_turn_score = 0
            player2_turn_score = 0
            continue
    print("Good Bye!")

""" this function handles the result of game. reveals the winner 
    and displays the final record"""
def start(): 
    """create a dictionary to record each player and their final score
        incase it is needed to write this data to a file"""
    players_final_score= {}
    name1 = input("Player1 please enter your first name? ")
    while not name1.isalpha():
        print("Please use Alphabetics only!")
        name1 = input("Player1 please enter your first name? ")
    print()
    name2 = input("Player2 please enter your first name ")
    while not name2.isalpha():
        print("Please use Alphabetics only!")
        name2 = input("Player2 please enter your first name? ")
        
    print()
    print(name1, 'And', name2, "Welcome again")
    print()
    while player1_turn_score < 50 and player2_turn_score < 50:
        print("current score is :")
        print("player1 score: ", player1_turn_score)
        print("payer2 score: ", player2_turn_score)
        print("player", turn, "it is your turn")
        playeGame()
    print()
    
    if player1_turn_score >= 50:
        print("Congrats! Player 1 winns")
        players_final_score["player1"] = [name1, player1_turns_Played, player1_turn_score]
        players_final_score["player2"] = [name2, player2_turns_played, player2_turn_score]
    elif player2_turn_score >= 50:
        print("Congrats! Player 2 winns")
        players_final_score["player2"] = [name2, player2_turns_played, player2_turn_score]
        players_final_score["player1"] = [name1, player1_turns_Played, player1_turn_score]    
        
    print ("{:<10} {:<15} {:<10}".format('NAME', 'Total Turns', 'Total Points')) 
    for key, value in players_final_score.items():
        name, num_turns, total_score = value
        print("{:<10} {:<15} {:<10}".format(name, num_turns, total_score))

#this function returns a randomly generately number between 1 and 6 when ever it is called
def roll_die():
    number_rolled = random.randint(1, 6)
    return number_rolled

"""This function handles all the main activies of the game.
    Including switching turns between players,tracking scores 
    earned by players during each turn, calculating final scores, and 
    taking appropiate action based on the game rules"""
def playeGame():
    global player1_turn_score
    global player2_turn_score
    global turn
    global player1_turns_Played
    global player2_turns_played 
    turn_score = 0
    roll = input("do you want to play? y/n ")
    if roll == "n":
        if turn == 1:
            turn = 2
        elif turn == 2:
            turn = 1
    while roll == "y":
        result = roll_die()
        #handles when the player rolls 1
        if result == 1:
            if turn == 1:
                turn = 2
                print("You rolled {} so your turn is over".format(result))
                turn_score = 0
                player1_turns_Played+=1
                print("Your score for this turn is ", turn_score) 
            elif turn == 2:
                turn = 1
                print("You rolled {} so your turn is over".format(result))
                turn_score = 0
                player2_turns_played+=1
                print("Your score for this turn is ", turn_score)
            break 
        else:
            print("you rolled ", result)
            turn_score+=result
            print("your current score is: ", turn_score)
            roll = input("Do you still want to continue? y/n ")
            if player1_turn_score > 50 or player2_turn_score > 50:
                    break
            if roll == "y":
                continue
            else:
                if turn == 1:
                    player1_turns_Played+=1
                    player1_turn_score+=turn_score
                    turn = 2 #switch turn to player 2
                    
                elif turn == 2:
                    player2_turns_played+=1
                    player2_turn_score+=turn_score
                    turn = 1 # switch turn back to player 1
def slashes():
    print("------------------------------------------------")
    print("------------------------------------------------")
    print("------------------------------------------------")
    print("------------------------------------------------")
    input("HIT ENTER TO CONTINUE")
            
main() # call the main function to start the program 


    











