from ..modules.db_conn import *

def update(c,old_item,new_item):
    x = noSQLdb(c).update_one(old_item,new_item)
    return x.acknowledged
