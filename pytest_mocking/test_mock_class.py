from unittest.mock import patch
import json
from types import SimpleNamespace
from kubernetes import client
from my_test_class import my_test_class


class TestK8sClient:
    @patch('kubernetes.client.CoreV1Api.list_namespace')
    def test_can_list_namespaces(self, mock_client):

        with open("./mock_data.json") as f:
            class_created_from_file = json.load(f, object_hook=lambda d: SimpleNamespace(**d))

        mock_client.return_value = class_created_from_file

        mock_data = client.CoreV1Api.list_namespace()

        test_class = my_test_class()

        test_function_output = test_class.filter_namespaces(mock_data, "1")

        print(test_function_output)

        assert "some-namespace-1" in test_function_output
        assert "some-namespace-2" not in test_function_output
        assert len(test_function_output) == 1
