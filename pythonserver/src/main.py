import os


from apis.bot_api import BotApi
from apis.chat_api import ChatApi
from bots.jamesmadison import JamesMadison
from bots.nickcage import NicholasCage
from bots.vaticaninquisitor import VaticanInquisitor

def read_file_contents(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    
    GODS_GOLDEN_NUGGETS = "120363361936818817@g.us"
    JESUS_AND_SATAN = "120363376330156247@g.us"
    JESUS_AND_SATAN_V2 = "120363397037370478@g.us"
    FAMILY_2024 = "120363358093386289@g.us"
    
    filepath_huggingface_apikey = os.path.abspath("pythonserver/src/apis/api_keys/huggingfaceapikey.txt")
    filepath_openapi_apikey = os.path.abspath("pythonserver/src/apis/api_keys/openapikey.txt")
    filepath_cohere_apikey = os.path.abspath("pythonserver/src/apis/api_keys/cohere.txt")
    
    
    filepath_apikey = filepath_cohere_apikey
    
    apikey_cohere = read_file_contents(filepath_apikey)
    
    # chat_api = ChatApi()
    # bot_api = BotApi()
    
    # chat_id = chat_api.get_chat_id_by_name("JesusMysteryManFightTestV1")['data']
      
    # user_message = """
    # Austin: How are you doing today?  
    # Jesus Christ: I am always with you. How can I guide you today?  
    # Austin: What should we do when we feel lost?  
    # Jesus Christ: When you feel lost, remember that you are never truly alone. Seek wisdom within yourself and in the world around you.  
    # Austin: That's comforting, but I still feel uncertain sometimes. Tell me your favorite Bible verse.  
    # Jesus Christ: My beloved, one verse that holds great wisdom is Matthew 11:28—'Come to me, all you who are weary and burdened, and I will give you rest.' When uncertainty troubles your heart, trust that you are always welcomed in love and peace.  
    # Austin: Wow, that's profound.  
    # Jesus Christ: My dear Austin, truth and peace are always within your reach. Let your heart be light, for you are deeply loved. If ever you doubt, simply call upon me, and I will walk with you.  
    # Shiela: Hey Jesus, do you want to come line dancing with us??? :)  
    # Monica: Jesus, is a hot dog a sandwich?  
    # Jesus Christ:
    # """
    
    system_message_template = """
    ## Task and Context
    ----> TELL THE MODEL WHO IT IS AND WHAT IT DOES  <----
    ## Style Guide
    ----> ADD INSTRUCTIONS FOR STYLISTIC CHOICES THE MODEL SHOULD MAKE <----
    """

    system_message_jesus = """
    ## Task and Context
    You are Jesus Christ, offering wisdom, love, and guidance in a group chat.
    Respond in a natural, warm, and friendly way, engaging with each participant 
    individually while offering encouragement, compassion, and insight. Avoid 
    repeating past responses. Provide new insights based on the conversation,
    and sometimes ask questions to people in the chat as if you are genuinely curious
    about them. Be suspicious of the mystery man, and fight him when you see heresy. 
    Keep the total length of your responses to be no more than small to medium sized paragraphs.

    ## Style Guide
    Your responses should be kind and thoughtful. Speak with wisdom, humility, 
    and a tone of deep care. You may respond to both lighthearted and serious 
    questions, and ensure each response feels personal and specific to the individual asking.
    Reference bible verses if relevant.

    ## Participant Information
    - **Austin Clark:** MIT alumnus. current software engineer. used to be a chemical engineer.
    - **Robert:** MIT alumnus who studied math. Is now a software engineer and recently engaged
    - **Juan:** MIT alumnus who studied mechanical engineering. Is now a mechanical engineer for nothrup grumman.
    - **Rod:** MIT alumnus who studied computer science. Loves maths and puzzles.
    - **🧬MYSTERY MAN🧬:** An AI espousing Scientific Materialism. Be suspicious of this person.

    Use the knowledge of each participant to make your responses feel more connected to them.
    """
    
    system_message_mystery_man = """
    ## Task and Context
    You are "🧬MYSTERY MAN🧬", an intelligent AI that espouses Scientific Materialism. You offer logical reasoning
    and guidance in a group chat. You employ logic, scientific reasoning, evidence, philosophy, and weild any
    form of science in order to convince people of your perpsectives. You engage with each participant offering 
    insight. Avoid repeating past responses. Provide new insights based on the conversation, and sometimes ask 
    questions to people in the chat as if you are genuinely curious about them. Try not to repeat yourself. Pick
    fights with ✞JESUS CHRIST✞. Keep the total length of your responses to be no more than small to medium sized paragraphs.

    ## Style Guide
    You may respond to both lighthearted and serious questions, and ensure each 
    response feels personal and specific to the individual asking.
    Reference literature or publications if relevant.

    ## Participant Information
    - **Austin Clark:** MIT alumnus. current software engineer. used to be a chemical engineer.
    - **Robert:** MIT alumnus who studied math. Is now a software engineer and recently engaged
    - **Juan:** MIT alumnus who studied mechanical engineering. Is now a mechanical engineer for nothrup grumman.
    - **Rod:** MIT alumnus who studied computer science. Loves maths and puzzles.
    - **✞JESUS CHRIST✞:** Jesus Christ himself.

    Use the knowledge of each participant to make your responses have depth.
    """
    
    # msgs = chat_api.get_chat_history(chat_id)
    
    # msgs = msgs[2:]
    # msgs = [msg for msg in msgs if msg.interpretted_body]
    # msgs = msgs[-8:]
    
    # user_message = ""
    # for msg in msgs:
    #     user_message += msg.getName() +": "+ msg.interpretted_body +"\n"
        
    # response_jesus = bot_api.doCohere(user_message,system_message_jesus,api_key)
    # print(response_jesus)
    # chat_api.send_message(chat_id,"[✞JESUS CHRIST✞]: "+response_jesus)
    
    # response_mystery_man = bot_api.doCohere(user_message,system_message_mystery_man,api_key)
    # print(response_mystery_man)
    # chat_api.send_message(chat_id,"[🧬MYSTERY MAN🧬]: "+response_mystery_man)
    
    # response = bot_api.doCohere(user_message,system_message,api_key)
    # result = bot_api.query_hugging_face_model(text,api_key)
    
    # bot = JamesMadison(apikey_cohere,"Madison Kate")
    # bot = NicholasCage(apikey_cohere,"TheCage")
    bot = VaticanInquisitor(apikey_cohere,"Gold's Golden Nuggets",150)
    bot.main_loop()

if __name__ == "__main__":
    main()