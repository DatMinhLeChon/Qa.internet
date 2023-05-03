import os
import pandas as pd
import json
import thefuzz

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
        self.score = None

class MultipleAnswer():
    def __init__(self, this_id, question, qa_pairs):
        self.id = this_id
        self.question = question
        self.qa_pairs = qa_pairs
        
class SingleAnswer():
    def __init__(self, id, question, answer):
        self.id = id
        self.question = question
        self.answer = answer
        self.score = None

class DataQA():
    def __init__(self, item, data_item_list):
        self.metric = "Bleu"
        self.data_item_list = data_item_list
        self.weight = 0.1
    
    #lọc step1
    def databaseVocab(self, vocab_db):
        item_list = []
        for item in self.data_item_list:
            for item2 in vocab_db:
                rattio = thefuzz.token_sort_ratio(item2, item)
                if rattio >= 0.3:
                    item_list.append(item)
        return item_list

        
def parsingDataset():
    single_container, annotation_container = [] , []
    json_path = 'train_light.json' # dataset
    json_open = open(json_path)
    json_load = json.load(json_open)
    for item in json_load:
        dict = item["annotations"][0] # parse the only 0 index list to this content 
        if dict.get("type") == "singleAnswer":
            single_container.append(SingleAnswer(item["id"], item["question"], item["annotations"][0].get("answer")))
        elif dict.get("type") == "multipleQAs":
            annotation_container_temp = []
            dict_temp = (dict.get("qaPairs"))[0]
                #annotation_container_temp.append(QaPairs(item2.get("question"), item2.get("answer")))
            annotation_container.append(MultipleAnswer(item["id"], item["question"], dict_temp))
    return single_container, annotation_container
            
def fuzzyMatching():
    

if __name__ == "__main__":
    parsingDataset()
