import pandas as pd

def transcription_site_to_promoter_region(unique_transcripts_df):
	'''
	'''
	prom_start = []
	prom_end = []

	for index,row in unique_transcripts_df.iterrows():
		if row['strand'] == '+':
			prom_start.append(int(row['tx_start']) - 750)
			prom_end.append(int(row['tx_start']) + 250)
		if row['strand'] == '-':
			prom_start.append(int(row['tx_end']) - 250)
			prom_end.append(int(row['tx_end']) + 750)
			
	return prom_start, prom_end