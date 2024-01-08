import asyncio
import aiohttp
import time

url = "https://jsonplaceholder.typicode.com/posts/"


async def fetch_all_post_data():
    post_ids = list(range(1, 50))
    start = time.time()
    async with aiohttp.ClientSession() as session:
        for i in post_ids:
            formatted_url = f"{url}/{i}"
            response = await session.get(formatted_url, ssl=False)
            print(await response.json())

    total_time = time.time() - start
    print(f"\n\nTotal time taken to make {len(post_ids)} API calls: {total_time} secs")


# Event loop concept
# =================
# loop = asyncio.get_event_loop()
# loop.run_until_complete(fetch_all_post_data())
# loop.close()

asyncio.run(
    fetch_all_post_data()
)  # This is run function is doing the above 3 line of code.
