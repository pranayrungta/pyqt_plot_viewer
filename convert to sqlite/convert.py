import os
import pandas as pd


def data(root, filename):
    filepath = os.path.join(root,filename)
    df = pd.read_csv(filepath, sep='\t', skiprows=2)
    df.rename(columns = {df.columns[0]:df.columns[0].strip('# ')},
              inplace=True)

    para = filename[:-4].split('_')
    param = {'wire':para.pop(0)}
    param.update(map(lambda val:val.split('='), para))
    return df, param

def read_data():
    ind = 0
    all_param, all_data = [], []
    for root,direc,files in os.walk('./'):
        print(root)
        for filename in files:
            if '=' in filename:
                df, param = data(root, filename)
                df['ids'] = ind
                param['ids'] = ind
                all_param.append(param)
                all_data.append(df)
                ind += 1
    all_param = pd.DataFrame(all_param)
    all_param.set_index('ids', inplace=True)
    all_data = pd.concat(all_data)
    all_data.set_index('ids', inplace=True)
    return all_param, all_data

def sample_filenames():
    i=0
    for root,direc,files in os.walk('./'):
        for filename in files:
            if '=' in filename:
                print(filename)
                i+=1
                if i==5:
                    return root, filename
    # root, filename = sample_filenames()


def main():
    param, sdata = read_data()
    import sqlite3
    con = sqlite3.connect('data.sqlite')
    param.to_sql('atr', con)
    sdata.to_sql('data',con)
