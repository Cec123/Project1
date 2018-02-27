
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
            keys_lista.append(line[1:-1])
            #print(keys_lista)
        elif nr %3 == 1:
            data_pepseq.append(line[:-1])
            #print(data_pepseq)
        elif nr%3 ==2:
            data_topology.append(line[:-1])
            #print(data_topology)
    
#-------------------------------------------------------------------------------
#Encode aminoacids to numbers:
    import numpy as np

    aminoacids = "ARNDCQEGHILKMFPSTWYV"
    aminoacids1 = "ARNDCQEGHILKMFPSTWYV"
    key =list(aminoacids)
    #print(key)
    
#encoded aminoacids in matrix
    matris = np.zeros((len(aminoacids), len(aminoacids1)), dtype=int)
    for i in range(len(aminoacids)):
        for j in range(len(aminoacids1)):
            if aminoacids[i] == aminoacids1[j]:
                matris[i,j]=1        
    
    listakod =list()
    
#take out each row, put each row in a dictionary later with its aa as key.
    for arrays in matris:       
        listakod.append(arrays)
    #print(listakod)
    bib1= dict(zip(key, listakod))
    bib1["0"] = np.zeros(20, dtype=int)
    #print(bib1)
#---------------------------------------------------------------------------------------
#create sliding window
    win_size = 3
    pad = win_size//2

  #  seq = data_pepseq[0]
    training_list = []
    #print(data_pepseq)
    for seq in data_pepseq:

        # print(seq)
        windowlist= list()

        for i in range(len(seq)):
    #define interval in sequence were the first ans last letter in seq not included(pad=1):
            if i>pad and i< len(seq)-pad:
                #print(i)
                #append each window to the list called window:
                windowlist.append(seq[i-pad:i+pad+1])
        #print(window)
                
        #handle the start:
            elif i<= pad:
                the_window = seq[:i + pad +1]
                #print(the_window)
                needzeros = win_size - len(the_window)
                #print(needzeros)
                windowlist.append("0"*needzeros + the_window)
                #print(window)
                
        #handle the end:
            else:
                #print(i)
                the_window = seq[i-1:]
                #print(the_window)
                needzeros = win_size - len(the_window)
                #print(needzeros)
                windowlist.append(the_window + "0"*needzeros)
                #print(windowlist)
#--------------------------------------------------------------------------------
    #connvert my windows to the codes of 1s and 0s.

        for elements in windowlist:
            #print(elements)
            a = list()
            for letters in elements:
                b = bib1[letters]
                a.extend(b)
            #print(a) 
            training_list.append(a)

    #print(training_list)
#------------------------------------------------------------------------------------
# Create the y vector:
    
    topology_to_numbers = {".":1,"t":1,"S":2}
    topology_prediction_nr = list()
    #print(data_topology)

    for elements in data_topology:
        for letters in elements:
            #print(letters)
            y = topology_to_numbers[letters]
            topology_prediction_nr.append(y)
    print(topology_prediction_nr)
#-----------------------------------------------------------------------
#training
    from sklearn import svm
    X= np.array(training_list)
    #print(X)
    Y= topology_prediction_nr
    #print(Y)       
    clf = svm.SVC()
    
    clf.fit(X, Y)
    result= clf.predict(X)
    numbers_to_topology = {1:"M", 2:"S"}
    topology_prediction_letter = list()

    for numbers in result:
        c = numbers_to_topology[numbers]
        topology_prediction_letter.append(c)

    print(topology_prediction_letter)

#---------------------------------------------------------------------
            


if __name__ == '__main__':
    parse_data("short.txt")
    
    
    
    
    





