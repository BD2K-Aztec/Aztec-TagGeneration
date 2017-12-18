# Aztec-TagGeneration

## Data

data/PaperSet: all the 4953 PubMed paper <br />
ProcessedNew: all the processed 4953 PubMed paper, all lowercased with space removed between capital letters in the original paper <br />
parsed_0.8: output of segphrase parsing with parameter 0.8, all frequent phrases are connected with "_" <br />

## Source Code

Doc2Vec.py: Read in processed and combined 4953 PubMed paper file, build and train a doc2vec model with dimension specified in the parameters <br />
dumpFiles.py: Extract all 4953 paper from a single file Output2.txt. These files have better format and less syntax errors. The extracted paper are further processed to train the doc2vec model. All the processed files are stored in /ProcessedNew <br />
insertSpace.py: Insert space between capital letters in the original papers then changed all these paper to lowercase for SegPhrase training purpose.

## Modified SegPhrase
SegPhrase is git cloned from the original author [(https://github.com/shangjingbo1226/SegPhrase)]. The source code are modified for the purpose of the current task.

src/online_query/segphrase_parser.cpp: the original code uses [] to indicate frequent phrases. Changed to "_" to connect phrase as a single word for the doc2vec training purpose.

 
