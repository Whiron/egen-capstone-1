import os
import json
import pandas as pd
from google.cloud import pubsub_v1

project_id = "egen-project-1-327215"
topic_id = "stock_market"
subscription_id="subscription_2"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/sarthak/egen-project-1-327215-261475be0596.json"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)
response = subscriber.pull(
    request={
        "subscription": subscription_path,
        "max_messages": 1,
    }
)

for msg in response.received_messages:
    # print("Received message:", msg.message.data)
    date=msg.message.data[-10:].decode('utf-8')
    message=msg.message.data[:-10]
    df = pd.DataFrame(json.loads(message))
    print(df)

ack_ids = [msg.ack_id for msg in response.received_messages]
subscriber.acknowledge(
    request={
        "subscription": subscription_path,
        "ack_ids": ack_ids,
    }
)
