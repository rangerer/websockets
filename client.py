#!/usr/bin/env python

import asyncio
import websockets

async def client(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(
        client('ws://localhost:8765'))
