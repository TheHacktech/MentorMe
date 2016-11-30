import os
import time
import config
from slackclient import SlackClient

'''
Wrapper for a SlackBot, using slackclient
'''
class SlackBot(object):
    def __init__(self, token):
        self.__connect(token)

    def __connect(self, token):
        self.client = SlackClient(token)

    def getID(self, name):
        '''
        Get the ID of a user given their name.
        '''
        api_call = self.client.api_call("users.list")
        if api_call.get('ok'):
            users = api_call.get('members')
            for user in users:
                if 'name' in user and user.get('name') == name:
                    return user.get('id')

    def privateMessage(self, message, channel):
        '''
        Send a private message to a user in the given PM channel.
        '''
        self.client.api_call("chat.postMessage", channel=channel, text=message, as_user=False)

    def run(self):
        '''
        Open socket reading for input.
        '''
        READ_WEBSOCKET_DELAY = 1
        if self.client.rtm_connect():
            print("Mentorbot connected and running!")
            while True:
                command, channel = parse_slack_output(self.client.rtm_read())
                print command, channel
                time.sleep(READ_WEBSOCKET_DELAY)
        else:
            print("Connection failed. Invalid Slack token or bot ID?")


if __name__ == "__main__":
    bot = SlackBot(config.SLACK_TOKEN)
    bot.getID("mentor")
