import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure
from controls import Controls

class UI(QtWidgets.QMainWindow):
    def __init__(self, p): # parameters
        super().__init__()
        self.setWindowTitle("Plot Viewer")
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.setGeometry(100,50,1200,650)
        #=================================================================
        self.controls = Controls(p)
        para_grpBox = QtWidgets.QGroupBox("Parameters")
        para_layout = QtWidgets.QVBoxLayout()
        para_layout.addStretch()
        para_layout.addWidget(self.controls)
        para_layout.addStretch()
        para_grpBox.setLayout(para_layout)
        para_grpBox.setFixedWidth(200)
        #==============================================================
        self.fig = Figure()
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.axes = self.fig.add_subplot(111)
        self.toolbar = NavigationToolbar2QT(self.canvas, self.centralwidget)
        self.fig.tight_layout()
        #create new layout
        plot_layout = QtWidgets.QVBoxLayout()
        plot_layout.addWidget(self.canvas)
        plot_layout.addWidget(self.toolbar)
        plot_grpBox = QtWidgets.QGroupBox("Plot")
        plot_grpBox.setLayout(plot_layout)
        #=================================================================
        horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        horizontalLayout.addWidget(para_grpBox)
        horizontalLayout.addWidget(plot_grpBox)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.statusbar.showMessage('Working...')

    def getComboValue(self):
        print((self.comboBox.currentText(), self.comboBox.currentIndex()))


if __name__ == '__main__':
    p = {'wire': ['static', 'dynamic'],
         'c'   : ['1'],
         'k'   : ['2', '4'],
         'n'   : ['100'],
         'b'   : ['0', '-0.04', '-0.08', '-0.1'],
         'p'   : ['0', '0.1', '0.3', '0.5', '0.7'] }
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = UI(p)
    form.show()
    app.exec_()
    print('done')
