from workout_gens.chest_and_shoulders_day import generate_chest_and_shoulders_day
from workout_gens.back_day import generate_back_day
from workout_gens.legs_day import generate_leg_day
from workout_gens.arm_day import generate_arm_day
from workout_gens.abs_day import generate_abs_day
import time
import requests

connect_url = "https://workout-mixer.vercel.app/"
close_url = "https://workout-mixer.vercel.app/close"

if __name__ == "__main__":
    requests.get(connect_url)
    v = int(input("Chest and shoulders, arms, back, legs or abs? (1,2,3,4 or 5)"))
    if v == 1:
        generate_chest_and_shoulders_day()
    elif v == 2:
        generate_arm_day()
    elif v == 3:
        generate_back_day()
    elif v == 4:
        generate_leg_day()
    elif v == 5:
        generate_abs_day()
    else:
        print("Invalid entry. Start over!")
        exit()
    print("Generating workout. Please wait...")
    time.sleep(1)
    input("Workout generated. Press Enter to continue")
