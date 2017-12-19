from gensim.models import Word2Vec
from gensim.models import Doc2Vec
from nltk import word_tokenize
from scipy import spatial
import operator
import sys

def main(argv):
	DIM = argv[1]
	indexes = argv[2]
	model_name = 'doc2vec_model_'+str(DIM)
	model = Doc2Vec.load(model_name)
	f = open("results.txt", "a")
	for index in range(1, int(indexes)):
		docvec = model.docvecs['doc'+str(int(index))]
		doc = open('../Parsed_Paper/parsed/'+str(index) + "_parsed.txt",'r').readlines()[0].replace('\n','')
		print "document"+str(index)
		f.write(doc)
		f.write("\n")
		#print ""
		words = word_tokenize(doc.decode('utf8'))
		Sim_Dict = {}
		for word in words:
			try:
				wordvec = model[word]
				Sim_Dict[word] = 1 - spatial.distance.cosine(docvec,wordvec)
			except:
				pass
		sorted_dict = sorted(Sim_Dict.items(), key=operator.itemgetter(1),reverse=True)
		f.write("significant words: \n")
		for item in sorted_dict[:20]:
			f.write(str(item))

		print ""

if __name__ == "__main__":
	main(sys.argv)


