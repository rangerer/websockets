#!/usr/bin/env python

import asyncio
import websockets

async def client(uri):
    async with websockets.connect(uri) as websocket:
        print("Quit by pressing Ctrl+D")
        while True:
            try:
                message = input("> ")
            except EOFError:
                break
            await websocket.send(message)
            response = await websocket.recv()
            print("< {}".format(response))

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(
        client('ws://localhost:8765'))
