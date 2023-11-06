import random
import requests
from common.common import write_to_file
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("BACKEND_URL")


def generate_arm_day(start=True):
    random.seed(random.SystemRandom().randint(1, 100))
    generate_trap_workout(start)
    generate_tricep_workout()
    generate_biceps_workout()
    generate_forearms_workout()


def generate_trap_workout(start):
    traps_data = requests.get(url, params={"musclegroup": "traps"}).json()
    traps_workout = random.sample(list(traps_data), 1)
    write_to_file(["50 Dips", "Handstand Finger Press"] + traps_workout, start=start)


def generate_tricep_workout():
    triceps_data = requests.get(url, params={"musclegroup": "triceps"}).json()
    tricep_workout = random.sample(list(triceps_data), 2)

    write_to_file(tricep_workout)


def generate_biceps_workout():
    biceps_data = requests.get(url, params={"musclegroup": "biceps"}).json()
    long_head = random.sample(biceps_data["longhead"], 1)
    short_head = random.sample(biceps_data["shorthead"], 1)

    write_to_file(long_head + short_head)


def generate_forearms_workout():
    forearms_workout = requests.get(url, params={"musclegroup": "forearms"}).json()
    write_to_file(list(forearms_workout))
