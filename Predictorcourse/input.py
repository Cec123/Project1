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
            keys_lista.append(line[1:-1])
            #print(keys_lista)
        else: 
            pep = line[:-1]
            data_pepseq.append(pep)
            #print(data_pepseq)
    
    return data_pepseq, keys_lista

#(Throughout the rest of the code: by having a temporary lists that I append
#to, and then append these in a later stage to the list of interest,
#I treat my sequences element by element instead of putting everything into one "line")

def divide_slidingwindows(data, wz):
    inputs = data
    pad = wz//2
    windowlist= list()
    
    for seq in inputs:
        pad = wz//2
        temp = list()
        for i in range(len(seq)):
            if i>pad and i< len(seq)-pad:
                #append each window to the list called window:
                temp.append(seq[i-pad:i+pad+1])
                
        #handle the start:
            elif i<= pad:
                the_window = seq[:i + pad +1]
                needzeros = wz - len(the_window)
                temp.append("0"*needzeros + the_window)               
        #handle the end:
            else:
                #print(i)
                the_window = seq[i-1:]
                #print(the_window)
                needzeros = wz - len(the_window)
                #print(needzeros)
                temp.append(the_window + "0"*needzeros)
        windowlist.append(temp)
    #print(len(windowlist))
    
    return windowlist

def convert_windows(inputs):
    listan =list()    
    for elements in inputs:
        #print(elements)
        temp2=list()
        for win in elements:
            #print(win)
            a=list()
            dictionary = predictor.encode_aa()
            for letters in win:
                b= dictionary[letters]
                a.extend(b)
                #print(a)
            temp2.append(a)
            #print(temp2)
        listan.append(temp2)           
    #print(len(listan))
        
    pred_list=list()
    for element in listan:
        x= np.array(element)
    #print(len(x))
        result = my_model.predict(x)
        #print(result)
        pred_list.append(result)

    numbers_to_topology = {1:"M", 2:"S"}
    topology_prediction = list()

    for arrays in pred_list:
        f =list()
        for numbers in arrays:
            c = numbers_to_topology[numbers]
            f.append(c)
        topology_prediction.append(f)
    return topology_prediction

def protein_prediction(keys, listan, pep):
    top= list()
    for element in listan:
        top.append("".join(element))
    
    with open("results.txt", 'w') as f:
        for items in range(len(keys)):
            f.write(keys[items] + "\n")
            f.write(pep[items] + "\n")
            f.write(top[items] + "\n")
        f.close()
         
    #li= list(zip(pep, top))
    #dictionary_prediction = dict(zip(keys, li))

    #print(li)
    #print(dictionary_prediction)
    #return dictionary_prediction

if __name__ == '__main__':
   n, m = parse_newinput(input("Type the name of your file that you want to predict secondary structure for: "))
   l = divide_slidingwindows(n, 17)
   o=convert_windows(l)
   protein_prediction(m, o, n)
   
   
