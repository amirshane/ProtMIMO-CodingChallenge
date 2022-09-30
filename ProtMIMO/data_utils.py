"""Shared data utils."""

import copy
from math import ceil

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
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


def create_batched_train_data():
    # IMPLEMENT THIS
    # Batch data for training.
    pass


def create_batched_eval_data(test_df, num_inputs, bs, feature_name):
    # IMPLEMENT THIS
    # Batch data for evaluation.
    pass


def create_plot(targets, preds, title, path, feature_name, show_plot=False):
    plt.figure(figsize=(8, 6))
    plt.scatter(targets, preds, alpha=0.15)
    plt.xlabel(f"True {feature_name}")
    plt.ylabel(f"Predicted {feature_name}")
    plt.title(title)
    plt.savefig(path)
    if show_plot:
        plt.show()
