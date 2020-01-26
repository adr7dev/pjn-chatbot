from nltk.chat.util import Chat, reflections
from chats import Chats
from pairs import pairs

def chatty():
    print("\n\n#############\nHello, world!\n#############\n\nAsk me a question or give a command...\n") #default message at the start
    chat = Chats(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatty()