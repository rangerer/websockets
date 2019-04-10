# Websockets

Simple Python websocket implementation using `websockets`.

see [WebSockets Library](http://websockets.readthedocs.io/en/stable/index.html)

## Usage

    pipenv install

Start the echo server with

    pipenv run python server.py

Start the client with

    pipenv run python client.py

Start an OCPP session with

    pipenv run python client.py ws://<host>:<post>/<path>
    
    > [0,1,"Heartbeat",[]]
    < ...
    > C-d

## Secure Websockets

Generate self-signed server certificate

    openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout server.key -out server.crt

Start secure websocket server with

    pipenv run python server.py --certfile=server.crt --keyfile=server.key

Start secure websocket client with

    pipenv run python client.py wss://localhost:8765 --cafile=server.crt
