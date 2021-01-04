res = '['
val_list = self.list()
val = [v for v in val_list].join(', \n')
res += val
res += ']'
return res