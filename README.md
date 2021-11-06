# Project Milestone 2 (P2)

## Abstract 

...

**150 words max**

**Quotebank**


## Research questions 

...
**Goals:
**show that you have a reasonable plan and ideas for methods you’re going to use, giving their essential mathematical details in the notebook.
**show that your plan for analysis and communication is reasonable and sound, potentially discussing alternatives to your choices that you considered but dropped.
**Rem: 
**Do several research questions in case one does not turn into something interesting between professions (gender fixed)/genders (profession fixed)/...


## Proposed additional datasets
To complement the Quotebank dataset, we use the open source stored data on Wikidata, as well as data to train a classifier on a public GitHub repository.
### Wikidata
...
### Uncertainty Detection Classifier
...
It is available for download at: https://github.c-om/pajean/uncertaintyDetection.

## Methods

```bash
0    Loading and merging of quotebank and wikidata
1    Exploratory Data Analysis (EDA)
2    Cleaning quotebank and wikidata
3    Creation of subdataframes per professions
4    Classification of quotes using the uncertainty detection classifier
5    Statistical Analysis 
6    Additional analysis
7    Interpretation of results
8    Conclusion
```


## Proposed timelize 

Upcoming steps in milestone 3:
- optimization of classsifier
- analyse differences between professions
- analyse a possible trend from 2015 to 2020
- analyse differences between countries


## Organization with the team

- Coralie Grobel: 0, 4
- Assia Ouanaya: 3 
- Clement Chaffard: 0, 1
- Fannie Kerff: 4


## Questions for Tas (optional)


---------------------------------------------------------------------------------------------------------------------------------------
Brouillon:

<object data="https://github.com/CS-433/ml-project-1-ccd_ml/blob/main/Machine_Learning_to_discover_Higgs_Boson.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://github.com/CS-433/ml-project-1-ccd_ml/blob/main/Machine_Learning_to_discover_Higgs_Boson.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://github.com/CS-433/ml-project-1-ccd_ml/blob/main/Machine_Learning_to_discover_Higgs_Boson.pdf">Download PDF</a>.</p>
    </embed>
</object>

[Github](https://github.com/CS-433/ml-project-1-ccd_ml.git)

1.You can download the code to run the models from the github repository 

Clone the repository:
```bash
git clone https://github.com/CS-433/ml-project-1-ccd_ml.git
```
2.Unzip the train.csv in the data directory. Once in the right directory, type the following line:

```bash
Unzip train.zip
```

3.Unzip the test.csv in the data directory. Once in the right directory, type the following line:

```bash
Unzip test.zip
```

To run the program, you have to open a terminal on jupyter notebook or an anaconda prompt on anaconda. You have to go in the project repository (in the folder scripts) and run the following command :
```bash
python run.py
```
