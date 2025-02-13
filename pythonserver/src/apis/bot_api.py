import time
import cohere
import httpx
import openai
import requests


class BotApi:
    
    def __init__(self):
        pass
        
        
    def doCohere(self, user_message: str, system_message: str, api_key: str) -> str:
        # Initialize the Cohere client
        co = cohere.ClientV2(api_key)

        # Add the messages
        messages = [{'role': 'system', 'content': system_message},
                    {'role': 'user', 'content': user_message}]


        # Generate the response
        response = co.chat(model="command-r-plus-08-2024",
                   messages=messages,
                   max_tokens=200,  # Limit response length
                   temperature=0.2   # Make responses more concise
                   repetition_penalty=1.2,  # Penalize repetitive words
                   presence_penalty=1.1  # Discourage topic redundancy
                   )

        # Print the generated text
        return response.message.content[0].text
        
        
    def doChatGpt(self, prompt: str, api_key: str) -> str:
        # Set your OpenAI API key
        openai.api_key = api_key
        
        while True:
            try:
                response = openai.completions.create(
                    model="gpt-3.5-turbo",
                    prompt=prompt,
                    max_tokens=150
                )
                return response['choices'][0]['text']
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 429:
                    print("Rate limit exceeded. Retrying in 60 seconds...")
                    time.sleep(60)  # Wait for 1 minute before retrying
                else:
                    raise  # Raise other exceptions
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                break
            
    def doDeepSeek(self, prompt: str, api_key: str) -> str:
        
        # Deepseek API URL (replace with the correct endpoint)
        api_url = 'https://api.deepseek.ai/v1/completions'

        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
        # Payload for the request
        data = {
            "model": "deepseek-xyz",  # Replace with the model you want to use (e.g., deepseek-xyz) MAYBE deepseek-chat
            "prompt": prompt,
            "max_tokens": 150  # Adjust the number of tokens as needed
        }

        try:
            # Send the request
            response = requests.post(api_url, headers=headers, json=data)
            response.raise_for_status()  # Check if the response is successful
            
            # Get the response text
            response_json = response.json()
            return response_json.get('choices', [{}])[0].get('text', 'No response')
        
        except requests.exceptions.HTTPError as err:
            if response.status_code == 429:  # Rate limit exceeded
                print("Rate limit exceeded. Retrying in 60 seconds...")
                time.sleep(60)  # Wait for 1 minute
                return self.doDeepSeek(prompt)  # Retry the request
            else:
                print(f"HTTP error occurred: {err}")
                return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
    
    def do(self, prompt: str, api_key: str):
        # Load the text generation pipeline with the model

        # tokenizer = AutoTokenizer.from_pretrained("distilbert/distilgpt2")
        # model = AutoModelForCausalLM.from_pretrained("distilbert/distilgpt2")

        model_url = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"  # DialoGPT model URL

        headers = {
            "Authorization": f"Bearer {api_key}"
        }

        # Send request to Hugging Face API
        response = requests.post(model_url, headers=headers, json={"inputs": prompt, "max_length": 150, "num_return_sequences": 1})

        # Print the result
        if response.status_code == 200:
            print(response.json()[0]['generated_text'])
        else:
            print(f"Error: {response.status_code} - {response.text}")
        
    
    def query_hugging_face_model(self,text, api_key):
        url = f"https://api-inference.huggingface.co/models/{self._model_name}"
        headers = {
            "Authorization": f"Bearer {api_key}"
        }
        payload = {
            "inputs": text
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()
