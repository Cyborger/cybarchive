import click
from utils import *


@click.command()
@click.option("-e", "--encrypt")
@click.option("-n", "--name")
@click.argument("source_path", type=click.Path(exists=True))
def main(name, encrypt, source_path):
    click.echo("Archiving " + click.format_filename(source_path))

    tgz_archive_path = archive_and_compress(name, source_path)
    click.echo("File archived to " + tgz_archive_path)

    if encrypt is None:
        return

    gpg_archive_path = encrypt_file(tgz_archive_path, encrypt)
    click.echo("File encrypted to " + gpg_archive_path)


if __name__ == "__main__":
    main()
