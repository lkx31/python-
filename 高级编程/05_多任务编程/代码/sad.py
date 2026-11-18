import asyncio

async def hello(name):                # 1. async 定义协程函数
    print(f"开始: {name}")
    await asyncio.sleep(1)            # 2. await 让出控制权
    print(f"结束: {name}")

async def main():
    await hello("Alice")              # 3. 单个协程调用
    # 4. 并发执行
    task1 = asyncio.create_task(hello("Bob"))
    task2 = asyncio.create_task(hello("Charlie"))
    await task1
    await task2

asyncio.run(main())