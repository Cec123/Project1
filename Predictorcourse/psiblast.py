import inputs

def parse_psi(data):
    pep, keys = inputs.parse_newinput(data)
    name = keys
    seq = pep
   
    for items in range(len(name)):
        outfile = open("./PSIBLAST/fastafiles/" + name[items] + ".fasta", "w")
        outfile.write(name[items] + "\n")
        outfile.write(seq[items] + "\n")
        outfile.close()
    

if __name__ == '__main__':
    parse_psi("datapsi.txt")
