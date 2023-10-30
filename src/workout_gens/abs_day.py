import random
import requests
from common.common import write_to_file
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("BACKEND_URL")


def generate_abs_day(start=True):
    random.seed(random.SystemRandom().randint(1, 100))
    generate_abs_workout(start)


def generate_abs_workout(start):
    abs_data = requests.get(url, params={"musclegroup": "abs"}).json()
    abs_workout = abs_data[random.choice(["set1", "set2", "set3"])]
    write_to_file(["Handstand Finger Press"] + abs_workout, start=start)
