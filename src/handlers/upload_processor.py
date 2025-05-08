import os
import json
import logging
import boto3
from botocore.exceptions import ClientError
from src.lib.dynamo import put_metadata

log = logging.getLogger()
log.setLevel(logging.INFO)

s3 = boto3.client("s3")

def handler(event, context):
    log.info("Received event: %s", json.dumps(event))
    for record in event.get("Records", []):
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]

        try:
            head = s3.head_object(Bucket=bucket, Key=key)
            size = head["ContentLength"]
            content_type = head.get("ContentType", "unknown")

            metadata = {
                "id": key,
                "bucket": bucket,
                "size": size,
                "content_type": content_type,
            }
            put_metadata(metadata)
            log.info("Stored metadata for %s", key)
        except ClientError as exc:
            log.error("Error processing %s: %s", key, exc)
            raise

    return {"statusCode": 200, "body": json.dumps({"message": "OK"})}
