import pandas as pd

df1 = pd.read_excel('kinome_data_profiling.xlsx')
df2 = pd.read_excel('output.xlsx')

# Merge the DataFrames on the 'HGNC Name' column
merged_df = pd.merge(df1, df2, on='HGNC Name', how='left')

#print(merged_df)
merged_df.to_excel('final.xlsx', index = False)