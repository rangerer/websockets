#!/usr/bin/env python

from os.path import abspath
import argparse
import asyncio
import ssl

import websockets


def print_headers(title, headers):
    print("--- {} begin ---".format(title))
    for header in headers:
        print("{}: {}".format(*header))
    print("--- {} end ---".format(title))


async def client(uri, verbosity=0, sslcontext=False):
    websocket_options = {
        # add support for OCPP
        'subprotocols': ('ocpp1.6', 'ocpp1.5')
    }
    if sslcontext:
        websocket_options["ssl"] = sslcontext
    async with websockets.connect(uri, **websocket_options) as websocket:
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
    parser.add_argument("--cafile", nargs="?", help="SSL CA file")
    parser.add_argument("--certfile", nargs="?", help="SSL client certificate file")
    parser.add_argument("--keyfile", nargs="?", help="SSL private key file")
    parser.add_argument("--ignorecert", default=False, action="store_true", help="SSL ignore server cert failures")
    args = parser.parse_args()

    client_options = {}

    # configure SSL context for secure websocket connections
    if args.uri.startswith('wss'):
        sslcontext = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        if args.cafile:
            sslcontext.load_verify_locations(cafile=abspath(args.cafile))
        if args.certfile:
            cert_chain_options = {}
            if args.keyfile:
                cert_chain_options["keyfile"] = abspath(args.keyfile)
            sslcontext.load_cert_chain(abspath(args.certfile), **cert_chain_options)
        if args.ignorecert:
            sslcontext.check_hostname = False
            sslcontext.verify_mode = ssl.CERT_NONE

        client_options["sslcontext"] = sslcontext

    asyncio.get_event_loop().run_until_complete(
        client(args.uri, args.verbose, **client_options))
