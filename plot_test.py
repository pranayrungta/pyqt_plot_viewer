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

def get_data(p, vary, const_vals):
    dfs = {}
    allp = p.copy()
    k,v = vary, allp.pop(vary)
    for vr in v:
        const_vals[k]=vr
        # print(const_vals)
        dfs[f'{vary}={vr}']=get_nvsx(const_vals, verbose=False)
    return dfs

def test_get_data():
    p = {'wire': ['static', 'dynamic'],
         'c'   : ['1'],
         'k'   : ['2', '4'],
         'n'   : ['100'],
         'b'   : ['0', '-0.04', '-0.08', '-0.1'],
         'p'   : ['0', '0.1', '0.3', '0.5', '0.7'] }
    const_vals = {k:v[0] for k,v in p.items()}
    vary = 'b'
    dfs = get_data(p, vary, const_vals)
    return dfs

def plot_param():
    p = dict(
        set_grid = False,  # True   False
        log = 'None', #'None' 'x' 'y' 'xy'

        xlabel = ( r'$N_1$', dict(fontsize=25) ),
        ylabel = ( '<x>',  dict(fontsize=25) ), #{'fontsize':20}

        xlim= dict(),#dict(xmin=-0.1, xmax=1)
        ylim= dict(),#dict(ymin=-0.1, ymax=1)

        # using = lambda df: (df.iloc[:,0], df.iloc[:,1], 'o-'),
        plot_title = 'auto', # 'auto' 'None' 'TITLE'
        legend_loc = 'best', # 'None' 'best', 'right'
    )
    return p

if __name__=='__main__':
    pass
