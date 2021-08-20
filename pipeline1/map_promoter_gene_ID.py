import pandas as pd
import remove_multiple_transcripts as rmt
import extract_NCBI_gene_ID as ncbi
import transcription_site_to_promoter_region as pr

def map_promoter_gene_ID(txt_file,old_ncbi_filepath,filename,new_ncbi_filepath):
	'''
	'''
	unique_transcripts = rmt.remove_multiple_transcripts(txt_file)
	ncbi_genes,genes_to_remove = ncbi.extract_NCBI_gene_ID(old_ncbi_filepath,txt_file,new_ncbi_filepath)
	chromosome = unique_transcripts['chromosome']
	gene_name = unique_transcripts['gene_name']
	
	prom_start, prom_end = pr.transcription_site_to_promoter_region(unique_transcripts)
	

	# create the new data frame
	gene_table = pd.DataFrame({'chromosome':chromosome,'prom_start':prom_start,'prom_end':prom_end,'gene_name':gene_name,'ncbi_ID':ncbi_genes})

	# remove genes without NCBI ID
	for index,row in gene_table.iterrows():
		if row['gene_name'] in genes_to_remove:
			gene_table.drop(index,inplace=True)

	# save to a csv file
	gene_table.to_csv(str(filename),
	 header=None, index=None, sep='\t', mode='a')