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
    client = socketio.AsyncClient()
    await asyncio.sleep(1/500)
    await client.connect('http://localhost:8080', namespaces=['/chat'])
    await client.emit('my_custom_event', {'foo': 'bar'}, namespace='/chat')
    await asyncio.sleep(1)



if __name__ == '__main__':
    loop.run_until_complete(start_server())