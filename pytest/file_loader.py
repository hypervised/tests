import yaml
import json


class FileLoader:
    def __init__(self) -> None:
        self.version = 1.0

    def load_yaml(self, filepath):
        with open(filepath, 'r') as f:
            yaml_file = yaml.safe_load(f)

        return yaml_file

    def load_json(self, filepath):
        with open(filepath, 'r') as f:
            json_file = json.load(f)

        return json_file
