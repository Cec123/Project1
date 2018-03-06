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
            temp_seq = line[:-1]
            data_pepseq.append(temp_seq)
            keys_lista.append(temp_key)
    return data_pepseq

def  go(data, wz):
    inputs = data
    dictionary = predictor.encode_aa()
    #print(dictionary)
    x = predictor.sliding_windows(inputs, dictionary, wz)
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
    

if __name__ == '__main__':
   n = parse_newinput("oneprot.txt")
   go(n, 27)
   
