
from io import StringIO

from featurefetch.regions import find_introns

import pytest

import pandas as pd
import numpy as np


@pytest.fixture
def single_exon():

    c = """Chromosome Feature Source Start End Score Strand Frame GeneID TranscriptID ExonNumber ExonID
1 transcript mirbase 17369 17436 . - . ENSG00000278267 ENST00000619216
1 exon mirbase 17369 17436 . - . ENSG00000278267 ENST00000619216 1.0 ENSE00003746039"""

    return pd.read_table(StringIO(c), sep=" ")

@pytest.fixture
def reverse_complex():

    c = """Chromosome Feature Source Start End Score Strand Frame GeneID TranscriptID ExonNumber ExonID
1 transcript ensembl 120725 133723 . - . ENSG00000238009 ENST00000610542
1 exon ensembl 133374 133723 . - . ENSG00000238009 ENST00000610542 1.0 ENSE00003748456
1 exon ensembl 129055 129223 . - . ENSG00000238009 ENST00000610542 2.0 ENSE00003734824
1 exon ensembl 120874 120932 . - . ENSG00000238009 ENST00000610542 3.0 ENSE00003740919"""

    return pd.read_table(StringIO(c), sep=" ")

@pytest.fixture
def expected_reverse_complex():

    c = """Chromosome Feature Source Start End Score Strand Frame GeneID TranscriptID ExonNumber ExonID
1 intron ensembl 120725 120874.0 . - . ENSG00000238009 ENST00000610542 3.0 ENSE00003740919
1 intron ensembl 120932 129055.0 . - . ENSG00000238009 ENST00000610542 3.0 ENSE00003740919
1 intron ensembl 129223 133374.0 . - . ENSG00000238009 ENST00000610542 2.0 ENSE00003734824"""

    return pd.read_table(StringIO(c), sep=" ")

@pytest.fixture
def forward_simple():

    c = """Chromosome Feature Source Start End Score Strand Frame GeneID TranscriptID ExonNumber ExonID
1 transcript havana 29554 31097 . + . ENSG00000243485 ENST00000473358
1 exon havana 29554 30039 . + . ENSG00000243485 ENST00000473358 1.0 ENSE00001947070
1 exon havana 30564 30667 . + . ENSG00000243485 ENST00000473358 2.0 ENSE00001922571
1 exon havana 30976 31097 . + . ENSG00000243485 ENST00000473358 3.0 ENSE00001827679"""

    return pd.read_table(StringIO(c), sep=" ")

@pytest.fixture
def expected_forward_simple():

    c = """Chromosome Feature Source Start End Score Strand Frame GeneID TranscriptID ExonNumber ExonID
1 1 intron havana 30039 30564.0 . + . ENSG00000243485 ENST00000473358 1.0 ENSE00001947070
2 1 intron havana 30667 30976.0 . + . ENSG00000243485 ENST00000473358 2.0 ENSE00001922571"""

    return pd.read_table(StringIO(c), sep=" ", index_col=0)


# @pytest.mark.parametrize("df,expected", [(forward_simple, None)])
# wtf does this test fail?
def test_find_introns_forward_simple(forward_simple, expected_forward_simple): #, expected):

    df = forward_simple

    # print(df)
    introns = find_introns(df)
    cols_to_compare = "Start End".split()

    introns_subset = introns[cols_to_compare]
    expected_subset = expected_forward_simple[cols_to_compare]

    assert list(introns_subset.Start.values) == list(expected_subset.Start.values)
    assert list(introns_subset.End.values) == list(expected_subset.End.values)


# def test_find_introns_reverse_complex(reverse_complex, expected_reverse_complex): #, expected):

#     df = reverse_complex

#     introns = find_introns(df)

#     cols_to_compare = "Start End".split()

#     introns_subset = introns[cols_to_compare]
#     expected_subset = expected_reverse_complex[cols_to_compare]

#     assert list(introns_subset.Start.values) == list(expected_subset.Start.values)
#     assert list(introns_subset.End.values) == list(expected_subset.End.values)


def test_find_introns_single_exon(single_exon): #, expected_reverse_complex): #, expected):

    df = single_exon

    introns = find_introns(df)

    assert introns.empty # single transcripts that are equal to exon have no introns
