import click

smallnum = [str(i) for i in range(15)]
basic = "the quick brown fox jumped over the lazy dog".split()

@click.command()
@click.option("--dicts", default="basic,smallnum", help="What list of words should be used.")
@click.option("--format", default="{smallnum}-{basic}-{basic}", help="Format for the generated identifier.")
@click.option("--count", default=1, help="How many identifiers to generate.")

def main():
    pass
