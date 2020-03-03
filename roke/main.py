from itertools import cycle
from pathlib import Path
from random import shuffle

import click

DICTS = {}


def load_dicts():
    for d in get_dict_list():
        if d == "smallnum":
            data = [str(x) for x in range(1, 21)]
            name = d
        else:
            with open(d) as f:
                data = [s.strip() for s in f.readlines()]
            name = d.stem
        shuffle(data)
        DICTS[name] = cycle(data)


def gen_identifier(format):
    for d in DICTS.keys():
        key = "{%s}" % d
        while key in format:
            format = format.replace(key, next(DICTS[d]), 1)
    return format


def get_dict_list():
    dicts = ["smallnum"]
    places = [Path(__file__).parent / "data", Path("~/.local/roke"), Path(".roke")]
    for place in places:
        if place.is_dir():
            dicts.extend(list(place.glob("*.txt")))
    return dicts


@click.command()
@click.option(
    "--format",
    default="{smallnum}-{noun}-{noun}",
    help="Format for the generated identifier.",
)
@click.option("--count", default=1, help="How many identifiers to generate.")
def main(format, count):
    load_dicts()
    for _ in range(count):
        print(gen_identifier(format))
