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

    pipenv run python client.py <host> <post>
    
    > [0,1,"Heartbeat",[]]
    < ...
    > C-d
