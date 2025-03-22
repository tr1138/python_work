from message_functions import *

messages = ["Hello", "this", "is", "a", "series of messages."]
sent_messages = []

send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)