import click
from utils import *


@click.command()
@click.option("-o", "--output_filename", default="output.tar.gz")
@click.argument("source_path", type=click.Path(exists=True))
def main(output_filename, source_path):
    click.echo("Archiving " + click.format_filename(source_path))
    archive_and_compress(output_filename, source_path)


if __name__ == "__main__":
    main()
