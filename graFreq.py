import os
import glob
from collections import defaultdict
import nltk
from nltk.corpus.reader import CHILDESCorpusReader
import pandas as pd



def scandirs(path, part_ofspeech, dependencies):
    corpus_root = nltk.data.find(path)
    for currentFile in glob.glob( os.path.join(path,  '*') ):
    	if os.path.isdir(currentFile):
    		print(currentFile)
    		s = sentence_cut(currentFile) # returns name of kid (directory)
    		s += '/.*.xml'
    		print(s)
    		manchester = CHILDESCorpusReader(corpus_root, s)
    		li = manchester.words(relation=True, speaker='MOT') #only the parents words
    		for i in li:
    			for k in i:
    				if(len(k) >= 3):
    					depen(k, dependencies)
    				partOfSpeech(k, part_ofspeech)
					

def sentence_cut(s):
	result = ''
	i = -1
	while(s[i] != '/'):
          result = s[i] + result
          i -= 1
	
	return result 

def depdency_cut(s):
	result = ''
	i = -1
	while(s[i] != '|'):
          result = s[i] + result
          i -= 1
	
	return result 

def partOfSpeech(k, part_ofspeech):
	if(part_ofspeech.has_key(k[1])):
		part_ofspeech[k[1]] += 1
	else:
		part_ofspeech[k[1]] = 1


def depen(k, dependencies):
	indiv_depen = depdency_cut(k[2])
	if(dependencies.has_key(indiv_depen)):
		dependencies[indiv_depen] += 1
	else: 
		dependencies[indiv_depen] = 1

			





def main():
	part_ofspeech = defaultdict(int)
	dependencies = defaultdict(int)
	CORPUS_PATH = "/Users/lilycaplan/school/spring2018/colag/childes/Manchester"
	scandirs(CORPUS_PATH, part_ofspeech, dependencies )
	
	df = pd.DataFrame.from_dict(dependencies, orient="index")
	df.to_csv("dependencies.csv")
	df = pd.read_csv("dependencies.csv", index_col=0)
	dependencies = df.to_dict("split")
	dependencies= dict(zip(dependencies["index"], dependencies["data"]))

	df1 = pd.DataFrame.from_dict(part_ofspeech, orient="index")
	df1.to_csv("partofspeech.csv")
	df1 = pd.read_csv("partofspeech.csv", index_col=0)
	part_ofspeech = df1.to_dict("split")
	part_ofspeech= dict(zip(part_ofspeech["index"], part_ofspeech["data"]))


    
if __name__ == "__main__":
    main()
