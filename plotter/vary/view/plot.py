from PyQt5 import QtWidgets
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import (
         FigureCanvasQTAgg, NavigationToolbar2QT)
from matplotlib.figure import Figure

class Plotter(QtWidgets.QWidget):
    def __init__(self, plot_param):
        super(Plotter, self).__init__()
        self.fig = Figure(tight_layout=True)
        self.plot_param = plot_param
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        plot_layout = QtWidgets.QVBoxLayout()
        plot_layout.addWidget(self.canvas)
        plot_layout.addWidget(self.toolbar)
        self.setLayout(plot_layout)

    def set_data(self, dfs, title):
        self.ax.clear()
        for label, df in dfs.items():
            using = self.plot_param['using']
            self.ax.plot( *using(df), label=label)
        self.set_plot_param(title)
        self.canvas.draw()

    def set_plot_param(self, title):
        p = self.plot_param
        self.ax.grid(p['set_grid'])

        if('x' in p['log']):self.ax.set_xscale('log')
        if('y' in p['log']):self.ax.set_yscale('log')
        self.ax.set_xlabel(*p['xlabel'])
        self.ax.set_ylabel(*p['ylabel'])
        self.ax.set_xlim(**p['xlim'])
        self.ax.set_ylim(**p['ylim'])

        if(p['plot_title']=='auto'):
            self.ax.set_title(title)
        elif(p['plot_title']!='None'):
            self.ax.set_title(p['plot_title'])
        if(p['legend_loc']!='None'):
            self.ax.legend( loc=p['legend_loc'] )



if __name__ == '__main__':
    from plotter.tests import test_get_data, plot_param
    dfs, title = test_get_data()

    app = QtWidgets.QApplication([])
    form = Plotter( plot_param )
    form.set_data(dfs, title)
    form.show()
    app.exec_()
    print('done')
