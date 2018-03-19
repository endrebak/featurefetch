
from io import StringIO

import pytest

import pandas as pd
import numpy as np

from featurefetch.sort import sort_features, sort_and_select


@pytest.fixture
def expected_sorted_features():

    c = """Group  Length           GeneID
25    0-25      67  ENSG00000278267
36    0-25     137  ENSG00000284332
47    0-25     839  ENSG00000268020
39   25-50    1527  ENSG00000237613
28   25-50    1555  ENSG00000243485
0    50-75    2540  ENSG00000223972
57   50-75    6166  ENSG00000186092
50  75-100    6518  ENSG00000240361
12  75-100   15166  ENSG00000227232
76  75-100   44428  ENSG00000238009"""

    return pd.read_table(StringIO(c), sep="\s+")

def test_sort_features(expected_result_parse_ensembl_gtf, expected_sorted_features):

    df = expected_result_parse_ensembl_gtf

    result = sort_features(df, "gene", "Length", "quartiles")

    pd.testing.assert_frame_equal(result, expected_sorted_features)


def test_sort_and_select(expected_result_parse_ensembl_gtf, expected_result_sort_and_select):

    df = expected_result_parse_ensembl_gtf
    result = sort_and_select(df, "gene", "Length", "quartiles", "exon")

    pd.testing.assert_frame_equal(result, expected_result_sort_and_select)
