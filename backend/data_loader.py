import pandas as pd

def load_data(file):
    try:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file, sep=";")
        elif file.name.endswith('.json'):
            df = pd.read_json(file)
        elif file.name.endswith('.xml'):
            df = pd.read_xml(file)
        else:
            raise ValueError("Unsupported file format")
        return df
    except Exception as e:
        raise ValueError(f"Error loading file: {e}")