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

def generate_chest_and_shoulders_day(start=True):
    random.seed(random.SystemRandom().randint(1, 100))
    generate_chest_workout(start)
    generate_shoulder_workout()

def generate_chest_workout(start):
    chest_data = requests.get(url, params={"musclegroup": "chest"})

    if chest_data.status_code == 200:
        chest_workout = random.sample(chest_data.json(), 2)
        write_to_file(mandatory_data["chest_workout"] + chest_workout, start=start)
    else:
        print(f"Failed to fetch chest workout data. Status code: {chest_data.status_code}")

def generate_shoulder_workout():
    shoulder_data = requests.get(url, params={"musclegroup": "shoulders"})

    if shoulder_data.status_code == 200:
        shoulders_workout = random.sample(shoulder_data.json(), 2)
        write_to_file(mandatory_data["shoulder_workout"] + shoulders_workout)
    else:
        print(f"Failed to fetch shoulder workout data. Status code: {shoulder_data.status_code}")
