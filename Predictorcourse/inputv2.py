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
    return data_pepseq

def go(inputs, wz):
    output=list()
    for elements in inputs:
        dictionary = predictor.encode_aa()
        #print(dictionary)
        x = predictor.sliding_windows(inputs, dictionary, wz)
        #print(len(x))
        result = my_model.predict(x)
        #print(result)
    for letters in result:
        if len(letters) == len(inputs[0])
        
        numbers_to_topology = {1:"M", 2:"S"}
        topology_prediction = list()
        
        for numbers in result:
            c = numbers_to_topology[numbers]
            topology_prediction.extend(c)
        
        #print(topology_prediction_letter)
    print("Predicted output:", topology_prediction)
   
if __name__ == '__main__':
   n = parse_newinput("oneprot.txt")
   go(n, 39)
   
