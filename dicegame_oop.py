"""
dice game for linux
--- requires espeak
"""

import random
import os
import time
import sys


class bcolors:

    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    RED = '\033[0;31m'


class Text:

    title = bcolors.WARNING + """
                    ██████╗ ██╗ ██████╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗
                    ██╔══██╗██║██╔════╝██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
                    ██║  ██║██║██║     █████╗      ██║  ███╗███████║██╔████╔██║█████╗  
                    ██║  ██║██║██║     ██╔══╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
                    ██████╔╝██║╚██████╗███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
                    ╚═════╝ ╚═╝ ╚═════╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                     """ + bcolors.ENDC

    game_over = bcolors.WARNING + """
            
                     ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
                    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
                    ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
                    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
                    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
                     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                                            """ + bcolors.ENDC

    p1_win = bcolors.RED + """
    
    ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗      ██████╗ ███╗   ██╗███████╗    ██╗    ██╗██╗███╗   ██╗███████╗
    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ██╔═══██╗████╗  ██║██╔════╝    ██║    ██║██║████╗  ██║██╔════╝
    ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ██║   ██║██╔██╗ ██║█████╗      ██║ █╗ ██║██║██╔██╗ ██║███████╗
    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗    ██║   ██║██║╚██╗██║██╔══╝      ██║███╗██║██║██║╚██╗██║╚════██║
    ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║    ╚██████╔╝██║ ╚████║███████╗    ╚███╔███╔╝██║██║ ╚████║███████║
    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═══╝╚══════╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝ 
                                                                                                     """ + bcolors.ENDC

    p2_win = bcolors.OKBLUE + """
    
    ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗     ████████╗██╗    ██╗ ██████╗     ██╗    ██╗██╗███╗   ██╗███████╗
    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ╚══██╔══╝██║    ██║██╔═══██╗    ██║    ██║██║████╗  ██║██╔════╝
    ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝       ██║   ██║ █╗ ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║███████╗
    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗       ██║   ██║███╗██║██║   ██║    ██║███╗██║██║██║╚██╗██║╚════██║
    ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║       ██║   ╚███╔███╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║███████║
    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝       ╚═╝    ╚══╝╚══╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝ 
                                                                                                      """ + bcolors.ENDC

    computer_wins = bcolors.OKBLUE + """
    
       ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗   ██╗████████╗███████╗██████╗     ██╗    ██╗██╗███╗   ██╗███████╗
      ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔══██╗    ██║    ██║██║████╗  ██║██╔════╝
      ██║     ██║   ██║██╔████╔██║██████╔╝██║   ██║   ██║   █████╗  ██████╔╝    ██║ █╗ ██║██║██╔██╗ ██║███████╗
      ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║   ██║   ██║   ██╔══╝  ██╔══██╗    ██║███╗██║██║██║╚██╗██║╚════██║
      ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ╚██████╔╝   ██║   ███████╗██║  ██║    ╚███╔███╔╝██║██║ ╚████║███████║
       ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝      ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝
                                                                                            """ + bcolors.ENDC

    draw = bcolors.WARNING + """
                                ██████╗ ██████╗  █████╗ ██╗    ██╗    ██╗██╗
                                ██╔══██╗██╔══██╗██╔══██╗██║    ██║    ██║██║
                                ██║  ██║██████╔╝███████║██║ █╗ ██║    ██║██║
                                ██║  ██║██╔══██╗██╔══██║██║███╗██║    ╚═╝╚═╝
                                ██████╔╝██║  ██║██║  ██║╚███╔███╔╝    ██╗██╗
                                ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝     ╚═╝╚═╝                     
                                                          """ + bcolors.ENDC

    golden_game = bcolors.WARNING + """
    
         ██████╗  ██████╗ ██╗     ██████╗ ███████╗███╗   ██╗     ██████╗  █████╗ ███╗   ███╗███████╗    ██╗██╗██╗
        ██╔════╝ ██╔═══██╗██║     ██╔══██╗██╔════╝████╗  ██║    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██║██║██║
        ██║  ███╗██║   ██║██║     ██║  ██║█████╗  ██╔██╗ ██║    ██║  ███╗███████║██╔████╔██║█████╗      ██║██║██║
        ██║   ██║██║   ██║██║     ██║  ██║██╔══╝  ██║╚██╗██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ╚═╝╚═╝╚═╝
        ╚██████╔╝╚██████╔╝███████╗██████╔╝███████╗██║ ╚████║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ██╗██╗██╗
         ╚═════╝  ╚═════╝ ╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚═╝╚═╝╚═╝
                                                                                               """ + bcolors.ENDC



class Dice:
    """ class for the game dice """
    def __init__(self):
        self.sides = 0

    def roll(self):
        """ roll the game dice """
        return random.randint(1, self.sides)


class Player:
    """ a class for human players """
    def __init__(self, p_num):
        self.p_num = p_num
        self.wins = 0
        self.score = 0
        self.roll = 0


class Computer:
    """ a class for computer player """
    def __init__(self, p_num):
        self.p_num = p_num
        self.wins = 0
        self.score = 0
        self.roll = 0


class Game:
    """ a class for game functions """
    def __init__(self):
        self.best_of = 0
        self.match_count = 0
        self.players = []
        self.dice = None

    def title(self):
        os.system("clear")
        print(Text.title)

    def setup(self):
        """ set some game variables """
        self.set_players()
        self.set_dice()
        self.set_matches()

    def welcome(self):
        """ welcome the player and display title """
        self.title()
        print(bcolors.OKGREEN + "\n\t\t\t\t\t\t\t\t\t\ta game by Philip & Luke" + bcolors.ENDC)
        speak(words['welcome'])

    def set_players(self):
        """ set game PvP or PvC """
        self.title()
        players = []
        print(bcolors.OKBLUE + "\n                                   [!] PLEASE SELECT AN OPTION [!]")
        print("                                   ===============================")
        print("                                       [1] 2 PLAYER GAME")
        print("                                       [2] 1 PLAYER vs COMPUTER" + bcolors.ENDC)

        try:
            choice = str(input("                                   >>> "))
            if choice == '1':
                speak(words['pvp'])
                self.players.append(Player(1))
                self.players.append(Player(2))

            elif choice == '2':
                speak(words['pvc'])
                self.players.append(Player(1))
                self.players.append(Computer(2))
            else:
                speak(words['invalid'])
                self.set_players()

        except ValueError:
            speak(words['invalid'])
            self.set_players()

        except KeyboardInterrupt:
            speak(words['bye'])
            sys.exit(0)

    def set_dice(self):
        """ set the sides of the game dice """
        self.title()
        self.dice = Dice()
        speak(words['sides'])

        try:
            sides = int(input(bcolors.WARNING + "\n\t\t\t\tHow many sides does the game dice have? : " + bcolors.ENDC))
            if sides in range(2, 1001):
                self.dice.sides = sides
                dice_sides = "'{0} sided dice.'".format(str(self.dice.sides))
                speak(dice_sides)
            else:
                speak(words['unfortunate'])
                self.set_dice()

        except ValueError:
            speak(words['invalid'])
            self.set_dice()

        except KeyboardInterrupt:
            speak(words['bye'])
            sys.exit(0)

    def set_matches(self):
        """ setup the match """
        self.title()
        speak(words['best_of'])

        try:
            matches = int(input(bcolors.WARNING + "\n\t\t\t\t\tBest out of how many games? : " + bcolors.ENDC))

            if matches in range(1, 101):
                self.best_of = matches
                self.match_count = matches
                game_matches = "'Best of {}'".format(str(self.best_of))
                speak(game_matches)

            elif matches < 1:
                speak(words['unfortunate'])
                self.set_matches()
            else:
                print("\nSomething has gone wrong. Quitting....")
                sys.exit(0)

        except ValueError:
            speak(words['invalid'])
            self.set_matches()

        except KeyboardInterrupt:
            speak(words['bye'])
            sys.exit(0)

    def game_stats(self):
        """ print game title and stats """
        p1 = bcolors.RED + 'PLAYER 1 WINS' + bcolors.ENDC
        if type(self.players[1]) != Computer:

            p2 = bcolors.OKBLUE + 'PLAYER 2 WINS' + bcolors.ENDC
        else:
            p2 = bcolors.OKBLUE + 'COMPUTER WINS' + bcolors.ENDC

        print("\n====================================================================================================")
        print("MATCHES REMAINING: {}".format(self.match_count))
        print("\n      ||            {}: {}                ||                   {}: {}       ||".format(p1,
                                                                    self.players[0].score, p2, self.players[1].score))
        print("====================================================================================================\n")

    def print_nums(self, roll):
        """ prints the dice roll numbers side by side """
        lines = [dice_nums[i].splitlines() for i in roll]
        for l in zip(*lines):
            print(*l, sep='')

    def play(self, players):
        """ play dice game """
        self.title()
        self.game_stats()

        while self.match_count != 0:

            try:
                self.title()
                self.game_stats()
                self.player_roll(players[0].p_num)
                self.title()
                self.game_stats()
                self.player_roll(players[1].p_num)
                self.check_game_win()
                self.check_match_win()

            except KeyboardInterrupt:
                speak(words['bye'])

    def start(self):
        self.welcome()
        self.setup()
        self.play(self.players)

    def player_roll(self, p_num):
        """ player rolls the dice """
        self.title()
        self.game_stats()

        if p_num == 2 and type(self.players[1]) == Computer:
            print("Computer's turn..")
            time.sleep(1)
            self.players[1].roll = self.dice.roll()
            print(bcolors.OKBLUE)
            self.print_nums([int(i) for i in str(self.players[p_num - 1].roll)])
            print(bcolors.ENDC)
            proll = "'i rolled a {}'".format(str(self.players[p_num - 1].roll))
            speak(proll)
            time.sleep(2)

        else:

            speak("'player {}, roll the dice,'".format(p_num))

            try:
                input("PLAYER {} - Push enter to roll the dice...".format(str(p_num)))

            except KeyboardInterrupt:
                speak("'goodbye'")
                sys.exit(0)

            # for player 1
            if p_num == 1:
                self.players[0].roll = self.dice.roll()
                print(bcolors.RED)
                self.print_nums([int(i) for i in str(self.players[p_num - 1].roll)])
                print(bcolors.ENDC)
                proll = "'{}'".format(str(self.players[p_num - 1].roll))
                speak(proll)

            elif p_num == 2:
                self.players[1].roll = self.dice.roll()
                print(bcolors.OKBLUE)
                self.print_nums([int(i) for i in str(self.players[p_num - 1].roll)])
                print(bcolors.ENDC)
                proll = "'{}'".format(str(self.players[p_num - 1].roll))
                speak(proll)
            else:
                print("Something went wrong. Quitting....")
                sys.exit(0)

            time.sleep(2)

    def check_match_win(self):
        """ check to see if someone has won the match """

        if self.players[0].score > self.best_of / 2:
            self.match_win(self.players[0].p_num)

        elif self.players[1].score > self.best_of / 2:
            self.match_win(self.players[1].p_num)

        elif self.players[0].score == self.players[1].score and self.match_count == 0:
            self.draw()

    def check_game_win(self):
        """ check to see which player won the -game-  """

        if type(self.players[1] == Computer) and self.players[1].roll > self.players[0].roll:
            self.players[1].score +=1
            self.match_count -= 1
            print(bcolors.OKBLUE + "\t\t\t\t\t===================")
            print("\t\t\t\t\t== COMPUTER WINS ==")
            print("\t\t\t\t\t===================" + bcolors.ENDC)
            speak(words['computer_win'])
            time.sleep(2)

        else:
            # if it's player 1
            if self.players[0].roll > self.players[1].roll:

                # add one to P1's score
                self.players[0].score += 1

                # subtract from matches left
                self.match_count -= 1
                print(bcolors.RED + "\t\t\t\t\t===================")
                print("\t\t\t\t\t== PLAYER 1 WINS ==")
                print("\t\t\t\t\t===================" + bcolors.ENDC)
                speak(words['p1win_game'])
                time.sleep(2)

            elif self.players[1].roll > self.players[0].roll:
                self.players[1].score += 1
                self.match_count -= 1
                print(bcolors.OKBLUE + "\t\t\t\t\t===================")
                print("\t\t\t\t\t== PLAYER 2 WINS ==")
                print("\t\t\t\t\t===================" + bcolors.ENDC)
                speak(words['p2win_game'])
                time.sleep(2)

            else:
                print(bcolors.OKGREEN + "\t\t\t\t\t===================")
                print("\t\t\t\t\t= DRAW! PLAY AGAIN =")
                print("\t\t\t\t\t===================" + bcolors.ENDC)
                speak(words['draw'])

    def match_win(self, p_num):
        """ a player has won the match """
        os.system("clear")
        self.game_over()

        if p_num == 2 and type(self.players[1] == Computer):
            print(Text.computer_wins)
            speak(words['c_match_win'])
            self.play_again()

        elif p_num == 1:
            print(Text.p1_win)
            speak(words['p1win_match'])
            self.play_again()

        elif p_num == 2:
            print(Text.p2_win)
            speak(words['p2win_match'])
            self.play_again()

    def draw(self):
        """ display DRAW text """
        os.system("clear")
        print(Text.draw)
        speak(words['match_draw'])
        os.system("clear")
        print(Text.golden_game)
        time.sleep(2)
        self.match_count = 1
        self.play(self.players)

    def game_over(self):
        print(Text.game_over)
        speak(words['game_over'])

    def reset(self):
        self.best_of = 0
        self.match_count = 0
        self.players = []
        self.dice = None

    def play_again(self):
        """ check if the user would like to play again """
        speak(words['play_again'])
        try:
            again = str(input("Would you like to play again?:: "))
            if again in 'Yes' or again in 'yes':
                speak(words['of_course'])
                self.reset()
                self.setup()
                self.play(self.players)

            elif again in 'No' or again in 'no':
                speak("'goodbye, thankyou for playing, dice game.'")
                print("quitting...")
                time.sleep(1)
                print("\n\n")
                sys.exit(0)
            else:
                print("Something went wrong. Quitting...")
                speak(['bye'])
                sys.exit(0)

        except KeyboardInterrupt:
            speak('bye')
            print("quitting...")
            sys.exit(0)

2
def speak(game_words):
    os.system("espeak " + game_words)


words = {

    "pvc"         : "'do you think you can beat me? i guess we'll find out.'",
    "c_match_win" : "'ha ha ha, i won the match'",
    "computer_win": "'i won that game,'",
    "pvp"         : "'2 player game,'",
    "bye"         : "'goodbye'",
    "of_course"   : "'of course you would,'",
    "play_again"  : "'would you like to play again?'",
    "best_of"     : "'best out of how many games?'",
    "sides"       : "'How many sides does the game dice have?'",
    "invalid"     : "'not a valid choice, try again.'",
    "unfortunate" : "'Unfortunately, that will not work'",
    "match_draw"  : "'the match was a draw, it will go to golden game'",
    "welcome"     : "'Welcome, to the Dice Game. Player with the highest roll, will win.'",
    "stupid"      : "'that is really stupid.'",
    "roll"        : "'roll the dice'",
    "p2win_game"  : "'player two wins'",
    "p1win_game"  : "'player one wins'",
    "p1win_match" : "'Congratulations player one. You won the match,'",
    "p2win_match" : "'Congratulations player two. You won the match,'",
    "game_over"   : "'game,over.'",
    "draw"        : "'the game was a tie, play the last game again.'"
}


dice_nums = {

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


if __name__ == '__main__':
    game = Game()
    game.start()
