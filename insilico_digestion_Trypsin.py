import pandas as pd
import re

def tryptic_digest_absolute_positions(sequence, missed_cleavages=0):
    pattern = re.compile(r'(?<=[KR])(?!P)')
    peptides = pattern.split(sequence)
    digested_peptides = []
    current_position = 0
    
    start = 0
    while start < len(peptides):
        for end in range(start, min(start + missed_cleavages + 1, len(peptides))):
            
            peptide = ''.join(peptides[start:end + 1])
            
            s_positions = [str(current_position + i + 1) for i, aa in enumerate(peptide) if aa == 'S']
            t_positions = [str(current_position + i + 1) for i, aa in enumerate(peptide) if aa == 'T']
            y_positions = [str(current_position + i + 1) for i, aa in enumerate(peptide) if aa == 'Y']
            
            position_str = ''
            if s_positions:
                position_str += 'S' + ','.join(s_positions)
            if t_positions:
                if position_str:
                    position_str += ' '
                position_str += 'T' + ','.join(t_positions)
            if y_positions:
                if position_str:
                    position_str += ' '
                position_str += 'Y' + ','.join(y_positions)
           
            if position_str:
                formatted_peptide = f"[{peptide}; {position_str}]"
            else:
                formatted_peptide = f"[{peptide}]"
                
            digested_peptides.append(formatted_peptide)

           
            current_position += len(peptide)
            start = end + 1
            break

    return digested_peptides

def process_proteins_excel(input_file, output_file, missed_cleavages=0):
    
   
    df = pd.read_excel(input_file, sheet_name='Sheet3')


    formatted_results = []
    
  
    for index, row in df.iterrows():
        uniprot_id = row['ACC_ID']
        sequence = row['FASTA']
        
        
        peptides_with_positions = tryptic_digest_absolute_positions(sequence, missed_cleavages)
        
        
        peptides_str = ' '.join(peptides_with_positions)

       
        formatted_results.append({
            'ACC_ID': uniprot_id,
            'FASTA': sequence,
            'Tryptic peptides': peptides_str
        })

    
    result_df = pd.DataFrame(formatted_results)
    result_df.to_excel(output_file, index=False)


input_file = 'LT_only_kinase_sites.xlsx'  
output_file = 'digested_peptides_absolute_positions.xlsx'  

process_proteins_excel(input_file, output_file, missed_cleavages=1)

print(f"Digestion results saved to {output_file}")
