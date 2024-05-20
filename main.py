from datetime import datetime, timedelta
from auth import get_twitter_connection_v1, get_twitter_connection_v2
from utils import create_and_post_tweet

# Authenticate to Twitter
client_v1 = get_twitter_connection_v1()
client_v2 = get_twitter_connection_v2()

# Specific times to post in EST
post_times = [(4,0)]

def job():
    now_utc = datetime.utcnow()
    now_est = now_utc - timedelta(hours=4)
    print(f"Job run at {now_est}")
    
    for post_time_hour, post_time_minute in post_times:
        if now_est.hour == post_time_hour and (now_est.minute - post_time_minute) == 1:
            create_and_post_tweet(client_v1, client_v2)
            return


if __name__ == "__main__":
    job()
