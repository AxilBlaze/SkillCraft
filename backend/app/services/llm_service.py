import requests
from flask import current_app

class LLMService:
    def __init__(self):
        self.api_token = None
        self.model_id = None
        self.api_url = None
        
    def initialize(self):
        """Initialize the service with configuration."""
        if not self.api_url:
            self.api_token = current_app.config['HF_API_TOKEN']
            self.model_id = current_app.config['MODEL_ID']
            self.api_url = f"https://api-inference.huggingface.co/models/{self.model_id}"
    
    def generate_response(self, message, context=None):
        """Generate response using Hugging Face Inference API."""
        self.initialize()
        
        # Prepare the prompt
        prompt = self._prepare_prompt(message, context)
        
        # Prepare headers with API token
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        
        # Adjust parameters based on model
        if self.model_id.startswith('google/flan'):
            parameters = {
                "max_length": 256,
                "temperature": 0.7,
                "top_p": 0.9,
                "return_full_text": False
            }
        else:
            parameters = {
                "max_length": 512,
                "temperature": 0.7,
                "top_p": 0.9,
                "return_full_text": False
            }
        
        # Prepare payload
        payload = {
            "inputs": prompt,
            "parameters": parameters
        }
        
        try:
            # Make API request
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()
            
            # Process response
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                generated_text = result[0].get('generated_text', '')
                return self._process_response(generated_text)
            
            return self._process_response("I apologize, but I couldn't generate a response.")
            
        except requests.exceptions.RequestException as e:
            print(f"Error calling Hugging Face API: {str(e)}")
            return {
                'text': "I apologize, but I'm having trouble generating a response right now.",
                'explanation': None,
                'suggestions': []
            }
    
    def _prepare_prompt(self, message, context=None):
        """Create a structured prompt based on the context."""
        if self.model_id.startswith('google/flan'):
            # Flan-T5 specific format
            base_prompt = "Answer as a helpful tutor: "
            if context:
                base_prompt += f"Context: {context}. "
            base_prompt += f"Question: {message}"
            return base_prompt
        else:
            # Default format for other models
            base_prompt = (
                "You are a helpful AI tutor. "
                "Provide clear explanations and examples when needed.\n\n"
            )
            if context:
                base_prompt += f"Context: {context}\n\n"
            base_prompt += f"Student: {message}\nTutor:"
            return base_prompt
    
    def _process_response(self, response):
        """Process the raw response to extract different components."""
        return {
            'text': response,
            'explanation': None,  # Extract explanation if present
            'suggestions': []  # Extract suggestions if present
        }

# Singleton instance
llm_service = LLMService()

def get_ai_response(message, context=None):
    """Get AI response for a given message and context."""
    return llm_service.generate_response(message, context) 