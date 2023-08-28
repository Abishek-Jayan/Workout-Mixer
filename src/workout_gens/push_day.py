import random
import requests
from common.common import write_to_file

url = "https://workout-mixer.vercel.app/getWorkoutData"


def generate_push_day(start=True):
    random.seed(random.SystemRandom().randint(1, 100))
    generate_chest_workout(start)
    generate_shoulder_workout()
    generate_tricep_workout()


def generate_chest_workout(start):
    chest_data = requests.get(url, params={"musclegroup": "chest"}).json()
    chest_workout = random.sample(list(chest_data), 3)

    write_to_file(chest_workout, start=start)


def generate_shoulder_workout():
    shoulder_data = requests.get(url, params={"musclegroup": "shoulders"}).json()
    traps_data = requests.get(url, params={"musclegroup": "traps"}).json()
    shoulders_workout = random.sample(list(shoulder_data), 2)
    traps_workout = random.sample(list(traps_data), 1)

    write_to_file(shoulders_workout + traps_workout)


def generate_tricep_workout():
    triceps_data = requests.get(url, params={"musclegroup": "triceps"}).json()
    tricep_workout = random.sample(list(triceps_data), 2)

    write_to_file(tricep_workout)
