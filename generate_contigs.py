import random
import string

# Define the number of contigs and the length range
num_contigs = 100
min_length = 1000
max_length = 10000

# Generate a list of contig sequences with random lengths and bases
contigs = []
for i in range(num_contigs):
    length = random.randint(min_length, max_length)
    sequence = ''.join(random.choice(string.ascii_uppercase) for _ in range(length))
    contigs.append(sequence)

# Write the contigs to a FASTA format file
with open('contigs.fasta', 'w') as f:
    for i, sequence in enumerate(contigs):
        f.write(f'>contig_{i+1}\n{sequence}\n')
