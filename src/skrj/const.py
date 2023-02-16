import os
import pathlib

BUILD_DIR = pathlib.Path(os.environ["BUILD_DIR"])
SRC_DIR = pathlib.Path(__file__).parent
TEMPLATES_DIR = SRC_DIR / "templates"

JSON_TRAIN = SRC_DIR / "train.json"
