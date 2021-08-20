import pandas as pd

def remove_duplicates(filename):

	anno_plain = pd.read_csv(str(filename),sep='\t',skiprows=1)
	duplicated_transcripts = anno_plain.loc[anno_plain.duplicated(subset=['name'],keep=False)].copy()
	duplicated_transcripts_nofirst = anno_plain.loc[anno_plain.duplicated(subset=['name'])].copy()
	num_duplic = duplicated_transcripts.groupby(duplicated_transcripts.name.tolist(),as_index=False).size()
	duplic_names = anno_plain.set_index('name').loc[num_duplic.index.tolist()].reset_index()
	my_selec = duplic_names[duplic_names['chrom'].map(lambda x: (x[-1].isdigit()) | (x[-1]=='X'))]
	rows_to_remove = duplic_names.merge(my_selec,how='left', indicator=True).pipe(lambda df:df.loc[df._merge=='left_only'])
	final_anno = anno_plain[rows_to_remove.columns[:-1]].merge(rows_to_remove.iloc[:,:-1],how='left', indicator=True).pipe(lambda df:df.loc[df._merge=='left_only']).iloc[:,:-1]
	return final_anno


