# Featurefetch

Get and sort features from gtfs. Example query: give me all the introns, sorted
by gene length where the introns are split into quartiles by gene length. Many
more to come.

Will grow organically as I need features, not rushing to finish this.

## Example

(\#\# is stderr, \# stdout)

```bash
featurefetch -g test_data/ensembl.gtf   -sf gene -so Length -kf exon -s quartiles -kt longest --which-intron-exon internal
## Parsing gtf.
## Removing all but longest transcript.
## Sorting and selecting.
# Chromosome Feature Source Start End Score Strand Frame GeneID TranscriptID ExonNumber ExonID Group Length
# 1 exon havana 35277 35481 . - . ENSG00000237613 ENST00000417324 2.0 ENSE00001669267 25-50 1527
# 1 exon havana 12613 12721 . + . ENSG00000223972 ENST00000456328 2.0 ENSE00003582793 50-75 2540
# 1 exon havana 30564 30667 . + . ENSG00000243485 ENST00000473358 2.0 ENSE00001922571 25-50 1555
# 1 exon havana 120721 120932 . - . ENSG00000238009 ENST00000477740 2.0 ENSE00001171005 75-100 44428
# 1 exon havana 112700 112804 . - . ENSG00000238009 ENST00000477740 3.0 ENSE00001957285 75-100 44428
# 1 exon havana 24738 24891 . - . ENSG00000227232 ENST00000488147 2.0 ENSE00003507205 75-100 15166
# 1 exon havana 18268 18366 . - . ENSG00000227232 ENST00000488147 3.0 ENSE00003477500 75-100 15166
# 1 exon havana 17915 18061 . - . ENSG00000227232 ENST00000488147 4.0 ENSE00003565697 75-100 15166
# 1 exon havana 17606 17742 . - . ENSG00000227232 ENST00000488147 5.0 ENSE00003475637 75-100 15166
# 1 exon havana 17233 17368 . - . ENSG00000227232 ENST00000488147 6.0 ENSE00003502542 75-100 15166
# 1 exon havana 16858 17055 . - . ENSG00000227232 ENST00000488147 7.0 ENSE00003553898 75-100 15166
# 1 exon havana 16607 16765 . - . ENSG00000227232 ENST00000488147 8.0 ENSE00003621279 75-100 15166
# 1 exon havana 15796 15947 . - . ENSG00000227232 ENST00000488147 9.0 ENSE00002030414 75-100 15166
# 1 exon havana 15005 15038 . - . ENSG00000227232 ENST00000488147 10.0 ENSE00001935574 75-100 15166
# 1 exon havana 65520 65573 . + . ENSG00000186092 ENST00000641515 2.0 ENSE00003813641 50-75 6166
# 1 exon havana 58700 58856 . + . ENSG00000240361 ENST00000642116 2.0 ENSE00003812505 75-100 6518
```

## TODO:

* Add feature TSS
* Fix intron code
* Add ways to remove genes with overlapping TSS.
* Add more splits
* Fetch data from UCSC mysql db if no GTF given on command line.

## Usage:

```
usage: featurefetch [-h] --gtf GTF [--keep-transcript KEEP_TRANSCRIPT]
                    --sort-feature SORT_FEATURE --sort-on SORT_ON
                    --keep-feature KEEP_FEATURE --split SPLIT
                    [--which-intron-exon WHICH_INTRON_EXON]

Complex fetching and sorting and aggregation of features. (Visit
github.com/endrebak/featurefetch for examples and help.)

optional arguments:
  -h, --help            show this help message and exit
  --gtf GTF, -g GTF     GTF file to fetch features from.
  --keep-transcript KEEP_TRANSCRIPT, -kt KEEP_TRANSCRIPT
                        Which transcripts to keep during analyses. Removing
                        some transcripts will also remove the exons belonging
                        to them. Currently available: longest, all. Default:
                        all.
  --sort-feature SORT_FEATURE, -sf SORT_FEATURE
                        Feature to sort on. Typically available: gene,
                        transcript, exon.
  --sort-on SORT_ON, -so SORT_ON
                        Characteristic to sort on. Currently available:
                        Length.
  --keep-feature KEEP_FEATURE, -kf KEEP_FEATURE
                        Feature to keep: gene, transcript, exon.
  --split SPLIT, -s SPLIT
                        Where to split --sort-on into groups. Currently
                        available: Quartiles.
  --which-intron-exon WHICH_INTRON_EXON, -wie WHICH_INTRON_EXON
                        Allows you to select a subset of introns/exons (if
                        introns/exons are the feature to keep). Options: all,
                        first, last, internal, first_and_last.
```
