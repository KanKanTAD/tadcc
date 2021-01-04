res = '' + self.get_funcname()
res += '(\n'
arg_list = self.get_arglist()
arg = ', \n'.join([a.stringify() for a in arg_list])
res += ')'
return res
