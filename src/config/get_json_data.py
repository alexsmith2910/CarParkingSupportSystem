import json
import os
import pathlib


def get_data(json_file):
    json_files = [file for file in os.listdir(pathlib.Path(__file__).parent.resolve()) if file.endswith(".json")]

    if not json_file.endswith(".json"):
        json_file += ".json"
    if json_file not in json_files:
        return None

    with open(f"{pathlib.Path(__file__).parent.resolve()}\\{json_file}") as f:
        data = json.load(f)
    f.close()
    return data
