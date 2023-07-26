import xml.etree.ElementTree as ET
import random

from common.common import write_to_file


def generate_push_day(start=True):
    random.seed(random.SystemRandom().randint(1,100))
    generate_chest_workout(start)
    generate_shoulder_workout()
    generate_tricep_workout()


def generate_chest_workout(start):
    chest_tree = ET.parse("assets/Chest.xml")
    chest_tree_root = chest_tree.getroot()
    chest_workout = random.sample(list(chest_tree_root), 3)

    write_to_file(chest_workout, start=start)


def generate_shoulder_workout():
    shoulders_tree = ET.parse("assets/Shoulders.xml")
    traps_tree = ET.parse("assets/Traps.xml")
    shoulders_tree_root = shoulders_tree.getroot()
    traps_tree_root = traps_tree.getroot()
    shoulders_workout = random.sample(list(shoulders_tree_root), 2)
    traps_workout = random.sample(list(traps_tree_root), 1)

    write_to_file(shoulders_workout + traps_workout)


def generate_tricep_workout():
    triceps_tree = ET.parse("assets/Triceps.xml")
    tricep_tree_root = triceps_tree.getroot()
    tricep_workout = random.sample(list(tricep_tree_root), 3)

    write_to_file(tricep_workout)
