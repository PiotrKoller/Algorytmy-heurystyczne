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
        k = 1
        l = 0
        m = 1
        p = 2

        while j < len(self.randvalues) or k < (len(self.randvalues)-1):
            if entropia > ent:
                for i in range(j,k+1):
                    self.values[i] = 1
                self.randvalues = np.array(self.values)
                self.entropy_list = []
                for i in np.unique(self.randvalues):
                    self.entropy_list.append(-(np.count_nonzero(self.randvalues == i)/self.randvalues.size)*np.log2(np.count_nonzero(self.randvalues == i)/self.randvalues.size))
                entropia = sum(self.entropy_list)
                div = int(round((entropia-ent)/p*len(self.values)))
                if div == 0:
                    div = 1
                self.entropy_list = []
                j = k+1
                k = j+div
                p += 1
                if entropia < ent:
                    break 
            elif entropia <= ent:
                """
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
                """
                break
            

        self.array = random.shuffle(self.randvalues)
        self.array = np.array(self.array)
        self.array = np.reshape(self.randvalues,(int(x),int(y)))
        plt.imshow(self.array)
        plt.title("Entropia: {}".format(round(entropia,3)))
        plt.show()
