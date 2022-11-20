import os
import json

config = json.load(open('.env/config.json', 'r'))

for k, v in config.items():
    os.environ[k] = v