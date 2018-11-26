#!/usr/bin/python3

from flask import Flask, jsonify, request
import json, argparse

ram = {}
ramfile = "backup.json"
filename = "onions.json"

def read(fn=filename):
	return json.loads(open(fn, "r").read())
def search(term, onions=lambda: read()):
	res = []
	for domain in onions():
		if term in domain.split(".onion")[0]:
			res.append(domain)
	return res
def delete(domain):
	old = read()
	priv = old[domain]
	ram[domain] = priv # just in case
	del old[domain]
	with open(filename, "w") as f:
		f.write(json.dumps(old))
def dumpram():
	with open(ramfile, "w") as f:
		f.write(json.dumps(ram))

def main(host, port):
	app = Flask(__name__)
	@app.route("/")
	def all_onions():
		everything = read()
		domains = []
		for i in everything:
			domains.append(i)
		return jsonify(domains)
	@app.route("/search/<term>")
	def search_onions(term):
		return jsonify(search(term))
	@app.route("/claim/<domain>")
	def claim_onion(domain):
		if not domain in read():
			return str(False)
		res = {domain:read()[domain]}
		delete(domain)
		return jsonify(res)
	@app.route("/dump")
	def dump_ram():
		dumpram()
		return "done"
	app.run(host=host, port=port)

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"-o","--onion",
		help=("File where the onions are stored (json). Default=[onions.json]. Eg: --onion onions.json"))
	parser.add_argument(
		"-r","--ram",
		help=("Ram dump filename, Default=[backup.json]. Eg: --ram backup.json"))
	parser.add_argument(
		"-i","--ip",
		help=("IP to listen on. Eg: --ip 0.0.0.0"),
		required=True)
	parser.add_argument(
		"-p","--port",
		help=("Port to listen on. Eg: --port 5000"),
		required=True,
		type=int)
	return parser.parse_args()

if __name__ == "__main__":
	args = parse_args()
	if args.onion:
		globals()['filename'] = args.onion
	if args.ram:
		globals()['ramfile'] = args.ram
	main(args.ip, args.port)