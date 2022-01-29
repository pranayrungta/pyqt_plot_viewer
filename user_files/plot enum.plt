[Program]
action = 'plot-enum'


[Data_Source]
db = 'data.sqlite'
query = 'SELECT N1, X from nvsx where id={id}'


[Parameters]
wire = [{'id':1},
    {'id':2},
    {'id':3},
   ]


[Plot_Paramters]
set_grid = True
log = 'None' # 'x' 'y' 'xy'
xlabel = ('$N_1$', {'fontsize': 18})
ylabel = ('<x>', {'fontsize': 18})
xlim = {'xmin': -1.5, 'xmax': 62}
ylim = {'ymin': -1.15, 'ymax': 1.25}
using = lambda df: (df.iloc[:,0], df.iloc[:,1], 'o-')
plot_title = 'auto' # 'None' 'sample title'
legend_loc = 'right'

