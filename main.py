import click

from utils import *


@click.command()
@click.option("-e", "--encrypt")
@click.option("-n", "--name")
@click.option("-b", "--bucket-name")
@click.argument("source_path", type=click.Path(exists=True))
def main(name, encrypt, bucket_name, source_path):
    click.echo("Archiving " + click.format_filename(source_path))

    tgz_archive_path = archive_and_compress(name, source_path)
    click.echo("File archived to " + tgz_archive_path)

    archive_path = tgz_archive_path

    gpg_archive_path = ""
    if encrypt is not None:
        gpg_archive_path = encrypt_file(tgz_archive_path, encrypt)
        click.echo("Encrypted file saved to " + gpg_archive_path)

        archive_path = gpg_archive_path

    click.echo("Instantiating S3 connection")
    s3 = instantiate_s3()

    click.echo("Uploading archive to S3")
    upload_to_s3(s3, bucket_name, archive_path)

    click.echo("Archive uploaded successfully")
    click.echo("Cleaning up")

    os.remove(tgz_archive_path)
    if encrypt is not None:
        os.remove(gpg_archive_path)

    click.echo("Thank you for using cybarchive!")


if __name__ == "__main__":
    main()
