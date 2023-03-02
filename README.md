# N50 Calculator
This program calculates the N50 from a FASTA format contigs file. The N50 is a statistic used in genomics to describe the average length of the nucleotide sequences that make up a set of contigs. It is the length of the shortest contig such that 50% of the total length of the sequence assembly is contained in contigs of that length or longer.

# Installation
Clone the repository to your local machine.
Install the required packages by running the command pip install -r requirements.txt.

# Usage
To use this program, run the following command in your terminal:

python n50.py input_file.fasta -o output_directory

input_file.fasta is the path to your input FASTA format contigs file.
-o output_directory is an optional argument that specifies the path to the output directory. 
If not specified, the output file will be created in the same directory as the input file.

# Output
The program will generate a report.txt file containing the following information:

Number of contigs
Total length of the sequence assembly
Length of the largest contig
N50 value of the contigs
If the -o argument is specified, the output file will be created in the specified directory. Otherwise, it will be created in the same directory as the input file.

# Contributing
If you encounter any issues while using this program, or if you have suggestions for improvements, please open an issue on the GitHub repository.

Pull requests are also welcome!
