#!/usr/bin/python3

from hackerman.crypto import onion
import argparse, _thread, os, time

quit = False

def my_thread(exit_var=quit):
	while not quit:
		domain, priv = onion.generate()
		out = domain+":"+priv.decode()
		print(out)

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"-t","--threads",
		help=("Amount of threads to start. Default is 20. Eg: --threads 75"),
		type=int)
	return parser.parse_args()

def main(args):
	th = args.threads
	if th is None: th = 20
	started = 0
	while started <= th:
		_thread.start_new_thread(my_thread, ( ))
		started += 1
	while True:
		try:
			pass
		except KeyboardInterrupt:
			quit = True
			time.sleep(0.3)
			break

if __name__ == "__main__":
	main(parse_args())