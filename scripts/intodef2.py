import numpy as np
from sklearn import svm
import pickle
from sklearn import model_selection
from itertools import islice

def parse_data(data):
    filen = open(data, "r")
    #print(filen)
    top = list()
    pep = list()
    keys =list()

    with open(data) as f:
        for line in islice(f,0,None,3):
            keys.append(line[1:-1])
    with open(data) as f:
        for line in islice(f,1,None,3):
            pep.append(line[1:-1])

    with open(data) as f:
        for line in islice(f,2,None,3):
            top.append(line[1:-1])

    print(top, keys)
    return top, pep


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

def sliding_windows(data):
    win_size = 15
    pad = win_size//2
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
    #print(len(windowlist))
                
    return windowlist


def convert_windows(data, dicti):
    training_list = []
    for elements in data:
        a = list()
        #print(elements)
        for letters in elements:
            b = dicti[letters]
    
            a.extend(b)
        
        training_list.append(a)

    #print(len(training_list))
    np.savez("xvector", training_list)
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
    np.savez("yvector", topology_prediction_nr)
    return topology_prediction_nr


def training_model(x, y):
    X= np.array(x)
    #print(X)
    Y= y
    #print(Y)       
    model = svm.SVC()
    model.fit(X, Y)
    
    result= model.predict(X)

    numbers_to_topology = {1:"M", 2:"S"}
    topology_prediction_letter = list()
    for numbers in result:
        c = numbers_to_topology[numbers]
        topology_prediction_letter.extend(c)

    #print("Predicted output:", topology_prediction_letter)
    filename = "model_predictor.sav"
    pickle.dump(model, open(filename, "wb"))

    return filename
#===============================================================================================
"""
def parse_newinput(inputs):
    filen = open(inputs, "r")
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
                    #print(len(temp_seq))
                    #print(temp_seq)
                    data_pepseq.append(temp_seq)
                    keys_lista.append(temp_key)

    return data_pepseq

def encode_input(inputs):
    dicti = encode_aa()
    windows = sliding_windows(inputs)
    #print(windows)
    convert = convert_windows(windows, dicti)
    #print(len(convert))
    #print(convert)
    
#def try_predicting(data):
    #loaded_model = pickle.load("model_predictor.sav","rb")

"""
if __name__ == '__main__':
   top, pep = parse_data("euk-signal.3line.txt")
   #print(parse_data("kort.txt")) 
   p = encode_aa()
   c = sliding_windows(pep)
   d = convert_windows(c,p)
   e = y_vector(top)
   training_model(d, e)
   #n = parse_newinput("newinput.txt")
   #m= encode_input(n)
   #try_predicting(m)

