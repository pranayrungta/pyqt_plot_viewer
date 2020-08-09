p = {'wire': ['static', 'dynamic'],
     'c'   : ['1'],
     'k'   : ['2', '4'],
     'n'   : ['100'],
     'b'   : ['0', '-0.04', '-0.08', '-0.1'],
     'p'   : ['0', '0.1', '0.3', '0.5', '0.7'] }


plot_param = dict(
    set_grid = True,  # True   False
    log = 'None', #'None' 'x' 'y' 'xy'

    xlabel = ( r'$N_1$', dict(fontsize=18) ),
    ylabel = ( '<x>',  dict(fontsize=18) ), #{'fontsize':20}

    xlim= dict(xmin=-1.5, xmax=62),
    ylim= dict(ymin=-1.15, ymax=1.25),

    using = lambda df: (df.iloc[:,0], df.iloc[:,1], 'o-'),
    plot_title = 'auto', # 'auto' 'None' 'TITLE'
    legend_loc = 'right', # 'None' 'best', 'right'
)

def test_get_data():
    from model import get_data
    variable = 'b', ['0', '-0.04', '-0.08', '-0.1']
    const_vals = {'c': '1', 'n': '700', 'k': '2',
                  'wire': 'static', 'p': '0.5'}
    dfs, title = get_data(variable, const_vals)
    return dfs, title


def test_get_nvsx():
    from model import get_nvsx
    vals = {'c': '1', 'n': '700', 'k': '2', 'b': '0'
            'wire': 'static', 'p': '0.5'}
    df = get_nvsx(vals, verbose=True)
    return df
