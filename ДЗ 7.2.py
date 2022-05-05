def find_unique_value(lst):
    d = {}
    for i in lst:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1
            
    for key, value in d.items():
        if value == 1:
            return key
        
print(find_unique_value(lst))
        
    
