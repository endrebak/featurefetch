
from io import StringIO

import pytest

import pandas as pd
import numpy as np

splits = {"quartiles": ([0, .25, .5, .75, 1.],
                        "0-25 25-50 50-75 75-100".split())}

merge_features = {"gene": "GeneID", "transcript": "TranscriptID", "exon": "ExonID"}


def sort_features(df, sort_feature, sort_on, split):

    fdf = df.loc[df.Feature == sort_feature]

    if sort_on == "Length":
        length = (fdf.End - fdf.Start)
        fdf.insert(fdf.shape[1], "Length", length)

    split = pd.qcut(fdf[sort_on], splits[split][0], splits[split][1]).astype(str)
    fdf.insert(fdf.shape[1], "Group", split)

    fdf = fdf.sort_values(["Group", sort_on])

    return fdf[["Group", sort_on, merge_features[sort_feature]]]


def sort_and_select(df, sort_feature, sort_on, split, keep_feature):

    "Need to sort features, then merge them with original df, lastly"
    "pick them out the feature to keep after using sort order of sort_features"

    pass



def test_sort_features(expected_result_parse_ensembl_gtf):

    df = expected_result_parse_ensembl_gtf

    result = sort_features(df, "gene", "Length", "quartiles")

    print(result)

    assert 0
