import re
def is_protein_coding (DNASEQUENCE):
    DNASEQUENCE = DNASEQUENCE.upper()
    total_length = len(DNASEQUENCE)
    a = 'ATG'
    b = 'TGA'
    start_index = re.search(a, DNASEQUENCE).start()
    stop_index = re.search(b, DNASEQUENCE).start()
    if start_index == -1 or stop_index == -1:
        return 0, 'non-coding'
    coding_length = stop_index - start_index + 3
    coding_percentage = coding_length / total_length * 100
    if coding_percentage > 50:
        return coding_percentage, 'protein-coding'
    elif coding_percentage < 10:
        return coding_percentage, 'non-coding'
    else:
        return coding_percentage, 'unclear'    
DNASEQUENCE = "aaaaaaaaaattttttgggggggggatggtgatgtgacatgtttaaaatgctgctaggtgaccactagtgaaatgaagtttctga"
coding_percentage, coding_type = is_protein_coding(DNASEQUENCE)
print(f"The coding percentage of the sequence is {coding_percentage:.2f}% and it is {coding_type}.")