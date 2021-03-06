from itertools import cycle
from pathlib import Path
from random import shuffle
from typing import List

import click

DICTS = {}


def load_internal_dicts():
    data = [str(x) for x in range(1, 21)]
    shuffle(data)
    DICTS["smallnum"] = cycle(data)


def load_dicts():
    load_internal_dicts()
    for d in get_dict_list():
        with open(d) as f:
            data = [s.strip() for s in f.readlines()]
        name = d.stem
        shuffle(data)
        DICTS[name] = cycle(data)


def gen_identifier(pattern: str) -> str:
    for d in DICTS.keys():
        key = "{%s}" % d
        while key in pattern:
            pattern = pattern.replace(key, next(DICTS[d]), 1)
    return pattern


def get_dict_list() -> List[Path]:
    dicts = []
    places = [
        Path(__file__).parent / "data",
        Path.home() / ".local" / "roke",
        Path(".roke"),
    ]
    for place in places:
        if place.is_dir():
            dicts.extend(list(place.glob("*.txt")))
    return dicts


def gen_identifiers(pattern, count):
    result = []
    for _ in range(count):
        result.append(gen_identifier(pattern))
    return result


@click.command()
@click.option(
    "--pattern",
    default="{smallnum}-{noun}-{noun}",
    help="Pattern for the generated identifier.",
)
@click.option("--count", default=1, help="How many identifiers to generate.")
def main(pattern, count):
    load_dicts()
    print("\n".join(gen_identifiers(pattern, count)))
