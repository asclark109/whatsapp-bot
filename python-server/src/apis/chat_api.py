import requests


class ChatApi:
    

    DEFAULT_BASE_URL = "http://localhost:3000"
    
    def __init__(self, base_url: str = DEFAULT_BASE_URL):
        self._base_url: str = base_url


    def send_message(self, phoneIDOrChatID, message):
        url = f"{self._base_url}/send-message"
        print(f"sending request to {url}")
        response = requests.post(f"{self._base_url}/send-message", json={"phoneIDOrChatID": phoneIDOrChatID, "message": message})
        if response.status_code == 200:
            print("Message sent successfully:", response.json())
        else:
            print("Error sending message:", response.json())

    def get_chat_history(self, phoneIDOrChatID):
        url = f"{self._base_url}/chat-history"
        print(f"sending request to {url}")
        response = requests.get(url, params={"phoneIDOrChatID": phoneIDOrChatID})
        if response.status_code == 200:
            return response.json()
        else:
            print("Error fetching chat history:", response.json())
            
    def get_chat_id_by_name(self,chatName):
        url = f"{self._base_url}/chat-id"
        print(f"sending request to {url}")
        response = requests.get(url, params={"chatName": chatName})
        if response.status_code == 200:
            return response.json()
        else:
            print("Error fetching chat name:", response.json())
