import json, boto3
from datetime import datetime

firehose = boto3.client('firehose')
STREAM_NAME = "FoodOrdersFirehose"

def lambda_handler(event, context):
    for record in event['Records']:
        if record['eventName'] != 'INSERT':
            continue
        
        data = record['dynamodb']['NewImage']
        
        output = {
            "order_id": data['order_id']['S'],
            "stage": data['stage']['S'],
            "customer": data['customer']['S'],
            "restaurant": data['restaurant']['S'],
            "time": datetime.utcnow().strftime("%H:%M:%S")
        }

        firehose.put_record(
            DeliveryStreamName=STREAM_NAME,
            Record={'Data': json.dumps(output) + "\n"}
        )

    return {"statusCode": 200}
