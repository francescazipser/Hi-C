def convert(loops_filename,new_filename1,new_filename2,A_or_B):
	loops = open(loops_filename,'r')
	new = open(new_filename1,'w')
	new2 = open(new_filename2,'w')
	index = 0
	for line in loops.readlines()[2:]:
		row = line.split()
		new.write(row[0] + '\t' + row[1] + '\t' + row[2] + '\t' + row[3].replace('chr','') + ':' + row[4] + ':' + row[5] + '\t'+ A_or_B + str(index) + '\n')
		new2.write(row[3] + '\t' + row[4] + '\t' + row[5] + '\t' + row[0].replace('chr','') + ':' + row[1] + ':' + row[2] + '\t' + A_or_B + str(index) + '\n')
		index += 1
	loops.close()
	new.close()
	new2.close()

