import asyncio


async def fib():
    lst_fib = []
    a, b = 0, 1

    for i in range(1, 11):
        a, b = b, a + b
        await asyncio.sleep(0.1)
        lst_fib.append(a)
        
    return lst_fib


async def factorial():
    fac, i = 1, 0
    lst_fac = []

    for m in range(1, 11):
        while i < m:
            i += 1
            fac = fac * i
            await asyncio.sleep(0.1)
            lst_fac.append(fac)

    return lst_fac


async def expo(x):
    lst_expo = []

    for p in range(1, 11):
        m = x
        t = 1
        while p:
            if p % 2:
                t *= m
            m *= m
            p //= 2
        await asyncio.sleep(0.1)
        lst_expo.append(t)

    return lst_expo


async def main():
    task1 = asyncio.create_task(fib())
    task2 = asyncio.create_task(factorial())
    task3 = asyncio.create_task(expo(2))
    task4 = asyncio.create_task(expo(3))

    res = await asyncio.gather(task1, task2, task3, task4)
    print(res)


if __name__ == '__main__':
    asyncio.run(main())
