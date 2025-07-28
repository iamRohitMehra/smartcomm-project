import json

def lambda_handler(event, context):
    print("EVENT:", json.dumps(event))  # Logs everything coming in

    # Read query parameters from URL
    query_params = event.get("queryStringParameters") or {}

    job_id = query_params.get("jobId")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Received parameters",
            "id": job_id,
            "status": "success" if job_id else "missing jobId"
        }),
        "headers": {
            "Content-Type": "application/json"
        }
    }
