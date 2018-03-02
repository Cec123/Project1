from itertools import islice
top= list()
pep= list()
keys=list()

with open("short.txt") as f:
    for line in islice(f,0,None,3):
        keys.append(line[1:-1])


with open("short.txt") as f:
    for line in islice(f,1,None,3):
            pep.append(line[1:-1])

with open("short.txt") as f:
    for line in islice(f,2,None,3):
        top.append(line[1:-1])


    
print(pep, top, keys)
    
        
              
