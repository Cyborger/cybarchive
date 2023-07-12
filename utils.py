import os.path
import tarfile
import tempfile
import datetime
import gnupg
import boto3
from dotenv import load_dotenv

load_dotenv()


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


def instantiate_s3():
    return boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        endpoint_url=os.getenv("AWS_ENDPOINT_URL")
    )


def list_buckets(s3):
    print(s3.list_buckets())


def upload_to_s3(s3, bucket_name, archive_path):
    archive = open(archive_path, "rb")
    s3.upload_fileobj(archive, bucket_name, os.path.basename(archive_path))
