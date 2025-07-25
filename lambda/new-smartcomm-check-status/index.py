import json

def lambda_handler(event, context):
    # Read query parameters from URL
    query_params = event.get("queryStringParameters") or {}

    id_param = query_params.get("id")
    status_param = query_params.get("status")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Received parameters",
            "id": id_param,
            "status": status_param
        })
    }
