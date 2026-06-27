from app.modules.chats.schemas import HuggingFaceEmbeddingModelConfig
from app.modules.chats.embedding_models.huggingFace import HuggingFace
class EmbeddingModelFactory:
    
    def get_method(model_type: str , config: dict):
        
        if (model_type == "hugging_face"):
            validated_data = HuggingFaceEmbeddingModelConfig(**config)
            embeddingModel =  HuggingFace()
            embeddingModel.set_model(validated_data.model_name)
            return embeddingModel ;
            
    