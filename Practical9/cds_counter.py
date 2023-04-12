#Introduce re and related variables
#use re.findall() to find the string_to_search in the seq
#Calculate the length of the list and sum
#But this method cannot compute overlapping sequences
import re
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
string_to_search_1 = 'TGA'
string_to_search_2 = 'TAA'
L_1 = len(re.findall(string_to_search_1, seq))
L_2 = len(re.findall(string_to_search_2, seq))
Length_all = L_1 + L_2
print(Length_all)

#Define a new kind of function
#Split the regular expression
#Add the start posiition to control the start of re.search()
#Applied from the following website: "https://stackoverflow.com/questions/1374457/find-out-how-many-times-a-regex-matches-in-a-string-in-python"
def countoverlappingdistinct(seq, string_to_search):
  total = 0
  start = 0
  there = re.compile(seq)
  while True:
    mo = there.search(string_to_search, start)
    if mo is None: return total
    total += 1
    start = 1 + mo.start()
#L_1 = countoverlappingdistinct(seq, string_to_search_1)
#L_2 = countoverlappingdistinct(seq, string_to_search_2)
#Length_all = L_1 + L_2
#print(Length_all)

