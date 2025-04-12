def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f'Sending: "{current_message}"')
        sent_messages.append(current_message)

messages = ["Hello", "this", "is", "a", "series of messages."]
sent_messages = []

send_messages(messages, sent_messages)
print(messages)
print(sent_messages)