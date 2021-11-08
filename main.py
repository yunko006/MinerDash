import os
from dotenv import load_dotenv

import requests
import json
import pandas as pd

load_dotenv()

MINER_KEY = os.getenv("MINER_KEY")

response_API = requests.get(
    f"https://api.ethermine.org/miner/:{MINER_KEY}/dashboard")

data = response_API.text

parse_json = json.loads(data)

statistics = parse_json['data']['statistics']

df = pd.DataFrame.from_dict(statistics)

print(df)

df.to_excel('statistics.xlsx')
