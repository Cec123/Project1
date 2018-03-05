import predictor
import numpy as np
from sklearn import svm
import pickle
from sklearn import model_selection
from itertools import islice
from sklearn.model_selection import cross_val_score


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

def encode_input(inputs):
    dicti = predictor.encode_aa()
    windows = predictor.sliding_windows(inputs)
    #print(windows)
    convert = predictor.convert_windows(windows, dicti)
    #print(len(convert))
    #print(convert)
    
    return convert
    
def trymodel(convert):
    print(convert)
    result2 = my_model.predict(convert)
    print(result2)
    
    return result2
    
def convert_output(trymodel):

    numbers_to_topology = {1:"M", 2:"S"}
    topology_prediction_letter = list()
    for numbers in trymodel:
        c = numbers_to_topology[numbers]
        topology_prediction_letter.extend(c)
    
    #print(topology_prediction_letter)
    print("Predicted output:", topology_prediction_letter)

if __name__ == '__main__':

   n = parse_newinput("oneprot.txt")
   m= encode_input(n)
   l=trymodel(m)
   convert_output(l)

