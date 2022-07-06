# Blast-plus

## packages

```bash
sudo apt install ncbi-entrez-direct
sudo apt install ncbi-blast+
```

## Console

```bash

# download insecta refseq fasta
esearch -db nucleotide -query "("Insecta"[Organism] OR Insecta[All Fields]) AND (biomol_genomic[PROP] AND refseq[filter] AND mitochondrion[filter])" | efetch -format fasta > data/insecta_refseq.fna

# make db for blasting
makeblastdb -dbtype nucl -parse_seqids -in data/insecta_refseq.fna -out db/insecta -title "Insecta mtDNA"

blastn -task blastn -query data/bobmus_ND6.fasta -db db/insecta -out data/blastn_out.txt
tblastn -db db/insecta -db_gencode 2 -num_alignments 20 -query data/bombus_ND6.faa -out data/tblastn_out.txt 

blastdbcmd -db db/insecta -entry NC_064531.1 -range 5878-6297
```

## References

- [e-utils](https://www.ncbi.nlm.nih.gov/books/NBK25497/#chapter2.chapter2_table1)
- [nr/nt db](https://ftp.ncbi.nlm.nih.gov/blast/db/)
