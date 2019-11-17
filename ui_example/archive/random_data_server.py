#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
import json
import random

PORT_NUMBER = 8000

# This class will handles any incoming request from
# the browser
                    #  -16.015715, 34.545973
                    #  -15.733854, 34.790082

class myHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        if self.path == "/":
            self.path = "/real_time_monitor.html"

        if self.path == "/data":
            print "DATA"
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # Send the html message
            # self.wfile.write({"geometry": {"type": "Point", "coordinates": [19.272678, -15.462675]}, "type": "Feature", "properties": {}})
            ret = {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',

                    'coordinates': [random.uniform(34.545973, 34.790082), random.uniform(-16.015715, -15.733854)],
                },
                'properties': {
                    'ipAddress': 'X.X.X.X',
                    'score': '1000'
                }
            }
            # self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}))
            self.wfile.write(json.dumps(ret))
            return
            #

        try:
            # Check the file extension required and
            # set the right mime type

            sendReply = False
            if self.path.endswith(".html"):
                mimetype = 'text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype = 'image/jpg'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype = 'image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype = 'application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype = 'text/css'
                sendReply = True

            if sendReply == True:
                # Open the static file requested and send it
                f = open(curdir + sep + self.path)
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ', PORT_NUMBER

    # Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
