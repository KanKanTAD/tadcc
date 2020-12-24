from typing import List


class Attribute:
    def __init__(self,name:str,multi:bool=False):
        pass
        
    def getName(self)->str:
        pass 
        
    def isMulti(self)->bool:
        pass 
        
    def getContent(self)->List[str]:
        pass 

class Rule:
    def __init__(self,name:str):
        pass
        
    def getName(self)->str:
        pass 
        
    def addAttr(self,attr:Attribute)->(bool,str):
        pass 
        
    def listAttr(self)->List[Attribute]:
        pass 
        
    def searchAttrByName(self,pattern:str)->List[Attribute]:
        pass 
        
    def selectAttrByName(self,name:str)->Attribute:
        pass
        
    def selectAttrByContent(self,content:str)->List[Attribute]:
        pass 
        
    def searchAttrByContent(self,pattern:str)->List[Attribute]:
        pass
        
    

class Target:
    def __init__(self,name):
        pass
        
class Bazel:
    def load(self,file_path):
        pass
        
    def create(self)->str:
        pass
        
    def selectByName(self,name)->Target:
        pass
        
    