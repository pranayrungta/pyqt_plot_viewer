[Program]
action = 'plot-spt'


[Data_Source]
db = 'data.sqlite'
query = '''SELECT node, time, value
    from spt_dat inner join spt_atr
         on spt_atr.ids=spt_dat.ids'''


[Parameters]
wire = ['static', 'dynamic', 'regular']
c = ['1']
k = ['2', '4']
n = ['100']
b = ['-0.035', '0' ]
p = ['0.8', '0']
N1 = ['1', '30']


[Plot_Paramters]
log = 'None'
xlabel = ('$time$', {'fontsize': 18})
ylabel = ('$N_i$', {'fontsize': 18})
plot_title = 'auto'
