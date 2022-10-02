"""ProtMIMO model."""

import torch
import torch.nn as nn
import torch.nn.functional as F


class ProtMIMOOracle(nn.Module):
    """
    MIMO regression oracle for proteins.
    Input: Batched tuples of protein sequences.
    Output: Batched tuples of protein fluorescence predictions.
    """

    def __init__(self):
        # Specify parameters and initialize model here.
        pass

    def forward(self, x):
        # Define model forward method.
        pass
