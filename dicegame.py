# dice game for linux
# requirements: espeak on linux. install with 'apt install espeak'

import random
import os
import time
import sys


dice_sides = 0
best_of = 0
check = 0
p1score = 0
p2score = 0


class bcolors:

    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    RED = '\033[0;31m'


def text():

    print(bcolors.WARNING + """


                    ██████╗ ██╗ ██████╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗
                    ██╔══██╗██║██╔════╝██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
                    ██║  ██║██║██║     █████╗      ██║  ███╗███████║██╔████╔██║█████╗  
                    ██║  ██║██║██║     ██╔══╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
                    ██████╔╝██║╚██████╗███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
                    ╚═════╝ ╚═╝ ╚═════╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                    """ + bcolors.ENDC)


def game_over():

    print(bcolors.WARNING + """
            
                     ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
                    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
                    ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
                    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
                    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
                     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                                            """ + bcolors.ENDC)
    speak(words['game_over'])


def text_p1win():

    print(bcolors.RED + """
    ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗      ██████╗ ███╗   ██╗███████╗    ██╗    ██╗██╗███╗   ██╗███████╗
    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ██╔═══██╗████╗  ██║██╔════╝    ██║    ██║██║████╗  ██║██╔════╝
    ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ██║   ██║██╔██╗ ██║█████╗      ██║ █╗ ██║██║██╔██╗ ██║███████╗
    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗    ██║   ██║██║╚██╗██║██╔══╝      ██║███╗██║██║██║╚██╗██║╚════██║
    ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║    ╚██████╔╝██║ ╚████║███████╗    ╚███╔███╔╝██║██║ ╚████║███████║
    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═══╝╚══════╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝ 
                                                                                                    """ + bcolors.ENDC)


def text_p2win():

    print(bcolors.OKBLUE + """
    ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗     ████████╗██╗    ██╗ ██████╗     ██╗    ██╗██╗███╗   ██╗███████╗
    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ╚══██╔══╝██║    ██║██╔═══██╗    ██║    ██║██║████╗  ██║██╔════╝
    ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝       ██║   ██║ █╗ ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║███████╗
    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗       ██║   ██║███╗██║██║   ██║    ██║███╗██║██║██║╚██╗██║╚════██║
    ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║       ██║   ╚███╔███╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║███████║
    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝       ╚═╝    ╚══╝╚══╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝ 
                                                                                                    """ + bcolors.ENDC)


def draw():

    print(bcolors.WARNING + """
                                ██████╗ ██████╗  █████╗ ██╗    ██╗    ██╗██╗
                                ██╔══██╗██╔══██╗██╔══██╗██║    ██║    ██║██║
                                ██║  ██║██████╔╝███████║██║ █╗ ██║    ██║██║
                                ██║  ██║██╔══██╗██╔══██║██║███╗██║    ╚═╝╚═╝
                                ██████╔╝██║  ██║██║  ██║╚███╔███╔╝    ██╗██╗
                                ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝     ╚═╝╚═╝                     
                                                        """ + bcolors.ENDC)

    speak(words['match_draw'])
    time.sleep(1)
    os.system("clear")

    print(bcolors.WARNING + """
    
         ██████╗  ██████╗ ██╗     ██████╗ ███████╗███╗   ██╗     ██████╗  █████╗ ███╗   ███╗███████╗    ██╗██╗██╗
        ██╔════╝ ██╔═══██╗██║     ██╔══██╗██╔════╝████╗  ██║    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██║██║██║
        ██║  ███╗██║   ██║██║     ██║  ██║█████╗  ██╔██╗ ██║    ██║  ███╗███████║██╔████╔██║█████╗      ██║██║██║
        ██║   ██║██║   ██║██║     ██║  ██║██╔══╝  ██║╚██╗██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ╚═╝╚═╝╚═╝
        ╚██████╔╝╚██████╔╝███████╗██████╔╝███████╗██║ ╚████║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ██╗██╗██╗
         ╚═════╝  ╚═════╝ ╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚═╝╚═╝╚═╝
                                                                                            """ + bcolors.ENDC)
    time.sleep(2)


def setup_game():
    """ get game info from the user """

    global dice_sides
    global best_of
    global check

    os.system("clear")
    text()

    print(bcolors.OKGREEN + "\n\t\t\t\t\t\t\t            a game by Philip & Luke" + bcolors.ENDC)
    speak(words['welcome'])

    try:
        time.sleep(1)
        speak(words['sides'])
        sides = int(input("How many sides does the game dice have? : "))

        if sides > 0:
            dice_sides = sides
            game_dice_sides = "'{0} sided dice.'".format(str(dice_sides))
            speak(game_dice_sides)

        else:
            speak(words['unfortunate'])
            setup_game()

    except ValueError:
        print("Not a valid choice! Try again...")
        speak(words['invalid'])
        setup_game()

    except KeyboardInterrupt:
        speak("'goodbye'")
        sys.exit(0)

    try:
        speak(words['best_of'])
        matches = int(input("Best out of how many games? : "))

        if matches > 0:
            best_of = matches
            check = matches
            game_matches = "'Best of {}'".format(str(best_of))
            speak(game_matches)
        else:
            speak(words['unfortunate'])
            setup_game()

    except ValueError:
        print("Please enter a number, not letters....")
        speak(words['stupid'])
        time.sleep(1)
        setup_game()

    except KeyboardInterrupt:
        speak("'goodbye'")
        sys.exit(0)


def roll_dice():
    """ rolls the game dice """
    return random.randint(1, dice_sides)


def game_stats():
    """ print game title and stats """

    p1 = bcolors.RED + 'PLAYER 1 WINS' + bcolors.ENDC
    p2 = bcolors.OKBLUE + 'PLAYER 2 WINS' + bcolors.ENDC
    os.system("clear")
    text()
    print("\n====================================================================================================")
    print("MATCHES REMAINING: {}".format(best_of))
    print("\n      ||            {}: {}                ||                   {}: {}       ||".format(p1, p1score, p2, p2score))

    print("====================================================================================================\n")


def speak(game_words):
    os.system("espeak " + game_words)


words = {

        "play_again" : "'would you like to play again?'",
        "best_of"    : "'best out of how many games?'",
        "sides"      : "'How many sides does the game dice have?'",
        "invalid"    : "'not a valid choice. try again.'",
        "unfortunate": "'Unfortunately, that will not work'",
        "match_draw" : "'the match was a draw, it will go to golden game'",
        "welcome"    : "'Welcome, to the Dice Game. Player with the highest roll, will win.'",
        "stupid"     : "'that is really stupid.'",
        "roll"       : "'roll the dice'",
        "p2win_game" : "'player two wins'",
        "p1win_game" : "'player one wins'",
        "p1win_match": "'Congratulations player one. You won the match,'",
        "p2win_match": "'Congratulations player two. You won the match,'",
        "game_over"  : "'game,over.'",
        "draw"       : "'the game was a tie, play the last game again.'"

        }


# numbers on dice
numbers = {

    1: """
                             11  
                            111  
                             11  
                             11  
                            1111 """,

    2: """
                             22  
                            2  2 
                              2  
                             2   
                            2222 """,

    3: """
                            333  
                               3 
                             33  
                               3 
                            333  """,

    4: """
                            4  4 
                            4  4 
                            4444 
                               4 
                               4 """,

    5: """
                            5555 
                            5    
                            555  
                               5 
                            555  """,

    6: """
                              6   
                             6    
                            6666  
                            6   6 
                             666  """,

    7: """
                            77777 
                               7  
                              7   
                              7   
                              7   """,

    8: """
                             888  
                            8   8 
                             888  
                            8   8 
                             888  """,

    9: """
                             9999 
                            9   9 
                             9999 
                               9  
                              9   """,

    0: """
                             000  
                            0  00 
                            0 0 0 
                            00  0 
                             000  """

    }


def print_nums(roll):
    """ prints the dice roll numbers side by side """
    lines = [numbers[i].splitlines() for i in roll]
    for l in zip(*lines):
        print(*l, sep='')


def play_again():
    """ check if user would like to play again """
    global p1score
    global p2score

    print("\nWould you like to play again?  y/n")
    speak(words['play_again'])

    try:

        play = str(input(":: "))

        if play in 'Yes' or play in 'yes':
            speak("'of course you would'")
            time.sleep(1)
            setup_game()
            p1score = 0
            p2score = 0
            main()

        elif play in 'No' or play in 'no':
            speak("'goodbye, thankyou for playing, dice game.'")
            time.sleep(1)
            print("\n\n")

        else:
            speak("'that does not make sense'")
            time.sleep(1)
            play_again()

    except KeyboardInterrupt:
        speak("'goodbye'")
        sys.exit(0)


def main():

    global best_of
    global p1score
    global p2score

    # if there are matches left to play
    while best_of != 0:

        game_stats()

        # p1 has a turn
        speak("'player 1.'")
        speak(words['roll'])
        try:
            input("PLAYER 1 - Push enter to roll the dice...")

        except KeyboardInterrupt:
            speak("'goodbye'")
            sys.exit(0)

        p1roll = roll_dice()

        # return fancy numbers for the dice roll
        print(bcolors.RED)
        print_nums([int(i) for i in str(p1roll)])
        print(bcolors.ENDC)
        # computer tells us what the roll was
        proll = "'{}'".format(str(p1roll))
        speak(proll)
        time.sleep(2)

        game_stats()

        # p2 has a turn
        speak("'player 2.'")
        speak(words['roll'])

        try:
            input("PLAYER 2 - Push enter to roll the dice...")

        except KeyboardInterrupt:
            speak("'goodbye'")
            sys.exit(0)

        p2roll = roll_dice()

        # return the rolled number
        print(bcolors.OKBLUE)
        print_nums([int(i) for i in str(p2roll)])
        print(bcolors.ENDC)
        proll = "'{}'".format(str(p2roll))
        speak(proll)
        time.sleep(2)

        # we check who won
        # if player 1 beats player 2...
        if p1roll > p2roll:

            # add one to P1's score
            p1score +=1

            # subtract from matches left
            best_of -=1
            print(bcolors.RED + "\t\t\t\t\t===================")
            print("\t\t\t\t\t== PLAYER 1 WINS ==")
            print("\t\t\t\t\t===================" + bcolors.ENDC)
            speak(words['p1win_game'])
            time.sleep(2)

            # we don't play the unnecessary games
            if p1score > check / 2:
                break

        elif p2roll > p1roll:
            p2score +=1
            best_of -=1
            print(bcolors.OKBLUE + "\t\t\t\t\t===================")
            print("\t\t\t\t\t== PLAYER 2 WINS ==")
            print("\t\t\t\t\t===================" + bcolors.ENDC)
            speak(words['p2win_game'])
            time.sleep(2)
            if p2score > check / 2:
                break

        else:
            # if the game is tied, we play again
            # there is no change to the scores
            print("IT'S A DRAW !!! REMATCH!")
            speak(words['draw'])
            time.sleep(2)

    os.system("clear")
    time.sleep(1)

    if p1score > p2score:
        game_over()
        text_p1win()
        speak(words['p1win_match'])
        play_again()

    elif p2score > p1score:
        game_over()
        text_p2win()
        speak(words['p2win_match'])
        play_again()

    else:
        # if the match is a draw, we
        # go to 'golden game'
        draw()
        best_of = 1
        main()


setup_game()
main()
