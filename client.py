#!/usr/bin/env python

import argparse
import asyncio
import websockets

def print_headers(title, headers):
    print("--- {} begin ---".format(title))
    for header in headers:
        print("{}: {}".format(*header))
    print("--- {} end ---".format(title))

async def client(uri, verbosity=0):
    # add support for OCPP
    available_subprotocols = ('ocpp1.6', 'ocpp1.5')
    async with websockets.connect(uri, subprotocols=available_subprotocols) as websocket:
        print("Quit by pressing Ctrl+d")
        if verbosity > 0:
            print_headers("request headers", websocket.raw_request_headers)
            print_headers("response headers", websocket.raw_response_headers)
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
    parser.add_argument("uri", default="ws://localhost:8765", nargs="?", help="websocket server uri")
    parser.add_argument("--verbose", "-v", action='count', default=0, help="increase verbosity")
    args = parser.parse_args()

    asyncio.get_event_loop().run_until_complete(
        client(args.uri, args.verbose))
