import os.path
import tarfile
import tempfile
import datetime
import gnupg


def archive_and_compress(name, source_path):
    current_time = datetime.datetime.now().isoformat()
    filename = f"cybarchive{'-' + name if name is not None else ''}-{current_time}.tar.gz"
    save_path = os.path.join(tempfile.gettempdir(), filename)

    with tarfile.open(save_path, "w:gz") as tar:
        tar.add(source_path, arcname=os.path.basename(source_path))

    return save_path


def encrypt_file(source_path, key_fingerprint):
    gpg = gnupg.GPG()
    save_path = source_path + ".gpg"

    encrypted_data = gpg.encrypt_file(open(source_path, "rb"), key_fingerprint, output=save_path)

    if not encrypted_data.ok:
        raise Exception(encrypted_data.status)

    return save_path
