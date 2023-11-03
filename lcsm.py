
from Bio import SeqIO
dna=[]
for seq_record in SeqIO.parse("/Users/aditi/Desktop/Rosalind1/lcsm/rosalind_lcsm.txt","fasta"):
    dna.append(seq_record.seq)

def longestcommonstring(string):
    
    
    shortest_len= min(len(seq)for seq in dna)
    longest = ""

    for i in range (shortest_len):
        for j in range (i+len(longest)+1,shortest_len+1):
          commonseq=dna[0][i:j]
          if all (commonseq in seq for seq  in dna):
             longest =commonseq

    return longest         

print(longestcommonstring(dna))

