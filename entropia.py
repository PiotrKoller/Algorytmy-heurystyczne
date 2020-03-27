import numpy as np
import random
import matplotlib.pyplot as plt

class entropy:
    def entropy(self,class_num,x,y,ent):
        self.class_num = int(class_num)
        self.values = [random.randrange(1,class_num+1) for i in range(1,int(x)*int(y)+1)]
        self.randvalues = np.array(self.values)
        ent = float(ent)
        self.entropy_list = []
        for i in np.unique(self.randvalues):
            self.entropy_list.append(-(np.count_nonzero(self.randvalues == i)/self.randvalues.size)*np.log2(np.count_nonzero(self.randvalues == i)/self.randvalues.size))
        entropia = sum(self.entropy_list)

        j = 0 
        k = 3
        l = 0
        m = 1

        while ent/entropia > 1.03 or ent/entropia < 0.97:
            if entropia > ent:
                for i in range(j,k):
                    self.values[i] = 1
                self.randvalues = np.array(self.values)
                self.entropy_list = []
                for i in np.unique(self.randvalues):
                    self.entropy_list.append(-(np.count_nonzero(self.randvalues == i)/self.randvalues.size)*np.log2(np.count_nonzero(self.randvalues == i)/self.randvalues.size))
                entropia = sum(self.entropy_list)
                self.entropy_list = []
                j += 3
                k += 3
                if j > len(self.randvalues) or k > len(self.randvalues):
                    break
            elif entropia < ent:
                for i in range(l,m):
                    self.values[i] = 2
                self.randvalues = np.array(self.values)
                self.entropy_list = []
                for i in np.unique(self.randvalues):
                    self.entropy_list.append(-(np.count_nonzero(self.randvalues == i)/self.randvalues.size)*np.log2(np.count_nonzero(self.randvalues == i)/self.randvalues.size))
                entropia = sum(self.entropy_list)
                self.entropy_list = []
                l += 1
                m += 1
                if entropia > ent:
                    break
            

        self.array = random.shuffle(self.randvalues)
        self.array = np.array(self.array)
        self.array = np.reshape(self.randvalues,(int(x),int(y)))
        plt.imshow(self.array)
        plt.title("Entropia: {}".format(round(entropia,3)))
        plt.show()
        return self.array