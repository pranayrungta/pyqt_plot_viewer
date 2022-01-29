[Program]
action = 'plot-spt'


[Data_Source]
db = 'data.sqlite'
query = '''SELECT N1, aoic
    from spt_dat inner join spt_atr
         on spt_atr.ids=spt_dat.ids'''


[Parameters]
wire = ['static', 'dynamic']
ns = ['0.1', '0.01']
c = ['1']
k = ['2', '4']
n = ['100']
b = ['0', '-0.04', '-0.08', '-0.1']
p = ['0.1', '0.3', '0.5', '0.7', '0.9']


[Plot_Paramters]
set_grid = True
log = 'None'
xlabel = ('$N_1$', {'fontsize': 18})
ylabel = ('<x>', {'fontsize': 18})
xlim = {'xmin': -1.5, 'xmax': 62}
ylim = {'ymin': -1.15, 'ymax': 1.25}
using = lambda df: (df.iloc[:,0], df.iloc[:,1], 'o-')
plot_title = 'auto'
legend_loc = 'right'

