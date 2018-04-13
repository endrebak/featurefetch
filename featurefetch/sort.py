
import pandas as pd

from featurefetch.regions import find_introns

from pyranges import GRanges


splits = {"quartiles": ([0, .25, .5, .75, 1.],
                        "0-25 25-50 50-75 75-100".split())}


merge_features = {"gene": "GeneID", "transcript": "TranscriptID", "exon": "ExonID"}


def sort_features(df, sort_feature, sort_on, split):

    # e.g. Gene, Transcript
    fdf = df.loc[df.Feature == sort_feature]

    if sort_on == "Length":
        length = (fdf.End - fdf.Start)
        fdf.insert(fdf.shape[1], "Length", length)

    split = pd.qcut(fdf[sort_on], splits[split][0], splits[split][1]).astype(str)
    fdf.insert(fdf.shape[1], "Group", split)

    fdf = fdf.sort_values(["Group", sort_on])

    return fdf[["Group", sort_on, merge_features[sort_feature]]]


def sort_and_select(df, sort_feature, sort_on, split, keep_feature, which, exclude=None):

    "Need to sort features, then merge them with original df, lastly"
    "pick them out the feature to keep after using sort order of sort_features"

    merge_col = merge_features[sort_feature]

    sdf = sort_features(df, sort_feature, sort_on, split)
    sdf = sdf.loc[:,[merge_col, "Group", sort_on]]

    if keep_feature == "intron":
        df = find_introns(df)

    if exclude == "intron":
        exclude_df = find_introns(df)
    elif exclude:
        exclude_df = df[df.Feature == exclude]

    kdf = df[df.Feature == keep_feature]

    merged = kdf.merge(sdf, how="right", on=merge_col)
    merged = merged.sort_values(["Group", sort_on])

    if exclude:
        merged.to_csv("merged.csv", sep=" ")
        exclude_df.to_csv("exclude_df.csv", sep=" ")
        mgr = GRanges(merged)
        xgr = GRanges(exclude_df)

        print(mgr)
        print(xgr)
        print(mgr - xgr)

        merged = (mgr - xgr).df
        merged.to_csv("kept.csv", sep=" ")

    return merged
