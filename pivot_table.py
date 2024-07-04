import pandas as pd

df = pd.read_excel(r"test.xlsx")

df['site'] = df['mapped_phosphosite'] + ' (' + df['total_count'].astype(str) + ')'

df['site_num'] = df.groupby('HGNC Name').cumcount() + 1

pivot_df = df.pivot(index='HGNC Name', columns='site_num', values='site')
pivot_df = pivot_df.reset_index().rename_axis(None, axis=1)

pivot_df.columns = ['HGNC Name', 'site1', 'site2', 'site3', 'site4', 'site5', 'site6', 'site7', 'site8', 'site9', 'site10']

pivot_df.to_excel('output.xlsx',  index = False)
