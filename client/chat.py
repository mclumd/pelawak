#!/usr/bin/env python
from sdclient import DragonClient

# Handle exceptions from the chat client
def on_exception(error):
    print error

# Print every new message and the sender
def on_channel_message(channel, message):
    # print channel
    # print message
    output = '%(user)s says: %(message)s' % message['data']
    print(output)

# Sent a message
def on_send(context, data):
    print context
    print data

# Joined the chat
def on_subscribed(context, message):
    print('-you joined the chat-')
    print('Chat away...')


if __name__ == '__main__':
    url = 'ws://localhost:9999/data'
    client = DragonClient(url, on_channel_message=on_channel_message, on_exception=on_exception)
    client.connect()


    try:
        name = raw_input('name: ')
        # Subscribe to the chat channel
        client.call_router('subscribe', 'chat-route', callback=on_subscribed, channel='messages')

        message = raw_input()
        while message != 'q!':
            # Send message
            client.call_router('create', 'chat-route', username=name, message=message)
            message = raw_input()
    except KeyboardInterrupt:
        client.disconnect()
