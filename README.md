# Introduction

This repository contains the materials for the paper titled: Applied Machine-Learning Models to Identify Spectral Sub-Types of M Dwarfs from Photometric Surveys (https://iopscience.iop.org/article/10.1088/1538-3873/acc974).

### CDS8 Prediction Results
The results are provided in the directory `cds8_res/`. It can be downloaded by:

```
curl -o cds8_pred_results.csv https://raw.githubusercontent.com/sirinrats/ml-md-class/main/cds8_res/cds8_pred_results.csv
```

### Models
The default models are provided in the directory `models/`.

The models trained with Random Undersampling (RUS) are provided in the directory `models/models_rus`.

### Confusion Matrices
All confusion matrices are provided in the directory `cmats`.

### Examples of input data (to be predicted) 
See examples of input (format and order of feature columns used for each model) in the directory `example_input/`.

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
`git clone https://github.com/sirinrats/ml-md-class.git`

### Run the application
```
cd ml-md-class
python application.py
```

# Model Accuracy
Expected Accuracy within ±1 Sub-Type (%)

| Model | (default) | (RUS) |
|-------| --------- |-------|
| Model 1  | 99.6  | 99.5 |
| Model 2  | 99.4  | 99.4 |
| Model 3  | 92.6  | 92.4 |
| Model 4  | 92.4  | 92.4 |
| Model 5  | 74.2  | 71.3 |
| Model 6  | 49.2  | 41.9 |


# Contact
For any questions or concerns related to this project, please contact:

sirinrat@narit.or.th
sithajan.s@gmail.com
