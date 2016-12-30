class Mentor(object):
    def __init__(self, info_dict):
        '''
        in dict, topic and language are both lists
        '''
        self.name = info_dict['name']
        self.topics = info_dict['topic']
        self.languages = info_dict['language']
        self.busy = False
        self.currentTask = None

    def is_valid(self, req):
        match_topic = False
        match_language = False

        if req.topic in self.topics:
            match_topic = True
        if req.language in self.languages:
            match_language = True

        return (not self.busy) and (match_topic or match_language)

    def assignTask(self, task):
        self.currentTask = task
        self.busy = True
