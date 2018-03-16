# Project1
Bioinfo course
Cecilia Furugård

In Project1 a predictor is created for distinguishing weather an amino acid, of a protein, is in the signalpeptide region or in the sequence of the mature protein. The predictor is trained first using svm and second randomforest. All files mentioned further is found in the map "Predictorcourse".
- predictor.py; 
A 3line file parsed. The file used is biggerdata2.txt and contains protein ID (starting with">"), the peptidesequence for the proteins and the topology sequence for the proteins. The file biggerdata.txt has 212 eukaryotic proteins taken from euk-3line.txt, whereof 106 are non-signalpeptides and 106 are signalpeptides.
Further, the aminoacid sequences are encoded and split into windowsizes of 19 aminoacids.
When training, the predictor the first 40 amino acids of the proteins are used, in order to make the prediciton less biased towards the mature protein sequences. 

- accuracy.py;
In order to find the best window size insperation was taken from the paper "Identification of prokaryotic and eukaryotic signal peptides and prediction of their cleavage sites" by Von Heijne et al. (1997). Thereby windowsizes of 5-39 residues were tested using crossvalidation of 3-fold ("accuracy.py" using biggerdata2.txt as input file). The accuracy of different windowsizes where then plotted, revealing that a windowsize of 19 aminoacids give rize of the highest accuracy. Therefore the windowsize was set to 19 aminoacids when training.
How the accuracy changes with the windowsize is also saved in several files; accresult.txt (accuracy and corresponding windowsize using svm and 3-foldcrossvalidation, found in Predictorcourse/bin), accresult5.txt (accuracy and corresponding windowsize using svm and 5-foldcrossvalidation) and accresult_randomforest.txt (the randomforest is used as metod with 5-fold crossvalidation). 

- inputs.py;
When using the trained model and trying to predict the secondary structure of proteins (done in "input.py"), 10 new sequences (sequences that were not included in the training set) were used (found in "oneprot.txt"). This set only includes the name of the proteins and the peptide sequence for each protein. The five first protein in the set are signal peptide proteins and the five last are not. The output of the prediction is saved in the file results.txt.

-Q3.py;
Here is the Q3 score of the prediction calculated using the file results.txt (predicted topology) and ytrue.txt (the true topology taken from biggerdata2.txt). When executing the function it gives the ratio of ration of correct predicted topology in procent.

-psiblast.py;
Here is the data in file biggerdata2.txt divided into separate files consisting of the peptidesequens and corresponding protein ID. Each protein information is saved in PSIPLAST2/fastafiles.
Enter PSIBLAST2:
- runpssm.sh;
Bashscript that creates a pssm for all the files in fastafiles. These are then saved in the folder PSSM.
- parse_pssm.py;
Each pssm is parsed taking out ...... These are then converted into windows of 3, where each aminoacid also is being encoded based on the possibility scores parsed from the pssm:s.  These are then put as x-vector. Further the y-vector is established using the same number-encoding as before.


More I would like to do with more time:
- Try other parameters (gamma; a high gamma tells the model not be influenced by datapoints that are far away in the periphery,C parameter: a high value of the C parameters makes the model less forgiving of making missclassifications of datapoints but...).
- Make the predictor distinguish between different aminoacids not only in the manner of belonging to the peptide seq or not, but also if the aa is a part of the transmembrane region or not (distingush between the T/t and "." in the secondary structure sequence). 
- Create a confusion matrix with sklearn. Since I get a very high accuracy, the accuracy seem not to give a fair picture of how well my model perform (according to the input.py were I try to predict it predictions is crap). Doing a confusion matrix I think could view this better.
