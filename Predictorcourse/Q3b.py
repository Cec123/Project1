from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import numpy as np
import predictor

def q3(file1, file2):
    pre = list()
    ytrue = list()
    with open(file1, "r") as f:
        for nr, line in enumerate(f):
            if nr%3 ==2:
                linefix= line.strip("\n")
                pre.append(linefix)

    with open(file2, "r") as f:
        for nr, line in enumerate(f):
            if nr%3 ==2:
                linefix= line.strip("\n")
                ytrue.append(linefix)

    ytrue1 = ["".join(ytrue[0:len(ytrue)])]
    pre1 = ["".join(pre[0:len(pre)])]
    
    count =list()
    for letter1 in enumerate(ytrue1[0]):
        for letters2 in enumerate(pre1[0]):
            if letter1 == letters2:
                count.append("1")
    Q3= ((len(count)/len(ytrue1[0]))*100)


    return Q3, pre1, ytrue1

def confusionm(Q3, pre1, ytrue1):
    predicted=list()
    for letters in pre1[0]:
        a= predictor.y_vector(letters)
        predicted.extend(a)
        
    true=list()
    for letters in ytrue1[0]:
        b= predictor.y_vector(letters)
        true.extend(b)

    confusionmatrix= confusion_matrix(true,predicted, labels = [1,2,3,4])
    mcc = matthews_corrcoef(true,predicted)
    MCC = (mcc*100)
    with open("result_randomforest.txt", "w") as f:
        f.write("Q3-score:" + str(Q3) +"%" + "\n")
        f.write("MCC:" + str(MCC) +"%" + "\n")
        f.write("Confusionmatrix(x=true,y=predicted, 1-4):"+"\n" + str(confusionmatrix))
        f.close()


        
if __name__ == '__main__':
    a,b,c=q3("results2.txt", "y_true.txt")
    confusionm(a,b,c)
