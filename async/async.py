import asyncio

async def task_1():
    print("Task 1: Start")
    await asyncio.sleep(3)  # Simulates a long-running task
    print("Task 1: Done")

async def task_2():
    print("Task 2: Start")
    await asyncio.sleep(1)  # Simulates a shorter task
    print("Task 2: Done")

async def main():
    # Start both tasks concurrently
    task1 = asyncio.create_task(task_1())
    task2 = asyncio.create_task(task_2())

    # Wait for both tasks to finish
    await task1
    await task2

asyncio.run(main())
