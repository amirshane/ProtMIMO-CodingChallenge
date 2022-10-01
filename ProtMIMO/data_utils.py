"""Shared data utils."""

import pandas as pd
from tape.datasets import LMDBDataset


GFP_SEQ_LEN = 237
GFP_AMINO_ACID_VOCABULARY = [
    "A",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "K",
    "L",
    "M",
    "N",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "V",
    "W",
    "Y",
    ".",
]
GFP_ALPHABET = {}
for i, aa in enumerate(GFP_AMINO_ACID_VOCABULARY):
    GFP_ALPHABET[aa] = i


def gfp_dataset_to_df(in_name):
    dataset = LMDBDataset(in_name)
    df = pd.DataFrame(list(dataset)[:])
    df["log_fluorescence"] = df.log_fluorescence.apply(lambda x: x[0])
    return df


def get_gfp_dfs():
    train_df = gfp_dataset_to_df("fluorescence/fluorescence_train.lmdb")
    val_df = gfp_dataset_to_df("fluorescence/fluorescence_valid.lmdb")
    test_df = gfp_dataset_to_df("fluorescence/fluorescence_test.lmdb")
    return train_df, val_df, test_df
