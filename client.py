import asyncio
import time
import socketio
from loguru import logger

loop = asyncio.get_event_loop()


async def start_server():
    '''
    ipython for test
    '''
    clients = []
    # ulimit -n 4096 , 247
    for i in range(1000):
        client = socketio.AsyncClient()
        await asyncio.sleep(1/500)
        await client.connect('http://localhost:8080')
        clients.append(client)

    logger.debug(f"clients count {len(clients)}")
    await asyncio.sleep(3)

    for client in clients:
        await client.disconnect()
        await asyncio.sleep(1/500)
    
    await asyncio.sleep(1)



if __name__ == '__main__':
    loop.run_until_complete(start_server())