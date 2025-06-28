# python-codon-usage-analyzer

This is a simple Python program that analyzes codon usage in a 5' to 3' DNA sequence. It reads the sequence in frame (groups of three nucleotides), counts each codon, and shows how often each is used. It can also compare codon usage between two species.

## What it does:

- Asks the user to input a DNA sequence (A, T, C, G).
- Reads the sequence in triplets (codons) from the start.
- For each codon:
  - Counts how many times it appears
  - Shows its corresponding amino acid (e.g., `"ATG"` = Methionine)
- Calculates how frequent each codon is relative to the total.
- Shows the most used codon(s).
- Optionally compares codon usage with a second DNA sequence (species 2).

## Example Usage

python3 simple_codon_compare.py

enter a dna sequence for species 1: ATGGCTGCTGAACTGTAA
species 1 codon usage:
ATG (Met): 0.1667
GCT (Ala): 0.1667
GCT (Ala): 0.1667
...

most frequent codon(s) in species 1:
ATG (Met): 2 times

do you want to compare with another species? (yes/no): yes
enter a dna sequence for species 2: ATGAAAGGGGCTTAG
species 2 codon usage:
ATG (Met): 0.2500
...

comparison of codon usage:
ATG (Met): species 1 = 0.1667, species 2 = 0.2500
GCT (Ala): species 1 = 0.3333, species 2 = 0.0000
...
