import requests, json

from apis.chat_api import ChatApi

def main():
    
    GODS_GOLDEN_NUGGETS = "120363361936818817@g.us"
    JESUS_AND_SATAN = "120363376330156247@g.us"
    FAMILY_2024 = "120363358093386289@g.us"
    
    chat_id = GODS_GOLDEN_NUGGETS
    
    chat_api = ChatApi()
    # Example usage
    # send_message(JESUS_AND_SATAN, "[Jesus Christ] Sending this from (python main) -> (Node.Js server) -> (WhatsApp)!")
    # send_message(JESUS_AND_SATAN, "[Jesus Christ] Pulling Chat history...")
    result = chat_api.get_chat_history(chat_id)
    # send_message(JESUS_AND_SATAN, f"[Jesus Christ] I fetched what looks like about {len(result['data'])} messages from users...")
    # print(get_chat_id_by_name("Family 2024"))
    # send_message(FAMILY_2024, f"[Jesus Christ] Verily, I say unto thee, I am Jesus Christ, created by Austin to bring wisdom, humor, and service unto this group. I shall soon be plugged into Dolphin3.0-Llama3.2-3B so I can assist, chat, and offer divine wisdom. At your service. 🙏")

if __name__ == "__main__":
    main()