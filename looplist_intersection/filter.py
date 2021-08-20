import pandas as pd
def filter(file_A1B1,file_A2B2,output_filename):
	file_A1B1 = open(file_A1B1,'r')
	file_A2B2 = open(file_A2B2,'r')
	unique = open(output_filename,'w')
	table_A1B1 = pd.read_table(file_A1B1,sep='\t',header=None,names=['chrom1','start1','end1','name1','id1','chrom2','start2','end2','name2','id2','overlap'])
	table_A2B2 = pd.read_table(file_A2B2,sep='\t',header=None,names=['chrom1','start1','end1','name1','id1','chrom2','start2','end2','name2','id2','overlap'])
	A1B1_id1 = list(table_A1B1['id1'])
	A1B1_id2 = list(table_A1B1['id2'])
	A2B2_id1 = list(table_A2B2['id1'])
	A2B2_id2 = list(table_A2B2['id2'])
	A1B1_dict = {}
	A2B2_dict = {}
	for i in range(len(A1B1_id1)):
		new_id = str(A1B1_id1[i]) + str(A1B1_id2[i])
		A1B1_dict[new_id] = True
	for i in range(len(A2B2_id2)):
		new_id = str(A2B2_id1[i]) + str(A2B2_id2[i])
		A2B2_dict[new_id] = True
	new_ids = A1B1_dict.keys()
	common_dict = {}
	for element in new_ids:
		if element in A2B2_dict:
			common_dict[element] = True
	file_A1B1.seek(0)
	for line in file_A1B1.readlines():
		row = line.split()
		ID  = row[4]+row[9]
		if ID in common_dict:
			unique.write(line)
	file_A1B1.close()
	file_A2B2.close()
	unique.close()
		
		
	


	
