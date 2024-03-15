import xml.etree.ElementTree as ET
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

def generate_leg_day(start=True):
    random.seed(random.SystemRandom().randint(1, 100))
    generate_legs_workout(start)


def generate_legs_workout(start):
    legs_data = requests.get(url, params={"musclegroup": "legs"}).json()
    quads = random.sample(legs_data["quads"], 1)
    hamstrings = random.sample(legs_data["hamstrings"], 1)
    calves = random.sample(legs_data["calves"], 1)

    write_to_file(
        mandatory_data["leg_workout"] + quads + hamstrings + calves,
        start=start,
    )
