import time
from apis.bot_api import BotApi
from apis.chat_api import ChatApi


class Bot:
    
    def __init__(self, name:str, api_key:str, task_and_context: str, style_guide: str, participant_info: str, main_chat_name: str):
        self.name = name
        self.api_key = api_key
        self.bot_api = BotApi()
        self.chat_api = ChatApi()
        self.task_and_context = task_and_context
        self.style_guide = style_guide
        self.participant_info = participant_info
        self.main_chat_name = main_chat_name
        self._last_msg_body = None
        self._last_author = None
        
    def get_system_msg(self) -> str:
        return f"""
        ## Task and Context
        {self.task_and_context}

        ## Style Guide
        {self.style_guide}

        ## Participant Information
        {self.participant_info}
        """
        
    def main_loop(self):
        """Main loop to check for new messages and respond."""
        while True:
            chatId = self.chat_api.get_chat_id_by_name(self.main_chat_name)['data']
            msgs = self.chat_api.get_chat_history(chatId)
            
            # process msgs
            msgs = msgs[2:]
            msgs = [msg for msg in msgs if msg.interpretted_body]
            msgs = msgs[-6:]
            user_message = ""
            for msg in msgs:
                user_message += msg.getName() +": "+ msg.interpretted_body +"\n"

            if msgs:
                last_message = msgs[-1]  # Assuming messages are ordered
                last_author = last_message.getName()
                last_body = last_message.interpretted_body
                
                self._last_author = last_author if self._last_author is None else self._last_author
                # self._last_msg_body = last_body if self._last_msg_body is None else self._last_msg_body
                
                if self.name not in last_author: # was last msg written by someone else?
                    # it's a new message
                    self._last_msg_body = last_message # Update last seen message
                    print(f"New message(s) detected...")

                    response = self.bot_api.doCohere(user_message,self.get_system_msg(),self.api_key)
                    print(f"response: {response}")
                    if response:
                        msg_to_send = f"[{self.name}]: "+response
                        self._last_msg_body = msg_to_send
                        self.chat_api.send_message(chatId, msg_to_send)
                        
            time.sleep(60)  # Wait 1 minute before checking again