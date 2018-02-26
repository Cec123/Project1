
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
    
    #print(sequences)
                    

    filen.close()
    return seq
#-------------------------------------------------------------------------------
def sliding_window(data):
    import numpy as np
    filen = open(data, "r")
    #print(filen)

    aminoacids = "ARNDCQEGHILKMFPSTWYV"
    aminoacids1 = "ARNDCQEGHILKMFPSTWYV"
    key =list(aminoacids)
    #print(key)
    
#encoded aminoacids in matrix
    matris = np.zeros((len(aminoacids), len(aminoacids1)))
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
#---------------------------------

#create sliding window

    win_size = 3
    pad = win_size//2
    seq = "ASQRHIL"
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
#---------------------------------------------------------------
#connvert my windowns to the codes of 1s and 0s.
        #print(bib1)
        map_windows = list()

        for elements in windowlist:
            a = list()
            for letters in elements:
                b = bib1[letters]
                a.append(b)
            a = [letters for elements in a for letters in elements]
            map_windows.append(a)
            print(map_windows)
        #print(len(map_windows))
        
        

        
        
 
            
            
            


if __name__ == '__main__':
    #parse_data("testa.txt")
    sliding_window("kort.txt")
    
    
    
    





