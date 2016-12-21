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
    
    def parseMessage(self, msg_dict):
        '''
        Creates a Request object from the message dictionary
        '''
        try:
            req = request.Request(msg_dict[0])
            return req             
        except:
            print "wrong shit"
        return None
        
    def fromWho(self, req):
        '''
         return who the request is from
        for mentor_name in 
        '''
    def assignRequest(self, req):
        for m in self.mentors:
            if m.is_valid:
                # assign mentor
                print 'mentor assigned'
            else:
                print ' mentor not found'
    def run(self):
        '''
        Open socket reading for input.
        '''
        READ_WEBSOCKET_DELAY = 1
        if self.client.rtm_connect():
            print("Mentorbot connected and running!")
            while True:
                # for messages from participants
                print(self.client.rtm_read())
                req = self.parseMessage(self.client.rtm_read())
                self.assignRequest(req)
                time.sleep(READ_WEBSOCKET_DELAY)
                
                # for messages from mentors
                
        else:
            print("Connection failed. Invalid Slack token or bot ID?")


if __name__ == "__main__":
    mentor1 = mentor.Mentor({'name': 'mntr1', 'topic': 'stuff', 'language': 'C++'})
    mentor2 = mentor.Mentor({'name': 'mntr2', 'topic': 'stuff2', 'language': 'Java'})
    mentor_list = [mentor1, mentor2]
    bot = SlackBot(config.SLACK_TOKEN, mentor_list)
    print bot.getID("mentor")
    bot.run()

#[{u'type': u'user_typing', u'user': u'U34LJ4C11', u'channel': u'D341VTH4Y'}]
# format of inputs
