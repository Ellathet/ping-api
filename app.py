import asyncio
import websockets
from ping3 import ping, verbose_ping


async def server(websocket):
    async for message in websocket:

        await websocket.send(f'{ping(message)}')

async def main():
    async with websockets.serve(server, "localhost", 8000):
        await asyncio.Future()  # run forever

asyncio.run(main())