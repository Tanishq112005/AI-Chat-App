## model factory , defing the models used 


from app.modules.chats.schemas import HuggingFaceChatModelConfig
from app.modules.chats.chat_models.huggingFace import HuggingFace


class ChatModelFactory:
    
    def get_method(model_type: str , config: dict):
        
        if model_type == "hugging_face":
            validated_data = HuggingFaceChatModelConfig(**config)
            model = HuggingFace()
            model.setModel(repo_id=validated_data.repo_id , task = validated_data.task , max_length=validated_data.max_length , temperature=validated_data.temperature)
            return model ; 
        
        