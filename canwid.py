# import matplotlib
# matplotlib.use("Qt5Agg")
# import sys

# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
# from matplotlib.figure import Figure

# import pandas as pd
# import numpy as np

# from PyQt5 import  QtWidgets, uic  # works for pyqt5
# from PyQt5.Qt import  QVBoxLayout




# class PlotSeries(QtWidgets.QMainWindow, Ui_MainWindow):

#     def __init__(self):
#         QtWidgets.QMainWindow.__init__(self)
#         Ui_MainWindow.__init__(self)
#         self.setupUi(self)

#                 #create figure
#         self.fig=Figure()

#         self.axes = self.fig.add_subplot(111)
#         self.axes.grid()



#         self.canvas=FigureCanvas(self.fig)
#         #add plot toolbar from matplotlib
#         self.toolbar = NavigationToolbar(self.canvas, self)

#         #create new layout
#         layout = QVBoxLayout()

#         layout.addWidget(self.canvas)
#         layout.addWidget(self.toolbar)

#         #add layout to qwidget
#         self.plotlayout=self.widgetplot.setLayout(layout)

#         #draw the canvas !
#         self.canvas.draw()
#         #now let's call widget
#         self.plot_basegraph()


#     def plot_basegraph(self):
#         #create simple time series
#         for i in range(0,5):
#             ts=pd.Series(np.random.randn(2000), index=pd.date_range('1/1/2015',freq='h', periods=2000),name="series "+str(i))
#             if i==0:
#                 self.stackTSPD=ts.to_frame()
#             else:
#                 self.stackTSPD=self.stackTSPD.join(ts.to_frame(),how='inner')
#         print(matplotlib.__version__)

#         self.axes.clear()
#         self.axes.grid()

#         for i in self.stackTSPD.columns.values:
#             t=self.stackTSPD.index.to_pydatetime()

#             y=self.stackTSPD[i].values
#             self.axes.plot(t,y, label=i)










import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure


class MplCanvas:

    def __init__(self, parent):
        self.fig = Figure(figsize=(8,6))
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.axes = self.fig.add_subplot(111)
        self.toolbar = NavigationToolbar2QT(self.canvas, parent)
        #create new layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        self.layout = layout

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)


        self.sc = MplCanvas(self.centralwidget)
        horizontalLayout.addLayout(self.sc.layout)
        self.sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
