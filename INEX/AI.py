import requests
import openai

class AI:
    """
    Contains all AI related functions.
    """

    class Gemini:
        """
        Interacts with the Gemini AI API.
        """

        def __init__(self, api_key: str, base_url="https://api.gemini.ai/v1"):
            """
            Initializes the Gemini AI Class.

            Args:
            - api_key (str): The API Key for the Gemini AI API.
            """
            self.api_key = api_key
            self.base_url = base_url

        def send_message(self, message: str):
            """
            Sends a message to the Gemini AI API.

            Args:
            - message (str): The message to send.

            Returns:
            - str: The response from the Gemini AI API.
            """
            try:
                url = f"{self.base_url}/text"
                headers = {
                    'Authorization': f'Bearer {self.api_key}',
                    'Content-Type': 'application/json'
                }
                data = {
                    'input': message
                }
                response = requests.post(url, headers=headers, json=data)
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return None

        def get_conversations(self):
            """
            Gets all conversations from the Gemini AI API.

            Returns:
            - list: A list of conversations from the Gemini AI API.
            """
            try:
                url = f"{self.base_url}/conversations"
                headers = {
                    'Authorization': f'Bearer {self.api_key}',
                    'Content-Type': 'application/json'
                }
                response = requests.get(url, headers=headers)
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return None

        def get_conversation(self, conversation_id: str):
            """
            Gets a conversation by ID from the Gemini AI API.

            Args:
            - conversation_id (str): The ID of the conversation to get.

            Returns:
            - dict: The conversation from the Gemini AI API.
            """
            try:
                url = f"{self.base_url}/conversations/{conversation_id}"
                headers = {
                    'Authorization': f'Bearer {self.api_key}',
                    'Content-Type': 'application/json'
                }
                response = requests.get(url, headers=headers)
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return None

        def create_conversation(self, message: str):
            """
            Creates a new conversation on the Gemini AI API.

            Args:
            - message (str): The initial message for the conversation.

            Returns:
            - dict: The created conversation from the Gemini AI API.
            """
            try:
                url = f"{self.base_url}/conversations"
                headers = {
                    'Authorization': f'Bearer {self.api_key}',
                    'Content-Type': 'application/json'
                }
                data = {
                    'input': message
                }
                response = requests.post(url, headers=headers, json=data)
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return None

        def reply_to_conversation(self, conversation_id: str, message: str):
            """
            Replies to a conversation on the Gemini AI API.

            Args:
            - conversation_id (str): The ID of the conversation to reply to.
            - message (str): The message to send.

            Returns:
            - dict: The updated conversation from the Gemini AI API.
            """
            try:
                url = f"{self.base_url}/conversations/{conversation_id}/messages"
                headers = {
                    'Authorization': f'Bearer {self.api_key}',
                    'Content-Type': 'application/json'
                }
                data = {
                    'input': message
                }
                response = requests.post(url, headers=headers, json=data)
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return None

        def get_messages(self, conversation_id: str):
            """
            Gets all messages from a conversation on the Gemini AI API.

            Args:
            - conversation_id (str): The ID of the conversation to get messages from.

            Returns:
            - list: A list of messages from the Gemini AI API.
            """
            try:
                url = f"{self.base_url}/conversations/{conversation_id}/messages"
                headers = {
                    'Authorization': f'Bearer {self.api_key}',
                    'Content-Type': 'application/json'
                }
                response = requests.get(url, headers=headers)
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return None

        def get_message(self, conversation_id: str, message_id: str):
            """
            Gets a message by ID from the Gemini AI API.

            Args:
            - conversation_id (str): The ID of the conversation to get the message from.
            - message_id (str): The ID of the message to get.

            Returns:
            - dict: The message from the Gemini AI API.
            """
            try:
                url = f"{self.base_url}/conversations/{conversation_id}/messages/{message_id}"
                headers = {
                    'Authorization': f'Bearer {self.api_key}',
                    'Content-Type': 'application/json'
                }
                response = requests.get(url, headers=headers)
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return None

        def delete_conversation(self, conversation_id: str):
            """
            Deletes a conversation from the Gemini AI API.

            Args:
            - conversation_id (str): The ID of the conversation to delete.

            Returns:
            - dict: The deleted conversation from the Gemini AI API.
            """
            try:
                url = f"{self.base_url}/conversations/{conversation_id}"
                headers = {
                    'Authorization': f'Bearer {self.api_key}',
                    'Content-Type': 'application/json'
                }
                response = requests.delete(url, headers=headers)
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return None

        def delete_message(self, conversation_id: str, message_id: str):
            """
            Deletes a message from the Gemini AI API.

            Args:
            - conversation_id (str): The ID of the conversation to delete the message from.
            - message_id (str): The ID of the message to delete.

            Returns:
            - dict: The deleted message from the Gemini AI API.
            """
            try:
                url = f"{self.base_url}/conversations/{conversation_id}/messages/{message_id}"
                headers = {
                    'Authorization': f'Bearer {self.api_key}',
                    'Content-Type': 'application/json'
                }
                response = requests.delete(url, headers=headers)
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return None

    class ChatGPT:
        """
        Interacts with the OpenAI ChatGPT API.
        """

        def __init__(self, api_key: str, model: str = "gpt-4"):
            """
            Initializes the ChatGPT Class.

            Args:
            - api_key (str): The API Key for the OpenAI API.
            - model (str): The model to use (default: "gpt-4").
            """
            openai.api_key = api_key
            self.model = model

        def send_message(self, message: str, system_prompt: str = None):
            """
            Sends a message to ChatGPT.

            Args:
            - message (str): The message to send.
            - system_prompt (str): Optional system prompt to set context.

            Returns:
            - dict: The response from ChatGPT.
            """
            try:
                messages = []
                if system_prompt:
                    messages.append({"role": "system", "content": system_prompt})
                messages.append({"role": "user", "content": message})
                
                response = openai.ChatCompletion.create(
                    model=self.model,
                    messages=messages
                )
                return response
            except Exception as e:
                print(f"An error occurred: {e}")
                return None

        def create_chat(self, messages: list):
            """
            Creates a chat with multiple messages.

            Args:
            - messages (list): List of message dictionaries with 'role' and 'content'.

            Returns:
            - dict: The chat completion response.
            """
            try:
                response = openai.ChatCompletion.create(
                    model=self.model,
                    messages=messages
                )
                return response
            except Exception as e:
                print(f"An error occurred: {e}")
                return None

        def stream_chat(self, messages: list):
            """
            Creates a streaming chat response.

            Args:
            - messages (list): List of message dictionaries.

            Returns:
            - generator: Stream of response chunks.
            """
            try:
                response = openai.ChatCompletion.create(
                    model=self.model,
                    messages=messages,
                    stream=True
                )
                return response
            except Exception as e:
                print(f"An error occurred: {e}")
                return None

    class DeepSeek:
        """
        Interacts with the DeepSeek AI API.
        """

        def __init__(self, api_key: str, base_url: str = "https://api.deepseek.com/v1"):
            """
            Initializes the DeepSeek AI Class.

            Args:
            - api_key (str): The API Key for the DeepSeek API.
            - base_url (str): The base URL for the API.
            """
            self.api_key = api_key
            self.base_url = base_url

        def generate_text(self, prompt: str, max_tokens: int = 100):
            """
            Generates text using DeepSeek AI.

            Args:
            - prompt (str): The input prompt.
            - max_tokens (int): Maximum number of tokens to generate.

            Returns:
            - dict: The generated text response.
            """
            try:
                url = f"{self.base_url}/completions"
                headers = {
                    'Authorization': f'Bearer {self.api_key}',
                    'Content-Type': 'application/json'
                }
                data = {
                    'prompt': prompt,
                    'max_tokens': max_tokens
                }
                response = requests.post(url, headers=headers, json=data)
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return None

        def generate_code(self, prompt: str, language: str = "python"):
            """
            Generates code using DeepSeek AI.

            Args:
            - prompt (str): The input prompt.
            - language (str): The programming language.

            Returns:
            - dict: The generated code response.
            """
            try:
                url = f"{self.base_url}/code/completions"
                headers = {
                    'Authorization': f'Bearer {self.api_key}',
                    'Content-Type': 'application/json'
                }
                data = {
                    'prompt': prompt,
                    'language': language
                }
                response = requests.post(url, headers=headers, json=data)
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return None

        def analyze_code(self, code: str):
            """
            Analyzes code using DeepSeek AI.

            Args:
            - code (str): The code to analyze.

            Returns:
            - dict: The analysis response.
            """
            try:
                url = f"{self.base_url}/code/analyze"
                headers = {
                    'Authorization': f'Bearer {self.api_key}',
                    'Content-Type': 'application/json'
                }
                data = {
                    'code': code
                }
                response = requests.post(url, headers=headers, json=data)
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return None