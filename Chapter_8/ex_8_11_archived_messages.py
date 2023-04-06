def send_messages(messages, sent_messages):
    """Show all the messages that were printed."""
    while messages:
        current_message = messages.pop(0)
        print(f"From 703-248-7898: {current_message}")
        sent_messages.append(current_message)

messages = ['Hi!', 'This is your pediatrician.', 'Your dog has died.', 'Your bill is 7 dollars', 'Bye!']
sent_messages = []

send_messages(messages[:], sent_messages)
print(f"\nmessages is {messages}")
print(f"sent_messages is {sent_messages}")