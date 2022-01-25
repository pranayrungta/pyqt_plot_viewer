import os
import pandas as pd


def data(root, filename):
    filepath = os.path.join(root,filename)
    df = pd.read_csv(filepath, sep='\t', skiprows=2)
    df.rename(columns = {df.columns[0]:df.columns[0].strip('# ')},
              inplace=True)

    para = filename[:-4].split('_')
    param = {'type':para[0]}
    param.update(map(lambda val:val.split('='), para[1:]))
    return df, param

def read_data():
    ind = 0
    all_param, all_data = [], []
    for root,direc,files in os.walk('./'):
        print(root)
        for filename in files:
            if '=' in filename:
                df, param = data(root, filename)
                df['param_id'] = ind
                param['param_id'] = ind
                all_param.append(param)
                all_data.append(df)
                ind += 1
    all_param = pd.DataFrame(all_param)
    all_param.set_index('param_id', inplace=True)
    all_data = pd.concat(all_data)
    all_data.set_index('param_id', inplace=True)
    return all_param, all_data



param, sdata = read_data()
import sqlite3
con = sqlite3.connect('data.sqlite')
param.to_sql('param', con)
sdata.to_sql('data',con)