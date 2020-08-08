p = {'wire': ['static', 'dynamic'],
     'c'   : ['1'],
     'k'   : ['2', '4'],
     'n'   : ['100'],
     'b'   : ['0', '-0.04', '-0.08', '-0.1'],
     'p'   : ['0', '0.1', '0.3', '0.5', '0.7'] }

plot_param = dict(
    set_grid = False,  # True   False
    log = 'None', #'None' 'x' 'y' 'xy'

    xlabel = ( r'$N_1$', dict(fontsize=18) ),
    ylabel = ( '<x>',  dict(fontsize=18) ), #{'fontsize':20}

    xlim= dict(),#dict(xmin=-0.1, xmax=1)
    ylim= dict(),#dict(ymin=-0.1, ymax=1)

    # using = lambda df: (df.iloc[:,0], df.iloc[:,1], 'o-'),
    plot_title = 'auto', # 'auto' 'None' 'TITLE'
    legend_loc = 'right', # 'None' 'best', 'right'
)


if __name__ == '__main__':
    from PyQt5 import QtWidgets
    import sys

    app = QtWidgets.QApplication(sys.argv)
    from ui import UI
    ui = UI(p, plot_param)
    ui.show()
    app.exec_()
