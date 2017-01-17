 -----------====== Assignment  ======--------------
 
The network administrator gave you a log file containing all the connections
logged over the network on a certain day. As you are investigating an incident,
you want to know the list of the country towards which there was a connection
open at the time the problem occurred (unix timestamp 1364803829) from any
host in the 172.30.1/24 network. 

You can resolv an IP to a country by running: geoiplookup <ip>

For instance, if you run your code on the log snippet you find
in this folder, the output should be:

      6  US, United States
      3  IP Address not found
      1  TW, Taiwan
      1  MY, Malaysia
      1  FR, France
      1  ES, Spain
      1  DK, Denmark
      1  CA, Canada

 -----------====== Submission  ======--------------

Submit a text file containing the commands in your solution.
Your file will be tested running:

$> cat log_file | bash yourfile



