import asyncio
import os

import aiofiles
import aiohttp


async def fetchImgs():
    urls = open('urls.txt')
    if not os.path.exists('img'):
        os.makedirs('img')
    async with aiohttp.ClientSession() as session:
        for url in urls:
            url = url.strip()
            async with session.get(url) as resp:
                fileName = url.split('/')[-1].split('?')[0]
                if '.' not in fileName:
                    continue
                async with aiofiles.open(f'img/{fileName}', 'wb') as f:
                    await f.write(await resp.read())

    urls.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(fetchImgs())
