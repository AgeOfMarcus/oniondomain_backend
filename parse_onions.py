#!/usr/bin/python3

import json, argparse

def parse(text):
	res = {}
	for i in text.split("-----END RSA PRIVATE KEY-----"):
		if i == "" or i == "\n":
			continue
		try:
			onion, priv = i.split(":")
			if "\n" in onion:
				try:
					onion = onion.split("\n")[1]
				except:
					onion = onion.split("\n")[0]
			priv += "-----END RSA PRIVATE KEY-----"
			res[onion] = priv
		except Exception as e:
			print("Error with i=%s: %s" % (
				str(i),str(e)))
	return res

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"-f","--file",
		help=("File to parse. Eg: --file onions.txt"),
		required=True)
	return parser.parse_args()
def main(args):
	text = open(args.file, "r").read()
	res = parse(text)
	return json.dumps(res)
if __name__ == "__main__":
	print(main(parse_args()))