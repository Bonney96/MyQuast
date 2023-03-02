import argparse
from collections import defaultdict
from Bio import SeqIO
import os


def calculate_n50(contig_lengths):
    """Calculates the N50 from a list of contig lengths."""
    contig_lengths.sort(reverse=True)
    total_length = sum(contig_lengths)
    n50_length = total_length / 2
    n50 = 0
    length_so_far = 0
    for length in contig_lengths:
        length_so_far += length
        if length_so_far >= n50_length:
            n50 = length
            break
    return n50


def parse_contigs(fasta_file):
    """Parses the contigs from a FASTA format file and returns a dictionary
    with the contig IDs and lengths."""
    contig_lengths = defaultdict(int)
    with open(fasta_file) as f:
        for record in SeqIO.parse(f, 'fasta'):
            contig_lengths[record.id] = len(record.seq)
    return contig_lengths


def write_report(contig_lengths, output_dir=None):
    """Writes a report with the number of contigs, total length, largest contig,
    and N50."""
    report_file = 'report.txt'
    if output_dir is not None:
        os.makedirs(output_dir, exist_ok=True)
        report_file = os.path.join(output_dir, report_file)
    with open(report_file, 'w') as f:
        num_contigs = len(contig_lengths)
        total_length = sum(contig_lengths.values())
        largest_contig = max(contig_lengths.values())
        n50 = calculate_n50(list(contig_lengths.values()))
        f.write(f'Number of contigs: {num_contigs}\n')
        f.write(f'Total length: {total_length}\n')
        f.write(f'Largest contig: {largest_contig}\n')
        f.write(f'N50: {n50}\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculates N50 from a FASTA format contigs file.')
    parser.add_argument('fasta_file', help='Path to the input FASTA format contigs file')
    parser.add_argument('-o', '--output', help='Path to the output directory')
    args = parser.parse_args()

    contig_lengths = parse_contigs(args.fasta_file)
    write_report(contig_lengths, args.output)
