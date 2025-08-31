import google.generativeai as genai
import traceback

# Configure the Gemini API
genai.configure(api_key='AIzaSyC-wwRdTGUjc6zG7-V3kRbeBEOjPVIK4Ik')

# Set up the model with safety settings
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name='gemini-1.5-pro-latest',
    generation_config=generation_config,
    safety_settings=safety_settings
)

def get_mental_health_response(user_input):
    try:
        # Create a chat session
        chat = model.start_chat(history=[])
        
        # Prepare the prompt with mental health context
        prompt = f"""As a compassionate mental health companion, please respond to the following message. Remember to:
        1. Be empathetic and supportive
        2. Offer practical coping strategies when appropriate
        3. Encourage professional help if needed
        4. Maintain a positive and hopeful tone
        5. Never provide medical diagnoses
        6. Prioritize user safety and well-being

        User's message: {user_input}
        """
        
        # Generate response
        response = chat.send_message(prompt)
        
        if response and response.text:
            return response.text.strip()
        else:
            return "I apologize, but I couldn't generate a proper response. Please try again with your question."
            
    except Exception as e:
        print(f"Error in get_mental_health_response: {str(e)}")
        print(f"Traceback: {traceback.format_exc()}")
        return "I'm having trouble processing your request right now. Please try again in a moment. If you need immediate assistance, please reach out to a mental health professional." 