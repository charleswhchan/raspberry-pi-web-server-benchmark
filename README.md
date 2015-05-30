# raspberry-pi-web-server-comparison

- A comparison of different web frameworks, ran on a Raspeberry Pi 2.
- Each server returns a simple 'hello world' page.

## Flask (Python)
```
$ siege -b -t60s http://raspberrypi:5000
** SIEGE 3.0.5
** Preparing 15 concurrent users for battle.
The server is now under siege...
Lifting the server siege...      done.

Transactions:		       12477 hits
Availability:		      100.00 %
Elapsed time:		       59.43 secs
Data transferred:	        0.14 MB
Response time:		        0.07 secs
Transaction rate:	      209.94 trans/sec
Throughput:		        0.00 MB/sec
Concurrency:		       14.97
Successful transactions:       12477
Failed transactions:	           0
Longest transaction:	        0.12
Shortest transaction:	        0.03
```
Remarks
- Python 2.7.3
- Flask 0.10.1
