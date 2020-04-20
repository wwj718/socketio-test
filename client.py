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
    for i in range(200):
        client = socketio.AsyncClient()
        clients.append(client)
        await asyncio.sleep(1/50)
        await clients[i].connect('http://localhost:8080')

    logger.debug(f"clients count {len(clients)}")
    await asyncio.sleep(5)

    for client in clients:
        await client.disconnect()
        await asyncio.sleep(1/50)
    
    await asyncio.sleep(1)



if __name__ == '__main__':
    loop.run_until_complete(start_server())