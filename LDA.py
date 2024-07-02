import yaml
from tqdm import tqdm 
from pathlib import Path

import pandas as pd

import gensim

'''
conf_2017_2020 = pd.json_normalize(yaml.safe_load(Path("data/2017-2020.yml").read_text()))
conf_2021_2024 = pd.read_json("data/post-2020.json")

data = pd.concat([conf_2017_2020, conf_2021_2024])
data.to_csv("data/all-data.csv", index=False)
'''

