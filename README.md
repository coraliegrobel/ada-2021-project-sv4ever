# *Analysis of speech behaviours between genders*


## Abstract 

It is common knowledge that women’ speech contains more uncertainties (e.g., “We think this may be correct”) compared to men (e.g., “I know it is correct”). As a result, this project aims at comparing speech behaviours related to uncertainty between genders. For our data, we use _Quotebank_, an open corpus of more than 1 million quotations from 2015 to 2020, as well as the open-source information from wikidata to have access to the speakers' information. The classification of the quotes is done using an uncertainty detection classifier, based on the statistical analysis of multiple lexical and syntactic features. Specifically, we analyze differences in communicative acts in relation to gender within and between professional areas. Furthermore, we emphasise the roles of nationality, culture/tradition, and education in determining those differences. Finally, we also observe whether there is a possible change over time between 2015 and 2020.

Our results can be visualised, narrated as a data story, on the following website: https://assiaoua.github.io/blog/.

In order to run this project, one needs to download the directories and files from the following drive: https://drive.google.com/drive/folders/1UgvnLUFhs14NDcZYH6NuZx2f_YC5i06N?usp=sharing.


## Research questions 

We are interested in using this dataset to answer the following question: Do speech behaviours related to confidence and uncertainty vary between men and women?

To answer this question, we'll go through the following points:

- To what extent can we observe the differences in communicative acts in relation to gender within a professional area? Are there noticeable differences between those professional areas?

- What are the roles of nationality, culture/tradition (religion, ethnic groups), and education (whether the speaker obtained an academic degree) in determining those differences in speech between men and women? How are the lines drawn between the language we use and the environment around us?

- Has there been a possible change over time (from 2015 to 2020)?


## Additional datasets and tools
To complement the _Quotebank_ dataset, we use the open-source stored data on Wikidata, as well as a classifier.

#### Wikidata
It is an open-source dataset (https://www.wikidata.org/wiki/Wikidata:Main_Page). _Wikidata_ is used to retrieve information on the speakers.

#### Uncertainty Detection Classifier
To classify the quotes according to the uncertain lexical and syntactic features, we use the public uncertainty detection classifier from the paper "P. A. Jean, S. Harispe, S. Ranwez, P. Bellot, and J. Montmain, “Uncertainty detection in natural language: A probabilistic model” ACM Int. Conf. Proceeding Ser., vol. 13-15-June, no. June, 2016, doi: 10.1145/2912845.2912873". It is available for download at: https://github.c-om/pajean/uncertaintyDetection. As this was created on python2, we had to adapt it to run on python3.

The data from _Wikidata_ and the adapted classifier can be found on this public drive: https://drive.google.com/drive/folders/1UgvnLUFhs14NDcZYH6NuZx2f_YC5i06N. More instructions are provided within the notebook.


## Methods

1. #### Pre-processing of the data

We started by cleaning the data by removing rows containing missing values on mandatory features for our study, like the speaker's identity and gender. We also checked that there were no duplicate data (no duplicate quotes in _Quotebank_ and speaker id in _Wikidata_). Then, only the quotes where the speaker's probability was greater than 0.5 in _Quotebank_ were kept.
  
Then, we did some exploratory data analysis, at first on the distribution of genders and then on the language of the quotes. We observed a vast distribution of 31 genders. Still, to simplify our study, we only kept the `female` and `male` genders, the others representing less than 0.03% of the data. Concerning the language of the quotes, we found that some quotes are not in English. Only English quotes were kept.

2. #### Creation of our sub data frames

We now created two data frames: one for all professional fields and one containing speakers' background information.

In order to do that, we had to merge _Quotebank_ and _Wikidata_. We merged on the `label` for _Wikidata_ and `speaker` in _Quotebank_. As several `label` are often selected (speakers having the same name), we chose the speaker (`label`) having his/her `id` (in _Wikidata_) equal to the first speaker in `qids` (`qids`[0] in _Quotebank_).

To be able to avoid the bias of different backgrounds between males and females, we sub-divided our data into 4 professional fields: artists, scientists, economists, and politicians. To achieve the separation, we searched for the speaker’s occupation of each quote with the help of _Wikidata_, then hand-picked fields' professions and returned them in separate pickle files for each field.

Another dataframe with no condition on profession, containing background information on the speakers was created, then also saved as a pickle file.

3. #### Classification of the quotes

To be able to use the classifier, we first needed to create text files with only the quotes and their index. Then, we ran the classifier on these files and it returned the uncertainty quotes for each file. Instructions on how to run the classifier are present in the notebook.

4. #### Results

To start, as we have unbalanced data (most speakers are males), gender distributions are displayed for each condition. As our speakers are mostly males, for the following analysis, we had to normalize our uncertain speakers by the total number of speakers of each gender.

The first analysis consisted in looking at the gender distribution of uncertain speakers in each professional field (artists, scientists, economists, and politicians). 
 
To extend our research on the question of gender speech uncertainty, we then investigated how do culture and education shape the way men and women speak. We based this study on the `nationality`, `ethnic_group`, `religion` and `academic_degree` columns of the speaker. This allows each time to remove the bias of the cultural, educational and environmental influence and to compare the gender speech.

Finally, we investigated a possible change from 2015 to 2020, for each professional field, and for the more general data frame.

5. #### Statistical-analysis

Statistical analysis is performed using OLS (Ordinary Least Squares), a mathematical regression method.

6. #### Interpretation of results & Conclusion

We concluded on our observations and proposed further extensions on the project.

## Timeline 

#### Milestone 1

Each team member brainstormed about possible project ideas using the _Quotebank_ dataset.

#### Milestone 2

The project goal and research questions were chosen. The data was therefore cleaned accordingly to our research: we removed (1) speakers with missing identity and/or gender, (2) duplicate speakers, and (3) unlikely speakers. To answer our first research question, speakers are separated across professional fields (politicians, artists, scientists, and economists). Quotes are then classified as certain or uncertain using the classifier using 2 features. Finally, results are displayed in plots, allowing us to visualise the gender distribution of uncertain speakers across (1) professional fields, (2) speakers' background, and (3) 2015 and 2020.

Still, only the 2015 and 2020 datasets are loaded at this point.

#### Milestone 3

In this last part of the project, the main change was to perform the analysis (4. **Results**) on the entire dataset (2015 to 2020). The analysis of the differences in communicative acts in relation to gender within and between professional areas is now performed using a much greater dataset. The analysis of the speakers' environments' influence is also performed on this greater dataset. To finish, the possible change over time is analysed using the 6 yearly datasets (from 2015 to 2020).

Statistical analysis is performed using Ordinary Least Squares to evaluate the reliability of our findings.A conclusion and possible further extensions on the project are then stated.


## Organization with the team

All the members of the team worked on all project steps. Still, these are the main sections that each team member worked on:

- Clement Chaffard: 1., 5.
- Coralie Grobel: 1., 2., 3., 4.
- Fannie Kerff: 3., 4., 6., READ_ME
- Assia Ouanaya: 2., 4., Website

The numbers refer to the "Method" steps.
