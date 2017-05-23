import random

def parse(x):
	output = {}
	for item in x.split(' '):
		temp = item.split(",")
		output[int(temp[0])] = int(temp[1])
	return output

def diceRoll(p):
	pro = random.random()
	if pro <= p[0]:
		return 1
	elif pro <= sum(p[0:2]):
		return 2
	elif pro <= sum(p[0:3]):
		return 3
	elif pro <= sum(p[0:4]):
		return 4
	elif pro <= sum(p[0:5]):
		return 5
	else:
		return 6
	
def snakeLadder(p,l,s,p_l,p_s):
	current, counter = 1, 0
	while current != 100:
		dice = diceRoll(p)
		next = current + dice
		if next in p_l:
			next = p_l[next]
		if next in p_s:
			next = p_s[next]
		
		if next > 100:
			next = current
		counter += 1
		current = next
	return counter
	
def mean(x):
	return sum(x) / len(x)
	
def monteCarlo(p,l,s,p_l,p_s,n):
	counter = [0]*n
	for i in xrange(n):
		counter[i] = snakeLadder(p,l,s,p_l,p_s)
	print counter
	return mean(counter)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in xrange(t):
		p = map(float, raw_input().split(','))
		l,s = map(int, raw_input().split(','))
		p_l = parse(raw_input())
		p_s = parse(raw_input())
		
		n = 5000
		print monteCarlo(p,l,s,p_l,p_s,n)
'''
if __name__ == '__main__':
	p = [0.32,0.32,0.12,0.04,0.07,0.13]
	l,s = 3,7
	p_l = parse('32,62 42,68 12,98')
	p_s = parse('95,13 97,25 93,37 79,27 75,19 49,47 67,17')
	n = 5000
	print monteCarlo(p,l,s,p_l,p_s,n)