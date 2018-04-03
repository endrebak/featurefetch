
import pandas as pd

def find_introns(df):

    introns_to_concat = []
    for t, tdf in df.groupby("TranscriptID"):
        transcript = tdf.loc[tdf.Feature == "transcript"]
        exons = tdf.loc[tdf.Feature == "exon"]
        exons = exons.sort_values("Start")

        starts = exons.End.shift().iloc[1:]
        ends = exons.Start[1:]

        introns = exons[1:].copy()

        introns.loc[:, "Start"] = starts
        introns.loc[:, "End"] = ends

        introns.loc[:, "Feature"] = "intron"

        introns_to_concat.append(introns)

    return pd.concat(introns_to_concat).reset_index(drop=True)
