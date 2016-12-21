# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 17:45:47 2016

@author: ayanb_000
"""

class Mentor(object):
    def __init__(self, info_dict):
        '''
        in dict, topic and language are both lists
        '''
        self.name = info_dict['name']
        self.topics = info_dict['topic']
        self.languages = info_dict['language']
        self.busy = False
    def is_valid(self, req):
        match_topic = False
        match_language = False
        
        if req.topic in self.topics:          
            match_topic = True
        if req.language in self.languages:          
            match_language = True
        
        return (not self.busy) and (match_topic or match_language)
    
