#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from Bio import SeqIO

import glob
from collections import Counter
import itertools

file_in = '/mnt/lustre/nknyazeva/courseWork5/data/result/genes_GRCh38/ortho_MACMU18455_HUMAN23250/orf_MACMU18455_align_mafft.afa'
file_out = '/mnt/lustre/nknyazeva/courseWork5/data/result/genes_GRCh38/ortho_MACMU18455_HUMAN23250/pn_ps_orf_MACMU18455_align_mafft.afa'


codontable = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
    'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
}

four_folded_codons = ['L', 'V', 'S', 'P', 'T', 'A', 'R', 'G']
four_folded_triplets = ['CCT', 'CCC', 'CCA', 'CCG', 'CTT', 'CTC', 'CTA', 'CTG', 'GGT', 'GGC', 'GGA', 'GGG', 'TCT', 'TCC', 'TCA', 'TCG', 'GCT', 'GCC', 'GCA', 'GCG', 'GTT', 'GTC', 'GTA', 'GTG', 'ACT', 'ACC', 'ACA', 'ACG', 'CGT', 'CGC', 'CGA', 'CGG']

list_of_genes = ['first_gene', 'second_gene', 'third_gene']

def get_gene_name(filename):
    return filename.split("/")[-1][:-6]

def main():
    names = glob.glob(file_in)
    with open(file_out, "w") as outfile:
        outfile.write('{}\t{}\t{}\n'.format('gene_name', 'pn', 'ps'))
        for name in names:
            gene_name = get_gene_name(name)
            print(gene_name)
            # if gene_name in list_of_genes:
            with open(name, 'r') as handle:
                seq_triplet = []

                for a in SeqIO.parse(name, "fasta"):
                    if a.id != 'dm5':
                        seqs = str(a.seq.upper())
                        seq_triplet.append(list(seqs[i:i+3] for i in xrange(3, len(seqs)-3, 3)))


                # so after all operations above I have a seq_triplet list which consists of all sequences, for instance [['ATG', 'CCC'], ['ATG', 'TTG'], ['GGG', 'CCC']] if I have 3 sequences in alignment
                # now I will make some transformations for make this data more handy

                seq_izip = [] # new list for sequences
                for x in itertools.izip(*seq_triplet):
                    seq_izip.append(x)

                seq_izip = map(list, seq_izip)

                new_seq_izip = []
                for i in seq_izip:
                    new_seq_izip.append([x for x in i if x in codontable.keys()])
                seq_izip = new_seq_izip

                # And finally this data is ready for calculating pN/pS for gene's sequences

                number_syn_sites, number_nosyn_sites = 0, len(seq_izip)
                lst_ps, lst_pn = [], []


                # for syn sites and syn mutations
                for codon_position in xrange(len(seq_izip)):
                    # so here I choose first position of alignment. There are first codons of all sequences
                    if len(seq_izip[codon_position]) > 0 and all(codontable[x] == codontable[seq_izip[codon_position][0]] for x in seq_izip[codon_position]) and all(x in four_folded_triplets for x in seq_izip[codon_position]):
                        number_syn_sites += 1

                        triplets = seq_izip[codon_position]
                        len_triplets = len(triplets)
                        counter_triplets = dict(Counter(triplets))
                        if len(counter_triplets) > 1:
                            ps = 1
                            values = counter_triplets.values()
                            for value in values:
                                ps -= ((float(value)/len_triplets) ** 2)
                            lst_ps.append(ps)

                # for nosyn sites and nosyn mutations
                for codon_position in xrange(len(seq_izip)):
                    if len(seq_izip[codon_position]) > 1:
                        triplets = list(i[1] for i in seq_izip[codon_position])
                        if len(list(set(triplets))) > 1:
                            pn = 1
                            len_triplets = len(triplets)
                            counter_triplets = dict(Counter(triplets))
                            values = counter_triplets.values()
                            for value in values:
                                pn -= ((float(value)/len_triplets) ** 2)
                            lst_pn.append(pn)
                if number_nosyn_sites > 0 and number_syn_sites > 0: # try to avoid zero division
                    print('{}\t{}\t{}\n'.format(gene_name, float(sum(lst_pn))/number_nosyn_sites, float(sum(lst_ps))/number_syn_sites))
                    outfile.write('{}\t{}\t{}\n'.format(gene_name, float(sum(lst_pn))/number_nosyn_sites, float(sum(lst_ps))/number_syn_sites))
                elif number_nosyn_sites > 0 and number_syn_sites == 0:
                    print('{}\t{}\t{}\n'.format(gene_name, float(sum(lst_pn))/number_nosyn_sites, 0))
                    outfile.write('{}\t{}\t{}\n'.format(gene_name, float(sum(lst_pn))/number_nosyn_sites, 0))
main()

