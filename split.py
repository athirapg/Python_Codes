import pandas as pd

df=pd.read_excel("test.xlsx")


def split_interactions(row):
    interactions = row["ON_PROT_INTERACT"].split("; ")
    result = []
    for interaction in interactions:
        try:
            parts = interaction.split(")(")
            if len(parts) == 2:
                protein, regulation = parts[0].split("(")[0], parts[1].rstrip(")")
            else:
                protein, regulation = interaction.split("(")
                regulation = regulation.rstrip(")")
            result.append([row["GENE"], row["MOD_RSD"], protein, regulation])
        except ValueError:
            continue
    return result

split_rows = []
for _, row in df.iterrows():
    split_rows.extend(split_interactions(row))

split_df = pd.DataFrame(split_rows, columns=["GENE", "MOD_RSD", "ON_PROT_INTERACT", "Regulation"])

#print(split_df)

split_df.to_csv("output.csv", index=False)
