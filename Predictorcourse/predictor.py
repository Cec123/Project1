import numpy as np
from sklearn import svm
import pickle
from sklearn import model_selection
from itertools import islice
from sklearn.model_selection import cross_val_score

def parse_data(data):
    filen = open(data, "r")
    #print(filen)
    topology = list()
    pep = list()
    keys =list()
   
    temp_key = ''
    temp_seq = ''
    for nr, line in enumerate(filen):
        if line.startswith(">") == True:
            key = line[1:-1]
            temp_key = key
            #print(temp_key)
        elif nr %3 == 1:
                temp_seq = line[:-1]
                #print(temp_seq)

        
        elif nr%3 ==2 and len(temp_seq)>0:
            topo = line[:-1]
            #print(topo)
            if len(topo) == len(temp_seq):
                keys.append(temp_key)
                pep.append(temp_seq[:80])
                #print(data_pepseq)
                topology.append(topo[:80])
                
                
    #print(keys, topology)
    return topology, pep


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
                matris[i,j]= 1        
    

#take out each row, put each row in a dictionary later with its aa as key.
    for arrays in matris:       
        listakod.append(arrays)
    #print(listakod)
    bib1= dict(zip(key, listakod))
    bib1["0"] = np.zeros(20, dtype=int)
    bib1["X"] = 1/20*np.ones(20, dtype=int)
    
    d = bib1.get("D")
    n = bib1.get("N")
    c= ((d + n)/2)
    bib1["B"] = c

    e = bib1.get("E")
    q = bib1.get("Q")
    s = ((e+q))/2
    bib1["Z"] = s

    C= bib1.get("C")
    bib1["U"] = C

    #print(bib1)
    return bib1

def sliding_windows(data, dicti, wz):
    
    pad = wz//2
    windowlist= list()
    for seq in data:
        for i in range(len(seq)):
    #define interval in sequence were the first ans last letter in seq not included(pad=1):
            if i>pad and i< len(seq)-pad:
                #append each window to the list called window:
                windowlist.append(seq[i-pad:i+pad+1])
                
        #handle the start:
            elif i<= pad:
                the_window = seq[:i + pad +1]
                needzeros = wz - len(the_window)
                windowlist.append("0"*needzeros + the_window)               
        #handle the end:
            else:
                #print(i)
                the_window = seq[i-1:]
                #print(the_window)
                needzeros = wz - len(the_window)
                #print(needzeros)
                windowlist.append(the_window + "0"*needzeros)
    #print(len(windowlist))
                

    training_list = []
    for elements in windowlist:
        a = list()
        for letters in elements:
            b = dicti[letters]
    
            a.extend(b)
        
        training_list.append(a)

    #print(len(training_list))
    #np.savez("xvector", training_list)
    
    return training_list


def y_vector(data):
    topology_to_numbers = {"T":1,".":1,"t":1,"S":2}
    topology_prediction_nr = list()
    #print(data_topology)

    for elements in data:
        for letters in elements:
            #print(letters)
            y = topology_to_numbers[letters]
            topology_prediction_nr.append(y)
    #print(topology_prediction_nr)
    #np.savez("yvector", topology_prediction_nr)
    
    return topology_prediction_nr


def training_model(x, y):
    X= np.array(x)
    #print(X)
    Y= y
    #print(Y)       
    model = svm.SVC()
    model.fit(X, Y) 
   
    pickle.dump(model, open("model_predictore.p", "wb"))



if __name__ == '__main__':
   top, pep = parse_data("euk-3line.txt")
   dicti = encode_aa()
   s = sliding_windows(pep, dicti, 39)
   e = y_vector(top)
   training_model(s, e)


