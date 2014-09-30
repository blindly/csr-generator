#!/bin/env python
## Script to generate CSR
## 11/25/2013
import sys, getopt, commands

def usage():
	print "help: parameters required are --domain, --state, --city, --organization"

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["domain=","state=","city=","organization="])
	except getopt.GetoptError:
		usage()
		sys.exit()

	domain = None
	organization = None
	city = None
	state = None

	for opt, arg in opts:
		if opt == '-h':
			usage()
			sys.exit()
		elif opt in ("-d", "--domain"):
			domain = arg
		elif opt in ("-o", "--organization"):
			organization = arg
		elif opt in ("-c", "--city"):
			city = arg
		elif opt in ("-s", "--state"):
			state = arg

	required = ['domain', 'state', 'city', 'organization']
	if domain == None or state == None or city == None or organization == None:
		usage()
		sys.exit()
	else:
		underscore_domain = domain.replace('.', '_')
		key = underscore_domain + '.key'
		csr = underscore_domain + '.csr'
		country = 'us'

		command = 'openssl req -new -newkey rsa:2048 -nodes -out %s -keyout %s -subj "/C=%s/ST=%s/L=%s/O=%s/CN=%s"' % ( csr, key, country, state, city, organization, domain )
		### openssl req -new -newkey rsa:2048 -nodes -out domain_com.csr -keyout domain_com.key -subj "/C=us/ST=State/L=City/O=Organization/CN=domain.com"
		output = commands.getoutput( command )

		print output
		print "Done"

if __name__ == "__main__":
	main(sys.argv[1:])
