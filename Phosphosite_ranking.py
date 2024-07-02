import pandas as pd

# Create the DataFrame
df = pd.read_excel(r"Kinase_sitecount.xlsx", 'Sheet2')


# Rank each kinase phosphosite based on profiling count
df['Rank'] = df.groupby('mapped_genesymbol')['exp_condition_count_diff'].rank(ascending=False, method='min')

# Sort by gene symbol and rank
df = df.sort_values(by=['mapped_genesymbol', 'Rank'])

#print(df)
df.to_excel('count.xlsx',index = False)