import predictor
import numpy as np
import matplotlib.pyplot as plt 
from sklearn import svm
import pickle
from sklearn import model_selection
from sklearn.model_selection import cross_val_score

def all_in_one(data, wz):
    parsing = predictor.parse_data(data)
    #print(parsing[1])
    dictionary = predictor.encode_aa()
    #print(dictionary)
    x = predictor.sliding_windows(parsing[1], dictionary, wz)
    #print(len(sliding))
    y = predictor.y_vector(parsing[0])
    #print(y)
    
    return x, y

def accuracy(data):
    with open("accresult5.txt", "w") as f:
        for wz in range(5,80,4):
            clf = svm.SVC()
            X, Y = all_in_one(data, wz)
            scores = cross_val_score(clf, X, Y, cv=5, verbose=True)
            score = np.average(scores)
            print(wz, score)
            f.write("wz:" + str(wz) + "\n")
            f.write("score:" + str(score) + "\n")
        f.close()
        



if __name__ == '__main__':
    x, y = all_in_one("biggerdata2.txt", 5)
    accuracy("biggerset.txt")

