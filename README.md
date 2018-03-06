# Project1
Bioinfo course
In Project1 a predictor for distinguish weather an aa is a part of the signalpeptide sequence or in the sequence of the mature protein. The predictor is trained using using svm.
In order to find the best window size insperation was taken from the paper "Identification of prokaryotic and eukaryotic signal peptides and prediction of their cleavage sites" by Von Heijne et al. (1997). Thereby windowsizes of 5-39 residues were tested. From this the windowsize was set to 39 when training on the complete dataset, and this gave rise of an accuracy of .......
The predictor is trained on eukaryotic signalproteins only. When training the predictor the first 80 aa of the proteins are used, in order to reduce that the prediction being biased towards the mature protein sequences. Only the proteins that had the same lenght in their peptidesequence and topologysequence were used when training and testing the model. 

Some improvals from now(2018-03-06):
- Use five fold cross validation
- Try other parameters (gamma; a high gamma tells the model not be influenced by datapoints that are far away in the periphery,C parameter: a high value of the C parameters makes the model less forgiving of making missclassifications of datapoints but...).
- Make the predictor distinguish between different aminoacids not only in the manner of belonging to the peptide seq or not, but also if the aa is a part of the transmembrane region or not (distingush between the T/t and "." in the secondary structure sequence). 
- Add negative examples (non-signal peptides) in my training dataset.
- When predicting the secondary structure of a set of new input, present my new inputs to my model sequence by sequence and not in a continous stretch. This would be further used to get an output that gives a prediction of the secondary structure for each inputsequence separatly.
- Try other methods than svm.SVC, in order to find the modeltype that give rise of the best description of my data-pattern.
- Look at the confusion matrix for different windowsizes in order to determine the size with highest specificity and sensistivity.
