# codon to amino acid map
codon_table = {
    "TTT": "Phe", "TTC": "Phe", "TTA": "Leu", "TTG": "Leu",
    "CTT": "Leu", "CTC": "Leu", "CTA": "Leu", "CTG": "Leu",
    "ATT": "Ile", "ATC": "Ile", "ATA": "Ile", "ATG": "Met",
    "GTT": "Val", "GTC": "Val", "GTA": "Val", "GTG": "Val",
    "TCT": "Ser", "TCC": "Ser", "TCA": "Ser", "TCG": "Ser",
    "CCT": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "ACT": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "GCT": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "TAT": "Tyr", "TAC": "Tyr", "TAA": "Ter", "TAG": "Ter",
    "CAT": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
    "AAT": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
    "GAT": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
    "TGT": "Cys", "TGC": "Cys", "TGA": "Ter", "TGG": "Trp",
    "CGT": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AGT": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
    "GGT": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
}

from collections import defaultdict

def count_codons(dna):
    dna = dna.upper()
    codon_count = defaultdict(int)
    total = 0
    for i in range(0, len(dna) - 2, 3):
        codon = dna[i:i+3]
        if len(codon) == 3:
            codon_count[codon] += 1
            total += 1
    return codon_count, total

def show_codon_usage(codon_count, total, label):
    print(f"\n{label} codon usage:")
    for codon in sorted(codon_count):
        aa = codon_table.get(codon, "---")
        freq = codon_count[codon] / total
        print(f"{codon} ({aa}): {freq:.4f}")

def show_most_common(codon_count, label):
    max_count = max(codon_count.values())
    common = [c for c in codon_count if codon_count[c] == max_count]
    print(f"\nmost frequent codon(s) in {label}:")
    for codon in common:
        aa = codon_table.get(codon, "---")
        print(f"{codon} ({aa}): {codon_count[codon]} times")

def compare_usages(freq1, freq2):
    print("\ncomparison of codon usage:")
    all_codons = sorted(set(freq1) | set(freq2))
    for codon in all_codons:
        aa = codon_table.get(codon, "---")
        f1 = freq1.get(codon, 0)
        f2 = freq2.get(codon, 0)
        print(f"{codon} ({aa}): species 1 = {f1:.4f}, species 2 = {f2:.4f}")

if __name__ == "__main__":
    dna1 = input("enter a dna sequence for species 1: ")
    count1, total1 = count_codons(dna1)
    if total1 == 0:
        print("no codons found in species 1.")
    else:
        freq1 = {c: count1[c] / total1 for c in count1}
        show_codon_usage(count1, total1, "species 1")
        show_most_common(count1, "species 1")

        compare = input("\ndo you want to compare with another species? (yes/no): ").strip().lower()
        if compare == "yes":
            dna2 = input("enter a dna sequence for species 2: ")
            count2, total2 = count_codons(dna2)
            if total2 == 0:
                print("no codons found in species 2.")
            else:
                freq2 = {c: count2[c] / total2 for c in count2}
                show_codon_usage(count2, total2, "species 2")
                show_most_common(count2, "species 2")
                compare_usages(freq1, freq2)
        else:
            print("\nno comparison selected.")
