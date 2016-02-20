import json
from subprocess import Popen, PIPE
from tempfile import mkdtemp
from werkzeug import secure_filename
import urllib2
import os
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
from flask import Flask, request, redirect, url_for, Response, render_template
#from keys import access_key_id, secret_access_key

app = Flask(__name__)

@app.route("/")
def index():
    return ""
	
@app.route("/version", methods=['GET'])
def version():
	"""
	Print Boto version
	curl -s -X GET localhost:8080/version
	"""
	return "Boto version: "+boto.Version+ "\n"

@app.route('/queues',	methods=['GET'])
def queues_index():
	"""
	List all queues
	curl -s -X GET -H 'Accept: application/json' http://localhost:8080/queues | python -mjson.tool
	"""
	
	all = []
	conn = get_conn()
	
	for q in conn.get_all_queues():
		all.append(q.name)
	resp = json.dumps(all)
	return Response(response=resp, mimetype="application/json")
	
@app.route('/queues',	methods=['POST'])
def queues_create():
	"""
	Create a queue
	curl -X POST -H 'Content-Type: application/json' http://localhost:8080/queues -d '{"name": "python-test"}'
	"""
	body = request.get_json(force=True)
	name = body['name']
	
	conn = get_conn()
	
	conn.create_queue(name)
	
	resp = "Created queue " + name + ".\n"
	return Response(response=resp, mimetype="application/json")
	
@app.route('/queues/<name>', methods=['DELETE'])
def queues_delete(name):
	"""
	Delete a queue
	curl -X DELETE -H 'Accept: application/json' http://localhost:8080/queues/python-test
	"""
	
	conn = get_conn()
	
	q = conn.get_queue(name)
	conn.delete_queue(q)
	
	resp = "Deleted queue " + name + ".\n"
	return Response(response=resp, mimetype="application/json")
	
@app.route('/queues/<name>/msgs/count', methods=['GET'])
def queues_msgcount(name):
	"""
	Count messages in a queue
	curl -X GET -H 'Accept: application/json' http://localhost:8080/queues/python-test/msgs/count
	"""
	
	conn = get_conn()
	
	q = conn.get_queue(name)
	
	resp = "There are " + str(q.count()) + " messages in the queue " + name+ ".\n"
	return Response(response=resp, mimetype="application/json")
	
@app.route('/queues/<name>/msgs', methods=['POST'])
def queues_addmsg(name):
	"""
	Add a message to a queue
	curl -s -X POST -H 'Accept: application/json' http://localhost:8080/queues/python-test/msgs -d '{"content": "this is the message I want to put on the queue"}'
	"""
	body = request.get_json(force=True)
	msg = body['content']
	
	conn = get_conn()
	
	m = Message()

	q = conn.get_queue(name)
	m.set_body(msg)

	q.write(m)
	
	resp = "Added message \"" + msg + "\" to the queue " + name+ ".\n"
	return Response(response=resp, mimetype="application/json")
	
@app.route('/queues/<name>/msgs', methods=['GET'])
def queues_readmsg(name):
	"""
	Read a message from a queue
	curl -X GET -H 'Accept: application/json' http://localhost:8080/queues/python-test/msgs
	"""
	
	conn = get_conn()
	
	q = conn.get_queue(name)
	m = q.read()
	resp = "Read message \"" + m.get_body() + "\" from the queue " + name+ ".\n"
	return Response(response=resp, mimetype="application/json")
	
@app.route('/queues/<name>/msgs', methods=['DELETE'])
def queues_consumemsg(name):
	"""
	Read a message from a queue
	curl -X DELETE -H 'Accept: application/json' http://localhost:8080/queues/python-test/msgs
	"""
	conn = get_conn()
	
	q = conn.get_queue(name)
	m = q.read()
	msg = m.get_body()
	q.delete_message(m)
	
	resp = "Comsumed message \"" + msg + "\" from the queue " + name+ ".\n"
	return Response(response=resp, mimetype="application/json")

def get_conn():
	key_id, secret_access_key = urllib2.urlopen("http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key").read().split(':')
	return boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=key_id, aws_secret_access_key=secret_access_key)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)