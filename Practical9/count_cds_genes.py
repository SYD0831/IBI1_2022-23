stop_name = input('choose one of the three stop	codons ,TAA,TAG,TGA')
if stop_name not in ["TAA", "TAG", "TGA"]:
    print("Invalid stop codon. Please enter one of TAA, TAG or TGA.")
    exit()

import re
input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = stop_name + "_stop_genes.fa"


with open(input_file, "r") as file_in, open(output_file, "w") as file_out:
    sequence = ""
    for line in file_in:
        if line.startswith(">"):
            if sequence and re.findall(stop_name,sequence):
                file_out.write(header + " the number of coding sequences is :" + str(sequence.count(stop_name)) +"\n" + sequence + "\n")
            gene = re.split(r'\s+', line)
            gene_name = gene[0]
            header = gene_name
            sequence = ""
        else:
            sequence += line.strip()
    if sequence and sequence.endswith(stop_name):
        file_out.write(header + "\n" + sequence + "\n")



