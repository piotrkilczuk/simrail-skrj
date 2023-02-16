import datetime
import re
import warnings

from skrj import train_definitions

HOUR_RE = re.compile(r">([0-2][0-9]:[0-6][0-9])<")


def build_fodts():
    for train_group_definition in train_definitions.registry:
        for train in train_group_definition:
            print(train.category, train.number)
            text_out = train_group_definition.template.replace("{{ cat }}", train.category)
            text_out = text_out.replace("{{ num }}", str(train.number))
            for hour in HOUR_RE.findall(text_out):
                hour_parsed = datetime.datetime(2023, 1, 1, hour=int(hour[:2]), minute=int(hour[3:]))
                hour_adjusted = hour_parsed + train.offset
                hour_adjusted_as_str = hour_adjusted.strftime("%H:%M")
                text_out = text_out.replace(hour, hour_adjusted_as_str)
            with train.fodt_file() as f:
                f.write(text_out)


def build_htmls():
    warnings.warn("Building HTML is not supported yet.")


def build():
    build_fodts()
    build_htmls()
