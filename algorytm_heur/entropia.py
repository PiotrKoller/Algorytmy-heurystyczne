import numpy as np
import random
import matplotlib.pyplot as plt

class entropy:
    def entropy(self,class_num,x,y,ent): #metoda wykonująca algorytm heurystyczny
        self.class_num = int(class_num)   #zmienna zawierająca liczbę klas podaną przez użytkownika
        classes = list(range(1,class_num+1))
        q, r = divmod(int(x)*int(y), len(classes))
        self.values = q * classes + classes[:r] #wygenerowanie listy wartości o maksymalnej wartości entropii dla danej liczby klas
        self.randvalues = np.array(self.values) #zapisanie listy wartości do numpy array
        ent = float(ent) #zapisanie entropii podanej przez użytkownika do formatu float
        self.entropy_list = []
        for i in np.unique(self.randvalues):
            self.entropy_list.append(-(np.count_nonzero(self.randvalues == i)/self.randvalues.size)*np.log2(np.count_nonzero(self.randvalues == i)/self.randvalues.size))
        entropia = sum(self.entropy_list)  #obliczenie entropii ze wzrou

        j = 0 
        k = 1
        p = 2
        entropies = []

        while True:
            if entropia >= ent:
                for i in range(j,k+1):  #iterowanie po wyznaczonym przedziale
                    if i > len(self.values)-1:  #jeżeli iterator jest większy od długości listy przerwij
                        break
                    self.values[i] = 1  #zamieniaj napotkane wartości na 1 podczas iteracji
                self.randvalues = np.array(self.values)
                self.entropy_list = []
                for i in np.unique(self.randvalues):
                    self.entropy_list.append(-(np.count_nonzero(self.randvalues == i)/self.randvalues.size)*np.log2(np.count_nonzero(self.randvalues == i)/self.randvalues.size))
                entropia = sum(self.entropy_list)  #oblicz wartości entropii
                entropies.append(entropia) #dołącz do listy zawierającej wartości entropii
                print(entropia)
                div = int(round((entropia-ent)*len(self.values))/p)  #wyznacz przedział w którym dojdzie do zamianie wartości zanim ponownie zostanie obliczona entropia
                if div == 0: #zabezpieczenie przed sytuacją w której długość przedziału wyniesie 0
                    div = 1
                self.entropy_list = []  #wyczyszczenie obliczonej entropii
                j = k+1
                k = j+div
                p += 1  #wyznaczenie długości przedziału
                if abs(entropia-ent) == 0:  #przerwij jeżeli zostanie wyznaczona dokładna wartość entropii (głównie jeżeli użytkownik wpisze wartość 0)
                    break
            elif entropia < ent:
                self.values_test = self.values
                for i,value in enumerate(self.values_test): #iteruj po wartościach i tym razem zamień na 2 jeżeli trafi na 1
                    if self.values_test[i] == 1:
                        self.values_test[i] = 2
                    break  #przerwij po zamianie 
                self.randvalues_test = np.array(self.values_test)
                self.entropy_list = []
                for i in np.unique(self.randvalues_test):
                    self.entropy_list.append(-(np.count_nonzero(self.randvalues_test == i)/self.randvalues_test.size)*np.log2(np.count_nonzero(self.randvalues_test == i)/self.randvalues_test.size))
                entropia_test = sum(self.entropy_list) #oblicz testową entropię
                print(entropia_test)
                if abs(entropia_test-ent) < abs(entropies[-1]-ent):  #jeżeli różnica pomiędzy testową entropią a zadaną jest mniejsza niż entropią wyliczoną w poprzedniej pętli nadpisz jej wartość
                    self.randvalues = self.randvalues_test
                    entropia = entropia_test
                break #przerwij po wykonaniu
            
        self.array = random.shuffle(self.randvalues) #przetasuj wartości losowo
        self.array = np.array(self.array)
        self.array = np.reshape(self.randvalues,(int(x),int(y)))
        plt.imshow(self.array)
        plt.title("Entropia: {}".format(round(entropia,3)))
        plt.show()  #wyświetl plot z entropią

    def max_entropy(self,class_num,x,y): #metoda obliczająca maksymalną entropię dla pierwotnie wylosowanej listy (placeholder w GUI)
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