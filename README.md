# raspberry-pi-web-server-comparison

- A comparison of different web frameworks, ran on a Raspeberry Pi 2.
- Each server returns a simple 'hello world' string.

## BaseHTTPServer (Python)
- Python 2.7.3
```
$ siege -b -t60s http://raspberrypi:8000
** SIEGE 3.0.5
** Preparing 15 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:		       35731 hits
Availability:		      100.00 %
Elapsed time:		       59.05 secs
Data transferred:	        0.41 MB
Response time:		        0.02 secs
Transaction rate:	      605.10 trans/sec
Throughput:		        0.01 MB/sec
Concurrency:		       14.84
Successful transactions:       35731
Failed transactions:	           0
Longest transaction:	        3.03
Shortest transaction:	        0.00
```

## Flask (Python)
- Python 2.7.3
- Flask 0.10.1
```
$ siege -b -t60s http://raspberrypi:5000
** SIEGE 3.0.5
** Preparing 15 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:		       15052 hits
Availability:		      100.00 %
Elapsed time:		       59.59 secs
Data transferred:	        0.17 MB
Response time:		        0.06 secs
Transaction rate:	      252.59 trans/sec
Throughput:		        0.00 MB/sec
Concurrency:		       14.97
Successful transactions:       15052
Failed transactions:	           0
Longest transaction:	        0.09
Shortest transaction:	        0.02
```

## Node.js
- Node.js 0.10.38
```
$ siege -b -t60s http://raspberrypi:1337
** SIEGE 3.0.5
** Preparing 15 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:		       42866 hits
Availability:		      100.00 %
Elapsed time:		       59.26 secs
Data transferred:	        0.49 MB
Response time:		        0.02 secs
Transaction rate:	      723.35 trans/sec
Throughput:		        0.01 MB/sec
Concurrency:		       14.95
Successful transactions:       42866
Failed transactions:	           0
Longest transaction:	        0.12
Shortest transaction:	        0.01
```

## Golang
- Go 1.4.2
```
$ siege -b -t60s http://raspberrypi:8000
** SIEGE 3.0.5
** Preparing 15 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:		       63690 hits
Availability:		      100.00 %
Elapsed time:		       59.06 secs
Data transferred:	        0.73 MB
Response time:		        0.01 secs
Transaction rate:	     1078.39 trans/sec
Throughput:		        0.01 MB/sec
Concurrency:		       14.24
Successful transactions:       63690
Failed transactions:	           0
Longest transaction:	       10.02
Shortest transaction:	        0.00

```
