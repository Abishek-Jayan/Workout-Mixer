import random
import requests
from common.common import write_to_file
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("BACKEND_URL")


def generate_back_day(start=True):
    random.seed(random.SystemRandom().randint(1, 100))
    generate_back_workout(start)


def generate_back_workout(start):
    back_data = requests.get(url, params={"musclegroup": "back"}).json()
    vertical = random.sample(back_data["vertical"], 1)
    horizontal = random.sample(back_data["horizontal"], 1)
    lowerback = random.sample(back_data["lower_back"], 1)

    write_to_file(
        ["100 Pullups", "Handstand Finger Press"] + vertical + horizontal + lowerback,
        start=start,
    )
