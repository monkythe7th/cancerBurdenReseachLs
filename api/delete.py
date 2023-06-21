from ..modules.db_conn import *

def delete(item):
    return noSQLdb().delete_one(item)
