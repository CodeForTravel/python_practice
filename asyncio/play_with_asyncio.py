import time
import asyncio


###### This is a traditional function which will wait for two sec
# def say_hello():
#     time.sleep(2)
#     print("Hello, Async World? (not yet)")
# say_hello()


###### This is a async Function which will wait for two sec as well
# async def say_hello_async():
#     await asyncio.sleep(2)
#     print("Hello, Async World!")
# asyncio.run(say_hello_async())


async def say_hello_async():
    await asyncio.sleep(2)  # Simulates waiting for 2 seconds
    print("I run first ")


async def do_something_else():
    print("Starting another task...")
    await asyncio.sleep(1)  # Simulates doing something else for 1 second
    print("Finished another task!")


async def main():
    # Schedule both tasks to run concurrently
    await asyncio.gather(
        say_hello_async(),
        do_something_else(),
    )


asyncio.run(main())
