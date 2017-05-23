import numpy as np

physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

x = np.vstack([physics, np.ones(len(physics))]).T
y = np.array(history)

m,c = np.linalg.lstsq(x,y)[0]
print m,c

print 10*m+c