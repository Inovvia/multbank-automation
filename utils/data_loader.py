
import json
import os

def load_test_data(file_name="test_data.json"):
    """
    Loads test data from the data directory.
    """
    # Assuming data is one level up from utils or in the root/data
    # Adjust path according to project structure
    # current file is in /utils/
    # data is in /data/
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    data_path = os.path.join(project_root, "data", file_name)
    
    with open(data_path, 'r') as f:
        return json.load(f)
