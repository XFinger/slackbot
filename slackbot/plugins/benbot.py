#coding: UTF-8
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import json
import http.client


#Ben you can add listeners and responders here
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



