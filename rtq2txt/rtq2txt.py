#!/usr/bin/env python
import rt
import re
import os
import errno
import inspect

def execute(tracker, queue, outputdir, _status):

	# Check if tracker is logged in
	try:
		if tracker.login_result == None:
			raise Exception("tracker is not logged in.")
	except:
		raise
	
	# Check if queue exists
	try:
		tracker.get_queue(queue)['Name']
	except:
		raise Exception("queue " + queue + " does not exist.")

	# Create output directory of it doesn't exist
	try:
		os.makedirs(outputdir)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise
		else:
			pass
	
	q_tickets = map(lambda t: int(t['id'].split('/')[1]), tracker.search(Queue=queue))

	for ticket in q_tickets:
		# Get the first.. this is usually containing Content and Headers
		try:
			_header = tracker.get_attachment(ticket, tracker.get_attachments_ids(ticket)[0])['Headers']
			_content = tracker.get_attachment(ticket, tracker.get_attachments_ids(ticket)[0])['Content']
			__content = tracker.get_attachment(ticket, tracker.get_attachments_ids(ticket)[1])['Content']
		except:
		        if _status:
				tracker.edit_ticket(ticket, Status=_status)	
			continue

		# If we can't get the content, well.. we don't care, there's a lot of spam elements essentially. Now there is the odd
		# situation where 'content' variable contains text relating to the Ticket and is instead in get_...(ticket)[0]. Why is this?
		# Who reallly knows...?


		if re.search(r'The last correspondence on this ticket', __content) and len(_content) == 0:
			# print("Found ticket " + str(ticket) + " which has a content of length 0 and invalid text in the body: The last correspondence on this ticket. This means the body is probably empty.")

			if _status:
				tracker.edit_ticket(ticket, Status=_status)

			continue
		elif re.search(r'The last correspondence on this ticket', __content):
			content = _content
		else:
			content = __content
		
		# We don't care about any headers starting with X or To, because it's from RT and we don't wanna muck it up
		valid_headers = set(_header) - set(map(lambda x: re.match(r'^X.*|^To.*|^RT.*', x).group() if re.match(r'^X.*|^To.*|^RT.*', x) else None, _header))

		with open(outputdir + '/' + str(ticket) + '.txt', 'w+') as email:
			map(lambda hdr: email.write(hdr + ': ' + _header[hdr] + '\n'), valid_headers)
			email.write(content)

		if _status:
			tracker.edit_ticket(ticket, Status=_status)
