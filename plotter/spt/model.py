from plotter.utils.bk import BaseModel

class Model(BaseModel):
    def __init__(self, wd, data_source):
        super(Model, self).__init__(wd, data_source)

    def get_data(self, vals):
        where = ' AND '.join(f"{k}='{v}'" for k,v in vals.items())
        query = f'{self.query} \n where {where}'
        df = self.read_sql(query)
        title = '  '.join(f'{k}={v}' for k,v in vals.items())
        c1, c2, v = df.columns
        df = df.pivot(c1,c2,v)
        return df, title

def test_model():
    import plotter
    from pathlib import Path
    wd = Path(plotter.__file__).parent.parent
    wd = wd/'user_files'
    d = {'query': '''SELECT node, time, value
                from spt_dat inner join spt_atr
                     on spt_atr.ids=spt_dat.ids'''}
    m = Model(wd, d)
    vals = {'c': '1', 'k': '2', 'n': '100',
     'b': '-0.035', 'wire': 'static',
     'p': '0.8', 'N1': '1'}
    df, title = m.get_data(vals)
    return df, title

if __name__=='__main__':
    df, title = test_model()