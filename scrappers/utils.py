import requests
from bs4 import BeautifulSoup
from constants import *
import json
import os

# Fetches a page (BASE URL by default) and returns soup
def fetch_page(url=BASE_URL):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        return soup
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error fetching the page: {e}")

# Save data to json
def save_data_to_json(data, filename, directory):
    if filename is None or directory is None:
        raise Exception("Error while saving data, filename and directory are required")
    # Create the directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, f"{filename}.json")
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)

# return data in JSON format
def str_to_json(data):
    if data is None:
        raise Exception("Error while formatting data, no data input")
    return json.dumps(data, indent=4)
