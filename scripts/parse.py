
def parse_data(data):
    filen = open(data, "r")
    data_topology = list()
    data_pepseq = list()
    keys_lista =list()
    bib_sec = dict()
    bib_aa = dict()
    for nr, line in enumerate(filen):
        if line.startswith(">") == True:
            key = line[1:-1]
            #keys_lista.append(line[1:-1])
            #print(keys_lista)
        elif nr %3 == 1:
            data_pepseq.append(line[:-1])
    #print(data_pepseq)
        elif nr%3 ==2:
            data_topology.append(line[:-1])

            for element in data_topology:
                bib_sec[key] = element
            for element in data_pepseq:
                bib_aa[key] = element
                    
                seq = bib_aa.values()
                    

    filen.close()
    return seq
#-------------------------------------------------------------------------------
from numpy import argmax

def letter_to_number(data):
    sequences = parse_data(data)
    #print(sequences)
    aminoacids = "ARNDCQEGHILKMFPSTWYV"
    onehot_encoded = list()
    
#make each character into a number, since enumerate is used it will be an array of numbers, starting at 0 -->n-1
    char_to_int = dict((c, i) for i, c in enumerate(aminoacids))
    int_to_char = dict((i, c) for i, c in enumerate(aminoacids))

#use the char_to_int for my sequences
    for element in sequences:
        encoded_seq = [char_to_int[char] for char in element]
        #print(encoded_seq)

#for each value that represents one aminoacid:
    for value in encoded_seq:
#create an array with the length of all aminoacids, were each position is set to zero
        aa = [0 for _ in range(len(aminoacids))]
        #print(aa)
#for each value(aminoacid) set the value to one 
        aa[value] = 1
#put each array of ones and zeros into the defined list
        onehot_encoded.append(aa)
    #print(onehot_encoded)
#-------------------------------------------------------------------------------
from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


def l_to_n(data):
    sequences = parse_data(data)
    

          
        

    
   
    

if __name__ == '__main__':
    parse_data("testa.txt")
    #letter_to_number("testa.txt")
    l_to_n("testa.txt")
    
    





