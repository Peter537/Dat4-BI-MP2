import pandas as pd

def load_paths(file_paths):
    return [load(file_path) for file_path in file_paths]

def load(file_path):
    if not file_path.endswith('.xlsx'):
        return None

    return pd.read_excel(file_path)
