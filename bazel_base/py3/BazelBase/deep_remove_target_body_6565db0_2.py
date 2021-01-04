ls = self.__build.get_call_metis()
i = 0
while i < len(ls):
    target = Target(ls[i]) 
    if target.get_name() == target_name:
        self.by_index(i)
        continue 
    i += 1