import json
import boto3
from moto import mock_s3, mock_dynamodb
import pytest

from src.handlers import upload_processor
from src.lib import dynamo

BUCKET = "test-bucket"

@mock_s3
@mock_dynamodb
def test_upload_processor_stores_metadata():
    # Arrange
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket=BUCKET)
    body = b"hello world"
    s3.put_object(Bucket=BUCKET, Key="hello.txt", Body=body, ContentType="text/plain")

    # DynamoDB
    ddb = boto3.client("dynamodb", region_name="us-east-1")
    ddb.create_table(
        TableName="ImageMetadata",
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST",
    )

    event = {
        "Records": [
            {
                "s3": {
                    "bucket": {"name": BUCKET},
                    "object": {"key": "hello.txt"},
                }
            }
        ]
    }

    # Act
    resp = upload_processor.handler(event, None)
    assert resp["statusCode"] == 200

    # Assert DynamoDB item exists
    table = boto3.resource("dynamodb", region_name="us-east-1").Table("ImageMetadata")
    item = table.get_item(Key={"id": "hello.txt"}).get("Item")
    assert item is not None
    assert item["size"] == len(body)
    assert item["content_type"] == "text/plain"
