# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 17:28:21 2016

@author: ayanb_000
"""

class Request(object):
    def __init__(self, input_dict):
        self.username = input_dict['user']
        self.topic, self.location, self.language = self.text_parser(input_dict['text'])
        self.channel = input_dict['channel']
    def text_parser(self, text):
        (topic, location, language) = text.split('|')
        return topic, location, language
