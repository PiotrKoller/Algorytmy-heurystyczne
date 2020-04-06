import numpy as np
import random
import matplotlib.pyplot as plt

class entropy:
    def entropy(self,class_num,x,y,ent):
        self.class_num = int(class_num)
        #self.values = [random.randrange(1,class_num+1) for i in range(1,int(x)*int(y)+1)]
        classes = list(range(1,class_num+1))
        q, r = divmod(int(x)*int(y), len(classes))
        self.values = q * classes + classes[:r]
        self.randvalues = np.array(self.values)
        ent = float(ent)
        self.entropy_list = []
        for i in np.unique(self.randvalues):
            self.entropy_list.append(-(np.count_nonzero(self.randvalues == i)/self.randvalues.size)*np.log2(np.count_nonzero(self.randvalues == i)/self.randvalues.size))
        entropia = sum(self.entropy_list)

        j = 0 
        k = 1
        p = 2
        entropies = []

        while True: #ent/entropia > 1.03 or ent/entropia < 0.97:
            if entropia >= ent:
                for i in range(j,k+1):
                    if i > len(self.values)-1:
                        break
                    self.values[i] = 1
                self.randvalues = np.array(self.values)
                self.entropy_list = []
                for i in np.unique(self.randvalues):
                    self.entropy_list.append(-(np.count_nonzero(self.randvalues == i)/self.randvalues.size)*np.log2(np.count_nonzero(self.randvalues == i)/self.randvalues.size))
                entropia = sum(self.entropy_list)
                entropies.append(entropia)
                print(entropia)
                div = int(round((entropia-ent)*len(self.values))/p)
                if div == 0:
                    div = 1
                self.entropy_list = []
                j = k+1
                k = j+div
                p += 1
                if entropia == 0:
                    break
            elif entropia < ent:
                self.values_test = self.values
                for i,value in enumerate(self.values_test):
                    if self.values_test[i] == 1:
                        self.values_test[i] = 2
                    break
                self.randvalues_test = np.array(self.values_test)
                self.entropy_list = []
                for i in np.unique(self.randvalues_test):
                    self.entropy_list.append(-(np.count_nonzero(self.randvalues_test == i)/self.randvalues_test.size)*np.log2(np.count_nonzero(self.randvalues_test == i)/self.randvalues_test.size))
                entropia_test = sum(self.entropy_list)
                print(entropia_test)
                if abs(entropia_test-ent) < abs(entropies[-1]-ent):
                    self.randvalues = self.randvalues_test
                    entropia = entropia_test
                break
            
        self.array = random.shuffle(self.randvalues)
        self.array = np.array(self.array)
        self.array = np.reshape(self.randvalues,(int(x),int(y)))
        plt.imshow(self.array)
        plt.title("Entropia: {}".format(round(entropia,3)))
        plt.show()

    def max_entropy(self,class_num,x,y):
        self.class_num = int(class_num)
        classes = list(range(1,class_num+1))
        q, r = divmod(int(x)*int(y), len(classes))
        self.values = q * classes + classes[:r]
        self.randvalues = np.array(self.values)
        self.entropy_list = []
        for i in np.unique(self.randvalues):
            self.entropy_list.append(-(np.count_nonzero(self.randvalues == i)/self.randvalues.size)*np.log2(np.count_nonzero(self.randvalues == i)/self.randvalues.size))
        entropia = sum(self.entropy_list)
        return entropia

if __name__ == "__main__":
    print("Uruchom plik entropy.py")