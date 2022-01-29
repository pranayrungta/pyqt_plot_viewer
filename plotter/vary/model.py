import pandas as pd
import sqlite3


class Model:
    def __init__(self, wd, data_source):
        self.db = data_source.get('db', 'data.sqlite')
        self.db = f'{wd}/{self.db}'
        default_query = '''SELECT N1, X
                           from nvsx inner join atr
                                on atr.ids=nvsx.ids'''
        self.query = data_source.get('query', default_query)
        self.check_db_validity()

    def check_db_validity(self):
        import os
        if not os.path.isfile(self.db):
            raise ValueError('Database does not exist')

    def get_nvsx(self, vals, verbose=False):
        where = ' AND '.join(f"{k}='{v}'" for k,v in vals.items())
        query = f'{self.query} \n where {where}'
        if verbose:print(query)
        conn = sqlite3.connect(self.db)
        df = pd.read_sql(query, conn)
        conn.close()
        return df

    def get_data(self, variable, const_vals):
        dfs = {}
        const = const_vals.copy()
        key, vals = variable
        for val in vals:
            const[key]=val
            dfs[f'{key}={val}']= self.get_nvsx(const, False)
        title = '  '.join(f'{k}={v}' for k,v in const_vals.items())
        return dfs, title

