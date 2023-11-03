from Bio import SeqIO
s1=()
s2=()
for seq_rec in SeqIO.parse("/Users/aditi/Desktop/Rosalind1/Trans/rosalind_tran.txt","fasta"):
    if not s1:
        s1=seq_rec.seq
    else:
        s2=seq_rec.seq
    
transitions= [('A', 'G'), ('T', 'C'), ('C', 'T'), ('G', 'A')]
transversions = [('A', 'T'), ('A', 'C'), ('T', 'A'), ('T', 'G'), ('C', 'A'),('C', 'G'), ('G', 'T'), ('G', 'C')]
transversions_n=0 
transitions_n=0

for i in range (len(s1)):
    if (s1[i], s2[i]) in transitions:
        transitions_n += 1
    if (s1[i], s2[i]) in transversions:
        transversions_n += 1
    
if transversions_n!=0:
    ratio =transitions_n/transversions_n

print(ratio)
    