import asyncio
import aiohttp
import time

url = "https://jsonplaceholder.typicode.com/posts/"


def get_tasks(session):
    post_ids = list(range(1, 51))
    tasks = []
    for i in post_ids:
        formatted_url = f"{url}/{i}"
        tasks.append(asyncio.create_task(session.get(formatted_url, ssl=False)))
    return tasks


async def fetch_all_post_data():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)

        for response in responses:
            print(await response.json())

    total_time = time.time() - start
    print(f"\n\nTotal time taken to make {len(responses)} API calls: {total_time} secs")


# Event loop concept
# =================
# loop = asyncio.get_event_loop()
# loop.run_until_complete(fetch_all_post_data())
# loop.close()

asyncio.run(
    fetch_all_post_data()
)  # This is run function is doing the above 3 line of code.
