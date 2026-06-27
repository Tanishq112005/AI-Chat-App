from app.modules.chats.embedding_models.interfaces import IEmbedder
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from app.core.config import settings


class HuggingFace(IEmbedder):
    
    def set_model(self , model_name):
        self.__model = HuggingFaceEndpointEmbeddings(
            model_name = model_name ,
            huggingfacehub_api_token=settings.HUGGINGFACEHUG_API_TOKEN 
        )
        
    
    def embedding_query(self , dataForEmbedding):
        return self.__model.aembed_query(dataForEmbedding) 
    
    
    def embedding_document(self , dataOfPdf):
        return self.__model.aembed_documents(dataOfPdf) 
    
    
    
        