import predictor
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.ensemble import RandomForestClassifier
import pickle
from sklearn import model_selection
from sklearn.model_selection import cross_val_score

def all_in_one(data, wz):
    parsing = predictor.parse_data(data)
    dictionary = predictor.encode_aa()
    x = predictor.sliding_windows(parsing[1], dictionary, wz)
    y = predictor.y_vector(parsing[0])
    
    return x, y

def accuracy(data):
    with open("accresult_forest.txt", "w") as f:
        for wz in range(5,39,2):
            clf = RandomForestClassifier()
            X, Y = all_in_one(data, wz)
            scores = cross_val_score(clf, X, Y, cv=5, verbose=True)
            score = np.average(scores)
            f.write("wz:" + str(wz) + "\n")
            f.write("score:" + str(score) + "\n")
        f.close() 

def curve(data):
    windows =list()
    cross=list()
    with open(data, "r") as f:
        for nr, line in enumerate(f):
            linjer = line[:-1]
            if line.startswith("wz"):
                linefix=linjer.split(":")
                value = linefix[1]
                windows.append(float(value))
            elif line.startswith("score"):
                linefix=linjer.split(":")
                value =linefix[1]
                cross.append(float(value))
    
    xdata= np.array(windows)
    ydata= np.array(cross)
        
                
    plt.scatter(xdata,ydata, alpha=0.5, s=200)
    plt.ylabel("Accuracy")
    plt.xlabel("Windowsize")             
    plt.show()
    
       
    



if __name__ == '__main__':
    x, y = all_in_one("biggerdata2.txt", 5)
    accuracy("biggerdata2.txt")
    curve("accresult_forest.txt")

