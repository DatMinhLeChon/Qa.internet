import os
import pandas as pd
import json
from fuzzywuzzy import fuzz
# jsol light:
# id
# questions
# annotation:
    # type
    # answers

class QaPairs():
    def __init__(self, question, answer):
        self.question =question
        self.answer = answer
class Annotation():
    def __init__(self, type, content):
        self.type = type
        self.content = content
    
    def parseAnswer(self):
        if self.type == "singleAnswer":
            return self.content
        elif self.type == "multipleQAs":
            return 
        
        

class DataItem():
    def __init__(self, question, annotation):
        self.question = question
        self. annotation = annotation
        self.score = None

class DataQA():
    def __init__(self, item, data_item_list):
        self.metric = "Bleu"
        self.data_item_list = data_item_list
        self.weight = 0.1
        
    def databaseVocab(self):
        
        for item in self.data_item_list:
            fuzz()
        
        return
        
def parsingDataset():
    json_path = 'train_light.json' # dataset
    json_open = open(json_path)
    json_load = json.load(json_open)
    for item in json_load:
        dict = item["annotations"][0] # parse the only 0 index list to this content 
        if dict.get("type") == "singleAnswer":
            
            

if __name__ == "__main__":
    parsingDataset()
