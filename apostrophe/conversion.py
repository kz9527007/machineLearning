import json

fid = open('source.csv')
noun = []
verb = []
for line in fid:
	temp = line.split(',')
	temp[1] = temp[1].replace('\n','')
	if temp[1] == 'n' or temp[1] == 'a':
		noun.append(temp[0][3::])
	elif temp[1] == 'v':
		verb.append(temp[0][3::])
output1 = open('noun.txt','wb')
output1.write(str(noun))

output2 = open('verb.txt','wb')
output2.write(str(verb))