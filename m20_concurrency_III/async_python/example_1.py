import asyncio


async def helper_a():
    a = 0
    for x in range(100_000_000):
        a += x


async def helper_b():
    print("bbbb")


async def func_a():
    print("Jestem A")
    print("Teraz idę spać")
    await asyncio.sleep(1)
    print("Mogę działać dowolnie długo - aż dobrowolnie oddam sterowanie")
    a = 0
    for x in range(100_000_000):
        a += x

    print("Mogę też wywołać inne korutyny")
    await helper_a()
    print("To A kończy na dziś")


async def func_b():
    print("Jestem B")
    print("Teraz idę spać")
    await asyncio.sleep(1)
    print("To B kończy na dziś")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    tasks = [
        loop.create_task(func_a()),
        loop.create_task(func_b()),
    ]

    loop.run_until_complete(asyncio.wait(tasks))
