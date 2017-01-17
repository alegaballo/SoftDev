import socket
import pickle
import re
import datetime
def hash_count(str):
    cnt=0
    for c in str:
        if c=='#':
            cnt+=1
    
    return cnt;
def decode(str):
    cnt=hash_count(str)
    if cnt==19:
        return '0'
    elif cnt==13:
        return '1'
    elif cnt==22:
        #5 or 2
        if str[42:49]=='#######':
            return '2'
        else:
            return '5'
    elif cnt==21:
        return '3'
    elif cnt==15:
        return '4'
    elif cnt ==14:
        return '7'
    elif cnt==23:
        #6 8 9
        if str[14:21]=='#      ':
            return '6'
        elif str[28:35]=='      #':
            return '9'
        else:
            return '8'


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost',9999))
print s.recv(300)
print s.recv(300)
s.sendall('VeryCoolUsername\n') 
print s.recv(300)
s.sendall('7d98bb41b35399f83a3f29167843f0d0\n')
print s.recv(300)
min=1
max=12000


while True:
	first=(min+max)/2
	s.sendall(str(first)+('\n'))
	ans=s.recv(300)
	if 'bigger' in ans:
		min=first
	elif 'smaller' in ans:
		max=first
	else:
		print ans
		break

msg=s.recv(512)
print msg
number=msg.split('\n')[:-2]
first=''
second=''
third=''
for line in number:

    first+=line[0:7]
    second+=line[16:23]
    third+=line[32:]
    if len(line[32:]) < 7 and len(line[32:]) > 0:
        third+=' '*(7-len(line[32:]))
final=decode(first)+decode(second)+decode(third)

s.sendall(final+'\n')
print s.recv(512)
qst= s.recv(512)
pickl=qst.split('\n')[1:-3]
serialized=''
for i in pickl:
    serialized+=i+'\n'
final=pickle.loads(serialized).microsecond
s.sendall(str(final)+'\n')
print s.recv(512)
qst=s.recv(512)
print qst
day=re.findall('\d\d\s\w\w\w\s\d\d', qst)[0]
print day
dt=str(datetime.datetime.strptime(day,'%d %b %y').strftime('%A'))
print dt

s.sendall(dt+'\n')
print s.recv(512)
#print s.recv(512)
