#!/usr/bin/Python

import subprocess


q = subprocess.Popen(['finger'], stdout = subprocess.PIPE)
output = q.communicate()[0]
users =[]
out = output.splitlines()
for i in range(1, len(out)):
	line = out[i].split()
	users.append(line[1])
	
user = users.sort()

user = {}
for i in  range(0 , len(users)):
	if user.get(users[i]):
		user[users[i]] +=1

	else :
		user[users[i]] = 1

for user, process in user.items():
	print (" \n %s has  %s session running" %(user, process))
