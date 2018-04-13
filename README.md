# Featurefetch

Get and sort features from gtfs. Example query: give me all the introns, sorted
by gene length where the introns are split into quartiles by gene length. Many
more to come.

Will grow organically as I need features, not rushing to finish this.

## Why?

Creating beautiful heatmaps in deeptools. If you have another use case I'd love to hear it.

## Example

(\#\# is stderr, \# stdout)

```bash
featurefetch -g  ~/code/featurefetch/test_data/ensembl.gtf -sf gene -so Length -kf intron -s quartiles -kt longest -O output_folder/ -o outfile.txt
# Parsing gtf.
# Removing all but longest transcript.
# Computing introns.
# Sorting on gene
# Splitting gene into quartiles
head output_folder/exon_last.txt
Chromosome      Feature Source  Start   End     Score   Strand  Frame   GeneID  TranscriptID    ExonNumber      ExonID  Group
1       exon    havana  34554   35174   .       -       .       ENSG00000237613 ENST00000417324 3.0     ENSE00001727627 25-50
1       exon    havana  13221   14409   .       +       .       ENSG00000223972 ENST00000456328 3.0     ENSE00002312635 50-75
1       exon    havana  30976   31097   .       +       .       ENSG00000243485 ENST00000473358 3.0     ENSE00001827679 25-50
1       exon    havana  92230   92240   .       -       .       ENSG00000238009 ENST00000477740 4.0     ENSE00001896976 75-100
1       exon    havana  14404   14501   .       -       .       ENSG00000227232 ENST00000488147 11.0    ENSE00001843071 75-100
1       exon    havana  52473   53312   .       +       .       ENSG00000268020 ENST00000606857 1.0     ENSE00003698237 0-25
1       exon    mirbase 30366   30503   .       +       .       ENSG00000284332 ENST00000607096 1.0     ENSE00003695741 0-25
1       exon    mirbase 17369   17436   .       -       .       ENSG00000278267 ENST00000619216 1.0     ENSE00003746039 0-25
1       exon    havana  69037   71585   .       +       .       ENSG00000186092 ENST00000641515 3.0     ENSE00003813949 50-75
```

## TODO:

* Add feature TSS
* Fix intron code
* Add ways to remove genes with overlapping TSS.
* Add more splits
* Fetch data from UCSC mysql db if no GTF given on command line.

## Usage:

```
usage: featurefetch [-h] --gtf GTF [--outfolder OUTFOLDER] --outfile OUTFILE
                    [--keep-transcript KEEP_TRANSCRIPT]
                    [--sort-feature SORT_FEATURE] [--sort-on SORT_ON]
                    [--keep-feature KEEP_FEATURE] [--split SPLIT]
                    [--exclude-feature EXCLUDE_FEATURE] [--deeptools-output]

Complex fetching and sorting and aggregation of features. (Visit
github.com/endrebak/featurefetch for examples and help.)

optional arguments:
  -h, --help            show this help message and exit
  --gtf GTF, -g GTF     GTF file to fetch features from.
  --outfolder OUTFOLDER, -O OUTFOLDER
                        If --outfolder is given, one featurefile is written to
                        <outfolder>/<feature>.txt for each feature.
  --outfile OUTFILE, -o OUTFILE
                        The file to write the results in.
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
                        Feature to keep: gene, transcript, exon, intron.
  --split SPLIT, -s SPLIT
                        Where to split --sort-on into groups. Currently
                        available: Quartiles.
  --exclude-feature EXCLUDE_FEATURE, -x EXCLUDE_FEATURE
                        Feature to exclude. E.g. if you want the exons (use
                        --keep-feature exon), but do not want any exon that
                        overlaps an intron you can use --exclude intron
  --deeptools-output, -do
                        Write the output in the correct 7-column bed-like
                        format for deeptools computematrix. (#chrom start end
                        name score strand deepTools_group)
```
