import requests
import pandas as pd

# Load UniProt IDs from Excel file
df = pd.read_excel(r"uniprot_ids.xlsx")

def get_uniprot_gene_symbol(uniprot_id):
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.json"

    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            
            gene_symbol = data['genes'][0]['geneName']['value']
            return gene_symbol
        except (KeyError, IndexError):
            print(f"No gene symbol found for UniProt ID {uniprot_id}")
            return None
    else:
        print(f"Error fetching data from UniProt for ID {uniprot_id}: {response.status_code}")
        return None


ids = df['ids'].to_list()
gene_symbols = []

for i in ids:
    gene_symbol = get_uniprot_gene_symbol(i)
    if gene_symbol is not None:
        print(f"The gene symbol for UniProt ID {i} is {gene_symbol}")
    else:
        print(f"Gene symbol not found for UniProt ID {i}")
    gene_symbols.append(gene_symbol)

results_dict = {'ids': ids, 'gene_symbols': gene_symbols}
results_df = pd.DataFrame(results_dict)

print(results_df)
results_df.to_excel('Uniprot_gene_symbols.xlsx', index=False)
