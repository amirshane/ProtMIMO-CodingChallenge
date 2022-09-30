"""Test ProtMIMO models."""

import numpy as np
import torch
import torch.nn as nn

from model import ProtMIMOOracle


_test_alphabet = {}
for i, aa in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    _test_alphabet[aa] = i
_test_alphabet["."] = len("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def test_oracle():
    # IMPLEMENT THIS
    # Write a test to verify that ProtMIMOOracle's inputs and outputs are as intended.
    pass


def test_oracle_training():
    # IMPLEMENT THIS
    # Write a test to verify ProtMIMOOracle can fit to some dummy data.
    pass
