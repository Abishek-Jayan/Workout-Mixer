import xml.etree.ElementTree as ET
import random
import requests
from common.common import write_to_file

url = "http://localhost:3000/getWorkoutData"


def generate_leg_day(start=True):
    random.seed(random.SystemRandom().randint(1, 100))
    generate_legs_workout(start)
    generate_forearms_workout()


def generate_legs_workout(start):
    legs_data = requests.get(url, params={"musclegroup": "legs"}).json()
    quads = random.sample(legs_data["quads"], 3)
    hamstrings = random.sample(legs_data["hamstrings"], 2)
    calves = random.sample(legs_data["calves"], 1)

    write_to_file(quads + hamstrings + calves, start=start)


def generate_forearms_workout():
    forearms_workout = requests.get(url, params={"musclegroup": "legs"}).json()
    write_to_file(list(forearms_workout))
