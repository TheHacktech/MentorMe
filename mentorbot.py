import os
import time
import config
import request
import mentor
from slackclient import SlackClient

'''
Wrapper for a SlackBot, using slackclient
'''
class SlackBot(object):
    def __init__(self, token, mentor_list):
        self.__connect(token)
        self.mentors = mentor_list
        self.mentor_names = []

        for mentor in self.mentors:
            self.mentor_names.append(mentor.name)


    def __connect(self, token):
        self.client = SlackClient(token)

    def getUsers(self):
        self.users = {}
        res = self.client.api_call("users.list")
        for user in res["members"]:
            self.users[user["id"]] = user["real_name"]
        return True

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

    def parseHackerMessage(self, msg_dict):
        '''
        Creates a Request object from the message dictionary
        '''
        try:
            if (msg_dict[0]["channel"][0] == "D"):
                req = request.Request(msg_dict[0])
                return req
        except:
            pass
        return None

    def fromWho(self, req):
        '''
         return who the request is from
        for mentor_name in
        '''
        pass

    def assignRequest(self, req):
        for m in self.mentors:
            if m.is_valid(req):
                m.assignTask(req)
                print 'mentor assigned'
                return True
        return False

    def run(self):
        '''
        Open socket reading for input.
        '''
        READ_WEBSOCKET_DELAY = 1
        if self.client.rtm_connect():
            print("Mentorbot connected and running!")
            self.getUsers()
            while True:
                inc = self.client.rtm_read()
                print inc
                req = self.parseHackerMessage(inc)
                if req is not None:
                    self.assignRequest(req)
                time.sleep(READ_WEBSOCKET_DELAY)

        else:
            print("Connection failed. Invalid Slack token or bot ID?")


if __name__ == "__main__":
    mentor1 = mentor.Mentor({'name': 'mntr1', 'topic': 'stuff', 'language': 'C++'})
    mentor2 = mentor.Mentor({'name': 'mntr2', 'topic': 'stuff2', 'language': 'Java'})
    mentor_list = [mentor1, mentor2]
    bot = SlackBot(config.SLACK_TOKEN, mentor_list)
    bot.run()

#[{u'type': u'user_typing', u'user': u'U34LJ4C11', u'channel': u'D341VTH4Y'}]
# format of inputs
