# playing with FB's graph API, the access token for this will expire at about 3:30 PM(IST) 5 AUG 17

import requests
import json

access_token ='<INSERT ACCESS TOKEN HERE>' 

def get_page_id(page_id):
	url = 'https://graph.facebook.com/'+page_id.encode('utf-8')+'/feed?limit=10&access_token='+access_token
	data = requests.get(url)
	response = json.loads(data.text)
	# print data.text


	next_page = response['paging']['next']
	while next_page:
		for post in response['data']:
			if 'message' in post:
				print (post['message']+'\nThe post id is '+post['id']+'\nThe time post was last updated is '+post['updated_time']).encode('utf-8')
				print "\n"
				print "------------------------------------------------------------------------"
				print "\n"
		response = json.loads(requests.get(next_page).text)
		if 'paging' in response:
			if'next' in response['paging']:
				next_page=response['paging']['next']
			else:
				for post in response['data']:
					if 'message' in post:
						print (post['message']+'\nThe post id is '+post['id']+'\nThe time post was last updated is '+post['updated_time']).encode('utf-8')
						print "\n"
						print "------------------------------------------------------------------------"
						print "\n"
				next_page= None
		else:
			# print "Paging not found"
			next_page=None


get_page_id('<INSERT GROUP ID HERE')

print "Good Bye"
exit()
# get_post_likes('')


