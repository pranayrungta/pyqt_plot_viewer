[Program]
action = 'plot'


[Data_Source]
db = 'data.sqlite'
query = '''SELECT N1, X
    from nvsx inner join atr
         on atr.ids=nvsx.ids'''


[Parameters]
wire = ['static', 'dynamic']
c = ['1']
k = ['2', '4']
n = ['100']
b = ['0', '-0.04', '-0.08', '-0.1']
p = ['0', '0.1', '0.3', '0.5', '0.7']


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

