import aiohttp
import asyncio
import json

com_lst = []
URL = 'http://api.pushshift.io/reddit/comment/search/'


async def get_comment(topic):
    async with aiohttp.ClientSession() as session:
        params = {'subreddit': topic, 'size': 25, 'sort': 'new'}
        async with session.get(URL, params=params) as resp:
            res = await resp.json()
            comment_lst = []

            for comment in res['data']:
                comment_lst.append(comment['body'])

            key_lst = list(range(1, 26))
            my_dict = dict(zip(key_lst, comment_lst))
            com_lst.append(my_dict)


async def main():
    task1 = asyncio.create_task(get_comment('cyberpunk'))
    task2 = asyncio.create_task(get_comment('ps5'))
    task3 = asyncio.create_task(get_comment('xbox'))

    await asyncio.gather(task1, task2, task3)


if __name__ == '__main__':
    asyncio.run(main())
    with open('comments_async.json', 'w') as file:
        json.dump(com_lst, file, indent=4)
