res = '['
val_list = self.list()
val = ', \n'.join([v for v in val_list])
res += val
res += ']'
return res
