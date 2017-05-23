n = 10
arr = [64630,11735,14216,99233,14470,4978,73429,38120,51135,67060]

def mean(x):
	return sum(x)/len(x)

def median(x):
	mid = len(x) / 2
	if len(x) % 2 == 0:
		return mean(x[mid-1:mid+1])
	else:
		return x[mid-1]

def mode(x):
    counter, value = 0, 0
    for index, i in enumerate(set(x)):
        current = x.count(i)
        if counter < current:
            value, counter = i, current
        elif counter == current and value > i:
            value, counter = i, current
    #print counter
    return value
	
def std(x):
	u = mean(x)
	return (sum([(i-u)**2 for i in x])/len(x))**0.5

def confidence(x, a=1.96):
	u = mean(x)
	s = std(x)
	n = len(x)
	return u - a*s/(n)**0.5, u + a*s/(n)**0.5
	
arr = sorted([float(x) for x in arr])
print arr
print("%.1f" % mean(arr))
print("%.1f" % median(arr))
print(int(mode(arr)))
print("%.1f" % std(arr))
print("%.1f %.1f" % confidence(arr))
