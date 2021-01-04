res = ''
name = self.get_name()
if name != '':
    res += name + ' = '
value = self.get_value()
res += value.stringify()
return res