import joblib
import parse_pssm
import numpy as np

my_model = joblib.load("pssm_model2.sav.xz")

def parse_newinput(data, wz):
    train_list= list()

    pssm =data
    parsed_pssm = np.genfromtxt(pssm, skip_header=3, skip_footer=5, usecols=range(22,42))
    train_list.append(parsed_pssm)
    
    predicted= list()   
    x_vector= parse_pssm.parsing_pssm(train_list, wz)
    result = my_model.predict(x_vector)
    predicted.append(result)
    
    return predicted
    
def convertion(predicted):
    nr_top = {1:"T", 2:".", 3:"t", 4:"S"}
    topology_prediction =list()
    for element in predicted:
        
        for number in element:
            c = nr_top[number]
            topology_prediction.append(c)
    top_pred= ["".join(topology_prediction[0:len(topology_prediction)])]
    
    #print(top_pred)
    
        
    with open("result_pssm.txt", 'w') as f:
        for element in top_pred:
            f.write("Predicted topology for your pssm:"+"\n"+str(element))
            f.close()
    


if __name__ == '__main__':
    predicted=parse_newinput(">11SB_CUCMA.fasta.pssm",3)
    convertion(predicted)
