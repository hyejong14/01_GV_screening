#!/usr/bin/env python3
"""
filter_contigs.py

Usage:
  filter_contigs.py -i <in.fasta> -o <out.fasta> -l <min_length>

Ex) filter_contigs.py \
      -i 02_assembly/SRR123456_assembly/contigs.fasta \
      -o 03_assembly_filtered/SRR123456_assembly/contigs_filtered.fasta \
      -l 800
"""
import argparse
from Bio import SeqIO

def filter_contigs(input_fasta: str, output_fasta: str, min_len: int) -> None:
    total = kept = 0
    with open(output_fasta, "w") as out:
        for rec in SeqIO.parse(input_fasta, "fasta"):
            total += 1
            if len(rec.seq) >= min_len:
                SeqIO.write(rec, out, "fasta")
                kept += 1
   
    print(f"Filtered {kept}/{total} contigs >= {min_len} bp")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Filter contigs by minimum length")
    p.add_argument("-i", "--input",  required=True, help="input FASTA")
    p.add_argument("-o", "--output", required=True, help="output FASTA")
    p.add_argument("-l", "--min_len", type=int, default=800,
                   help="minimum contig length [default: 800]")
    args = p.parse_args()
    filter_contigs(args.input, args.output, args.min_len)