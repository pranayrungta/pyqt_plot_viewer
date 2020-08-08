import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtWidgets
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

    def set_data(self, dfs, plot_param):
        self.ax.clear()
        for label, df in dfs.items():
            c = df.columns
            x,y = df[c[0]], df[c[1]]
            self.ax.plot( x, y, 'o-', label=label)
        self.set_plot_param(plot_param)
        self.canvas.draw()

    def set_plot_param(self, p):
        self.ax.grid(p['set_grid'])

        if('x' in p['log']):self.ax.set_xscale('log')
        if('y' in p['log']):self.ax.set_yscale('log')
        self.ax.set_xlabel(*p['xlabel'])
        self.ax.set_ylabel(*p['ylabel'])
        self.ax.set_xlim(**p['xlim'])
        self.ax.set_ylim(**p['ylim'])

        if(p['plot_title']=='auto'):
            self.ax.set_title('title in development')
        elif(p['plot_title']!='None'):
            self.ax.set_title(p['plot_title'])
        if(p['legend_loc']!='None'):
            self.ax.legend( loc=p['legend_loc'] )
        self.fig.tight_layout()



if __name__ == '__main__':
    from plot_test import test_get_data, plot_param
    dfs = test_get_data()
    p = plot_param()

    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = Plotter()
    form.set_data(dfs)
    # form.set_plot_param(**p)
    form.show()
    app.exec_()
    print('done')
