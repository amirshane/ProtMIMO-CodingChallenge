"""ProtMIMO model."""

from math import floor

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

from modules import MultiHeadLinear


def seq_encode(seq, alphabet):
    # IMPLEMENT THIS
    # Encode sequences using the alphabet.
    pass


def multi_seq_encode(seqs, alphabet):
    # IMPLEMENT THIS
    # Encode a list of multiple sequences.
    # Hint: Use seq_encode above.
    pass


def batch_seq_encode(batch_seqs, alphabet):
    # IMPLEMENT THIS
    # Encode a batch of lists of multiple sequences.
    # Hint: Use multi_seq_encode from above.
    pass


class ProtMIMOOracle(nn.Module):
    """
    MIMO oracle for proteins.
    """

    def __init__(self):
        # IMPLEMENT THIS
        # Specify parameters and initialize model here.
        pass

    def forward(self, x):
        # IMPLEMENT THIS
        # Define model forward method.
        pass
