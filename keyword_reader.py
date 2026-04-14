from scripts.StatisticsExtractor import StatisticsExtractor
import os
import json 
paths = "/home/linus-brewitz/Code/thesis/scyros/keywords"

# TODO: I might have to remove this file since it is no longer being used
#NOTE: this is assuming there is only ONE keyword per file
file_to_kw = dict()
def read_json():
    for e in os.scandir(paths):
        if e.is_file():
            with open(e.path, "r") as f:
                data = json.load(f)
                new_string = data["keywords"][0].replace("\\", "")
                file_to_kw[e.name] = new_string
    return file_to_kw
    

read_json()

