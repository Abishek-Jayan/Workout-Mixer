import xml.etree.ElementTree as ET
import random
import requests
from common.common import write_to_file
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("BACKEND_URL")


def generate_leg_day(start=True):
    random.seed(random.SystemRandom().randint(1, 100))
    generate_legs_workout(start)


def generate_legs_workout(start):
    legs_data = requests.get(url, params={"musclegroup": "legs"}).json()
    quads = random.sample(legs_data["quads"], 2)
    hamstrings = random.sample(legs_data["hamstrings"], 2)
    calves = random.sample(legs_data["calves"], 1)

    write_to_file(
        ["100 Squats", "Handstand Finger Press"] + quads + hamstrings + calves,
        start=start,
    )
