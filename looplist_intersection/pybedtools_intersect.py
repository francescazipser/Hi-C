import pybedtools

def intersect(filename_a,filename_b,output_filename):
	a = pybedtools.BedTool(filename_a)
	b = pybedtools.BedTool(filename_b)
	a_with_b = a.intersect(b,wo=True)
	c = a_with_b.moveto(output_filename)
