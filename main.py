import os
from dotenv import load_dotenv

load_dotenv()

MINER_KEY = os.getenv("MINER_KEY")

print(MINER_KEY)
