import map_promoter_gene_ID as mp

mp.map_promoter_gene_ID('<path to gene annotations table>', 
	'<path to NCBI gene ID table>',
	'<output file name for the promoter-to-gene file',
	'<path to NCBI gene ID table>' + 'tabs',
	)
# pandas version used: 1.2.5
# python version used: 3.8.10
# gene annotations table (txt file) -- gene annotations table from UCSC database https://genome.ucsc.edu/cgi-bin/hgTables. 
#	Settings -- settings Mammal, Human, GRCh38/hg38, Gene and Gene Predictions, NCBI RefSeq, RefSeq Curated (ncbiRefSeqCurated), 
#	region:genome, filter = NM_* 
# path to NCBI gene ID table (txt file) -- NCBI gene IDs from Go Ensembl http://uswest.ensembl.org/index.html 
#	Instructions: Go to BioMart, choose database 'Ensembl Genes 104', choose dataset 'human genes GRCh38.p13', 
#	click on Attributes and select 'Gene name','RefSeq mRNA ID', 'strand',and 'NCBI gene (formerly Entrezgene) ID'. Then download the file.
