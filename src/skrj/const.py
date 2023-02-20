import os
import pathlib

BUILD_DIR = pathlib.Path(os.environ["BUILD_DIR"])
SRC_DIR = pathlib.Path(__file__).parent
TEMPLATES_DIR = SRC_DIR / "templates"

DATA = SRC_DIR / "data"
DATA_TRAINS = DATA / "trains"
DATA_SPEED = DATA / "speed.json"
