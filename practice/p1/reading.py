"""
steps:
- read gb
- get elemnts
- get seqs
- get kmer

"""

from collections import defaultdict

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Bio import SeqIO
import Bio
from Bio import SeqRecord

FEATURE_TYPES = {'tRNA', 'CDS', 'rRNA'}
path_to_gb = "./practice/p1/tarakan.gb"

gb = SeqIO.parse(path_to_gb, "genbank")


def kmer_iterator(seq: str, k=3):
    for i in range(0, len(seq) - k + 1, 1):
        cur_kmer = seq[i: i + k]
        yield cur_kmer


def get_gb_features(gb: SeqRecord.SeqRecord):
    for record in gb:
        sp_data = [None for _ in range(len(record))]
        for feature in record.features:
            ftype = feature.type
            # TODO collect all trinucleotides
            # if ftype == "source":
            #     for genome_pos, trinucl in enumerate(kmer_iterator(seq, 3), 2):
            #         sp_data[genome_pos] = {"Context": trinucl}

            if ftype == "tRNA" or ftype == "rRNA":
                fgene = feature.qualifiers["product"][0]
            elif ftype == "CDS":
                fgene = feature.qualifiers["gene"][0]
            elif ftype == "D-loop":
                fgene = None
            else:
                continue

            fvalue = feature.extract(record)
            seq = str(fvalue.seq)
            for pos, pentanucl in enumerate(kmer_iterator(seq, 5), 2):
                row = {
                    "Species": record.annotations["organism"],
                    "Type": ftype,
                    "Gene": fgene,
                    "Strand": feature.strand,
                    "PosInGene": pos,
                    "Context": pentanucl,
                    "Codon": None,
                    "PosInCodon": None,
                }

    return


def main():
    get_gb_features(gb)


if __name__ == "__main__":
    main()
