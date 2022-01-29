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

    def set_data(self, df, title):
        self.fig.clear()
        self.ax = self.fig.add_subplot(111)
        if len(df)==0:
            self.ax.text(0.5, 0.5, 'No Data',
                         fontdict={'fontSize':18, 'ha':'center'})
        else:
            im = self.ax.imshow(df.values, aspect='auto', origin='lower',
                interpolation='none', extent=(df.columns.min(),df.columns.max(),
                                              df.index.min(),df.index.max()) )
            self.fig.colorbar(im)
            self.set_plot_param(title)
        self.canvas.draw()

    def set_plot_param(self, title):
        p = self.plot_param
        if('x' in p['log']):self.ax.set_xscale('log')
        if('y' in p['log']):self.ax.set_yscale('log')
        self.ax.set_xlabel(*p['xlabel'])
        self.ax.set_ylabel(*p['ylabel'])

        if(p['plot_title']=='auto'):
            self.ax.set_title(title)
        elif(p['plot_title']!='None'):
            self.ax.set_title(p['plot_title'])

if __name__ == '__main__':
    from plotter.spt.model import test_model
    plot_param = dict( log = 'None',
        xlabel = ( 'Nodes',  ),
        ylabel = ( 'Time',   ),
        plot_title = 'auto' )
    df, title = test_model()
    form = Plotter( plot_param )
    form.set_data(df, title)
    form.show()
