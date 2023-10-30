import random
import requests
from common.common import write_to_file
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("BACKEND_URL")


def generate_chest_and_shoulders_day(start=True):
    random.seed(random.SystemRandom().randint(1, 100))
    generate_chest_workout(start)
    generate_shoulder_workout()


def generate_chest_workout(start):
    chest_data = requests.get(url, params={"musclegroup": "chest"}).json()
    chest_workout = random.sample(list(chest_data), 2)

    write_to_file(
        ["100 Pushups", "Handstand Finger Press"] + chest_workout, start=start
    )


def generate_shoulder_workout():
    shoulder_data = requests.get(url, params={"musclegroup": "shoulders"}).json()
    shoulders_workout = random.sample(list(shoulder_data), 2)

    write_to_file(shoulders_workout)
