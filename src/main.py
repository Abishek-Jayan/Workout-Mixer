from workout_gens.multi_workout import multi_workout_generator
from workout_gens.push_day import generate_push_day
from workout_gens.pull_day import generate_pull_day
from workout_gens.legs_day import generate_leg_day
import time

if __name__ == "__main__":
    while True:
        v = int(input("Single Day or Multiple days? (1 or 2)"))
        try:
            if v == 1:
                v = int(input("Push, pull or legs? (1,2 or 3)"))
                while True:
                    if v == 1:
                        generate_push_day()
                    elif v == 2:
                        generate_pull_day()
                    elif v == 3:
                        generate_leg_day()
                    else:
                        print("Invalid entry. Start over!")
                        continue
                    break
            elif v == 2:
                days = int(
                    input("Enter number of days of workouts needed. Even numbers only!")
                )
                multi_workout_generator(days)

            break
        except:
            print("Invalid entry. Start over!")
            continue
    print("Generating workout. Please wait...")
    time.sleep(1)
    input("Workout generated. Press Enter to continue")
