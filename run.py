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


if __name__ == '__main__':
    from controller import interactive_plot
    interactive_plot(p, plot_param)

