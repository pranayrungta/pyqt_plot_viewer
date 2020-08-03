import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure

class Plotter(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(Plotter, self).__init__(*args, **kwargs)
        self.fig = Figure()
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        plot_layout = QtWidgets.QVBoxLayout()
        plot_layout.addWidget(self.canvas)
        plot_layout.addWidget(self.toolbar)
        self.setLayout(plot_layout)

    def set_data(self, dfs):
        self.ax.clear()
        for label, df in dfs.items():
            c = df.columns
            x,y = df[c[0]], df[c[1]]
            self.ax.plot( x, y, 'o-', label=label)

    def set_plot_param(self, **p):
        self.ax.grid(p['set_grid'])

        if('x' in p['log']):self.ax.set_xscale('log')
        if('y' in p['log']):self.ax.set_yscale('log')
        self.ax.set_xlabel(*p['xlabel'])
        self.ax.set_ylabel(*p['ylabel'])
        self.ax.set_xlim(**p['xlim'])
        self.ax.set_ylim(**p['ylim'])

        if(p['plot_title']=='auto'):
            self.ax.set_title('title in development')
        elif(plot_title!='None'):
            self.ax.set_title(p['plot_title'])
        if(p['legend_loc']!='None'):
            self.ax.legend( loc=p['legend_loc'] )
        self.fig.tight_layout()


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

if __name__ == '__main__':
    from plot_test import test_get_data
    dfs = test_get_data()
    p = plot_param()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = Plotter()
    form.set_data(dfs)
    form.set_plot_param(**p)
    form.show()
    app.exec_()
    print('done')
