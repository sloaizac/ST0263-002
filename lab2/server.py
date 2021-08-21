#!/usr/bin/env python
"""
August 1, 2021
Created by: Sebastian Loaiza Correa
"""

import os
import constants
import shutil
import sys
from _thread import *
from http.server import BaseHTTPRequestHandler, HTTPServer


class HandlerConection(BaseHTTPRequestHandler):
	def _set_response(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		print("GET request,\nPath: {} \nHeaders: {} \n".format(self.path, self.headers))
		options = str(self.path).split
		checkStatus(options)
		self._set_response()
		self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

	def do_POST(self):
		content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
		post_data = self.rfile.read(content_length) # <--- Gets the data itself
		print("POST request,\nPath: {}\nHeaders:{}\nBody:\n%s\n",
		str(self.path), str(self.headers), post_data.decode('utf-8'))

		self._set_response()
		self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

	def checkStatus(options):
		if options[1] == constants.NEW_BUCKET:
			createBucket(options[2])
		elif options[1] == constants.UPLOAD_FILE:
			createFile(options[2], options[3])
		elif options[1] == constants.LIST_FILE:
			getFileList(options[2])
		elif options[1] == constants.DELETE_FILE:
			deleteFile(options[2], options[3])
		elif options[1] == constants.DOWNLOAD_FILE:
			downloadFile(options[2], options[3])
		elif options[1] == constants.DELETE_BUCKET:
			deleteBucket(options[2])
		elif options[1] == constants.LIST_BUCKET or options[1] == constants.HELLO:
			getBucketList()

	def downloadFile(filename, bucketName):
		f = open(os.path.join(test_db, bucketName, filename), "rb")
		while True:
			bytes_read = f.read(constants.BUFFER_SIZE)

			if not bytes_read:
				break
			print('send')
			client.sendall(bytes_read)
		client.send('EOF'.encode('ascii'))
		while True:
			response = client.recv(constants.BUFFER_SIZE)
			if response.decode('ascii') == 'OK':
				break

	def deleteFile(filename, bucketName):
		os.remove(os.path.join(test_db, bucketName, filename))
		client.send('file deleted successfully'.encode('ascii'))

	def deleteBucket(bucketName):
		shutil.rmtree(os.path.join(test_db, bucketName))
		client.send('bucket deleted successfully'.encode('ascii'))

	def createFile(filename, bucketName):
		if os.path.exists(os.path.join(test_db, bucketName, filename)):
			client.send('EXIST'.encode('ascii'))
		else:
			client.send('ACK'.encode('ascii'))
			f = open(os.path.join(test_db, bucketName, filename), "wb")
			while True:
				bytes_read = client.recv(constants.BUFFER_SIZE)
				if bytes_read.decode('ascii')[-3:] == "EOF":
					f.write(bytes_read.decode('ascii')[:-3].encode('ascii'))
					print('terminado')
					break
				print('received bites')
				f.write(bytes_read)
			f.close()
			print('received-completed')
			client.send('OK'.encode('ascii'))

	def getFileList(bucketName):
		fileList = os.listdir(os.path.join(test_db, bucketName))
		if len(fileList) > 0:
			strList = '\n'.join([str(e) for e in fileList])
		else:
			strList = "Empty bucket."
		client.send(strList.encode('ascii'))

	def getBucketList():
		fileList = os.listdir(test_db)
		if len(fileList) > 0:
			strList = '\n'.join([str(e) for e in fileList])
		else:
			strList = "Zero buckets avaiables."
		client.send(strList.encode('ascii'))

	def createBucket(bucketName):
		newBucket = os.path.join(test_db, bucketName)
		if not os.path.exists(newBucket):
			os.makedirs(newBucket)
			client.send('New bucket created'.encode('ascii'))
		else:
			client.send('Bucket name already exist'.encode('ascii'))

try:
	server = HTTPServer(('localhost', constants.PORT), HandlerConection)
	print("Starting server, use <Ctrl-C> to stop")
	server.serve_forever()
	try:
		test_db = sys.argv[1]
	except:
		test_db = input("Enter buckets path >> ")

	if not os.path.exists(test_db):
		os.makedirs(test_db)
	print("SERVER UP!\nlistening...")
except Exception as error:
	print("Server error")
	print(error)
