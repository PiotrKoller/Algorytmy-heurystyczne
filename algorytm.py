import numpy as np
import random
import matplotlib.pyplot as plt

values = [random.randrange(1,3) for i in range(1,65)]
randvalues = np.array(values)

print("Podaj wartość entropii (od 0 do 1): ")
ent = float(input())

entropy_list = []
for i in np.unique(randvalues):
    entropy_list.append(-(np.count_nonzero(randvalues == i)/randvalues.size)*np.log2(np.count_nonzero(randvalues == i)/randvalues.size))
entropia = sum(entropy_list)

j = 0 
k = 3
l = 0
m = 1


while ent/entropia > 1.03 or ent/entropia < 0.97:
    if entropia > ent:
        for i in range(j,k):
            values[i] = 1
        randvalues = np.array(values)
        entropy_list = []
        for i in np.unique(randvalues):
            entropy_list.append(-(np.count_nonzero(randvalues == i)/randvalues.size)*np.log2(np.count_nonzero(randvalues == i)/randvalues.size))
        entropia = sum(entropy_list)
        entropy_list = []
        j += 3
        k += 3
        if j > len(randvalues) or k > len(randvalues):
            break
    elif entropia < ent:
        for i in range(l,m):
            values[i] = 2
        randvalues = np.array(values)
        entropy_list = []
        for i in np.unique(randvalues):
            entropy_list.append(-(np.count_nonzero(randvalues == i)/randvalues.size)*np.log2(np.count_nonzero(randvalues == i)/randvalues.size))
        entropia = sum(entropy_list)
        entropy_list = []
        l += 1
        m += 1
        if entropia > ent:
            break

array = random.shuffle(randvalues)
array = np.array(array)
array = np.reshape(randvalues,(8,8))
plt.imshow(array)
plt.title("Entropia: {}".format(round(entropia,3)))
plt.show()