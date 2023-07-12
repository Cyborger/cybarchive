# Cybarchive

Cybarchive is a CLI application to easily archive whole folders to a tar.gz format and upload it to a given S3 bucket.

While I made this tool to help achieve a 3-2-1/3-2-2 backup strategy, it is not foolproof and I cannot be held responsible for data loss. This tool is provided without any kind of warranty whatsoever.

## Features

- GnuPG file encryption support
- S3 buckets support
- Configurable
- Designed for cron jobs

### Future plans

- Webhook support
- GnuPG signature support
- Setup tools
- Config file to replace environment variables

Docker?? 🥺👉👈

## Usage

Beware that the app is still in development and that the following instructions may be rapidly outdated.

### S3 configuration

The tool must be able to find your S3 bucket for it to work properly. As such, you have to set the following environment variables :

- `AWS_ACCESS_KEY_ID`: Your S3 access key
- `AWS_SECRET_ACCESS_KEY`: Your S3 secret key
- `AWS_ENDPOINT_URL`: The S3 endpoint (most useful when using non-AWS providers but still a requirement anyway)

### The tool

The setup tool doesn't work yet. After installing the requirements, you can do the following:

```
$ python main.py -b bucket_name -e MY_GPG_FINGERPRINT /home/me/very_important_folder_to_backup
```

This will generate a tar.gz archive and encrypt it using the GPG fingerprint if provided, then it will upload it to the given bucket.

The file format is the following `cybarchive(-{name})-{current_iso8601_utc_time}.tar.gz(.gpg)`

## I am not happy with this tool!!!! 😡😡

too bad then
