def load_data(file_path):
    import pandas as pd
    data = pd.read_csv(file_path)
    return data

def process_data(data):
    # Example processing: remove duplicates
    processed_data = data.drop_duplicates()
    return processed_data