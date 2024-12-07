import asyncio
import aiofiles


# Synchronously reading multiple files
def read_file_sync(filepath):
    with open(filepath, "r") as file:
        return file.read()


def read_all_sync(filepaths):
    return [read_file_sync(filepath) for filepath in filepaths]


filepaths = ["asyncio/file1.txt", "asyncio/file2.txt"]
data = read_all_sync(filepaths)
print(data)


# Asynchronously reading a single file
async def read_file_async(filepath):
    async with aiofiles.open(filepath, "r") as file:
        return await file.read()


async def read_all_async(filepaths):
    tasks = [read_file_async(filepath) for filepath in filepaths]
    return await asyncio.gather(*tasks)


# Running the async function
async def main():
    filepaths = ["asyncio/file1.txt", "asyncio/file2.txt"]
    data = await read_all_async(filepaths)
    print(data)


asyncio.run(main())
