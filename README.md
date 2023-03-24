# Introduction
### CDS8 Prediction Results
The results are provided in the directory `cds8_res/`. It can also be downloaded by:

`curl -o cds8_pred_results.csv https://raw.githubusercontent.com/sirinrats/ml-mdwarf/main/cds8_res/cds8_pred_results.csv`

### Models
Models are provided in the directory `models/` 

### Input data (to be predicted) 
See examples of input (format and order of feature columns used for each model) in the directory `data_input/` 

# Setup
### Install Anaconda
See: https://www.anaconda.com/

### Create environment
```
conda create -n mlmdwarf python=3.9.7
conda activate mlmdwarf
```

### Install the required packages
```
conda install numpy==1.20.3 scipy==1.7.3 pandas==1.4.1 joblib==1.1.0 scikit-learn==1.0.2
conda install -c conda-forge imbalanced-learn==0.9.0
```

### Clone the repository
`git clone https://github.com/sirinrats/ml-mdwarf.git`

### Run the application
```
cd ml-mdwarf
python application.py
```
