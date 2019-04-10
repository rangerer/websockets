#!/usr/bin/env python

from os.path import abspath
import argparse
import asyncio
import ssl

import websockets


async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)


if __name__ == "__main__":
    # parse command line arguments
    parser = argparse.ArgumentParser(description="Websocket Server")
    parser.add_argument("--certfile", nargs="?", help="SSL server certificate file")
    parser.add_argument("--keyfile", nargs="?", help="SSL private key file")
    args = parser.parse_args()

    server_options = {}

    # configure SSL context for secure websocket connections
    if args.certfile:
        sslcontext = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        cert_chain_options = {}
        if args.keyfile:
            cert_chain_options["keyfile"] = abspath(args.keyfile)
        sslcontext.load_cert_chain(abspath(args.certfile), **cert_chain_options)
        server_options["ssl"] = sslcontext

    asyncio.get_event_loop().run_until_complete(
        websockets.serve(echo, 'localhost', 8765, **server_options))
    asyncio.get_event_loop().run_forever()
