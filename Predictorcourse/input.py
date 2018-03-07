import predictor
import accuracy
import numpy as np
from sklearn import svm
import pickle
from sklearn import model_selection
from itertools import islice

#My model:
my_model = pickle.load(open("model_predictore.p", "rb"))

def parse_newinput(inputs):
    data_pepseq = list()
    keys_lista =list()
    
    with open(inputs, "r") as f:
        file= f.readlines()
        
    for nr, line in enumerate(file):
        if line.startswith(">")==True:
            keys_lista.append(line[:-1])
            #print(keys_lista)
        else: 
            pep = line[:-1]
            data_pepseq.append(pep)
            #print(data_pepseq)
        
    """
    filen = open(inputs, "r")
   
    temp_key = ''
    temp_seq = ''
    for nr, line in enumerate(filen):
        if line.startswith(">") == True:
            key = line[1:-1]
            temp_key = key
            #print(temp_key)
        elif nr %3 == 1:
            temp_seq = line[:-1]
            data_pepseq.append(temp_seq)
            keys_lista.append(temp_key)
    #print(data_pepseq)
    """
    
    return data_pepseq

def go(data, wz):
    inputs = data
    #print(inputs[0])
 
    pad = wz//2
    windowlist= list()
    for seq in inputs:
        a=list()
        for letters in seq:
            if letters != ",":
                for i in range(len(seq)):
            #define interval in sequence were the first ans last letter in seq not included(pad=1):
                    if i>pad and i< len(seq)-pad:
                        #append each window to the list called window:
                        a.extend(seq[i-pad:i+pad+1])

                #handle the start:
                    elif i<= pad:
                        the_window = seq[:i + pad +1]
                        needzeros = wz - len(the_window)
                        a.extend("0"*needzeros + the_window)               
                #handle the end:
                    else:
                        #print(i)
                        the_window = seq[i-1:]
                        #print(the_window)
                        needzeros = wz - len(the_window)
                        #print(needzeros)
                        a.extend(the_window + "0"*needzeros)
            else:
                
            
    print(len(windowlist))
                    
"""
    #print(inputs)
    for elements in inputs:
        dictionary = predictor.encode_aa()
        #print(dictionary)
        #x = predictor.sliding_windows(inputs, dictionary, wz)
        #print(len(x))
        result = my_model.predict(x)
        #print(result)

        numbers_to_topology = {1:"M", 2:"S"}
        topology_prediction = list()
        
        for numbers in result:
            c = numbers_to_topology[numbers]
            topology_prediction.extend(c)
        
        #print(topology_prediction_letter)
    print("Predicted output:", topology_prediction)
"""

if __name__ == '__main__':
   n = parse_newinput("oneprot.txt")
   go(n, 39)
   
