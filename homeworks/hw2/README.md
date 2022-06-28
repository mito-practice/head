# Рестрикционный анализ

## Инструменты

- genbank
- biopython or alternative
- что-нить еще

## Задание

1. Скачать геном человека 37 версии. Изучить что есть в этой фасте, какие хромосомы, какие последовательности...
2. Посчитать частоты тринуклеотидов и пентануклеотидов для каждой хромосомы и записать все это в таблицу, где в рядах будут хромосомы, а в колонках три- или пентанулеотиды, сделайте 2 таблицы, чтобы не нагромождать
3. *Найти выборку рестриктаз, которые режут весь геном человека на куски НЕ ДЛИННЕЕ 15000 нуклеотидов И НЕ РЕЖУТ митохондриальную ДНК совсем. Задача имеет большое прикладное значение, по завершении расскажу какое

## Pseudocode for collecting kmers (k-nucleorides)

```python
k = 3
kmer_freqs = defauldict(int)
for seq in fasta:
    for i in range(0, len(seq), 1):
        cur_kmer = seq[i: i + k]
        kmer_freq[cur_kmer] += 1
```

## Useful code

В биопитоне есть очень мощный модуль по работе с рестриктазами, предлагаю использовать его, хотя если найдете что-то еще, будет интересно посмотреть. Пример кода приложен

```python
from Bio.Restriction import Analysis, AllEnzymes
from Bio.SeqRecord import SeqRecord

rec = SeqRecord("ACTGACTGACTGACTG")
anal = Analysis(enzymes, rec.seq, linear=True)
anal.mapping # dict[RS_name, positions]

for rest_enz, positions in anal.mapping.items():
    if len(positions) == 1:
        pot_rs.append(rest_enz)
```
