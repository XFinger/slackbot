from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import json
import http.client

@respond_to('hi', re.IGNORECASE)
def hi(message):
	#uname = message.channel._client.users[message.body['user']][u'name']
    message.reply('Hi, ' + message.channel._client.users[message.body['user']][u'name'] + ' what can I do for you today?')
    # react with thumb up emoji
    message.react('+1')

@respond_to('count_rows')
def count_rows(message):
	conn = http.client.HTTPConnection("api.us.socrata.com")
	headers = {'cache-control': "no-cache",'postman-token': "9f9ac581-9189-ab58-e18e-3908a1f2fcb3"}
	conn.request("GET", "/api/catalog/v1/domains", headers=headers)
	res = conn.getresponse()
	string = res.read().decode('utf-8')
	parsed_json = json.loads(string)
	data = len(parsed_json['results'])
	message.reply('There are currently ' + str(data) + ' rows in the dataset')

