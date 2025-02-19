import os


def get_data_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "knowledge_graph"))


def get_templates_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "templates"))
