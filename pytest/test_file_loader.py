from operator import eq
from file_loader import FileLoader


class TestFileLoader:

    def test_can_load_yaml_files(self):
        file_loader = FileLoader()
        yaml_file = file_loader.load_yaml("mock_data.yaml")

        assert eq(yaml_file["data"]["someKey"], "someValue")

    def test_can_load_json_files(self):
        file_loader = FileLoader()
        json_file = file_loader.load_json("mock_data.json")

        assert eq(json_file["data"]["someKey"], "someValue")
