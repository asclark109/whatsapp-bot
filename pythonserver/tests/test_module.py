# test_math_operations.py

import os
import sys
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Now you can import your class from chatparser.py
from chathistoryparser import ChatHistoryParser

def read_file_contents(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
class TestMathOperations:

    # Test for addition function
    def test_parse(self):
        filepath_chat_history = os.path.abspath("pythonserver/tests/data/chat_history.txt")
        chat_history = read_file_contents(filepath_chat_history)
        parser = ChatHistoryParser()
        result = parser.parse(chat_history)
        print(result)