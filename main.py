import os
import pandas as pd
import json
# jsol light:
# id
# questions
# annotation:
    # type
    # answers

class Annotation():
    def __init__(self, type, answer):
        self.type = type
        self.answer = answer

class DataItem():
    def __init__(self, question, annotation):
        self.question = question
        self. annotation = annotation

class DataQA():
    def __init__(self, item):
        self.metric = "Bleu"
        self.score = None
        self.item = item
        
    def databaseVocab(self):
        return
        

        
def running():
    json_path = 'train_light.json'
    json_open = open(json_path)
    json_load = json.load(json_open)
    for item in json_load:
        print(item["annotations"])
    

if __name__ == "__main__":
    running()
