ls = self.__build.get_call_metis()
idx = idx if idx >= 0 else len(ls) + idx 
if not (0 <= idx < len(ls)):
    return False 
del ls[idx] 
return True 