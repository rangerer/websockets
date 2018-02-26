# Websockets

Simple Python websocket implementation using `websockets`.

see [WebSockets Library](http://websockets.readthedocs.io/en/stable/index.html)

## Usage

    mkvirtualenv -p /usr/bin/python3 -r requirements.txt websockets

Start the echo server with

    ./server.py

Start the client with

    ./client.py

Start an OCPP session with

    ./client.py <host> <port>
    
    > [0,1,"Heartbeat",[]]
    < ...
    > C-d
