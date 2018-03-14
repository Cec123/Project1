cd ./fastafiles/
for file in *.fasta
do

psiblast -query $file -evalue 0.001 -db ../swissprot.fasta -num_iterations 3 -out_ascii_pssm ../PSSM/$file.pssm -num_threads=8
done
