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

def generate_arm_day(start=True):
    random.seed(random.SystemRandom().randint(1, 100))
    generate_trap_workout(start)
    generate_tricep_workout()
    generate_biceps_workout()
    generate_forearms_workout()


def generate_trap_workout(start):
    traps_data = requests.get(url, params={"musclegroup": "traps"}).json()
    traps_workout = random.sample(list(traps_data), 2)
    write_to_file(mandatory_data["traps_workout"] + traps_workout, start=start)


def generate_tricep_workout():
    triceps_data = requests.get(url, params={"musclegroup": "triceps"}).json()
    tricep_workout = random.sample(list(triceps_data), 2)

    write_to_file(mandatory_data["triceps_workout"] + tricep_workout)


def generate_biceps_workout():
    biceps_data = requests.get(url, params={"musclegroup": "biceps"}).json()
    long_head = random.sample(biceps_data["longhead"], 1)
    short_head = random.sample(biceps_data["shorthead"], 1)

    write_to_file(mandatory_data["biceps_workout"] + long_head + short_head)


def generate_forearms_workout():
    forearms_workout = requests.get(url, params={"musclegroup": "forearms"}).json()
    write_to_file(mandatory_data["forearms_workout"] + list(forearms_workout))
