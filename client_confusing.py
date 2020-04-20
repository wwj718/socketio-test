import asyncio
import time
import random
import socketio
from loguru import logger

loop = asyncio.get_event_loop()

clients = []

async def start_server():
    '''
    ipython for test
    '''
    
    # ulimit -n 4096 , 247
    for i in range(1000):
        client = socketio.AsyncClient()
        await asyncio.sleep(1/500)
        await client.connect('http://localhost:8080')
        clients.append(client)
        if i % 20 < 10:
            await asyncio.sleep(0.1)
            await client.disconnect()
            clients.remove(client)

    logger.debug(f"clients count {len(clients)}")
    # await asyncio.sleep(3)


if __name__ == '__main__':
    # task
    loop.create_task(start_server())
    time.sleep(1)
    # loop.create_task(leave())
    loop.run_forever()
