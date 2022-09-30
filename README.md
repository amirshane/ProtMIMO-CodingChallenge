# ProtMIMO-CodingChallenge

This is a machine learning (for proteins) coding challenge.  It aims to assess general modeling skills as well as paper reading/implementation skills. It is intended to be done in PyTorch. 

## Instructions
The specific task is to use the Multi-Input Multi-Output (MIMO) architecture from [Havasi et al.](https://arxiv.org/abs/2010.06610) for protein function prediction. This architecture aims to replace traditional ensembles by taking in multiple inputs and predicting multiple outputs aiming to match a single distribution at each output head. For inference they input the same value multiple times and take the average of the multiple predictions made by the MIMO model. Check out the first three pages of their paper for more details. 

Some boilerplate code is provided, especially in `ProtMIMO/data_utils.py` which has code for downloading and processing the GFP (fluorescence) data from [Tasks Assessing Protein Embeddings (TAPE)](https://github.com/songlab-cal/tape) into Pandas DataFrames. A `requirements.txt` is also provided.

You are expected to do the following:
<ul>
  <li>Implement a MIMO model in along with helper modules. We recommend using a MIMO MLP and/or a MIMO CNN (preferably both).</li>
  <li>Implement dataloaders that enable you to train and evaluate the MIMO models.</li>
  <li>Train the MIMO models along with a traditional ensemble of regression models to compare to.</li>
  <li>Evaluate the MIMO models and the ensembles and compare their performance on metrics such as mean-squared error (MSE), Pearson correlation, Spearman Rho, and diversity (which can be measured by looking at residual correlations).</li>
</ul>
