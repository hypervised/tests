class my_test_class(object):
    def __init__(self) -> None:
        pass

    def filter_namespaces(self, data, filter: str):
        results = []
        for namespace in data.items:
            if filter in namespace.metadata.name:
                results.append(namespace.metadata.name)
        return results
