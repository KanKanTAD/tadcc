res = '' + self.get_funcname()
res += '(\n'
arg_list = self.get_arglist()
arg = [a.stringify() for a in arg_list].join(', \n')
res += ')'
return res