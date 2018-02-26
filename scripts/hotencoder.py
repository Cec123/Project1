#from numpy import argmax

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


#letter_to_number("kort.txt")
