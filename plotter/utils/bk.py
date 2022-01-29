import pandas as pd
import sqlite3

class BaseModel:
    def __init__(self, wd, data_source):
        self.db = data_source.get('db', 'data.sqlite')
        self.db = f'{wd}/{self.db}'
        default_query = 'SELECT * from atr limit 5'
        self.query = data_source.get('query', default_query)
        self.check_db_validity()

    def check_db_validity(self):
        import os
        if not os.path.isfile(self.db):
            raise ValueError('Database does not exist')

    def read_sql(self, query):
        conn = sqlite3.connect(self.db)
        df = pd.read_sql(query, conn)
        conn.close()
        return df

def test_model():
    import plotter
    from pathlib import Path
    wd = Path(plotter.__file__).parent.parent
    wd = wd/'user_files'
    data_source = {}
    m = BaseModel(wd, data_source)
    df = m.read_sql(m.query)
    return df

if __name__=='__main__':
    df = test_model()