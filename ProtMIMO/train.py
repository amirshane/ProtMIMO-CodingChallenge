"""Training ProtMIMOOracle for Fluorescence data."""

import os

import torch

from model import ProtMIMOOracle
from data_utils import (
    GFP_SEQ_LEN,
    GFP_ALPHABET,
    get_gfp_dfs,
)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


if __name__ == "__main__":
    try:
        train_df, val_df, test_df = get_gfp_dfs()
    except FileNotFoundError:
        if not os.path.exists("fluorescence.tar.gz"):
            os.system(
                "wget http://s3.amazonaws.com/songlabdata/proteindata/data_pytorch/fluorescence.tar.gz"
            )  # Note: This data can also be downloaded by searching the link above in a browser.
        os.system("tar xzf fluorescence.tar.gz")
        train_df, val_df, test_df = get_gfp_dfs()

    # Implement your training and evaluation loop here.
