def q3(file1, file2):
    pre = list()
    ytrue = list()
    with open(file1, "r") as f:
        for nr, line in enumerate(f):
            if nr%3 ==2:
                pre.append(line[:-1])
    #print(pre)
    with open(file2, "r") as f:
        for nr, line in enumerate(f):
            if nr%3 ==2:
                ytrue.append(line[:-1])
    #print(res)
    ytrue1 = ["".join(ytrue[0:len(ytrue)])]
    pre1 = ["".join(pre[0:len(pre)])]
    #print(ytrue1, pre1)
    count =list()
    for nr1, letter1 in enumerate(ytrue[0]):
        for nr2, letters2 in enumerate(pre1[0]):
            if nr1 == nr2 and letter1 == letters2:
                count.append("1")
    Q3= (len(count)/len(ytrue1[0]))

    print(Q3)
    #print(len(count))
    #print((len(ytrue1[0])))

    return Q3
            
        
if __name__ == '__main__':
    q3("results.txt", "y_true.txt")
