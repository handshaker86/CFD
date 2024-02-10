from preprocess import cavity_preprocessor,load_json,transform_data
import pandas as pd
from pathlib import Path
from autogluon.tabular import TabularDataset, TabularPredictor

path = Path("D:/CFDBench/dataset/cavity/bc/case0000")
preprocessor = cavity_preprocessor(path)
preprocessor.load_data()

train_data =  transform_data(preprocessor)

u_predictor = TabularPredictor(label='u', problem_type='regression')
# v_predictor = TabularPredictor(label='v', problem_type='regression')

u_predictor = u_predictor.fit(train_data,presets='high_quality')
# v_predictor = v_predictor.fit(train_data,presets='high_quality')




