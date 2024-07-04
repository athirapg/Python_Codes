import pandas as pd

df = pd.read_excel(r"Kinase_sitecount.xlsx", 'Sheet2')

df['Rank'] = df.groupby('mapped_genesymbol')['exp_condition_count_diff'].rank(ascending=False, method='min')

df = df.sort_values(by=['mapped_genesymbol', 'Rank'])

#print(df)
df.to_excel('count.xlsx',index = False)
