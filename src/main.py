
"""
Notify Budget 
Copyright Maven Wave, Jess Lampe 2019

See README.md for additional detail. 
"""

import base64
import sendgrid
import os
from sendgrid.helpers.mail import *
import json


sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))

def notify_budget(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.

    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    data = json.loads(pubsub_message)
    content = Content("text/plain", "Billing Alert Notification {}".format(data))
    from_email = Email(os.environ.get('FROM_EMAIL'))
    to_email = Email(os.environ.get('TO_EMAIL'))
    subject = "Billing Alert"
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)