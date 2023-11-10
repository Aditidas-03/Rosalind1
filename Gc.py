from Bio import SeqIO
max_gc = 0
rosalind_id = None

for seq_record in SeqIO.parse("/Users/aditi/Desktop/Rosalind1/GC/rosalind_gc-2.txt", "fasta"):
    seq=seq_record.seq
    gc_count = seq.count('G') + seq.count('C')
    total_bases = len(seq)
    gc_content = (gc_count / total_bases) * 100
    if gc_content > max_gc:
        max_gc = gc_content
        rosalind_id = seq_record.id

print (rosalind_id) 
print (max_gc)
