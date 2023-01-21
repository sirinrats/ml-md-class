import pandas as pd
import joblib

# read input data
features = pd.read_csv('data_input/model1_example_input.csv')

# load model
model_filepath = 'models/pipe_model1_rf.joblib'
print('... loading model: ', model_filepath)
pipeline_load = joblib.load(model_filepath)

# make prediction
y_pred = pipeline_load.predict(features.values)
print('preditions: ', y_pred)