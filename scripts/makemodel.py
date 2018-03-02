import intodef
import numpy as np
from sklearn import svm
from sklearn import model_selection
import pickle

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
    encode = intodef.encode_aa()
    windows = intodef.sliding_windows(inputs)
    #print(len(windows))
 
    convert = intodef.convert_windows(windows, encode)
    #print(len(convert))
    #print(convert)
    
def training_model(file, file2):
    
    x = np.load(file,"r")

    print(x)
    
    
    y = np.load(file2)

    
    
    model = svm.SVC()
    

if __name__ == '__main__':
    a = parse_newinput("newinput.txt")
    encode_input(a)
    training_model("xvector.npz", "yvector.npz")
