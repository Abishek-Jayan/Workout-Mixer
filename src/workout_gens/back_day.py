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
    vertical = random.sample(back_data["vertical"], 2)
    horizontal = random.sample(back_data["horizontal"], 2)
    lowerback = random.sample(back_data["lower_back"], 1)

    write_to_file(
        mandatory_data["back_workout"] + vertical + horizontal + lowerback,
        start=start,
    )
