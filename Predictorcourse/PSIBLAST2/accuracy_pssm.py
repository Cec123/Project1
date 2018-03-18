import parse_pssm
import numpy as np
import matplotlib.pyplot as plt 
from sklearn import svm
import pickle
from sklearn import model_selection
from sklearn.model_selection import cross_val_score
import accuracy

def give_xy(data, wz):
    top, pep, key= parse_pssm.parse(data)
    x = parse_pssm.training_pssm(key, top)
    X = parse_pssm.parsing_pssm(x, wz)
    topnr = {"T":1,".":2,"t":3,"S":4}
    Y = list()
    for elements in top:
        for letters in elements:
            y = topnr[letters]
            Y.append(y)

           
    with open("accresult_pssm.txt", "w") as f:
        for wz in range(5,39,2):
            clf = svm.SVC()
            scores = cross_val_score(clf, X, Y, cv=5, verbose=True)
            score = np.average(scores)
            f.write("wz:" + str(wz) + "\n")
            f.write("score:" + str(score) + "\n")
        f.close()

def graph(data2):
    accuracy.curve(data2)

if __name__ == '__main__': 
    give_xy("datapsi.txt",3)
    graph("accresult_pssm.txt")
  
    
