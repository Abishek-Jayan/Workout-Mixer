from workout_gens.chest_and_shoulders_day import generate_chest_and_shoulders_day
from workout_gens.back_day import generate_back_day
from workout_gens.legs_day import generate_leg_day
from workout_gens.arm_day import generate_arm_day
from gui import UI
import time
import requests
connect_url = "https://workout-mixer.vercel.app/"
close_url = "https://workout-mixer.vercel.app/close"

if __name__ == "__main__":
    requests.get(connect_url)
    while True:
        try:
            v = int(input("Chest and shoulders, arms, back or legs? (1,2,3 or 4) or press 0 to exit: "))
            if v == 1:
                generate_chest_and_shoulders_day()
            elif v == 2:
                generate_arm_day()
            elif v == 3:
                generate_back_day()
            elif v == 4:
                generate_leg_day()
    # Writing ab workouts myself for now so no need for code
    #    elif v == 5:
    #       generate_abs_day()
            elif v==0:
                print("Thank you! Bye Bye!")
                break
            else:
                print("Invalid entry. Start over!")
            input("Workout generated. Press Enter to continue")
        except:
            print("\nForce exit sequence initiated!")
            break
