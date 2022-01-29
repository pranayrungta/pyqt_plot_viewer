from PyQt5 import QtWidgets
from plotter.spt.view import UI
from plotter.spt.model import Model

class MyApp:
    def __init__(self, wd, config): # parameters
        # self.wd = wd
        self.ui = UI(config['Parameters'], config['Plot_Paramters'])
        self.model = Model(wd, config['Data_Source'])
        self.ui.newValueSelected.connect(self.plot_interactive)
        self.ui.newValueSelected.emit()
        self.ui.show()

    def plot_interactive(self):
        vals = self.ui.controls.get_values()
        df, title = self.model.get_data(vals)
        self.ui.plotter.set_data(df, title)


def interactive_plot(wd, config):
    app = QtWidgets.QApplication([])
    myapp = MyApp(wd, config)
    app.exec_()
