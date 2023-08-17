import random
import requests
from common.common import write_to_file

url = "http://localhost:3000/getWorkoutData"


def generate_pull_day(start=True):
    random.seed(random.SystemRandom().randint(1, 100))
    generate_back_workout(start)
    generate_biceps_workout()
    generate_abs_workout()


def generate_back_workout(start):
    back_data = requests.get(url, params={"musclegroup": "back"}).json()
    vertical = random.sample(back_data["vertical"], 2)
    horizontal = random.sample(back_data["horizontal"], 2)
    lowerback = random.sample(back_data["lower_back"], 1)

    write_to_file(vertical + horizontal + lowerback, start=start)


def generate_biceps_workout():
    biceps_data = requests.get(url, params={"musclegroup": "biceps"}).json()
    long_head = random.sample(biceps_data["longhead"], 2)
    short_head = random.sample(biceps_data["shorthead"], 2)

    write_to_file(long_head + short_head)


def generate_abs_workout():
    abs_data = requests.get(url, params={"musclegroup": "abs"}).json()
    abs_workout = abs_data[random.choice(["set1", "set2", "set3"])]
    write_to_file(abs_workout)
