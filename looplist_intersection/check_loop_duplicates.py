def check_duplicates(filename,new_filename):
	'''checks if the two rows are the same loop, but just reversed'''
	print('0')
	old = open(filename,'r')
	new = open(new_filename,'w')
	lines = old.readlines()
	old.seek(0)
	lines_every_other = old.readlines()[::2]
	print('1')
	print(lines_every_other)
	for i in range(len(lines_every_other)):
		print('2')
		row = lines_every_other[i].split()
		row2 = lines[i*2+1].split()
		name_row = row[3].split(':')
		name_row2 = row2[3].split(':')
		print(row[0][3],name_row2[0])
		print(row[1],name_row2[1])
		print(row[2],name_row2[2])
		if row[0][3] == name_row2[0] and row[1] == name_row2[1] and row[2] == name_row2[2]:
			new.write(lines_every_other[i])
		





	old.close()
	new.close()

	
