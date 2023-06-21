from ..modules.db_conn import *

def update(old_item,new_item):
    x = noSQLdb().update_one(old_item,new_item)
    return x.acknowledged
