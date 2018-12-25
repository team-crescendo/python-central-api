import json, os


FILENAME = os.path.join(os.path.dirname(__file__), "secret.json")

with open(FILENAME, "r") as f:
    SECRET = json.load(f)


def get_secret(key):
    return SECRET[key]
