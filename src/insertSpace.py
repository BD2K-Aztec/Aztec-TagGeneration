import re
import multiprocessing as mp
import glob

#Created by Jingyi Yuan
#Processed the paper to insert space before capital letters

folder = './outputs/'
#filenames = glob.glob('[0-9]*')

#insert space before capital letters, read in line by line
def insertSpace(index, allocated_files):
	g = open(folder+'Output_'+str(index)+'.txt','a')
	 
	for line in allocated_files:
		re.sub('\.([A-Z])', r' \1', line)
		g.write(line.lower())
	print "Inserted"


def allocateFiles(list_lines, size):
	num_lines = len(list_lines)
	allocate_size = num_lines/size
        allocate = []

        start = 0

        for i in range(size):
                allocate_sublist = []
                for j in range(allocate_size):
                	allocate_sublist.append(list_lines[start + j])
		start += allocate_size;

                allocate.append(allocate_sublist)
        return allocate


if __name__ == "__main__":
        processes = []
        process_num = 20
	list_lines = open('Output2.txt').readlines()
		
		
        allocation = allocateFiles(list_lines, process_num)

        for i in range(process_num):
        	processes.append(mp.Process(target=insertSpace, args=(i,allocation[i],)))

        for p in processes:
        	p.start()
        for p in processes:
        	p.join()
