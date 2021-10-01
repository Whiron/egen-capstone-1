import pandas as pd
import requests
import json
import datetime
import os
import random

from google.cloud import pubsub_v1

def random_date():
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date.today()

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days

    random_number_of_days = random.randrange(days_between_dates)

    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return str(random_date)

class Publisher:
    def __init__(self):
        self.project_id = "egen-project-1-327215"
        self.topic_id = "stock_market"
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "egen-project-1-327215-1294007c4e28.json"

    def fetch_data(self):
        date=random_date()
        url="https://api.polygon.io/v3/reference/tickers?date="+date+"&apiKey=Kpmdf46Y_Qpdodwv5sj9Df92Dl9UiP2z"
        response = requests.get(url)
        df = pd.DataFrame(response.json()['results'])
        # print(df)

        string_msg = json.dumps(response.json()['results'])+date
        string_msg = string_msg.encode("utf-8")
        # print(string_msg)

        return string_msg

    def publish(self):
        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(self.project_id, self.topic_id)

        data=self.fetch_data()

        future = publisher.publish(topic_path,data)
        print(future.result())


if __name__ == "__main__":
    pub = Publisher()
    pub.publish()


