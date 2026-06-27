from abc import ABC , classmethod  


## define the work of the each of the chat models 


class ChatModels(ABC):
    
    @classmethod  
    def invoke(prompt):
        pass 
    
    
    @classmethod
    def setModel(modelName):
        pass
    