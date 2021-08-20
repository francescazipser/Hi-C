import pandas as pd
import remove_duplicates as rd
def convert(gene_id):
	''' A function that returns RefSeq mRNA ID as an integer.
	gene_id --  a string of the form NM_*
	'''
	new_id = gene_id.replace('NM_','')
	for letter in new_id:
		if letter == '0':
			new_id = new_id.replace('0','')
		else:
			break
	new_id = int(float(new_id))
	return new_id

def remove_multiple_transcripts(txt_file):
	'''
	'''
	txt = rd.remove_duplicates(str(txt_file))

	mRNA_ID = txt['name']
	chromosome = txt['chrom']
	strand = txt['strand']
	tx_start = txt['txStart']
	tx_end = txt['txEnd']
	gene_name = txt['name2']

	simple_table = pd.DataFrame(
		{'mRNA_ID':mRNA_ID,
		'chromosome':chromosome,
		'strand':strand,
		'tx_start':tx_start,
		'tx_end':tx_end,
		'gene_name':gene_name})

	# dict mapping gene names to smallest RefSeq mRNA IDs
	genes = {}
	for index,row in simple_table.iterrows():
		if row['gene_name'] not in genes:
			genes[row['gene_name']] = row['mRNA_ID']
		else:
			if convert(row['mRNA_ID']) < convert(genes[row['gene_name']]):
				genes[row['gene_name']] = row['mRNA_ID']

	# removing multiple transcripts for the same gene in the data frame
	for index,row in simple_table.iterrows():
		if row['mRNA_ID'] != genes[row['gene_name']]:
			simple_table.drop(index,inplace=True)

	return simple_table

