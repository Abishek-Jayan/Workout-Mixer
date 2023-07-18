import xml.etree.ElementTree as ET
import random

from common.common import write_to_file


def generate_leg_day(start=True):
    generate_legs_workout(start)
    generate_forearms_workout()


def generate_legs_workout(start):
    legs_tree = ET.parse("assets/Legs.xml")
    legs_tree_root = legs_tree.getroot()
    quads = random.sample(list(legs_tree_root.find("Quads")), 3)
    hamstrings = random.sample(list(legs_tree_root.find("Hamstrings")), 2)
    calves = random.sample(list(legs_tree_root.find("Calves")), 1)

    write_to_file(quads + hamstrings + calves, start=start)


def generate_forearms_workout():
    forearms_tree = ET.parse("assets/Forearms.xml")
    forearms_workout = forearms_tree.getroot()

    write_to_file(list(forearms_workout))
