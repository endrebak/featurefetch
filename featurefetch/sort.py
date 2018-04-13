
import pandas as pd

from featurefetch.regions import find_introns

from pyranges import GRanges


splits = {"quartiles": ([0, .25, .5, .75, 1.],
                        "0-25 25-50 50-75 75-100".split())}


merge_features_dict = {"gene": "GeneID", "transcript": "TranscriptID", "exon": "ExonID"}


def add_sort_feature(df, sort_feature, sort_on):

    df = df.loc[df.Feature == sort_feature]
    if sort_on == "Length":
        length = (df.End - df.Start)
        df.insert(df.shape[1], "Length", length)

    return df


def split_feature(df, split, sort_on, sort_feature):

    df = df[df.Feature == sort_feature]
    split_values, split_names = splits[split]
    split = pd.qcut(df[sort_on], split_values, split_names).astype(str)
    df.insert(df.shape[1], "Group", split)

    df = df.sort_values(["Group", sort_on])

    return df[["Group", merge_features_dict[sort_feature]]]
