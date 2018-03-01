import numpy as np
from sklearn import svm

def parse_data(data):
    filen = open(data, "r")
    data_topology = list()
    data_pepseq = list()
    keys_lista =list()
   
    temp_key = ''
    temp_seq = ''
    for nr, line in enumerate(filen):
        if line.startswith(">") == True:
            key = line[1:-1]
            temp_key = key
            #print(temp_key)
        elif nr %3 == 1:
            if "Z" not in line and "B" not in line and "X" not in line:
                    temp_seq = line[:-1]
                    #print(temp_seq)
            else:
                temp_seq = ''
            #print(temp_seq)
        elif nr%3 ==2 and len(temp_seq)>0:
            topo = line[:-1]
            #print(topo)
            keys_lista.append(temp_key)
    
            data_pepseq.append(temp_seq)
            #print(data_pepseq)
            data_topology.append(topo)
    #print(data_topology)
    #print(keys_lista)
    return data_topology, data_pepseq

def encode_aa():
    aminoacids = "ARNDCQEGHILKMFPSTWYV"
    key =list(aminoacids)
    #print(key)
    listakod =list()
    
#encoded aminoacids in matrix
    matris = np.zeros((len(aminoacids), len(aminoacids)), dtype=int)
    for i in range(len(aminoacids)):
        for j in range(len(aminoacids)):
            if aminoacids[i] == aminoacids[j]:
                matris[i,j]=1        
    
    
    
#take out each row, put each row in a dictionary later with its aa as key.
    for arrays in matris:       
        listakod.append(arrays)
    #print(listakod)
    bib1= dict(zip(key, listakod))
    bib1["0"] = np.zeros(20, dtype=int)
    #print(bib1)
    return bib1

def sliding_windows(data, dicti):
    win_size = 3
    pad = win_size//2
    training_list = []
    
    for seq in data:
        windowlist= list()
        for i in range(len(seq)):
    #define interval in sequence were the first ans last letter in seq not included(pad=1):
            if i>pad and i< len(seq)-pad:
                #append each window to the list called window:
                windowlist.append(seq[i-pad:i+pad+1])
                
        #handle the start:
            elif i<= pad:
                the_window = seq[:i + pad +1]
                needzeros = win_size - len(the_window)
                windowlist.append("0"*needzeros + the_window)               
        #handle the end:
            else:
                #print(i)
                the_window = seq[i-1:]
                #print(the_window)
                needzeros = win_size - len(the_window)
                #print(needzeros)
                windowlist.append(the_window + "0"*needzeros)
                #print(windowlist)

        for elements in windowlist:
            a = list()
            for letters in elements:
                b = dicti[letters]
                a.extend(b)
            training_list.append(a)

    #print(len(training_list))
    return training_list
    
def y_vector(data):
    
    topology_to_numbers = {".":1,"t":1,"S":2}
    topology_prediction_nr = list()
    #print(data_topology)

    for elements in data:
        for letters in elements:
            #print(letters)
            y = topology_to_numbers[letters]
            topology_prediction_nr.append(y)
    #print(topology_prediction_nr)
    return topology_prediction_nr

def training(x, y):
    X= np.array(x)
    #print(X)
    Y= y
    #print(Y)       
    clf = svm.SVC()
    
    clf.fit(X, Y)
    result= clf.predict(X)
    numbers_to_topology = {1:"M", 2:"S"}
    topology_prediction_letter = list()

    for numbers in result:
        c = numbers_to_topology[numbers]
        topology_prediction_letter.extend(c)

    #print(topology_prediction_letter)


    
    

if __name__ == '__main__':
   a, b = parse_data("kort.txt")
   p = encode_aa()
   c = sliding_windows(b,p)
   d = y_vector(a)
   training(c, d)

