import glob
import re

filenames = glob.glob('[0-9]*')

processed = "../ProcessedNew/"

def insertSpace():
	#loop through each file
	for filename in filenames:
		with open(processed + filename + "_processed.txt", 'w') as write_tofile:
			lines = open(filename).readlines()
			for line in lines:
				line = line.replace('\n', ' ')
				line += '\n'
				re.sub('\.([A-Z])', r' \1', line)
				write_tofile.write(line.lower())
insertSpace()	
				
			
			

