import io
import os
import zipfile
from pathlib import Path
import boto3


def unzip_object_in_s3(bucket, zip_key_name, file_key_name):
    """Download, unzip, and upload a file from a zip archive in an S3 bucket.

    Performs the unzipping in memory.

    Args:
        bucket: A boto3 Resource object for an S3 bucket
        zip_key_name: The key to the zip file in the bucket
        file_key_name: The name of the file in the zip archive to extract
    Returns:
        dst_key_name: The key to the extracted file in the bucket
    """
    dst_key_name = Path(zip_key_name).parent / Path(zip_key_name).stem / file_key_name
    with io.BytesIO() as compressed:
        s3_bucket.download_fileobj(Key=zip_key_name, Fileobj=compressed)
        with zipfile.ZipFile(compressed) as zip_handle:
            with zip_handle.open(file_key_name) as decompressed:
                s3_bucket.upload_fileobj(
                    Fileobj=decompressed, Key=str(dst_key_name)
                )

    return str(dst_key_name)


assert os.environ["AWS_PROFILE"]
# aws s3 cp pizzas.zip s3://madpy/warmup/2019-10-10/pizzas.zip
s3_bucket = boto3.resource("s3").Bucket("madpy")
zip_key_name = "warmup/2019-10-10/pizzas.zip"
file_key_name = "roman-candle.csv"
dst_key_name = unzip_object_in_s3(s3_bucket, zip_key_name, file_key_name)


with io.BytesIO() as test:
    s3_bucket.download_fileobj(Key=dst_key_name, Fileobj=test)
    test.seek(0)
    print(test.read().decode("utf-8"))