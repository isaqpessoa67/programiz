def replace_item(lst, old_item, new_item):
    
    if old_item in lst:
        lst[lst.index(old_item)] = new_item
        return lst
    

replace_item(['cat', 'dog', 'elephant'], 'dog', 'lion')