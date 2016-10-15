"""

Title: Project 1

Abstract: Text Based Game

Name: Akoni Morrison, Garred Murphy,

Date: 10/5/2016

"""



import random

import time

import cmd

from room import get_room

import textwrap

class Game(cmd.Cmd):

    def __init__(self):

        cmd.Cmd.__init__(self)



        self.loc = get_room(1)

        self.look()



    def move(self,dir):

        newroom = self.loc._neighbors(dir)

        if newroom is None:

            print("you can't go that way")

        else:

            self.loc = get_room(newroom)

            self.look()

            if (newroom == 11) or (newroom == 7) or (newroom == 15):

                print("Congrats, you win!")

                time.sleep(5)

                exit()

            if (newroom == 16) or (newroom == 17) or (newroom == 18) or (newroom == 19) or (newroom == 20) or (newroom == 21) or (newroom == 22) or (newroom == 23) or (newroom == 24):

                print("You suffer a horrible death")
                print("Game Over")

                time.sleep(5)

                exit()


    def look(self):

        print(self.loc.name)

        print("")

        for line in textwrap.wrap(self.loc.description, 72):

           print(line)



    

            

    def do_n(self,args):

        """Go North"""

        self.move('n')



    def do_s(self,args):

        """Go South"""

        self.move('s')



    def do_e(self,args):

        """Go East"""

        self.move('e')

    def do_w(self,args):

        """Go West"""

        self.move('w')

   

    def do_up(self,args):

        """Go up"""

        self.move('up')



    def do_down(self,args):

        """Go down"""

        self.move('down')



    def do_quit(self,args):

        """Leaves the game"""

        print("Thank you for playin")

        return True



if __name__ == "__main__":
	print("")
	print("Site 19 is a massive prizon and research facility where supernatural opjects and being are contained and studied.")
	print("Site is now under attack by the agents of a rival organization, and several of the most dangerous prizoners are escaping.")	
	print("Can you get to a safe place before the monsters or the enemy kills you?")
	print("")	
	print("Type 'help' for a list of commands.")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	g = Game()
	g.cmdloop()