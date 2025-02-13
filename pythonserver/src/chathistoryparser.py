from datetime import datetime
import re
from typing import Any, Dict, List

def read_file_contents(file_path):
    with open(file_path, 'r') as file:
        return file.read()

class ChatHistoryParser:
    
    def __init__(self):
        pass
    
    def parse(self, chat_history: str) -> List[Dict[str,Any]]:
        # Regex to match the structure of the chat history
        pattern = r"\[([^\]]+)\] (\d+@\w+\.\w+): (.*)"
        
        parsed_messages = []

        # Split the chat into lines and process each line
        for line in chat_history.splitlines():
            match = re.match(pattern, line)
            if match:
                timestamp_str, person_id, message = match.groups()
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%fZ")
                
                # Append the parsed message as a dictionary
                parsed_messages.append({
                    "timestamp": timestamp,
                    "person_id": person_id,
                    "message": message
                })
        
        return parsed_messages
