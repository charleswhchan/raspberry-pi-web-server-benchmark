var http = require('http');

# Disable request logging in console output
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

http.createServer(function (req, res) {
  // res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World\n');
}).listen(1337, '0.0.0.0');

console.log('Server running at http://0.0.0.0:1337/');
