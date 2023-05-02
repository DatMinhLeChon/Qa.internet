import os
import pandas as pd
import json

def running():
    json_path = 'dev.json'

    json_open = open(json_path)
    json_load = json.load(json_open)

    print(json_load)

if __name__ == "__main__":
    running()
