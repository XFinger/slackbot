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

@listen_to('haw')
def hey(message):
	message.reply('hey this')
	message.react('tropical_fish')

@respond_to('weather$', re.IGNORECASE)
@respond_to('weather (.*) (.*)', re.IGNORECASE)
def weather(message, city_str=None, state_str=None):
	WU_KEY = "11250e7453bcc141" #weather underground api key
	 
	conn = http.client.HTTPConnection("api.wunderground.com") # base url 
	conn.request("GET", "/api/%s/conditions/q/%s/%s.json" % (WU_KEY, state_str, city_str)) # the '%s represent variables for weather underground key, state and city from the user input'
	res = conn.getresponse()
	data = res.read().decode('utf-8')
	parsed_json = json.loads(data) #json parser
	#message reply with a few keys pulled from the json response
	message.reply("The weather in " + parsed_json['current_observation']['display_location']['full'] + '\n' + parsed_json['current_observation']['weather'] + '\n' + parsed_json['current_observation']['temperature_string']   )





