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
    # Run tasks synchronously by awaiting each one
    await task_1()  # This will run synchronously
    await task_2()  # This will run after task_1 finishes

# Run the main function
asyncio.run(main())
