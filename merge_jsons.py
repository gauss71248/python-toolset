import json
import os
from time import sleep
from tqdm import tqdm


def retrieve_jsons_from_path(path: str) -> list:
    result = []
    
    print("Reading files ...")
    
    for subdir, _, files in os.walk(path):  
        for file in tqdm(files):
            filepath = subdir + os.sep + file
            with open(filepath, 'r') as f:
                try:
                    data = json.load(f)
                except:
                    print(f"error in file {filepath}")
                    print("*"*20)
                result = result + data
        print("*"*20)
        print(f"{len(result)} records retrieved...")
        print("*"*20)
    return result

def write_json(data: list, path: str):
    print("Writing data ...")
    json_string = json.dumps(data)
    with open(path, 'w') as outfile:
        try:
            json.dump(json_string, outfile)
            print("Data successfully written.")
        except:
            print("error in writing file")
    

if __name__=="__main__":
    path = "/Users/sschlesinger/Downloads/test"
    data = retrieve_jsons_from_path(path)
    output_path = "/Users/sschlesinger/Downloads/out.json"
    write_json(data, output_path)
