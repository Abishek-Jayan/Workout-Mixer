from workout_gens.push_day import generate_push_day
from workout_gens.pull_day import generate_pull_day
from workout_gens.legs_day import generate_leg_day
import time

if __name__ == "__main__":
    v = int(input("Push, pull or legs? (1,2 or 3)"))
    if v == 1:
        generate_push_day()
    elif v == 2:
        generate_pull_day()
    elif v == 3:
        generate_leg_day()
    else:
        print("Invalid entry. Start over!")
    print("Generating workout. Please wait...")
    time.sleep(1)
    input("Workout generated. Press Enter to continue")
