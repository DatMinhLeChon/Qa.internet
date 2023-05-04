import os
import pandas as pd
import json
from fuzzywuzzy import fuzz
import xml.etree.ElementTree as ET

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
    def __init__(self, data_item_list, vocab_db):
        self.metric = "Bleu"
        self.data_item_list = data_item_list
        self.vocab_db = vocab_db
        self.weight = 0.3
            #lọc step1
    def databaseVocab(self):
        item_list = []
        for item in self.data_item_list:
            for item2 in self.vocab_db:
                rattio = fuzz.token_sort_ratio(item2.get("eng"), item.question)
                if rattio/100 >= self.weight:
                    item.score == rattio
                    item_list.append(item)
                    break
                    
        return item_list

class VocabularyDB():
    def __init__(self, file_name):
        self.root = ET.parse(file_name).getroot()
    
    def parsingVocabulary(self):
        container_vocabulary = []
        for child in self.root:
            container_vocabulary.append({"eng":child[0].text, "vie":child[1].text})
        return container_vocabulary

    def exportVocabulary(self):
        print(self.parsingVocabulary())

        
def parsingDataset(file_name):
    single_container, annotation_container = [] , [] # dataset
    json_open = open(file_name)
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


if __name__ == "__main__":
    vocab = VocabularyDB(r'vocab_db.xml')
    vocab_db= vocab.parsingVocabulary()
    single_container, multiple_container = parsingDataset(r'train_light.json')
    data = DataQA(single_container, vocab_db).databaseVocab()
    for item in data:
        print(item.question)
        print(item.answer)
