import requests
import pandas as pd

df=pd.read_excel(r"uniprot_ids.xlsx")

def get_uniprot_sequence_length(uniprot_id):
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.json"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        sequence_length = data['sequence']['length']
        return sequence_length
    else:
        print(f"Error fetching data from UniProt: {response.status_code}")
        return None


ids = df['ids'].to_list()
ids_length = []

for i in ids:
    length = get_uniprot_sequence_length(i)
    if length is not None:
        print(f"The sequence length for UniProt ID {i} is {length}")
        ids_length.append(length)
    


dict = {'ids': ids, 'ids_length': ids_length} 
   
df = pd.DataFrame(dict)
   
print(df) 

df.to_excel('Uniprot_kinase_length.xlsx', index = False)