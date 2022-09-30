# ProtMIMO-CodingChallenge

This is a machine learning (for proteins) coding challenge.  It aims to assess general modeling skills as well as paper reading/implementation skills. It is intended to be done in PyTorch. 

## Instructions
The specific task is to use the Multi-Input Multi-Output (MIMO) architecture from [Havasi et al.](https://arxiv.org/abs/2010.06610) for protein function prediction. This architecture aims to replace traditional ensembles by taking in multiple inputs and predicting multiple outputs aiming to match a single distribution at each output head. For inference they input the same value multiple times and take the average of the multiple predictions made by the MIMO model. Check out the first three pages of their paper for more details. 

Some boilerplate code is provided, especially in `ProtMIMO/data_utils.py` which has code for downloading and processing the GFP (fluorescence) data from [Tasks Assessing Protein Embeddings (TAPE)](https://github.com/songlab-cal/tape) into Pandas DataFrames. A `requirements.txt` is also provided.

You are expected to do the following:
<ul>
  <li>Implement a MIMO model in `ProtMIMO/model.py` along with helper modules in `ProtMIMO/modules.py`. We recommend using a MIMO MLP or a MIMO CNN for regression.</li>
  <li>Implement dataloaders that enable you to train and evaluate the MIMO models.</li>
</ul>
