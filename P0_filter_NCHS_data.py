'''
Filters metadata from data.cdc.gov so only NCHS remains,
returns a nicely formated CSV
'''

import json
import pandas as pd

f_src = 'data.json'

JS = json.load(open(f_src))
df = pd.DataFrame(JS['dataset'])
df = df.set_index('landingPage')

df['category'] = df['theme'].fillna("x").apply(lambda x:x[0])

idx = df['category'] == "NCHS"
df = df[idx]

print(df)
