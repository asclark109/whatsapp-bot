class Message:
    
    def __init__(self, literal_author: str, interpretted_author: str , literal_body: str, interpretted_body: str):
        self.literal_body = literal_body
        self.interpretted_body = interpretted_body
        self.literal_author = literal_author
        self.interpretted_author = interpretted_author
        
    def setName(self, name: str):
        self.name = name
        
    def __repr__(self):
        return f"Message(author={self.interpretted_author if self.interpretted_author is not None else self.name}, body={self.interpretted_body})"
