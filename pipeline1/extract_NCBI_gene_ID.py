import pandas as pd
import remove_multiple_transcripts as rmt



def extract_NCBI_gene_ID(old_ncbi_filepath,txt_file,new_ncbi_filepath):

	
	
	f = open(old_ncbi_filepath,'r')
	g = open(new_ncbi_filepath,'w')

	for line in f.readlines():
		row = line.split(',')
		g.write(row[0]+'\t'+row[1]+'\t'+row[2]+'\t'+row[3]+'\n')
	f.close()
	g.close()

	# getting the gene names from the original txt file
	gene_names = rmt.remove_multiple_transcripts(txt_file)['gene_name']

	
	ncbi_table = pd.read_table(new_ncbi_filepath)
	
	# a dictionary mapping gene names to ncbi gene ID
	name_to_ncbi = {}
	for index,row in ncbi_table.iterrows():
		if pd.isna(row['Gene name']) == False and pd.isna(row['NCBI gene (formerly Entrezgene) ID']) == False:
			name_to_ncbi[row['Gene name']] = int(row['NCBI gene (formerly Entrezgene) ID'])

	# make a list of NCBI gene IDs corresponding to 'hg38_unique_transcripts' table gene names
	ncbi_genes = []
	genes_to_remove = []
	for gene in gene_names:
		if gene in name_to_ncbi:
			ncbi_genes.append(name_to_ncbi[gene])
		else:
			# if there is no NCBI gene ID corresponding to gene name
			ncbi_genes.append(0)
			genes_to_remove.append(gene)
	
	return ncbi_genes, genes_to_remove

