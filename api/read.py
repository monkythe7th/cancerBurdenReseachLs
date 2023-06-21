from ..modules.db_conn import *

def read(item = None):
    col = noSQLdb()
    if item:
        x = col.find_one(item)
        return x
    else:
        return col.find_one()

def get_all():
    return noSQLdb().find()