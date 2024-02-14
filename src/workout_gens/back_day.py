import random
import requests
from common.common import write_to_file
import os
from dotenv import load_dotenv
import json

load_dotenv()

url = os.getenv("BACKEND_URL")
with open("src\workout_gens\mandatory.json", "r") as mandatory_file:
    mandatory_data = json.load(mandatory_file)

def generate_back_day(start=True):
    random.seed(random.SystemRandom().randint(1, 100))
    generate_back_workout(start)


def generate_back_workout(start):
    back_data = requests.get(url, params={"musclegroup": "back"}).json()
    rear_delts = random.sample(back_data["rear_delts"],1)
    upper_lats = random.sample(back_data["upper_lats"], 1)
    middle_lats = random.sample(back_data["middle_lats"], 1)
    lower_lats =  random.sample(back_data["lower_lats"], 1)
    lowerback = random.sample(back_data["lower_back"], 1)

    write_to_file(
        mandatory_data["back_workout"] + rear_delts + upper_lats + middle_lats + lower_lats + lowerback,
        start=start,
    )
