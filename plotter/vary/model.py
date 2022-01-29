from plotter.utils.bk import BaseModel

class Model(BaseModel):
    def __init__(self, wd, data_source):
        super(Model, self).__init__(wd, data_source)

    def get_nvsx(self, vals):
        where = ' AND '.join(f"{k}='{v}'" for k,v in vals.items())
        query = f'{self.query} \n where {where}'
        df = self.read_sql(query)
        return df

    def get_data(self, variable, const_vals):
        dfs = {}
        const = const_vals.copy()
        key, vals = variable
        for val in vals:
            const[key]=val
            dfs[f'{key}={val}']= self.get_nvsx(const)
        title = '  '.join(f'{k}={v}' for k,v in const_vals.items())
        return dfs, title

def test_model():
    import plotter
    from pathlib import Path
    wd = Path(plotter.__file__).parent.parent
    wd = wd/'user_files'
    d = {'query': '''SELECT N1, X
                from nvsx inner join atr
                     on atr.ids=nvsx.ids'''}
    m = Model(wd, d)
    v = ('b', ['0', '-0.04', '-0.08', '-0.1'])
    c = {'c': '1', 'n': '100', 'wire': 'static', 'k': '2', 'p': '0'}
    df, title = m.get_data(v,c)
    return df, title

if __name__=='__main__':
    df, title = test_model()