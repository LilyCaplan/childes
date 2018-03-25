import os
import glob
from collections import defaultdict
import nltk
from nltk.corpus.reader import CHILDESCorpusReader

# the path to the xml corpus on your disk




def scandirs(path, d):

	corpus_root = nltk.data.find(path)
	for currentFile in glob.glob( os.path.join(path,  '*') ):
		if os.path.isdir(currentFile):
			print(currentFile)
			s = sentence_cut(currentFile) # returns name of kid 
			s += '/.*.xml'
			manchester = CHILDESCorpusReader(corpus_root, s)
			li = manchester.words(speaker='MOT')
			for i in li:
				d[len(i)].append(i)
			








def sentence_cut(s):
	result = ''
	i = -1
	while(s[i] != '/'):
          result = s[i] + result
          i -= 1
	
	return result 




def main():
	d = defaultdict(list)
	CORPUS_PATH = "/Users/lilycaplan/school/spring2018/colag/childes/Manchester"
	scandirs(CORPUS_PATH, d )
	#print d[40]
	for i in d:
		print i,
		print ': ',
		print len(d[i])

if __name__ == "__main__":
    main()
