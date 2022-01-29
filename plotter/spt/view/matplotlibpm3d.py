from __main__ import *

import matplotlib.pyplot as plt
import pandas as pd

def dataframe_title(filename, vertical_on_x, title):
    data = pd.read_csv(filename, sep='\t', index_col=0)
    data.columns = data.columns.astype('float')
    if(vertical_on_x): data = data.transpose()

    if(title=='auto'):
        title = filename[:-4].split('_')
        title = ' '.join(title)
    return data, title


import os
ls=  os.listdir('./')
files = [ filename for filename in ls if(
          all(crit in filename for crit in criteria)
          and os.path.isfile(filename) ) ]


for filename in files:
    print('Plotting :',filename)

    df, title = dataframe_title(filename,vertical_on_x, title)
    plt.figure(figsize=figsize)
    if(title!='None'):plt.title(title)
    plt.xlabel(*xlabel); plt.ylabel(*ylabel)
    plt.xlim(**xlim); plt.ylim(**ylim)

    plt.imshow(df.values, aspect='auto', origin='lower', interpolation = 'none',
       extent=(df.columns.min(),df.columns.max(), df.index.min(),df.index.max()),
       **colorRange )
    plt.colorbar()
    plt.tight_layout()
    if(output=='show'): plt.show()
    else: plt.savefig(f'{filename[:-4]}.{output}')
    plt.close()
print('\nDone !')
