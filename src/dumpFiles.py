#Created by Jingyi Yuan
#Extract 4952 PubMed Paper from Output2.txt


folder = "PaperSet/"

with open('Output2.txt', 'r') as file_in:
	lines = file_in.readlines()
	index = 0
 
	for line in lines:
		if index < 4953:	
			g = open(folder+str(index),'w')
			g.write(line)
			index = index + 1
		
