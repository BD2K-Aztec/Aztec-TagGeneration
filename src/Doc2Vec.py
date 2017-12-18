
from gensim.models import Doc2Vec
from gensim.models.keyedvectors import KeyedVectors
from gensim.models.doc2vec import TaggedDocument
from gensim.models.word2vec import LineSentence
from nltk import word_tokenize
import multiprocessing as mp
from nltk.corpus import stopwords

#Created by Jingyi Yuan
#Read in parsed paper, remove stopwords and build doc2Vec model based on the n_dimension

def tag_doc():
	
        f = open('parsed.txt','r')
        n_dimension = 50
        taggeddoc = []
        line = f.readline()
        index = 0
	tokens = []

	#get all the stop words
	stopWords = set(stopwords.words('english'))

        while line != '':
                line = line.replace('\n','')
		for word in line:
			if word not in stopWords:
				line.replace(word, '')
                line = ' '.join(word_tokenize(line.decode('utf8')))
                td = TaggedDocument(line.encode('utf8').strip().split(' '),['doc'+str(index)])
                taggeddoc.append(td)
                line = f.readline()
                index += 1
        f.close()
	#return taggeddoc
	model = Doc2Vec(taggeddoc, size=50, window=5, min_count=1, workers=20, alpha=0.025, min_alpha=0.025)
        model.save('doc2vec_model_50')
        print "model save"

#calculte the documents similarity
def calculate(doc):
	model = Doc2Vec.load('doc2vec_model_50')

	doc = preprocess_doc(doc)
	
	new_vec = model.infer_vector(doc)
	
	sims = model.docvecs.most_similar([new_vec])
	
	print 'Found'
	print sims


#Preprocess input document as the parameter of calculate()

def preprocess_doc(doc):
	f = open(doc, 'r');
	stopWords = set(stopwords.words('english'))
	
	line = f.readline().replace('\n', '')
	for word in line:
		if word not in stopWords:
			line.replace(word, '')
	
	line = word_tokenize(line.decode('utf8'))
	
	return line	


#Find the target paper within the combined paper set
def findTarget(index):
	f = open('Output1.txt', 'r')
	#split by \n
	
	arr = f.read().split('\n')
	
	print arr[index]
	

if __name__ == '__main__':
        #Generate Model
	tag_doc()

