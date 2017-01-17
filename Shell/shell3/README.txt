 -----------====== Assignment  ======--------------
 
The network administrator still needs your skills.
This time, he has a number of log files (one per machine)
that describe how packets are allowed to flow among the hosts.
For instance, 

> cat logs/10.0.3.77.log 
10.0.3.4
10.0.3.44

means that the firewall allows host 77 to connect to 4 and 44.

Your goal is to find all the hosts that are recursively
reachable from 10.0.3.2.

Based on the logs in this folder, the output should be
(the order is not relevant)

10.0.3.2
10.0.3.1
10.0.3.4
10.0.3.55
10.0.3.199
10.0.3.44
10.0.3.201
10.0.3.77
10.0.3.12
10.0.3.7

There are several ways to solve this assignment. Some
only require what we learned in class (no IF or function
definition). But feel free to solve as you like.

 -----------====== Submission  ======--------------

Submit a text file containing your solution.
The file can assume there is a log folder in the same directory.

$> bash yourfile



