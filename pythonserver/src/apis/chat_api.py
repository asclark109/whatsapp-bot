import re
from typing import Any, Dict, List, Set
import requests
import os
import requests, json
from apis.message import Message

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

    def get_chat_history(self, phoneIDOrChatID) -> List[Message]:
        url = f"{self._base_url}/chat-history"
        print(f"sending request to {url}")
        response = requests.get(url, params={"phoneIDOrChatID": phoneIDOrChatID})
        
        # process response
        ids_encountered = set()
        
        msgs = []
        msg_data = response.json()['data']
        for raw_msg_data in msg_data:
            author_id = raw_msg_data.get("from","")
            literal_body = raw_msg_data.get("body","")
            interpretted_author, interpretted_body = parse_message(literal_body) if literal_body != "" else ("","")
            if author_id:
                ids_encountered.add(author_id)
            msgs.append(Message(author_id,interpretted_author,literal_body,interpretted_body))
            
        id_to_name_mapper = dict()
        data = self.get_contacts_by_ids(ids_encountered)
        for datadict in data['data']:
            author_id = datadict['id']['_serialized']
            name = datadict['name']
            id_to_name_mapper[author_id] = name
            
        for msg in msgs:
            msg.setName(id_to_name_mapper.get(msg.literal_author,None))
        
        if response.status_code == 200:
            return msgs
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
            
    def get_contacts_by_ids(self, ids):
        
        # Construct the comma-separated list of ids
        ids_str = ",".join(ids)
        
        
        fullurl = f"{self._base_url}/contacts?ids={ids_str}"
        print(f"Sending request to {fullurl}")
        
        
        response = requests.get(fullurl)
        
        if response.status_code == 200:
            print("Contacts retrieved successfully:", response.json())
            return response.json()  # You can return or process the contacts data here
        else:
            print("Error fetching contacts:", response.json())
            return None
            
def parse_message(message) -> Dict[str,Any]:
    # Regular expression pattern to match the author and the message
    pattern = r'^\[([^\]]+)\]\s*(.*)'  # Matches the format [author] message
    
    # Try to match the pattern
    match = re.match(pattern, message)
    
    if match:
        author = match.group(1)  # The author part (e.g., 'Jesus Christ')
        message_content = match.group(2)  # The message content (e.g., 'I like dogs')
        return author, message_content
    else:
        # If the message doesn't match the pattern, return it as-is with no author
        return None, message
            
class Message:
    
    def __init__(self, literal_author: str, interpretted_author: str , literal_body: str, interpretted_body: str):
        self.literal_body = literal_body
        self.interpretted_body = interpretted_body
        self.literal_author = literal_author
        self.interpretted_author = interpretted_author
        
    def setName(self, name: str):
        self.name = name
        
    def getName(self) -> str:
        return self.name if not self.interpretted_author else self.interpretted_author
        
    def __repr__(self):
        return f"Message(author={self.interpretted_author if self.interpretted_author is not None else self.name}, body={self.interpretted_body})"
