import numpy as np

def preprocessing(t):
	remove_list = ['what','which','why','where','are','was','were','they','these','those','that','this','their','his','her','have','had','under','over',':','-',',','how','when']
	for i in remove_list:
		t = t.replace(i,'')
		
	remove_list = [' of ',' in ',' by ',' on ',' a ',' to ',' and ',' i ',' is ',' the ']
	for i in remove_list:
		t = t.replace(i,' ')
	return t

def similiarity(t,q,a):
	best, score = [], 0
	print 'question', q
	for candidate in t:
		n = 0
		for word in candidate:
			if word in q:
				n += 1
		print n, candidate
		if n > score:
			best = [candidate]
			score = n
		elif n == score:
			best.append(candidate)
			
	answer, score = '', 0
	for option in a:
		print 'option', option
		for candidate in best:
			n = 0
			for word in candidate:
				if word in option:
					n += 1
			print n, candidate
			if n > score:
				answer = option
				n = score
	print answer
	a = raw_input('a')
	return answer

def removeNonAscii(s): return "".join(filter(lambda x: ord(x)<128, s))
	
if __name__ == '__main__':
	#text = raw_input()
	text = removeNonAscii("Zebras are several species of African equids (horse family) united by their distinctive black and white stripes. Their stripes come in different patterns, unique to each individual. They are generally social animals that live in small harems to large herds. Unlike their closest relatives, horses and donkeys, zebras have never been truly domesticated. There are three species of zebras: the plains zebra, the Grvy's zebra and the mountain zebra. The plains zebra and the mountain zebra belong to the subgenus Hippotigris, but Grvy's zebra is the sole species of subgenus Dolichohippus. The latter resembles an ass, to which it is closely related, while the former two are more horse-like. All three belong to the genus Equus, along with other living equids. The unique stripes of zebras make them one of the animals most familiar to people. They occur in a variety of habitats, such as grasslands, savannas, woodlands, thorny scrublands, mountains, and coastal hills. However, various anthropogenic factors have had a severe impact on zebra populations, in particular hunting for skins and habitat destruction. Grvy's zebra and the mountain zebra are endangered. While plains zebras are much more plentiful, one subspecies, the quagga, became extinct in the late 19th century though there is currently a plan, called the Quagga Project, that aims to breed zebras that are phenotypically similar to the quagga in a process called breeding back.")
	q = 'Which Zebras are endangered? What is the aim of the Quagga Project? Which animals are some of their closest relatives? Which are the three species of zebras? Which subgenus do the plains zebra and the mountain zebra belong to?'
	answer = "subgenus Hippotigris;the plains zebra, the Grvy's zebra and the mountain zebra;horses and donkeys;aims to breed zebras that are phenotypically similar to the quagga;Grvy's zebra and the mountain zebra"
	
	#text = removeNonAscii(text)
	text = preprocessing(text.lower())
	q = preprocessing(q.lower())
	answer = preprocessing(answer.lower())
	
	q = q.split('?')
	#print q
	answer = answer.split(';')
	
	t = text.split('.')
	t_list = []
	for line in t:
		t_list.append(list(np.unique(line.split())))
		
	for i in xrange(5):
		question = q[i].strip()
		print question
		print similiarity(t_list,question,answer)