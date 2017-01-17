import re
import sys

if len(sys.argv) != 2:
    print('correct usage: python <script.py> <n>')
else:
    n = int(sys.argv[1])
    head = {}
    for line in sys.stdin:
        stripped = line.rstrip()
        if len(stripped) != 0:
            key = int(re.findall('\d+', stripped)[0])
            if key in head.keys():
                head[key].append(stripped)
            else:
                head[key] = [stripped]
    for k in (sorted(head, reverse=True)):
        for l in head[k]:
            print l
            n -= 1
        if n <= 0:
            break

