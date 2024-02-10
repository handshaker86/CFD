import pandas as pd 
import numpy as np
from pathlib import Path
import json 

def load_json(path:Path):   
    """Load a JSON object from a file"""
    with open(path, "r", encoding="utf8") as f:
        return json.load(f)

class cavity_preprocessor:
    def __init__(self, case_dir: Path):
        self.case_dir = case_dir
        
        self.data = {'vel_top':[],
                     'density':[],
                     'viscosity':[],
                     'height':[],
                     'width':[],
                     'time':[],
                     'x':[],
                     'y':[],
                     'u':[],
                     'v':[]}
        
        self.params = ['vel_top','density','viscosity',
                       'height','width','time',
                       'x','y','u','v']
        
        self.case_params_keys = [
        "vel_top",   
        "density",
        "viscosity",
        "height",
        "width"]
        
        self.case_params = load_json(case_dir/'case.json')
        
    def load_data(self):
        u_file = self.case_dir / "u.npy"
        v_file = self.case_dir / "v.npy"
        u = np.load(u_file)
        v = np.load(v_file)
        
        T = u.shape[0]
        x_max = u.shape[1] 
        y_max = u.shape[2]

        for i in range(T):
            for j in range(x_max):
                for k in range(y_max):
                    self.data['time'].append(0.1 * i)
                    self.data['x'].append(j)
                    self.data['y'].append(k)
                    self.data['u'].append(u[i,j,k])
                    self.data['v'].append(v[i,j,k])
                    # velocity = (u[i,j,k],v[i,j,k])
                    for key in self.case_params_keys:
                        self.data[key].append(self.case_params[key])
        
def transform_data(preprocessor:cavity_preprocessor):
    data = preprocessor.data
    return pd.DataFrame(data)








    


    



        