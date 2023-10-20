#Function checks if there are duplicates in the incoming

def any_duplicates(elements):
    general_list = []
    for i in elements:
        general_list += i
    for w in general_list:
        if general_list.count(w)>1:
            return True
        else:
            continue
            
    return False
        
any_duplicates([[1,2,6], [5,4,7], [8,9,10]])