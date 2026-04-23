# storage.py

import json
import os

FILE_NAME = "history.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


def add_expense(expense):
    data = load_data()
    data.append(expense)
    save_data(data)