       -----------====== CHALLENGE ======-----------

Your task it to write a python program to provide directions
to a little mole that moves by digging tunnels underground.

The program receives as input the name of a file containing
the underground map. 
For instance, the file "underground.map" contains:

###########O###
###########O##E
#####OOO#######
###############
#######OOO#####
####OOOOOOO####
S##############
###############

Where # represents the ground, S represents the starting point of 
the mole, E represents the destination the more has to reach, 
and O represents a big rock.
(the map is seen from the "side", i.e., the sky is on top and the center
of the earth is at the bottom)

The mole is free to move wherever it wants, but cannot cut
though rocks, and neither it can dig a tunnel *under* a rock
(because it would fall and kill the poor animal).
To be clear, under a rock means the character just under the "O"

Your program has to print the sequences of step to move the
mole from the start (S) to the end (E).
Four steps are available:
 U to move up
 D to move down
 L to move left
 R to move right

For example, given the previous map, the program can print something like:
RRRUUUUURRRRRRDDRRRRUUR

       -----------====== SUBMISSION ======-----------

Try your program by executing it with "underground.map" as
parameter and make sure you only print the list of moves as output


