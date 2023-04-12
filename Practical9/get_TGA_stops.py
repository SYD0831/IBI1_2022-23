#import re module for regular expressions
#define input and output file names
#open input file for reading and output file for writing
    # initialize an empty string to store the current sequence
    # iterate over the lines of the input file
        # if the line starts with ">", it is a header line
            # if the sequence is not empty and ends with "TGA", it is a candidate gene
                # write the header and the sequence to the output file
            # extract the gene name from the header line using regular expressions
            # simplify the header by only keeping the gene name
            # reset the sequence to empty
            # append the line (without newline) to the current sequence
    # check the last sequence in the file
        # write the header and the sequence to the output file
import re
input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "TGA_genes.fa"
with open(input_file, "r") as file_in, open(output_file, "w") as file_out:
    sequence = ""
    for line in file_in:
        if line.startswith(">"):
            if sequence and sequence.endswith("TGA"):
                file_out.write(header + "\n" + sequence + "\n")
            gene = re.split(r'\s+', line)
            gene_name = gene[0]
            header = gene_name
            sequence = ""
        else:
            sequence += line.strip()
    if sequence and sequence.endswith("TGA"):
        file_out.write(header + "\n" + sequence + "\n")