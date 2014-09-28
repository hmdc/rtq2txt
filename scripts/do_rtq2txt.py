#!/usr/bin/env python
import argparse
from rtq2txt import execute
import rt

def run(user, passwd, uri, queue, outputdir, status):
	tracker = rt.Rt(uri + '/REST/1.0/', user, passwd)
	tracker.login()

	execute(tracker, queue, outputdir, status)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Transforms an RT queue into txt files, writing them to a specified directory.")

	parser.add_argument('-d', '--debug', action='store_true',
			    help="Enables verbose output.")
	parser.add_argument('-l', '--location', required=True,
			    help="URI of RequestTracker")
	parser.add_argument('-u', '--user', required=True,
			    help="RT Username")
	parser.add_argument('-p', '--passwd', required=True,
			    help="RT Password")
	parser.add_argument('-q', '--queue', required=True,
			    help="RT Queue")
	parser.add_argument('-o', '--outputdir', required=True,
			    help="Output dir")
	parser.add_argument('-s', '--status', default=None, 
			    help="Set status on ticket after download.")

	args = parser.parse_args()

	_user, _pass, _uri = args.user, args.passwd, args.location
	_queue, _outputdir, _status = args.queue, args.outputdir, args.status

	run(_user, _pass, _uri, _queue, _outputdir, _status)

	# Print to stdout this environment variable if we want to use this in later scripts
	print("OUTPUTDIR=" + _outputdir)
