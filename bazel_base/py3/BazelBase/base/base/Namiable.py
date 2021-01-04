

class Namiable(object):
    def set_name(self: Namiable, name: str) -> void:
        self.__name=name
        
    def get_name(self: Namiable) -> str:
        return self.__name
        
    def __init__(self):
        pass
    
