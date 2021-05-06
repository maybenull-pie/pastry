import config
import boto3
import json
import base64
from pastry.core.event import Event

class Queue:
    def __init__(self, name: str):
        self.sqs_queue = boto3.resource('sqs').get_queue_by_name(QueueName=name)

    def send(self, event: Event, attributes: dict=None):
        # base64 string of body
        body_json = json.dumps(event.body)
        body_bytes = body_json.encode('ascii')
        base64_bytes = base64.b64encode(body_bytes)
        base64_body = base64_bytes.decode('ascii')
        
        # message attributes
        # default is minimum needed for nservicebus to route to handler
        attributes = attributes if attributes is not None else {
            "MessageTypeFullName": {
                "DataType": "String",
                "StringValue": event.message_type
            }
        }

        # send message
        response = self.sqs_queue.send_message(
            MessageBody=base64_body, 
            MessageAttributes=attributes
        )
        print(response.get('MessageId'))
        
class Queues:
    DECISION: str = f'nservicebus-{config.PIE_ENVIRONMENT}-Pie-Decision-Worker'
    DOCUMENT: str = f'nservicebus-{config.PIE_ENVIRONMENT}-Pie-Document-Worker'
    MARKETING: str = f'nservicebus-{config.PIE_ENVIRONMENT}-Pie-Policy-Worker'
    SUBMISSION: str = f'nservicebus-{config.PIE_ENVIRONMENT}-Pie-Submission-Worker'
    POLICY: str = f'nservicebus-{config.PIE_ENVIRONMENT}-Pie-Policy-Worker'
