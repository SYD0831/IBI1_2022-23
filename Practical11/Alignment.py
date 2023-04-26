with open("ACE2_cat.fa", "r") as f:
    cat = ""
    for line in f:
        if line.startswith(">"):  
            continue
        cat += line.strip() 

with open("ACE2_human.fa", "r") as f:
    human = ""
    for line in f:
        if line.startswith(">"):  
            continue
        human += line.strip() 

with open("ACE2_mouse.fa", "r") as f:
    mouse = ""
    for line in f:
        if line.startswith(">"):  
            continue
        mouse += line.strip() 
BLOSUM62 = '''A  4  0 -2 -1 -2  0 -2 -1 -1 -1 -1 -2 -1 -1 -1  1  0  0 -3 -2
C  0  9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2
D -2 -3  6  2 -3 -1 -1 -3 -1 -4 -3  1 -1  0 -2  0 -1 -3 -4 -3
E -1 -4  2  5 -3 -2  0 -3  1 -3 -2  0 -1  2  0  0 -1 -2 -3 -2
F -2 -2 -3 -3  6 -3 -1  0 -3  0  0 -3 -4 -3 -3 -2 -2 -1  1  3
G  0 -3 -1 -2 -3  6 -2 -4 -2 -4 -3  0 -2 -2 -2  0 -2 -3 -2 -3
H -2 -3 -1  0 -1 -2  8 -3 -1 -3 -2  1 -2  0  0 -1 -2 -3 -2  2
I -1 -1 -3 -3  0 -4 -3  4 -3  2  1 -3 -3 -3 -3 -2 -1  3 -3 -1
K -1 -3 -1  1 -3 -2 -1 -3  5 -2 -1  0 -1  1  2  0 -1 -2 -3 -2
L -1 -1 -4 -3  0 -4 -3  2 -2  4  2 -3 -3 -2 -2 -2 -1  1 -2 -1
M -1 -1 -3 -2  0 -3 -2  1 -1  2  5 -2 -2  0 -1 -1 -1  1 -1 -1
N -2 -3  1  0 -3  0  1 -3  0 -3 -2  6 -2  0  0  1  0 -3 -4 -2
P -1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2  7 -1 -2 -1 -1 -2 -4 -3
Q -1 -3  0  2 -3 -2  0 -3  1 -2  0  0 -1  5  1  0 -1 -2 -2 -1
R -1 -3 -2  0 -3 -2  0 -3  2 -2 -1  0 -2  1  5 -1 -1 -3 -3 -2
S  1 -1  0  0 -2  0 -1 -2  0 -2 -1  1 -1  0 -1  4  1 -2 -3 -2
T  0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1  0 -1 -1 -1  1  5  0 -2 -2
V  0 -1 -3 -2 -1 -3 -3  3 -2  1  1 -3 -2 -2 -3 -2  0  4 -3 -1
W -3 -2 -4 -3  1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11  2
Y -2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7'''.split('\n')
for i in range(len(BLOSUM62)):
    BLOSUM62[i] = BLOSUM62[i].split()
m={}
for i in range(len(BLOSUM62)):
    for j in range(1, len(BLOSUM62[0])):
        m[BLOSUM62[i][0] + '\t' + BLOSUM62[j-1][0]] = BLOSUM62[i][j]
def calculate_scores(a,b):
    t=[[0]]
    for n in range(1, len(b)+1):
        t[0].append(n*(-5))
    for i in range(1, len(a)+1):
        t.append([i*(-5)] + [0]*len(b))
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                t[i][j] = t[i-1][j-1] + int(m[a[i-1]+'\t'+b[j-1]])
            else:
                t[i][j] = max(t[i-1][j]-5, t[i][j-1]-5, t[i-1][j-1]+int(m[a[i-1]+'\t'+b[j-1]]))
    return t[len(a)][len(b)]
def compare_sequences(seq1, seq2):
    diff_count = 0
    for i in range(min(len(seq1), len(seq2))):
        if seq1[i] != seq2[i]:
            diff_count += 1
    diff_count += abs(len(seq1) - len(seq2))
    percentage = (max(len(seq1), len(seq2)) - diff_count)/max(len(seq1), len(seq2))
    return percentage

human_and_cat = compare_sequences(human, cat)
human_and_mouse = compare_sequences(human, mouse)
mouse_and_cat = compare_sequences(mouse, cat)

print("the percentage of identical amino acids for human and cat is %.4f" % human_and_cat)
print("the alignment score of human and cat is %d" % calculate_scores(human,cat))
print("the percentage of identical amino acids for human and mouse is %.4f" % human_and_mouse)
print("the alignment score of human and mouse is %d" % calculate_scores(human,mouse))
print("the percentage of identical amino acids for mouse and cat is %.4f" % mouse_and_cat)
print("the alignment score of mouse and cat is %d" % calculate_scores(mouse,cat))

if human_and_cat >= human_and_mouse and human_and_cat >= mouse_and_cat:
    print("human and cat's sequences are most closely related")
elif human_and_mouse >= human_and_cat and human_and_mouse >= mouse_and_cat:
    print("human and mouse's sequences are most closely related")
else:
    print("mouse and cat's sequences are most closely related")

Analysis = "Analysis: The high percentage of identical amino acids (0.8522) between humans and cats indicates a significant degree of evolutionary conservation between the two species. This conservation suggests that these species share a common ancestor and have diverged relatively recently in evolutionary time.The fact that the percentage is not truly indicates that there have been some changes in the amino acid sequences of proteins over time due to mutations and natural selection. These changes may have resulted in functional differences between the proteins in humans and cats, which could explain some of the physiological and behavioral differences between the two species."
print(Analysis)