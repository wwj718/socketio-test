import asyncio
import time
import socketio
import random
from loguru import logger

loop = asyncio.get_event_loop()


async def start_server():
    '''
    ipython for test
    '''
    clients = []
    # ulimit -n 4096 , 247
    for i in range(500):
        client = socketio.AsyncClient()
        await asyncio.sleep(1/500)
        await client.connect('http://localhost:8080')
        clients.append(client)

    logger.debug(f"clients count {len(clients)}")
    logger.debug("sleep 1")
    await asyncio.sleep(1)

    for i in range(50):
        client = random.choice(clients)
        await client.disconnect()
        clients.remove(client)
        logger.debug(f"clients count {len(clients)}")
        
        for i in range(2):
            client_new = socketio.AsyncClient()
            await client_new.connect('http://localhost:8080')
            await asyncio.sleep(1/500)
            clients.append(client_new)
            logger.debug(f"clients count {len(clients)}")

    await asyncio.sleep(1)



if __name__ == '__main__':
    loop.run_until_complete(start_server())
