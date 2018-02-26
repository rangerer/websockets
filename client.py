#!/usr/bin/env python

import argparse
import asyncio
import websockets

async def client(uri):
    # add support for OCPP
    available_subprotocols = ('ocpp1.6', 'ocpp1.5')
    async with websockets.connect(uri, subprotocols=available_subprotocols) as websocket:
        print("Quit by pressing Ctrl+d")
        while True:
            try:
                message = input("> ")
            except EOFError:
                break
            await websocket.send(message)
            response = await websocket.recv()
            print("< {}".format(response))

if __name__ == "__main__":
    # parse command line arguments
    parser = argparse.ArgumentParser(description="Websocket Client")
    parser.add_argument("host", default="localhost", nargs="?", help="websocket server host")
    parser.add_argument("port", default="8765", nargs="?", help="websocket server port")
    args = parser.parse_args()

    asyncio.get_event_loop().run_until_complete(
        client('ws://{}:{}'.format(args.host, args.port)))
