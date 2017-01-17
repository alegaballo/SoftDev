       -----------====== CHALLENGE ======-----------

Your first task is to write something similar to "sort -nr | head ",
which order the lines it reads from standard input according
to the first number it finds in each line.

The command also takes one parameter, which tells how many 
entries it needs to print. However, it always prints every 
line with the same rank.

So, if you run: 

> cat test.txt | python yoursolution 5

There are 55 cats
9 dogs
Only 7 hyppos
4 tigers of 5 meters each
I wish there were more than 4 monkeys
I can see 4 mosquitos
Dolphins? I count 4

Note that it prints more than 5 lines!! It prints the first five position:
In fact, 55 is first, 9 second, 7 third, then you have four lines with 4.
The next line (with 3) would be in eight position as it has seven before it.

         -----------====== SUBMISSION ======-----------

Submit your python file. 
It will be tested by running:
> cat file | python yoursolution N

