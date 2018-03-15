import sys 
sys.path.insert(0,"../")
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
import pickle
import joblib

def parse(data):
    filen = open(data, "r")
    top = list()
    pep = list()
    key =list()
    temp_key = ''
    temp_seq = ''
    
    for nr, line in enumerate(filen):
        if line.startswith(">") == True:
            keys = line[:-1]
            temp_key = keys
            
        elif nr %3 == 1:
                temp_seq = line[:-1]
                
        elif nr%3 ==2 and len(temp_seq)>0:
            topo = line[:-1]

            if len(topo) == len(temp_seq):
                key.append(temp_key)
                pep.append(temp_seq)
                top.append(topo)


    
    return top, pep, key

def training_pssm(key, top, wz):
    
    train_list= list()
    for name in key:
        pssm = './PSSM/' + name + '.fasta.pssm'
        parsed_pssm = np.genfromtxt(pssm, skip_header=3, skip_footer=5, usecols=range(22,42))
        train_list.append(parsed_pssm)

    return train_list
    
def parsing_pssm(train_list, wz):
    padd = wz // 2
    arrays = list()
    numbers = list()
    
    for number, element in enumerate(train_list):
        ln = len(element)
        needzeros = np.zeros((ln, wz, 20))
        decimals = element / 100
        pad_element = np.vstack([np.zeros((padd, 20)), decimals, np.zeros((padd, 20))])
        for aa in range(ln):
            needzeros[aa] = pad_element[aa:aa + wz]
            numbers.append(number)
        arrays.append(needzeros.reshape(ln, wz *20))
    
    return np.vstack(arrays)

def training_y(top, o):
    
    topnr = {"T":1,".":2,"t":3,"S":4}
    y_train = list()
    for elements in top:
        for letters in elements:
            y = topnr[letters]
            y_train.append(y)


    clf = svm.SVC(C=10, gamma=0.01)
    clf.fit(o, y_train)
    name_of_file = "pssm_model2.sav.xz"
    joblib.dump(clf, open(name_of_file, "wb"), compress=9)
      
        





if __name__ == '__main__': 
    top, pep, key = parse("datapsi.txt")
    train_list=training_pssm(key, top, 3)
    o = parsing_pssm(train_list,3)
    training_y(top, o)
