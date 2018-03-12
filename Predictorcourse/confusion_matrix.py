import predictor
from itertools import islice
from sklearn.metrics import confusion_matrix

def confusionmatrix(true, pred):
    sann= list()
    predict= list()
    with open(true, "r") as f:
        for line in islice(f,2, None,3):
            sann.append(line[:-1])
    with open(pred, "r") as f:
        for line in islice(f,2,None,3):
            predict.append(line[:-1])
    #print(sann)
    #sann_nr= predictor.y_vector(sann)
    #print(sann_nr)
    #predict_nr= predictor.y_vector(predict)
    #print(predict_nr)
    
    b=list()
    for elements in sann:
        a=list()
        for letters in elements:
            a.extend(letters)
        b.append(a)
    print(len(a))
    
    c=list()
    for elements in predict:
        d=list()
        for letters in elements:
            d.extend(letters)
        c.append(d)
    print(len(d))
    #print(confusion_matrix(b, c, labels= ["S", "T","t","."]))        
        
            
        



if __name__ == '__main__':
    confusionmatrix("y_true.txt", "results.txt")
