import pandas as pd
import sqlite3

def get_nvsx(vals, verbose=False):
    where = ' AND '.join(f"{k}='{v}'" for k,v in vals.items())
    query = f'''SELECT N1, X
    from nvsx inner join atr
         on atr.ids=nvsx.ids
    where {where}'''
    if verbose:print(query)
    conn = sqlite3.connect('data.sqlite')
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def get_data(variable, const_vals):
    dfs = {}
    const = const_vals.copy()
    key, vals = variable
    for val in vals:
        const[key]=val
        dfs[f'{key}={val}']=get_nvsx(const, verbose=False)
    title = '  '.join(f'{k}={v}' for k,v in const_vals.items())
    return dfs, title

def test_get_data():
    variable = ('wire', ['static', 'dynamic'])
    const_vals = {'c': '1', 'n': '100', 'k': '2', 'b': '0', 'p': '0'}
    dfs, title = get_data(variable, const_vals)
