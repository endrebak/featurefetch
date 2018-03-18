import pytest

import pandas as pd

from io import StringIO

# def read_gtf(path):

#     df = pd.read_table(path, sep="\t", comment="#", header=None)

#     return df

def parse_gtf(path):

    """
    seqname - name of the chromosome or scaffold; chromosome names can be given with or without the 'chr' prefix. Important note: the seqname must be one used within Ensembl, i.e. a standard chromosome name or an Ensembl identifier such as a scaffold ID, without any additional content such as species or assembly. See the example GFF output below.
    source - name of the program that generated this feature, or the data source (database or project name)
    feature - feature type name, e.g. Gene, Variation, Similarity
    start - Start position of the feature, with sequence numbering starting at 1.
    end - End position of the feature, with sequence numbering starting at 1.
    score - A floating point value.
    strand - defined as + (forward) or - (reverse).
    frame - One of '0', '1' or '2'. '0' indicates that the first base of the feature is the first base of a codon, '1' that the second base is the first base of a codon, and so on..
    attribute - A semicolon-separated list of tag-value pairs, providing additional information about each feature.
    """

    df = pd.read_table(path, sep="\t", comment="#", header=None, names="Chromosome Source Feature Start End Score Strand Frame Attribute".split())

    extract = _fetch_gene_transcript_exon_id(df.Attribute)
    extract.columns = "GeneID TranscriptID ExonNumber ExonID".split()

    extract.ExonNumber = extract.ExonNumber.astype(float)

    df = pd.concat([df["Chromosome Feature Source Start End Score Strand Frame".split()],
                        extract], axis=1)

    return df


def _fetch_gene_transcript_exon_id(attribute):

    no_quotes = attribute.str.replace('"', '').str.replace("'", "")
    return no_quotes.str.extract("gene_id.?(.+?);(?:.*transcript_id.?(.+?);)?(?:.*exon_number.?(.+?);)?(?:.*exon_id.?(.+?);)?", expand=True)


def test_parse_gencode_gtf(gencode_gtf, expected_result_parse_gencode_gtf):

    result = parse_gtf(gencode_gtf)

    print(result.head())
    print(expected_result_parse_gencode_gtf.head())

    print(result.dtypes)
    print(expected_result_parse_gencode_gtf.dtypes)

    assert result.equals(expected_result_parse_gencode_gtf)



def test_parse_ensembl_gtf(ensembl_gtf, expected_result_parse_ensembl_gtf):

    result = parse_gtf(ensembl_gtf)

    print(result.head())
    print(expected_result_parse_ensembl_gtf.head())

    print(result.dtypes)
    print(expected_result_parse_ensembl_gtf.dtypes)
    # result.to_csv("test_data/expected_result_parse_ensembl_gtf.txt", sep=" ", index=False, header=True)


    assert result.equals(expected_result_parse_ensembl_gtf)
