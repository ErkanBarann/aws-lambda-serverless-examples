import json
import logging
from src.lib.dynamo import get_metadata

log = logging.getLogger()
log.setLevel(logging.INFO)

def handler(event, context):
    key = event["pathParameters"]["key"]
    log.info("Fetching metadata for %s", key)
    item = get_metadata(key)

    if not item:
        return {"statusCode": 404, "body": json.dumps({"error": "Not found"})}

    return {"statusCode": 200, "body": json.dumps(item)}
