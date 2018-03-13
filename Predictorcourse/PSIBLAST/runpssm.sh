cd ./fastafiles/
fore file in *.fasta
do

psiblast -query $file -evalue 0.001 -db /Users/ceciliafurugard/Desktop/uniprot_sprot.fasta -num_iterations 3 -out ../psi_out/$file -out_ascii_pssm ../pssm/$file.pssm -num_threads=8
done
