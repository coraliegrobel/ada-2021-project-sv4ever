import nltk, sys
import importlib


def formater_phrase(path_file):
	importlib.reload(sys)
	#sys.setdefaultencoding('utf-8')

	wnl = nltk.WordNetLemmatizer()
	with open("Data/Inputs/sentences.txt", "w", encoding="utf-8") as f:
    
	#out = open("Data/Inputs/sentences.txt", "w")
		fichier = open(path_file,"r",encoding="utf-8").readlines()
		for ligne in fichier:
			tokens = nltk.word_tokenize(ligne)

			tagged = nltk.pos_tag(tokens)
		
			lemmatisation = []
			for i in tagged:
				if i[1][0] == "J":
					lemmatisation.append(wnl.lemmatize(i[0], nltk.corpus.wordnet.ADJ))
				elif i[1][0] == "V":
					lemmatisation.append(wnl.lemmatize(i[0], nltk.corpus.wordnet.VERB))
				elif i[1][0] == "R":
					lemmatisation.append(wnl.lemmatize(i[0], nltk.corpus.wordnet.ADV))
				else:
					lemmatisation.append(wnl.lemmatize(i[0], nltk.corpus.wordnet.NOUN))
		
			if len(tokens) == len(tagged) and len(tokens) == len(lemmatisation):
				for i in range(len(tokens)):
					f.write(tokens[i]+"\t"+tagged[i][1]+"\t"+lemmatisation[i].lower()+"\n")
			f.write("\n")
			
	

