# Project1
Bioinfo course
Cecilia Furugård

In Project1 a predictor for distinguish weather an amino acid is a in of the signalpeptide region or in the sequence of the mature protein. The predictor is trained using using svm.

In order to find the best window size insperation was taken from the paper "Identification of prokaryotic and eukaryotic signal peptides and prediction of their cleavage sites" by Von Heijne et al. (1997). Thereby windowsizes of 5-39 residues were tested using crossvalidation of 3-fold ("accuracy.py"). This showed that the windowsize increased together with increased windowsize, hence the maximal accuracy was found for windowsize of 39 with an accuracy of ~95%. In order to look were/if the accuracy were peeking at some windowsize, the same biggerdata2.txt was used for crossvalidation of windowsizes of 5-80 and this showed a peek at a windowsize of 65 aminoacids, with an accuracy of ~97,6%.

The predictor is trained on eukaryotic signalproteins only, with a dataset of 100 proteins. When training the predictor the first 80 amino acids of the proteins are used, in order to make the prediciton less biased towards the mature protein sequences. Only the proteins that had the same lenght in their peptidesequence and topologysequence were used when training and testing the model. When training the model, the same number of sequences are of signal peptide charachters as of none signal peptide (negative examples), in order to balance the data. The file used when training is here called "biggerdata2.txt". When training a windowsize of 65 was used.

When using the trained model and trying to predict the secondary structure of proteins (done in "input.py"), 10 new sequences (sequences that were not included in the training set) were used (fount in "oneprot.txt"). This set only includes the name of the proteins and the peptide sequence for each protein. The five first protein in the set are signal peptide proteins and the five last are not. The output of the prediction is a dictionary wereof the key is the name of the protein that is being investigated and the values consist of first the peptidesequence, second the prediction of the secondary structure. 



More I would like to do with more time:
- Use five fold cross validation.
- Try other parameters (gamma; a high gamma tells the model not be influenced by datapoints that are far away in the periphery,C parameter: a high value of the C parameters makes the model less forgiving of making missclassifications of datapoints but...).
- Make the predictor distinguish between different aminoacids not only in the manner of belonging to the peptide seq or not, but also if the aa is a part of the transmembrane region or not (distingush between the T/t and "." in the secondary structure sequence). 
- Try the random forest method (could be done next week).
- Create a confusion matrix with sklearn. Since I get a very high accuracy, the accuracy seem not to give a fair picture of how well my model perform (according to the input.py were I try to predict it predictions is crap). Doing a confusion matrix I think could view this better.
