import pandas as pd
import sqlite3


class Model:
    def __init__(self, wd, data_source):
        self.db = data_source.get('db', 'data.sqlite')
        self.db = f'{wd}/{self.db}'
        default_query = '''SELECT time, node, value
                           from spt_atr inner join spt_dat
                                on spt_atr.ids=spt_dat.ids'''
        self.query = data_source.get('query', default_query)
        self.check_db_validity()

    def check_db_validity(self):
        import os
        if not os.path.isfile(self.db):
            raise ValueError('Database does not exist')

    def get_data(self, vals, verbose=False):
        where = ' AND '.join(f"{k}='{v}'" for k,v in vals.items())
        query = f'{self.query} \n where {where}'
        if verbose:print(query)
        conn = sqlite3.connect(self.db)
        df = pd.read_sql(query, conn)
        conn.close()
        title = '  '.join(f'{k}={v}' for k,v in vals.items())
        c1, c2, v = df.columns
        df = df.pivot(c1,c2,v)
        return df, title

def test_model():
    import plotter
    from pathlib import Path
    wd = Path(plotter.__file__).parent.parent
    wd = wd/'user_files'
    data_source = {}
    m = Model(wd, data_source)
    vals = {'c': '1', 'k': '2', 'n': '100',
     'b': '-0.035', 'wire': 'static',
     'p': '0.8', 'N1': '1'}
    df, title = m.get_data(vals)
    return df, title

if __name__=='__main__':
    test_model()