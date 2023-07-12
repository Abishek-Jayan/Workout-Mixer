def write_to_file(workout, start=False):
    if start:
        file = open("workout.txt", "w")
    else:
        file = open("workout.txt", "a")
    for exercise in workout:
        file.write(exercise.text + "\n")
    file.close()
