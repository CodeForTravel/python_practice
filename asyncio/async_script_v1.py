import asyncio
import aiohttp
import time
import requests


url = "https://jsonplaceholder.typicode.com/posts/"


# ================= Synchronously calling/fetching web page =================
def synchronously_web_page_fetching(count):

    start = time.time()
    for i in range(1, count):
        formatted_url = f"{url}/{i}"
        response = requests.get(formatted_url)
        print(response.json())

    total_time = time.time() - start
    print(f"\n\nTotal time taken to make {count-1} API calls: {total_time} secs (Synchronously)")


# =================  Asynchronously calling/fetching web page  =================
async def fetch_all_post_data_synchronously(count):
    start = time.time()
    async with aiohttp.ClientSession() as session:
        for i in range(1, count):
            formatted_url = f"{url}/{i}"
            response = await session.get(formatted_url, ssl=False)
            print(await response.json())

    total_time = time.time() - start
    print(f"\n\nTotal time taken to make {count-1} API calls: {total_time} secs (Asynchronously)")


# Event loop concept
# =================
# loop = asyncio.get_event_loop()
# loop.run_until_complete(fetch_all_post_data())
# loop.close()

synchronously_web_page_fetching(51)
asyncio.run(fetch_all_post_data_synchronously(51))  # This is run function is doing the above 3 line of code.
