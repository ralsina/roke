from itertools import cycle
from pathlib import Path
from random import shuffle

import click

DICTS = {}


def load_dicts(dicts):
    for d in dicts:
        if d == "smallnum":
            data = [str(x) for x in range(20)]
        else:
            with open(Path(__file__).parent / "data" / (d + ".txt")) as f:
                data = [s.strip() for s in f.readlines()]
        shuffle(data)
        DICTS[d] = cycle(data)


def gen_identifier(dicts, format):
    for d in dicts:
        key = "{%s}" % d
        while key in format:
            format = format.replace(key, next(DICTS[d]), 1)
    return format


@click.command()
@click.option(
    "--dicts", default="smallnum,noun", help="What list of words should be used."
)
@click.option(
    "--format",
    default="{smallnum}-{noun}-{noun}",
    help="Format for the generated identifier.",
)
@click.option("--count", default=1, help="How many identifiers to generate.")
def main(dicts, format, count):
    dicts = [d.strip() for d in dicts.split(",")]
    load_dicts(dicts)
    for _ in range(count):
        print(gen_identifier(dicts, format))
