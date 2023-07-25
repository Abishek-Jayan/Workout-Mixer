import xml.etree.ElementTree as ET
import random

from common.common import write_to_file


def generate_pull_day(start=True):
    generate_back_workout(start)
    generate_biceps_workout()
    generate_abs_workout()


def generate_back_workout(start):
    back_tree = ET.parse("assets/Back.xml")
    back_tree_root = back_tree.getroot()
    vertical = random.sample(list(back_tree_root.find("vertical")), 2)
    horizontal = random.sample(list(back_tree_root.find("horizontal")), 2)
    lowerback = random.sample(list(back_tree_root.find("lower_back")), 1)

    write_to_file(vertical + horizontal + lowerback, start=start)


def generate_biceps_workout():
    biceps_tree = ET.parse("assets/Biceps.xml")
    biceps_tree_root = biceps_tree.getroot()
    long_head = random.sample(list(biceps_tree_root.find("longhead")), 1)
    short_head = random.sample(list(biceps_tree_root.find("shorthead")), 2)

    write_to_file(long_head + short_head)


def generate_abs_workout():
    abs_tree = ET.parse("assets/Abs.xml")
    abs_tree_root = abs_tree.getroot()
    abs_workout = abs_tree_root.find(random.choice(["set1", "set2"]))
    write_to_file(abs_workout)
