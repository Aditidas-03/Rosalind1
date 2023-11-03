from Bio import SeqIO

dna = list(SeqIO.parse("/Users/aditi/Desktop/Rosalind1/Cons/rosalind_cons-2.txt", "fasta"))
seq_len = len(dna[0])
profile_matrix = {base: [0] * seq_len for base in "ACGT"}
cons = ""
for i in range(seq_len):
    base_count= {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    for j in dna:
        base = j[i]
        base_count[base] += 1

    common_base = max(base_count, key=base_count.get)
    cons += common_base
    for base in "ACGT":
        profile_matrix[base][i] = base_count[base]
        
print(cons)
for base in "ACGT":
    print(f"{base}: {' '.join(map(str, profile_matrix[base]))}")

