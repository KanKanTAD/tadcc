metis = self.get_call_metis()
res = ''
for m in metis:
    res += m.stringify()
    res += '\n'
return res
