import os.path
import tarfile


def archive_and_compress(output_filename, source_path):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_path, arcname=os.path.basename(source_path))
