import pytest

import pandas as pd

from io import StringIO

from featurefetch.parse import parse_gtf, _fetch_gene_transcript_exon_id

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
