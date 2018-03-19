# Project1
Bioinfo course
Cecilia FurugŒrd

In Project1 three predictors are created for distinguishing weather an amino acid, of a protein, is in the signalpeptide region or in the sequence of the mature protein. The predictors make four states predictions based on the secondary structures for signal peptides at the SignalP server; signal peptide amino acid (S), transmembrane amino acid experimentally determined (T), transmembrane not experimentally determined (t) and amino acid part of another secondary structure (.)

Enter Predictorcourse:
- predictor.py; \n
A 3-line file is parsed. The file used is biggerdata2.txt and contains protein ID (starting with">"), the peptidesequence for the proteins and the topology sequence for the proteins. The file biggerdata.txt has 212 eukaryotic proteins taken from euk-3line.txt, whereof 106 are non-signalpeptides and 106 are signalpeptides. (NOTE! sequence homology was not taking in account when making dataset, which makes the predictor biased towards a certain pattern and decreases its accuracy when predicting proteins that are evolutionary distant from the sequences in the dataset.)

Further, the amino acid are encoded into arrays of 20 numbers. encoded so that each amino acid had an identity code with the length of 20 numbers. The code consisted of zeros for all positions but one, which was set to Ò1Ó. The position for the Ò1Ó in the row of 20, was unique for each amino acid, giving rise of twenty unique codes with. Zeros and ones were used in order to avoid that some amino acids had a higher weight than others when presenting the sliding windows in encoded form, for the svm. Amino acid ÒBÓ was handled as having 50 % chance of being an aspartate or an asparagine and this was implemented by encoding ÒBÓ by splitting the Ò1Ó into two positions (the position for asparagine and aspartate) having the value of 0.5 each. The same strategy was used for encoding amino acid ÒZÓ, but with the value of 0.5 at the positions of glutamate and glutamine instead. The amino acid ÒXÓ was encoded as having the same possibility of being any amino acid, hence the value of 0.05 was set to each of the 20 positions in the code for ÒXÓ. Having the protein sequences in encoded, each sequence was the split into sliding windows with a window size of 19 amino acids. All encoded amino acids in their siding windows form was was arrayed into the same X-vector, used as x when straining the model.

When training, the predictor the first 40 amino acids of the proteins are used, in order to make the prediction less biased towards the mature protein sequences.

The y-vector was obtained from the topology sequence, parsed form the file biggerdata2.txt. Every topology type was encoded into a number of 1-4, giving rise of a four states predictor. These number was then put in an array and used as y when training the model.
Two predictor scripts are held, whereof predictor.py the model is trained using svm. Here was also the parameters (gamma and C) investigated using GridSearchCV. From GridSearchCV gamma was set to 0.01 and C to 10 and these were further used when training the final svm-based model (model_predictore.p), since they were seen to increase the models accuracy. 

- predictor2.py;
 All steps are the same but the model is trained using the random forest instead. This model was saved as model_predictore2.p.

- accuracy.py;
In order to find the best window size inspiration was taken from the paper "Identification of prokaryotic and eukaryotic signal peptides and prediction of their cleavage sites" by Von Heijne et al. (1997). Thereby, windowsizes of 5-39 residues were tested using crossvalidation of 3-fold ("accuracy.py" using biggerdata2.txt as input file). The accuracy of different windowsizes where then plotted, revealing that a windowsize of 19 aminoacids give rise of the highest accuracy. Therefore the windowsize was set to 19 aminoacids when training.
How the accuracy changes with the windowsize is also saved in several files; accresult.txt (accuracy and corresponding windowsize using svm and 3-foldcrossvalidation, found in Predictorcourse/bin), accresult5.txt (accuracy and corresponding windowsize using svm and 5-foldcrossvalidation).

- accuracy_forest.py;
The accuracy of the random forest based model is viewed in the same fashion as the first model. The results of the accuracies held for each window size is saved in the file accresult_randomforest.txt.

- inputs.py;
When using the trained model and trying to predict the secondary structure of proteins (done in "input.py"), 50 new sequences (sequences that were not included in the training set) are parsed (found in "oneprot.txt"). The dataset used only includes the name of the proteins and the peptide sequence for each protein (as a regular fasta file). The the dataset are divided in 50:50 ratio of signal peptide proteins and none signal peptide proteins. The output of the prediction is saved in the file results.txt. 

- inputs2.py;
The random forest model is used to predict new topologies. Also here the oneprot.txt is used and parsed in the same way as before. The output is now saved in results2.txt.

- Q3.py;
Here is the Q3-score of the prediction using the svm-model (model_predictore.p) calculated using the file results.txt (predicted topology) and y_true.txt (the true topology taken from biggerdata2.txt). Also, the MCC is calculated as well as a confusion matrix. All is saved in the file result_svm_tweaked_parameters.txt.

- Q3b.py;
Here the Q3-score is calculated for the model trained with random forest (model_predictore2.p). Files used for this are results2.txt and y_true.txt. Also here the MCC is calculated and a confusion matrix is computed. The output of Q3-score, MCC and the confusion matrix are saved in the file result_randomforest.txt. 

- psiblast.py;
Here is the data in file datapsi.txt divided into separate files consisting of the peptidesequens and corresponding protein ID. Each protein information is saved in PSIPLAST2/fastafiles. The file consists of 38 proteins, 19 of non-signal peptides and 19 that are signal peptides. (NOTE! sequence homology was not taking in account when making dataset, which makes the predictor biased towards a certain pattern and decreases its accuracy when predicting proteins that are evolutionary distant from the sequences in the dataset.)




Enter Predictorcourse/PSIBLAST2:
- runpssm.sh;
Bashscript that creates a pssm for all 39 files in fastafiles. These are then saved in the folder PSSM.

- parse_pssm.py;
Each pssm is parsed taking out column 22-42, since these are the part of the pssm that has the possibility score, in percentage, for each amino acid at a certain position. Also, the 5 rows in the footer and 3 rows of the header are excluded. Each score is divided with 100 in order to get the percentage in a decimal format. These are then converted into windows of 3, where each amino acid is encoded, but this time the encoding is based on the possibility scores parsed from the pssm:s. Then, these are put as x-vector. Further, the y-vector is established using the same number-encoding as when training the the svm with a none-evolutionary relationship taken in account. The model is trained with svm and is compressed and saved as pssm_model.sav.xz.

In this script the parameters C and gamma was also tested in the same intervals as before, using GridSearchCV. After testing, the parameters were set; C=10 and gamma=1, since this was giving rise of a higher accuracy of the model.


- accuracy_pssm.py;
In this script the accuracy of different window sizes were tested, using 5-fold cross validation. This was saved in the file accresult_pssm.txt and the graph where the accuracies was plotted against corresponding window sizes,  were printed when running the script.

- inputs_pssm; 
The pssm-model is used in this file, predicting the secondary structure of the protein 11SB_CUCMA (used file for input is >11SB_CUCMA.fasta.pssm). The peptide sequence is taken from biggerdata2.txt, and the pssm was created in the same stage as when creating the pssm:s for training the model, but the pssm for >11SB_CUCMA was then excluded when it came to the actual training of the model. The predicted output is saved in the file result_pssm.txt.

- Q3c.py;
The accuracy of the prediction using the pssm-model is calculated here using the predicted output i result_pssm.txt and the true topology obtained from biggerdata2.txt and saved in the file ytrue2_pssm.txt. Also a confusion matrix and MCC is computed. All outputs are saved in the file result_svm_model_pssm.txt. (NOTE! Both MCC and Q3 are only tested on one protein here).


More I would like to do with more time:
First I would like to do all the models over again, finding right parameters and windowsizes, with almost my whole dataset. I would still have equal amount of signal- versus none-signal peptides, in order to reduce bias, hence exclude a few sequences. I did try this once with the first svm model, but it did not finish after 24 hours.
 
Other factors having negative impact on my predictor are none-optimal parameters for the random forest model (could be tested with RandomizedSearchCV). In order to make a fair comparison with my  svm-models, this must be done. Also, the svm model based on the pssm:s only takes in one pssm. To make a reasonable comparison with my first svm model, I would have to take in 50 pssm:s here as well.

More, the training-data used is badly chosen, since they are strongly homologous. With more time, I would like to calculate the score of how certain my model is on the topology prediction for each amino acid, when predicting new data. The sequences that would be worst predicted and that my predictor is sure of being right, would I then include in my training-set, since this would imply that these sequences have information that is missing in my model. Doing this project over again I would also initiate the project with reducing my dataset by homology, since having sequences of high similarity makes my predictor biased to a certain protein pattern (the secondary structure is almost always conserved between closely related/homologous sequences) and it is also probably the reason to my pssm-based svm-model having the same accuracy for all window sizes.