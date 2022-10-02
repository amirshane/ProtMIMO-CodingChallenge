# ProtMIMO-CodingChallenge

This is a machine learning (for proteins) coding challenge.  It aims to assess general modeling skills as well as paper reading/implementation skills. It is intended to be done in PyTorch. 

## Instructions
The task is to use the Multi-Input Multi-Output (MIMO) architecture from [Havasi et al.](https://arxiv.org/abs/2010.06610) for protein function prediction. This architecture attempts to replace traditional ensembles by taking in multiple inputs and predicting multiple outputs aiming to match a single distribution at each output head. For inference they input the same value multiple times and take the average of the multiple predictions made by the MIMO model. Check out the first three pages of their paper for more details. 

Some code for working with the data is provided in `ProtMIMO/data_utils.py`, which has methods for downloading and loading the GFP (fluorescence) data from [Tasks Assessing Protein Embeddings (TAPE)](https://github.com/songlab-cal/tape) as Pandas DataFrames. There are also template files for modeling code in `ProtMIMO/model.py` and for training code in `ProtMIMO/train.py`. A `requirements.txt` is also provided. To install PyTorch with e.g., GPU support, we recommend referencing [PyTorch's official installation materials](https://pytorch.org/get-started/locally/). To help manage imports when e.g., working with integrated development environments (IDEs) such as Visual Studio Code, we recommend installing this project as a Python package using the command `pip3 install -e .` in the project's root directory. While waiting for the requirements to install, we recommend you read the paper.

We recommend you write clean code that is well-documented, organized, and utilizes helper functions. You are expected to do the following in 3 hours or less and you may use any resources available to you (except asking someone else for help or finding an existing solution):
<ol>
  <li>Load the data as Pandas DataFrames and investigate the columns "primary", "log_fluorescence", and "num_mutations". Create a brief summary of the data by creating histograms of the log fluorescence values and the number of mutations in both the train set and the test set. Do you notice anything interesting? You will be predicting log fluoresence from the primary sequences of the proteins, which is in the column "primary".</li>
  <li>As a first pass, implement linear regression to get a baseline value for the metrics of interest: mean-squared error (MSE), Pearson correlation, Spearman Rho, and diversity (this can be measured by looking at residual correlations).</li>
  <li>Implement a MIMO model; we recommend using a MIMO MLP and/or a MIMO CNN.</li>
  <li>Implement dataloaders and helper methods that enable you to train and evaluate the MIMO models.</li>
  <li>Train a 3-input 3-output MIMO model along with a traditional ensemble of 3 regression models to compare to.</li>
  <li>Evaluate the MIMO models and the ensembles and compare their performance on the aforementioned metrics.</li>
  <li>Create visuals such as tables of the metrics observed for the different models as well as plots of the predictions vs. the true fluoresence values. You can put them in the README or in a slide show on Google Drive.</li>
</ol>
