import requests
import time

url = "https://jsonplaceholder.typicode.com/posts/"


def fetch_all_post_data():
    post_ids = list(range(1, 51))
    start = time.time()

    for i in post_ids:
        formatted_url = f"{url}/{i}"
        response = requests.get(formatted_url)
        print(response.json())

    total_time = time.time() - start
    print(f"\n\nTotal time taken to make {len(post_ids)} API calls: {total_time} secs")


fetch_all_post_data()
