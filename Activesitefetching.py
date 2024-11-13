import requests
import pandas as pd

def get_active_site(accession):
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        active_sites = []

        # Look in 'features' for type 'active site'
        for feature in data.get("features", []):
            if feature.get("type") == "Active site":
                position = feature["location"].get("start", {}).get("value")
                description = feature.get("description", "No description")
                active_sites.append(f"Position: {position}, Description: {description}")
        
        return "; ".join(active_sites) if active_sites else "No active sites found"
    else:
        return "Failed to retrieve data"

input_file = "uniprotids_kinases.xlsx"  
output_file = "active_sites_output.xlsx"
uniprot_df = pd.read_excel(input_file)

results = []
for uniprot_id in uniprot_df['UniProt_ID']:
    active_site_info = get_active_site(uniprot_id)
    results.append({"UniProt_ID": uniprot_id, "Active_Site_Info": active_site_info})

results_df = pd.DataFrame(results)
results_df.to_excel(output_file, index=False)

print(f"Active site information saved to {output_file}")
