import datetime
import json
import re
import warnings

import jinja2

from skrj import train_definitions, const

HOUR_RE = re.compile(r">([0-2][0-9]:[0-6][0-9])<")


# def build_fodts():
#     for train_group_definition in train_definitions.registry:
#         for train in train_group_definition:
#             print(train.category, train.number)
#             text_out = train_group_definition.template.replace("{{ cat }}", train.category)
#             text_out = text_out.replace("{{ num }}", str(train.number))
#             for hour in HOUR_RE.findall(text_out):
#                 hour_parsed = datetime.datetime(2023, 1, 1, hour=int(hour[:2]), minute=int(hour[3:]))
#                 hour_adjusted = hour_parsed + train.offset
#                 hour_adjusted_as_str = hour_adjusted.strftime("%H:%M")
#                 text_out = text_out.replace(hour, hour_adjusted_as_str)
#             with train.fodt_file() as f:
#                 f.write(text_out)


def build_htmls():
    with const.JSON_TRAIN.open() as json_file:
        train_data = json.load(json_file)[0]
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(const.TEMPLATES_DIR))
    template = env.get_template("generic.html")
    rendered = template.render(train=train_data, timetable=train_data["timetable"])
    (const.BUILD_DIR / "train.html").write_text(rendered)


def build():
    # build_fodts()
    build_htmls()
