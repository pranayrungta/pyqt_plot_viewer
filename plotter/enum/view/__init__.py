def UI(p, plot_param):
    from .controls import Controls
    from .plot import Plotter
    from plotter.utils.ft import BaseUI
    controls = Controls(p)
    plotter = Plotter(plot_param)
    return BaseUI(controls, plotter)

