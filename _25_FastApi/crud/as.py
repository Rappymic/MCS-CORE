import asyncio
import sys
import os

async def some_work(num):
    print(f"computing script: {num}")
    await asyncio.sleep(3)
    print(f"square of {num} is {num**2}")
async def some_work1(num):
    print(f"computing script: {num}")
    await asyncio.sleep(3)
    print(f"cube of {num} is {num**3}")

async def main():
    task1 = asyncio.create_task(coro=some_work(33))
    task2 = asyncio.create_task(coro=some_work1(33))

    await task1
    await task2
    #create task


asyncio.run(main())