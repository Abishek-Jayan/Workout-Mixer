def write_to_file(workout):
    file = open("workout.txt","a")
    for exercise in workout:
        file.write(exercise.text+ "\n")
    file.close()