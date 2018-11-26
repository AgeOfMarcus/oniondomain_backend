# oniondomain_backend

The aim of this project is to serve as a backend server for a website hosting onion domain private keys.

# gen_onions.py

A multithreaded onion domain generator that outputs in this format:

	<domain>:<private_key>

For usage, direct output to a text file for later parsing.

# parse_onions.py

This parses a text file with onions in the format outputted from `gen_onions.py`. Returns a json dictionary in format:

	{<domain>:<private_key>}

For usage, direct output to a text file for the server.

# server.py

A flask server for searching and claiming onions.

## Urls
	/ - returns all onions in a list (json)
	/search/<term> - returns any domains with <term> in the domain
	/claim/<domain> - returns the private key for <domain> and deletes it from the list (stores in backup memory, in case)
	/dump - dumps backup memory to a file