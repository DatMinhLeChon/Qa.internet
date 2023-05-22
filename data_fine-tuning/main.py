import pandas as pd
import json
import os
from nltk.tokenize import sent_tokenize, word_tokenize

FILE_PATH = r"train_hotel.json"

class QaData():
    def __init__(self,id,  question,  annotation = {}):
        self._id = id 
        self._question = question 
        self._annotation = annotation
    
class QaDataList():
    def __init__(self):
        self._container = [] 
        
    def addOneItem(self, id, question, annotation):
        self._container.append( QaData(id, question, annotation))
    
    def parsingJsonDataset(self, file_path):
        container_qa_data = [] 
        json_open = open(file_path)
        json_load = json.load(json_open)
        for item in json_load:
            container_qa_data.append(QaData(json_load[0]["id"], \
            json_load[0]["question"], \
            {"type": json_load[0]["annotation"][0].get("type"),\
                "answer": json_load[0]["annotation"][0].get("answer")}))
        self._container = container_qa_data
            
 
class QaDataFormat():
    def __init__(self):
        self._container = []
    
    def parsingQaData(self, container_qa_data):
        for item in container_qa_data: 
            self._container.append({"prompt": item._question, "completion": item._annotation.get("answer")})
    
    def qaDataFormatToJson(self):
        if len(self._container)== 0:
            return 0
        else:
            with open('data_fine-tuning/FormatData.json', 'w') as outfile:
                json.dump(self._container, outfile)
                

if __name__ == "__main__":
    temp_list = QaDataList()
    temp_list.parsingJsonDataset(FILE_PATH)
    temp_list_format = QaDataFormat()
    temp_list_format.parsingQaData(temp_list._container)
    temp_list_format.qaDataFormatToJson()
    
    
