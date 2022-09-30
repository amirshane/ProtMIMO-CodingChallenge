"""Training ProtMIMOOracle for Fluorescence data."""

import os
import argparse
import json
import time

import pandas as pd
import torch
from scipy.stats import spearmanr, pearsonr
from sklearn.metrics import mean_squared_error
from pprint import pprint

from model import ProtMIMOOracle
from data_utils import (
    GFP_SEQ_LEN,
    GFP_ALPHABET,
    get_gfp_dfs,
    create_batched_train_data,
    create_batched_eval_data,
    create_plot,
)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def get_gfp_metrics():
    # IMPLEMENT THIS
    # Use this method to compute metrics such as MSE, Spearman Rho, and Pearson correlation.
    pass


if __name__ == "__main__":
    try:
        train_df, val_df, test_df = get_gfp_dfs()
    except FileNotFoundError:
        os.system(
            "wget http://s3.amazonaws.com/songlabdata/proteindata/data_pytorch/fluorescence.tar.gz"
        )
        os.system("tar xzf fluorescence.tar.gz")
        train_df, val_df, test_df = get_gfp_dfs()

    # IMPLEMENT THIS
    # Implement your training and evaluation loop here.
