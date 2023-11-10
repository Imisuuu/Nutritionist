from helper import Helper
from gui import gui
import datetime
import os

# Wywala gdy nie znajdzie peruwiańskiego pre-workoutu
if __name__ == "__main__":
    helper = Helper(input="potatoes")
    if not os.path.exists(f"./Data/{helper.date}.txt"):
        helper.create_file()
    gui()