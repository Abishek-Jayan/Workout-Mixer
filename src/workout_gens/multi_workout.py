from workout_gens.push_day import generate_push_day
from workout_gens.pull_day import generate_pull_day
from workout_gens.legs_day import generate_leg_day


def multi_workout_generator(days: int):
    start = False
    for day in range(0, days, 3):
        if days > 0:
            start = True
        generate_push_day(start)
        start = False
        generate_pull_day(start)
        generate_leg_day(start)
